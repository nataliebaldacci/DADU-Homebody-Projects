#!/usr/bin/env python3
"""
upload_permit_pdfs.py
Uploads all renamed permit PDFs to Google Drive using rclone,
then updates the manifest with Drive links.

Prerequisites:
  - rclone configured with a remote named "gdrive"
  - Permit PDFs in DADU/FINAL_FINAL/Permit_PDFs_Renamed/

Usage (run from repo root):
    python3 Scripts/upload_permit_pdfs.py

After this completes, run:
    python3 Scripts/update_gdrive_index.py
to wire the new Drive URLs into gdrive_docs_index.json.
"""

import csv
import json
import os
import subprocess
import sys
import time
from datetime import datetime

REPO_ROOT = "/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects"
LOCAL_DIR = os.path.join(REPO_ROOT, "DADU", "FINAL_FINAL", "Permit_PDFs_Renamed")
MANIFEST = os.path.join(LOCAL_DIR, "_manifest.csv")
GDRIVE_REMOTE = "gdrive:DADU_PDFs/Permit_PDFs"

# Rate limiting: pause between uploads to avoid Google throttling
PAUSE_BETWEEN_UPLOADS = 0.5  # seconds


def check_rclone():
    """Verify rclone is installed and the gdrive remote works."""
    try:
        result = subprocess.run(
            ["rclone", "about", "gdrive:"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            print(f"ERROR: rclone 'gdrive' remote not working: {result.stderr}")
            sys.exit(1)
        print("  rclone gdrive remote: OK")
    except FileNotFoundError:
        print("ERROR: rclone not found. Install it: brew install rclone")
        sys.exit(1)


def list_existing_gdrive_files():
    """Get all files already on Drive to skip re-uploads."""
    print("  Listing existing files on Google Drive...")
    result = subprocess.run(
        ["rclone", "lsjson", GDRIVE_REMOTE, "--no-modtime", "--no-mimetype"],
        capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        print(f"  Warning: Could not list Drive folder: {result.stderr}")
        return {}
    files = json.loads(result.stdout)
    existing = {}
    for f in files:
        if not f.get("IsDir"):
            existing[f["Name"]] = f.get("ID", "")
    print(f"  Found {len(existing)} files already on Drive")
    return existing


def upload_file(local_path, remote_path):
    """Upload a single file using rclone copyto."""
    result = subprocess.run(
        ["rclone", "copyto", local_path, remote_path],
        capture_output=True, text=True, timeout=120
    )
    return result.returncode == 0, result.stderr


def get_file_id(remote_path, filename):
    """Get the Drive file ID for a just-uploaded file."""
    result = subprocess.run(
        ["rclone", "lsjson", remote_path, "--no-modtime", "--no-mimetype",
         "--include", filename],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode == 0:
        files = json.loads(result.stdout)
        for f in files:
            if f["Name"] == filename:
                return f.get("ID", "")
    return ""


def main():
    print("=" * 60)
    print("UPLOAD PERMIT PDFs TO GOOGLE DRIVE")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Pre-flight checks
    print("\n--- PRE-FLIGHT CHECKS ---")
    check_rclone()

    if not os.path.exists(LOCAL_DIR):
        print(f"ERROR: Local directory not found: {LOCAL_DIR}")
        sys.exit(1)
    print(f"  Local directory: {LOCAL_DIR}")

    if not os.path.exists(MANIFEST):
        print(f"ERROR: Manifest not found: {MANIFEST}")
        sys.exit(1)

    # Load manifest
    print("\n--- LOADING MANIFEST ---")
    with open(MANIFEST, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    print(f"  {len(rows)} files in manifest")

    # Get local PDF files
    local_pdfs = set()
    for fname in os.listdir(LOCAL_DIR):
        if fname.lower().endswith('.pdf'):
            local_pdfs.add(fname)
    print(f"  {len(local_pdfs)} PDF files in local directory")

    # Check what's already on Drive
    existing = list_existing_gdrive_files()

    # Determine what needs uploading
    to_upload = []
    already_done = []
    missing_local = []

    for row in rows:
        renamed = row.get('renamed_filename', '').strip()
        if not renamed:
            continue
        if renamed in existing:
            already_done.append(row)
        elif renamed in local_pdfs:
            to_upload.append(row)
        else:
            missing_local.append(row)

    print(f"\n--- UPLOAD PLAN ---")
    print(f"  Already on Drive: {len(already_done)}")
    print(f"  Need to upload:   {len(to_upload)}")
    print(f"  Missing locally:  {len(missing_local)}")

    if missing_local:
        print(f"\n  Warning: {len(missing_local)} files in manifest not found locally:")
        for row in missing_local[:5]:
            print(f"    - {row.get('renamed_filename', 'UNKNOWN')}")
        if len(missing_local) > 5:
            print(f"    ... and {len(missing_local) - 5} more")

    if not to_upload:
        print("\n  All files already uploaded. Nothing to do.")
        print("  Run update_gdrive_index.py to refresh the document index.")
        return

    # Confirm
    unique_permits = set(r['permit_number'] for r in to_upload)
    print(f"\n  Uploading {len(to_upload)} files ({len(unique_permits)} permits)")
    print(f"  Destination: {GDRIVE_REMOTE}")
    input("  Press Enter to start (Ctrl+C to cancel)...")

    # Upload
    print(f"\n--- UPLOADING ---")
    uploaded = 0
    failed = 0
    upload_results = []

    for i, row in enumerate(to_upload, 1):
        filename = row['renamed_filename']
        local_path = os.path.join(LOCAL_DIR, filename)
        remote_path = f"{GDRIVE_REMOTE}/{filename}"

        size_mb = os.path.getsize(local_path) / 1e6
        print(f"  [{i}/{len(to_upload)}] {filename} ({size_mb:.1f} MB)...", end=" ", flush=True)

        success, err = upload_file(local_path, remote_path)
        if success:
            uploaded += 1
            print("OK")
            upload_results.append({
                'filename': filename,
                'permit_number': row['permit_number'],
                'status': 'uploaded'
            })
        else:
            failed += 1
            print(f"FAILED: {err.strip()}")
            upload_results.append({
                'filename': filename,
                'permit_number': row['permit_number'],
                'status': 'failed',
                'error': err.strip()
            })

        time.sleep(PAUSE_BETWEEN_UPLOADS)

    # Get file IDs for all uploaded files
    print(f"\n--- FETCHING DRIVE FILE IDS ---")
    all_drive_files = list_existing_gdrive_files()

    # Update manifest with gdrive_link
    print(f"\n--- UPDATING MANIFEST ---")
    updated_count = 0
    for row in rows:
        filename = row.get('renamed_filename', '').strip()
        if filename and filename in all_drive_files:
            file_id = all_drive_files[filename]
            if file_id:
                row['gdrive_link'] = f"https://drive.google.com/file/d/{file_id}/view"
                updated_count += 1

    # Write updated manifest
    backup = MANIFEST.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    os.rename(MANIFEST, backup)
    print(f"  Backed up manifest to: {os.path.basename(backup)}")

    with open(MANIFEST, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Updated manifest: {updated_count} rows now have gdrive_link")

    # Save upload log
    log_file = os.path.join(REPO_ROOT, "Scripts",
                            f"upload_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(log_file, 'w') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'uploaded': uploaded,
            'failed': failed,
            'skipped_existing': len(already_done),
            'results': upload_results
        }, f, indent=2)
    print(f"  Upload log: {log_file}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Uploaded:         {uploaded}")
    print(f"  Failed:           {failed}")
    print(f"  Already on Drive: {len(already_done)}")
    print(f"  Manifest updated: {updated_count} rows with Drive links")
    print(f"\nNEXT STEP: Run the index updater to wire Drive URLs into the website:")
    print(f"  python3 Scripts/update_gdrive_index.py")
    print(f"\nDone at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
