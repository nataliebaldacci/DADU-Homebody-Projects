#!/usr/bin/env python3
"""
update_gdrive_index.py
After uploading covenant and permit PDFs to Google Drive via rclone,
this script:
1. Lists all files in GDrive DADU_PDFs/Restrictive_Covenants and Permit_PDFs folders
2. Extracts APN + instrument (covenants) or permit number (permits) from filenames
3. Updates gdrive_docs_index.json with gdrive_url and download_url for each document

Run AFTER rclone uploads are complete.

Usage:
    python3 Scripts/update_gdrive_index.py
"""

import json
import subprocess
import re
import sys
import os
from datetime import datetime

REPO_ROOT = "/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects"
INDEX_FILE = os.path.join(REPO_ROOT, "data", "gdrive_docs_index.json")

# GDrive folder paths (rclone remote:path)
COVENANT_GDRIVE = "gdrive:DADU_PDFs/Restrictive_Covenants"
PERMIT_GDRIVE = "gdrive:DADU_PDFs/Permit_PDFs"


def rclone_lsjson(remote_path):
    """List all files in a GDrive folder with their IDs using rclone lsjson."""
    print(f"  Listing files in {remote_path}...")
    result = subprocess.run(
        ["rclone", "lsjson", remote_path, "--no-modtime", "--no-mimetype"],
        capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr}")
        return []
    files = json.loads(result.stdout)
    print(f"  Found {len(files)} files")
    return files


def make_gdrive_urls(file_id):
    """Create GDrive view and download URLs from a file ID."""
    view_url = f"https://drive.google.com/file/d/{file_id}/view"
    download_url = f"https://drive.google.com/uc?id={file_id}&export=download"
    return view_url, download_url


def parse_covenant_filename(filename):
    """
    Parse covenant filename patterns:
    - Covenant_APN_INSTRUMENT.pdf (renamed format)
    - Covenant_APN_ADDRESS_INSTRUMENT.pdf (renamed with address)
    - APN_Covenant_INSTRUMENT.pdf (original gdrive format)
    Returns (apn, instrument) or (None, None)
    """
    name = filename.replace('.pdf', '').replace('.PDF', '')
    parts = name.split('_')

    if parts[0] == 'Covenant':
        # Renamed format: Covenant_APN_..._INSTRUMENT.pdf
        if len(parts) >= 3:
            apn = parts[1]
            instrument = parts[-1]
            # Validate: APN should be numeric, instrument should be numeric
            if apn.isdigit() and instrument.isdigit():
                return apn, instrument
            elif instrument.isdigit():
                # APN might have address mixed in, instrument is last numeric
                return None, instrument
        elif len(parts) == 2:
            # Covenant_INSTRUMENT.pdf (no APN)
            if parts[1].isdigit():
                return None, parts[1]
    elif 'Covenant' in parts:
        # Original format: APN_Covenant_INSTRUMENT.pdf
        idx = parts.index('Covenant')
        if idx > 0 and idx + 1 < len(parts):
            apn = parts[0]
            instrument = parts[-1]
            if instrument.isdigit():
                return apn, instrument

    return None, None


def parse_permit_filename(filename):
    """
    Parse permit filename patterns:
    - PERMITNUM_ADDRESS_docN.pdf (renamed format)
    - UUID_CA-Permits-DATE_NUM_N.pdf (original gdrive format)
    Returns permit_number or None
    """
    name = filename.replace('.pdf', '').replace('.PDF', '')

    # Renamed format: starts with permit number (numeric, ~10 digits)
    match = re.match(r'^(\d{7,12})_', name)
    if match:
        return match.group(1)

    # Original format: UUID_CA-Permits-DATE_NUM_N
    # Try to extract the internal permit number
    match = re.search(r'CA-Permits-\d+_(\d+)_', name)
    if match:
        return match.group(1)

    return None


