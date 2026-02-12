#!/usr/bin/env python3
"""
build_apn_to_account.py

Reads assessor_accounts_20260114.csv and creates a JSON mapping from APN to ACCOUNTNUMBER.
Output: /Users/nataliebaldacci/DADU-Homebody-Projects/data/apn_to_account.json

APNs come in multiple formats:
  - 9-11 digit numeric: zero-padded to 11 digits for consistency
  - 14-17 char alphanumeric (e.g., 011150A00100CO): kept as-is
  - Scientific notation (e.g., 2E+11): SKIPPED (Excel corruption, ~207 rows)

The output JSON is a flat object: { "_total": N, "APN": "ACCOUNTNUMBER", ... }
"""

import csv
import json
import os
import sys

INPUT_CSV = "/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/assessor_accounts_20260114.csv"
OUTPUT_JSON = "/Users/nataliebaldacci/DADU-Homebody-Projects/data/apn_to_account.json"


def normalize_apn(raw_apn):
    """
    Normalize an APN value.
    - If purely numeric and 9-11 digits, zero-pad to 11 digits.
    - If alphanumeric (contains letters), keep as-is.
    - If scientific notation, return None (corrupted).
    """
    if "E+" in raw_apn or "e+" in raw_apn:
        return None

    stripped = raw_apn.strip()
    if not stripped:
        return None

    # Check if purely numeric
    if stripped.isdigit():
        if len(stripped) <= 11:
            return stripped.zfill(11)
        else:
            # Longer than 11 digits but still numeric -- keep as-is
            return stripped
    else:
        # Alphanumeric APN (e.g., 011150A00100CO) -- keep as-is
        return stripped


def main():
    if not os.path.exists(INPUT_CSV):
        print(f"ERROR: Input file not found: {INPUT_CSV}")
        sys.exit(1)

    mapping = {}
    skipped_sci = 0
    skipped_empty = 0
    skipped_dup = 0
    total_rows = 0

    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Verify expected columns
        if "APN" not in reader.fieldnames or "ACCOUNTNUMBER" not in reader.fieldnames:
            print(f"ERROR: Expected columns 'APN' and 'ACCOUNTNUMBER'. Found: {reader.fieldnames}")
            sys.exit(1)

        for row in reader:
            total_rows += 1
            raw_apn = row["APN"]
            account = row["ACCOUNTNUMBER"].strip()

            if not account:
                skipped_empty += 1
                continue

            normalized = normalize_apn(raw_apn)

            if normalized is None:
                if "E+" in raw_apn or "e+" in raw_apn:
                    skipped_sci += 1
                else:
                    skipped_empty += 1
                continue

            if normalized in mapping:
                # Keep the first occurrence (lower OBJECTID = more authoritative)
                skipped_dup += 1
                continue

            mapping[normalized] = account

    # Build output with _total metadata field first
    output = {"_total": len(mapping)}
    output.update(mapping)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, separators=(",", ":"))

    # Summary
    file_size_mb = os.path.getsize(OUTPUT_JSON) / (1024 * 1024)
    print(f"=== APN to ACCOUNTNUMBER Mapping ===")
    print(f"Input file:              {INPUT_CSV}")
    print(f"Output file:             {OUTPUT_JSON}")
    print(f"Total CSV rows:          {total_rows:,}")
    print(f"Mappings created:        {len(mapping):,}")
    print(f"Skipped (sci notation):  {skipped_sci:,}")
    print(f"Skipped (empty):         {skipped_empty:,}")
    print(f"Skipped (duplicate APN): {skipped_dup:,}")
    print(f"Output file size:        {file_size_mb:.2f} MB")
    print(f"Done.")


if __name__ == "__main__":
    main()
