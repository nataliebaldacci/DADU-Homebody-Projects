#!/usr/bin/env python3
"""
build_docs_index_v2.py

Builds a comprehensive docs_index.json (v2) that enhances the existing
gdrive_docs_index.json with:
  1. Permit entries with Nashville portal fallback URLs
  2. Card2 assessor card entries from Parcels_Dual_Cards_With_URLs.csv
  3. Card2 local image references from Card2_Images/ folder
  4. Trade permit sub-entries linked to parent DADU permits

Output: /Users/nataliebaldacci/DADU-Homebody-Projects/data/gdrive_docs_index.json
"""

import csv
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# === FILE PATHS ===
BASE = "/Users/nataliebaldacci/DADU-Homebody-Projects"
FINAL = os.path.join(BASE, "DADU/FINAL_FINAL")

EXISTING_INDEX = os.path.join(BASE, "data/gdrive_docs_index.json")
OUTPUT_INDEX = os.path.join(BASE, "data/gdrive_docs_index.json")

# Permit CSVs
CONFIRMED_PERMITS = os.path.join(FINAL, "confirmed_dadu_permits.csv")
CLEANED_PERMITS = os.path.join(FINAL, "Reference_Data/DADU_All_Permits_Cleaned.csv")
TRADE_PERMITS = os.path.join(BASE, "DADU/DADU_Trade_Permits/dadu_trade_permits.csv")

# Card2 data
CARD2_CSV = os.path.join(FINAL, "Parcels_Dual_Cards_With_URLs.csv")
CARD2_IMAGES_DIR = os.path.join(FINAL, "Card2_Images")

# Google Drive folder IDs (for reference/placeholders)
GDRIVE_FOLDERS = {
    "permits": "1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4",
    "property_cards": "1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ",
    "covenants": "1bEZN1kEZxqZLkdX0QjT0g9N7K0sXAy3Z",
    "udo_overlays": "1evPTz2SvAIDS74lwzgxjGF85kl2nDsrh",
    "dadu_overlays": "1KDQe3WhWz1H1ukTIlAfxtbDFmvX50kYu",
}


def normalize_apn(raw):
    """Normalize APN to 11-digit zero-padded string if numeric."""
    if not raw or not raw.strip():
        return None
    s = raw.strip()
    if "E+" in s or "e+" in s:
        return None
    if s.isdigit():
        return s.zfill(11) if len(s) <= 11 else s
    return s  # alphanumeric APNs kept as-is


def empty_parcel():
    """Return empty parcel doc structure."""
    return {
        "property_cards": [],
        "assessor_cards": [],
        "covenants": [],
        "permits": [],
        "aerials": [],
        "site_plans": [],
        "other": [],
    }


def load_existing_index():
    """Load the existing gdrive_docs_index.json."""
    if not os.path.exists(EXISTING_INDEX):
        print(f"WARNING: No existing index at {EXISTING_INDEX}, starting fresh")
        return {}

    with open(EXISTING_INDEX, "r", encoding="utf-8") as f:
        data = json.load(f)

    parcels = data.get("parcels", {})
    print(f"  Loaded existing index: {len(parcels)} parcels")

    # Count existing docs
    existing_counts = {}
    for apn, docs in parcels.items():
        for cat, items in docs.items():
            if isinstance(items, list):
                existing_counts[cat] = existing_counts.get(cat, 0) + len(items)
    for cat, count in sorted(existing_counts.items()):
        if count > 0:
            print(f"    {cat}: {count}")

    return parcels


