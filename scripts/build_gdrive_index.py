#!/usr/bin/env python3
"""
Transform gdrive_pdf_mapping.json into an APN-keyed document index
with Google Drive URLs for the Homebody document portal.
"""

import json
import re
import csv
from pathlib import Path
from collections import defaultdict

# Paths
GDRIVE_MAPPING = Path("/Users/nataliebaldacci/Desktop/Master_Data/DADU/MASTER_ADU_DATA/gdrive_pdf_mapping.json")
COVENANTS_CSV = Path("/Users/nataliebaldacci/Desktop/Master_Data/DADU/MASTER_ADU_DATA/Covenants_Final_With_APN_PDF.csv")
OUTPUT_FILE = Path("/Users/nataliebaldacci/DADU-Homebody-Projects/data/gdrive_docs_index.json")

def extract_apn_from_filename(filename):
    """Extract APN from filename patterns like PropertyCard_12500000600_139023.pdf"""
    patterns = [
        r'PropertyCard_(\d{11})_\d+\.pdf',
        r'Assessor_(\d{11})_\d+\.pdf',
        r'(\d{11})_PropertyCard\.pdf',
        r'(\d{11})_Assessor\.pdf',
        r'(\d{11})_Covenant.*\.pdf',
        r'(\d{11})_Permit.*\.pdf',
        r'(\d{11})_.*\.pdf',
    ]

    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            return match.group(1)
    return None

def determine_doc_type(filepath):
    """Determine document type from filepath"""
    filepath_lower = filepath.lower()

    if 'propertycard' in filepath_lower or 'property_card' in filepath_lower:
        return 'property_card'
    elif 'assessor' in filepath_lower:
        return 'assessor_card'
    elif 'covenant' in filepath_lower:
        return 'covenant'
    elif 'permit' in filepath_lower:
        return 'permit'
    elif 'aerial' in filepath_lower or 'screenshot' in filepath_lower:
        return 'aerial'
    elif 'site_plan' in filepath_lower or 'siteplan' in filepath_lower:
        return 'site_plan'
    else:
        return 'other'

def normalize_apn(apn):
    """Normalize APN to 11 digits"""
    if not apn:
        return None
    # Remove non-numeric characters except for condo suffixes
    cleaned = re.sub(r'[^0-9A-Za-z]', '', str(apn))
    # If it's 11 digits, return as-is
    if len(cleaned) == 11 and cleaned.isdigit():
        return cleaned
    # Pad with zeros if shorter
    if len(cleaned) < 11 and cleaned.isdigit():
        return cleaned.zfill(11)
    return cleaned if len(cleaned) >= 5 else None

def main():
    print(f"Loading Google Drive mapping from {GDRIVE_MAPPING}")

    with open(GDRIVE_MAPPING) as f:
        gdrive_mapping = json.load(f)

    print(f"Found {len(gdrive_mapping)} documents in mapping")

    # Build instrument to gdrive mapping for covenants
    instrument_to_gdrive = {}
    for filepath, gdrive_info in gdrive_mapping.items():
        if 'Restrictive_Covenants' in filepath or 'Covenant' in filepath:
            filename = Path(filepath).name
            # Extract instrument number from filename (e.g., 202311280091686.pdf)
            instrument = filename.replace('.pdf', '').replace('.PDF', '')
            instrument_to_gdrive[instrument] = gdrive_info

    print(f"Found {len(instrument_to_gdrive)} covenant documents in Drive")

    # Build APN-keyed index
    apn_docs = defaultdict(lambda: {
        'property_cards': [],
        'assessor_cards': [],
        'covenants': [],
        'permits': [],
        'aerials': [],
        'site_plans': [],
        'other': []
    })

    matched = 0
    unmatched = 0

    # Process property cards and other documents
    for filepath, gdrive_info in gdrive_mapping.items():
        filename = Path(filepath).name
        apn = extract_apn_from_filename(filename)

        if apn:
            doc_type = determine_doc_type(filepath)

            # Skip covenants here - we'll handle them from CSV
            if doc_type == 'covenant':
                continue

            doc_entry = {
                'filename': filename,
                'gdrive_url': gdrive_info['url'],
                'download_url': gdrive_info['download_url'],
                'file_id': gdrive_info['file_id']
            }

            # Add to appropriate category
            if doc_type == 'property_card':
                apn_docs[apn]['property_cards'].append(doc_entry)
            elif doc_type == 'assessor_card':
                apn_docs[apn]['assessor_cards'].append(doc_entry)
            elif doc_type == 'permit':
                apn_docs[apn]['permits'].append(doc_entry)
            elif doc_type == 'aerial':
                apn_docs[apn]['aerials'].append(doc_entry)
            elif doc_type == 'site_plan':
                apn_docs[apn]['site_plans'].append(doc_entry)
            else:
                apn_docs[apn]['other'].append(doc_entry)

            matched += 1
        else:
            unmatched += 1

    print(f"Matched {matched} property/permit docs to APNs")

    # Process covenants from CSV
    covenant_count = 0
    if COVENANTS_CSV.exists():
        print(f"\nLoading covenant mapping from {COVENANTS_CSV}")
        with open(COVENANTS_CSV, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                apn = normalize_apn(row.get('APN', ''))
                instrument = row.get('Instrument_Clean', '').strip()
                has_pdf = row.get('has_pdf', '').lower() == 'true'

                if apn and instrument and has_pdf:
                    # Look up Google Drive info
                    if instrument in instrument_to_gdrive:
                        gdrive_info = instrument_to_gdrive[instrument]
                        doc_entry = {
                            'filename': f"{instrument}.pdf",
                            'instrument': instrument,
                            'rec_date': row.get('Rec. Date', ''),
                            'grantor': row.get('Grantor', ''),
                            'gdrive_url': gdrive_info['url'],
                            'download_url': gdrive_info['download_url'],
                            'file_id': gdrive_info['file_id']
                        }
                        apn_docs[apn]['covenants'].append(doc_entry)
                        covenant_count += 1

        print(f"Matched {covenant_count} covenants to APNs with Google Drive links")

    print(f"\nTotal parcels with documents: {len(apn_docs)}")

    # Build output structure
    output = {
        '_schema_version': '1.0',
        '_description': 'Google Drive document index keyed by APN',
        '_total_parcels': len(apn_docs),
        '_total_documents': matched + covenant_count,
        'parcels': dict(apn_docs)
    }

    # Count by type
    type_counts = defaultdict(int)
    for apn, docs in apn_docs.items():
        for doc_type, doc_list in docs.items():
            type_counts[doc_type] += len(doc_list)

    output['_document_counts'] = dict(type_counts)

    print(f"\nDocument counts by type:")
    for doc_type, count in sorted(type_counts.items()):
        print(f"  {doc_type}: {count}")

    # Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nWrote {OUTPUT_FILE}")
    print(f"File size: {OUTPUT_FILE.stat().st_size / 1024 / 1024:.2f} MB")

if __name__ == '__main__':
    main()