def main():
    print("=" * 60)
    print("UPDATE GDRIVE DOCS INDEX")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Load existing index
    print(f"\nLoading {INDEX_FILE}...")
    with open(INDEX_FILE) as f:
        data = json.load(f)
    parcels = data.get("parcels", {})
    print(f"  {len(parcels)} parcels in index")

    # Build lookup: instrument -> list of APNs (from existing index)
    instrument_to_apns = {}
    permit_to_apns = {}
    for apn, docs in parcels.items():
        for cov in docs.get("covenants", []):
            inst = cov.get("instrument", "")
            if inst:
                instrument_to_apns.setdefault(inst, []).append(apn)
        for perm in docs.get("permits", []):
            pnum = perm.get("permit_number", "")
            if pnum:
                permit_to_apns.setdefault(pnum, []).append(apn)

    print(f"  {len(instrument_to_apns)} unique instruments in index")
    print(f"  {len(permit_to_apns)} unique permit numbers in index")

    # ================================================
    # STEP 1: Process covenant files from GDrive
    # ================================================
    print("\n--- COVENANTS ---")
    covenant_files = rclone_lsjson(COVENANT_GDRIVE)

    cov_updated = 0
    cov_new_entries = 0
    cov_no_match = 0

    # Build instrument -> file_id mapping from GDrive files
    instrument_to_fileid = {}
    for gf in covenant_files:
        if gf.get("IsDir"):
            continue
        filename = gf["Name"]
        file_id = gf.get("ID", "")
        if not file_id:
            continue

        apn_from_file, instrument = parse_covenant_filename(filename)
        if not instrument:
            continue

        # Store all files for this instrument
        instrument_to_fileid.setdefault(instrument, []).append({
            "file_id": file_id,
            "filename": filename,
            "apn_from_file": apn_from_file
        })

    print(f"  Parsed {len(instrument_to_fileid)} unique instruments from GDrive files")

    # Update index entries
    for apn, docs in parcels.items():
        for cov in docs.get("covenants", []):
            inst = cov.get("instrument", "")
            if not inst:
                continue
            if inst in instrument_to_fileid:
                gfiles = instrument_to_fileid[inst]
                # Prefer file that matches this APN
                best = None
                for gf in gfiles:
                    if gf["apn_from_file"] == apn:
                        best = gf
                        break
                if not best:
                    best = gfiles[0]

                view_url, download_url = make_gdrive_urls(best["file_id"])
                if not cov.get("gdrive_url") or cov["gdrive_url"] is None:
                    cov["gdrive_url"] = view_url
                    cov["download_url"] = download_url
                    cov["file_id"] = best["file_id"]
                    cov_updated += 1

    print(f"  Updated {cov_updated} covenant entries with GDrive URLs")

    # ================================================
    # STEP 2: Process permit files from GDrive
    # ================================================
    print("\n--- PERMITS ---")
    permit_files = rclone_lsjson(PERMIT_GDRIVE)

    perm_updated = 0

    # Build permit_number -> list of file entries
    permit_to_fileids = {}
    for gf in permit_files:
        if gf.get("IsDir"):
            continue
        filename = gf["Name"]
        file_id = gf.get("ID", "")
        if not file_id:
            continue

        permit_num = parse_permit_filename(filename)
        if not permit_num:
            continue

        permit_to_fileids.setdefault(permit_num, []).append({
            "file_id": file_id,
            "filename": filename
        })

    print(f"  Parsed {len(permit_to_fileids)} unique permit numbers from GDrive files")

    # Update index entries
    for apn, docs in parcels.items():
        for perm in docs.get("permits", []):
            pnum = perm.get("permit_number", "")
            if not pnum:
                continue
            if pnum in permit_to_fileids:
                gfiles = permit_to_fileids[pnum]
                # Use first file (doc1) as the primary link
                best = sorted(gfiles, key=lambda x: x["filename"])[0]
                view_url, download_url = make_gdrive_urls(best["file_id"])
                if not perm.get("gdrive_url") or perm["gdrive_url"] is None:
                    perm["gdrive_url"] = view_url
                    perm["download_url"] = download_url
                    perm["file_id"] = best["file_id"]
                    # If multiple docs, store all
                    if len(gfiles) > 1:
                        perm["additional_docs"] = [
                            {
                                "gdrive_url": make_gdrive_urls(gf["file_id"])[0],
                                "download_url": make_gdrive_urls(gf["file_id"])[1],
                                "filename": gf["filename"]
                            }
                            for gf in sorted(gfiles, key=lambda x: x["filename"])[1:]
                        ]
                    perm_updated += 1

    print(f"  Updated {perm_updated} permit entries with GDrive URLs")

    # ================================================
    # STEP 3: Recount document stats
    # ================================================
    print("\n--- UPDATING STATS ---")
    doc_counts = {
        "property_cards": 0,
        "assessor_cards": 0,
        "covenants": 0,
        "permits": 0,
        "site_plans": 0,
        "aerials": 0,
        "other": 0
    }
    total_docs = 0
    covenants_with_url = 0
    permits_with_url = 0

    for apn, docs in parcels.items():
        for cat in doc_counts:
            items = docs.get(cat, [])
            doc_counts[cat] += len(items)
            total_docs += len(items)
        for cov in docs.get("covenants", []):
            if cov.get("gdrive_url") and cov["gdrive_url"] is not None:
                covenants_with_url += 1
        for perm in docs.get("permits", []):
            if perm.get("gdrive_url") and perm["gdrive_url"] is not None:
                permits_with_url += 1

    data["_total_documents"] = total_docs
    data["_document_counts"] = doc_counts
    data["_generated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["_schema_version"] = "2.2"

    # ================================================
    # STEP 4: Save updated index
    # ================================================
    output_file = INDEX_FILE  # Overwrite in place
    backup_file = INDEX_FILE.replace(".json", f"_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

    # Save backup first
    print(f"\n  Saving backup to {backup_file}...")
    with open(backup_file, 'w') as f:
        json.dump(data, f)

    # Save updated index
    print(f"  Saving updated index to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=None, separators=(',', ':'))

    file_size = os.path.getsize(output_file) / 1e6
    print(f"  File size: {file_size:.1f} MB")

    # ================================================
    # SUMMARY
    # ================================================
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Covenant entries updated: {cov_updated}")
    print(f"  Permit entries updated: {perm_updated}")
    print(f"  Total covenants with GDrive URL: {covenants_with_url}")
    print(f"  Total permits with GDrive URL: {permits_with_url}")
    print(f"  Total documents in index: {total_docs}")
    print(f"  Document counts: {doc_counts}")
    print(f"\nDone at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