def load_confirmed_permits():
    """Load confirmed_dadu_permits.csv and return dict keyed by APN."""
    if not os.path.exists(CONFIRMED_PERMITS):
        print(f"WARNING: {CONFIRMED_PERMITS} not found, skipping")
        return {}

    permits_by_apn = {}
    count = 0
    with open(CONFIRMED_PERMITS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            apn = normalize_apn(row.get("APN", ""))
            if not apn:
                continue

            case_number = row.get("CASE_NUMBER", "").strip()
            if not case_number:
                continue

            # Parse date from epoch ms
            date_str = ""
            date_accepted = row.get("DATE_ACCEPTED", "")
            if date_accepted:
                try:
                    epoch_ms = int(float(date_accepted))
                    dt = datetime.fromtimestamp(epoch_ms / 1000)
                    date_str = dt.strftime("%Y-%m-%d")
                except (ValueError, OSError):
                    pass

            permit_entry = {
                "permit_number": case_number,
                "permit_type": row.get("CASE_TYPE_DESC", "").strip(),
                "permit_subtype": row.get("SUB_TYPE_DESC", "").strip(),
                "status": row.get("STATUS_CODE", "").strip().lower(),
                "date": date_str,
                "address": row.get("ADDRESS", "").strip() or row.get("LOCATION", "").strip(),
                "value": row.get("CONSTVAL", ""),
                "sqft": row.get("BLDG_SQ_FT", "").strip(),
                "scope": row.get("SCOPE", "").strip()[:200],  # truncate long scope text
                "docs_url": f"https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={case_number}",
                "epermits_url": row.get("epermits", "").strip() or f"https://epermits.nashville.gov/?#/?searchCode=PRMT={case_number}",
                "gdrive_url": None,  # placeholder for future Google Drive file ID
                "gdrive_folder": f"https://drive.google.com/drive/folders/{GDRIVE_FOLDERS['permits']}",
            }

            if apn not in permits_by_apn:
                permits_by_apn[apn] = {}
            permits_by_apn[apn][case_number] = permit_entry
            count += 1

    print(f"  Loaded confirmed permits: {count} permits for {len(permits_by_apn)} parcels")
    return permits_by_apn


def load_cleaned_permits():
    """Load DADU_All_Permits_Cleaned.csv and return dict keyed by APN."""
    if not os.path.exists(CLEANED_PERMITS):
        print(f"WARNING: {CLEANED_PERMITS} not found, skipping")
        return {}

    permits_by_apn = {}
    count = 0
    with open(CLEANED_PERMITS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            apn = normalize_apn(row.get("apn", ""))
            if not apn:
                continue

            permit_num = row.get("permit_number", "").strip()
            if not permit_num:
                continue

            permit_entry = {
                "permit_number": permit_num,
                "permit_type": row.get("permit_type", "").strip(),
                "permit_subtype": row.get("permit_subtype", "").strip(),
                "status": row.get("status", "").strip().lower(),
                "date": row.get("date_issued", "").strip(),
                "address": row.get("address", "").strip(),
                "contractor": row.get("contractor", "").strip(),
                "value": row.get("value", ""),
                "purpose": row.get("purpose", "").strip()[:200],
                "docs_url": row.get("url_documents", "").strip() or f"https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={permit_num}",
                "epermits_url": row.get("url_epermits", "").strip() or f"https://epermits.nashville.gov/?#/permit/{row.get('pid', '')}",
                "gdrive_url": None,
                "gdrive_folder": f"https://drive.google.com/drive/folders/{GDRIVE_FOLDERS['permits']}",
            }

            if apn not in permits_by_apn:
                permits_by_apn[apn] = {}
            # Only add if not already present (confirmed_permits takes priority)
            if permit_num not in permits_by_apn.get(apn, {}):
                if apn not in permits_by_apn:
                    permits_by_apn[apn] = {}
                permits_by_apn[apn][permit_num] = permit_entry
                count += 1

    print(f"  Loaded cleaned permits: {count} permits for {len(permits_by_apn)} parcels")
    return permits_by_apn


def load_trade_permits():
    """Load trade permits and return dict keyed by parent_permit_number."""
    if not os.path.exists(TRADE_PERMITS):
        print(f"WARNING: {TRADE_PERMITS} not found, skipping")
        return {}

    trades_by_parent = {}
    count = 0
    with open(TRADE_PERMITS, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            parent = row.get("parent_permit_number", "").strip()
            if not parent:
                continue

            trade_entry = {
                "trade_permit": row.get("trade_permit_number", "").strip(),
                "trade_type": row.get("trade_type", "").strip(),
                "trade_description": row.get("trade_description", "").strip(),
                "status": row.get("status", "").strip().lower(),
                "issued_date": row.get("issued_date", "").strip()[:10] if row.get("issued_date") else "",
            }

            if parent not in trades_by_parent:
                trades_by_parent[parent] = []
            trades_by_parent[parent].append(trade_entry)
            count += 1

    print(f"  Loaded trade permits: {count} trades for {len(trades_by_parent)} parent permits")
    return trades_by_parent


def load_card2_csv():
    """Load Card2 URLs from Parcels_Dual_Cards_With_URLs.csv."""
    if not os.path.exists(CARD2_CSV):
        print(f"WARNING: {CARD2_CSV} not found, skipping")
        return {}

    card2_by_apn = {}
    count = 0
    with open(CARD2_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            apn = normalize_apn(row.get("APN", ""))
            if not apn:
                continue

            account = row.get("ACCOUNTNUMBER", "").strip()
            if not account:
                continue

            entry = {
                "account_number": account,
                "structure_type": row.get("StructureType2", "").strip(),
                "finished_area": row.get("FinishedArea2", "").strip(),
                "card2_summary_url": row.get("Card2_Summary_URL", "").strip(),
                "card2_buildingprint_url": row.get("Card2_BuildingPrint_URL", "").strip(),
                "card2_photo_url": row.get("Card2_Photo_URL", "").strip(),
                "card2_sketch_url": row.get("Card2_Sketch_URL", "").strip(),
                "property_card_url": row.get("PropertyCard_URL", "").strip() or f"https://portal.padctn.org/OFS/WP/Print/{account}",
            }

            card2_by_apn[apn] = entry
            count += 1

    print(f"  Loaded Card2 CSV: {count} parcels with Card2 URLs")
    return card2_by_apn


def scan_card2_images():
    """Scan Card2_Images directory for local image files."""
    if not os.path.isdir(CARD2_IMAGES_DIR):
        print(f"WARNING: {CARD2_IMAGES_DIR} not found, skipping")
        return {}

    images_by_apn = {}
    total_files = 0

    for subdir in os.listdir(CARD2_IMAGES_DIR):
        subdir_path = os.path.join(CARD2_IMAGES_DIR, subdir)
        if not os.path.isdir(subdir_path):
            continue

        for fname in os.listdir(subdir_path):
            if not fname.lower().endswith(".jpg"):
                continue
            total_files += 1

            # Extract APN from filename: {APN}_card2_{type}.jpg
            match = re.match(r"^(.+?)_card2_(photo|sketch)\.jpg$", fname, re.IGNORECASE)
            if not match:
                continue

            apn_raw = match.group(1)
            img_type = match.group(2).lower()

            apn = normalize_apn(apn_raw) or apn_raw

            if apn not in images_by_apn:
                images_by_apn[apn] = {}

            # Store relative path from project root (for potential GitHub Pages serving)
            rel_path = f"DADU/FINAL_FINAL/Card2_Images/{subdir}/{fname}"
            images_by_apn[apn][f"local_{img_type}"] = rel_path
            images_by_apn[apn]["structure_type_folder"] = subdir

    print(f"  Scanned Card2 images: {total_files} files, {len(images_by_apn)} unique APNs")
    return images_by_apn


def merge_all(parcels, confirmed, cleaned, trades, card2_csv, card2_images):
    """Merge all data sources into the parcels dict."""

    permits_added = 0
    trades_added = 0
    card2_added = 0

    # 1. Merge confirmed permits (highest priority)
    for apn, permits_dict in confirmed.items():
        if apn not in parcels:
            parcels[apn] = empty_parcel()

        for permit_num, entry in permits_dict.items():
            # Check if this permit is already in the list
            existing_nums = {p.get("permit_number") for p in parcels[apn]["permits"]}
            if permit_num not in existing_nums:
                # Attach trade permits if available
                if permit_num in trades:
                    entry["trade_permits"] = trades[permit_num]
                    trades_added += len(trades[permit_num])

                parcels[apn]["permits"].append(entry)
                permits_added += 1

    # 2. Merge cleaned permits (fill gaps)
    for apn, permits_dict in cleaned.items():
        if apn not in parcels:
            parcels[apn] = empty_parcel()

        for permit_num, entry in permits_dict.items():
            existing_nums = {p.get("permit_number") for p in parcels[apn]["permits"]}
            if permit_num not in existing_nums:
                if permit_num in trades:
                    entry["trade_permits"] = trades[permit_num]
                    trades_added += len(trades[permit_num])

                parcels[apn]["permits"].append(entry)
                permits_added += 1

    # 3. Merge Card2 assessor cards
    all_card2_apns = set(card2_csv.keys()) | set(card2_images.keys())
    for apn in all_card2_apns:
        if apn not in parcels:
            parcels[apn] = empty_parcel()

        # Skip if assessor_cards already populated
        if parcels[apn]["assessor_cards"]:
            continue

        csv_data = card2_csv.get(apn, {})
        img_data = card2_images.get(apn, {})

        card2_entry = {
            "type": "card2",
            "structure_type": csv_data.get("structure_type", img_data.get("structure_type_folder", "")),
            "finished_area": csv_data.get("finished_area", ""),
            "card2_photo_url": csv_data.get("card2_photo_url", ""),
            "card2_sketch_url": csv_data.get("card2_sketch_url", ""),
            "card2_summary_url": csv_data.get("card2_summary_url", ""),
            "card2_buildingprint_url": csv_data.get("card2_buildingprint_url", ""),
            "property_card_url": csv_data.get("property_card_url", ""),
        }

        # Add local image paths if available
        if "local_photo" in img_data:
            card2_entry["local_photo"] = img_data["local_photo"]
        if "local_sketch" in img_data:
            card2_entry["local_sketch"] = img_data["local_sketch"]

        # Only add if we have at least one URL or local file
        has_data = any(v for k, v in card2_entry.items() if k != "type" and v)
        if has_data:
            parcels[apn]["assessor_cards"].append(card2_entry)
            card2_added += 1

    print(f"\n  === Merge Results ===")
    print(f"  Permits added:       {permits_added}")
    print(f"  Trade permits added: {trades_added}")
    print(f"  Card2 entries added: {card2_added}")

    return parcels


def count_docs(parcels):
    """Count documents by category."""
    counts = {}
    for apn, docs in parcels.items():
        for cat, items in docs.items():
            if isinstance(items, list):
                counts[cat] = counts.get(cat, 0) + len(items)
    return counts


def main():
    print("=" * 60)
    print("Building comprehensive gdrive_docs_index.json v2")
    print("=" * 60)

    # Step 1: Load existing index (preserves property cards + covenants with Drive URLs)
    print("\n[1/6] Loading existing index...")
    parcels = load_existing_index()

    # Step 2: Load confirmed DADU permits
    print("\n[2/6] Loading confirmed DADU permits...")
    confirmed = load_confirmed_permits()

    # Step 3: Load cleaned permits (broader set)
    print("\n[3/6] Loading cleaned permits...")
    cleaned = load_cleaned_permits()

    # Step 4: Load trade permits
    print("\n[4/6] Loading trade permits...")
    trades = load_trade_permits()

    # Step 5: Load Card2 data
    print("\n[5/6] Loading Card2 data...")
    card2_csv = load_card2_csv()
    card2_images = scan_card2_images()

    # Step 6: Merge everything
    print("\n[6/6] Merging all sources...")
    parcels = merge_all(parcels, confirmed, cleaned, trades, card2_csv, card2_images)

    # Count final docs
    doc_counts = count_docs(parcels)

    # Build output
    output = {
        "_schema_version": "2.1",
        "_description": "Comprehensive document index keyed by APN for Castlehold. Includes Google Drive files, Nashville portal fallback URLs, Card2 assessor images, and trade permits.",
        "_generated": datetime.now().isoformat(),
        "_total_parcels": len(parcels),
        "_total_documents": sum(doc_counts.values()),
        "_gdrive_folders": GDRIVE_FOLDERS,
        "parcels": parcels,
        "_document_counts": doc_counts,
    }

    # Write output
    os.makedirs(os.path.dirname(OUTPUT_INDEX), exist_ok=True)
    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, default=str)

    file_size_mb = os.path.getsize(OUTPUT_INDEX) / (1024 * 1024)

    print(f"\n{'=' * 60}")
    print(f"OUTPUT: {OUTPUT_INDEX}")
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"Total parcels: {len(parcels):,}")
    print(f"Total documents: {sum(doc_counts.values()):,}")
    print(f"\nDocument counts by category:")
    for cat, count in sorted(doc_counts.items(), key=lambda x: -x[1]):
        print(f"  {cat:20s} {count:,}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
