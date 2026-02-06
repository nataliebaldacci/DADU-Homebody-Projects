#!/usr/bin/env python3
"""
Build document indices for Homebody Platform.

Transforms documents_index.json into:
1. docs_index.json - Flat document list with metadata
2. parcels_docs_summary.json - Parcel-keyed summaries

Usage:
    python3 build_document_indices.py
"""

import json
import re
import os
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "documents_index.json"
DOCS_INDEX_OUTPUT = DATA_DIR / "docs_index.json"
PARCELS_SUMMARY_OUTPUT = DATA_DIR / "parcels_docs_summary.json"


def extract_covenant_date(filename):
    """Extract date from covenant filename like 08216018700_Covenant_201910100104029.pdf"""
    match = re.search(r'_Covenant_(\d{8})', filename)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')
        except ValueError:
            pass
    return None


def extract_instrument_number(filename):
    """Extract instrument number from covenant filename."""
    match = re.search(r'_Covenant_(\d+)\.pdf', filename)
    if match:
        return match.group(1)
    return None


def build_covenant_url(instrument_number):
    """Build URL to covenant document image."""
    if not instrument_number or len(instrument_number) < 8:
        return None
    year = instrument_number[:4]
    mmdd = instrument_number[4:8]
    return f"https://davidsonportal.com/landrecords/view_image.php?key=/img/tn/davidson/{year}/{mmdd}/{instrument_number}.tif"


def build_property_card_url(apn):
    """Build URL to property card. Note: ACCOUNTNUMBER is different from APN."""
    # Property cards use ACCOUNTNUMBER, not APN - return placeholder
    return f"https://portal.padctn.org/OFS/WP/Print/{{ACCOUNTNUMBER}}"


def classify_document(filename):
    """Classify document type based on filename."""
    filename_lower = filename.lower()

    if 'covenant' in filename_lower:
        return 'covenant', 'restrictive_covenant'
    elif 'assessor' in filename_lower:
        return 'property_card', 'assessor_card'
    elif 'propertycard' in filename_lower or 'property_card' in filename_lower:
        return 'property_card', 'property_record'
    elif 'screenshot' in filename_lower or 'aerial' in filename_lower:
        return 'aerial', 'aerial_image'
    elif any(x in filename_lower for x in ['permit', 'bl', 'el', 'pl', 'me']):
        return 'permit', 'building_permit'
    else:
        return 'unknown', 'unknown'


def build_docs_index(source_data):
    """Build flat document index."""
    documents = []
    doc_counter = 1

    for apn, parcel_docs in source_data.items():
        # Process property cards
        for filename in parcel_docs.get('property_cards', []):
            doc_type, doc_subtype = classify_document(filename)
            documents.append({
                "doc_id": f"DOC_{doc_counter:06d}",
                "filename": filename,
                "filepath": f"/documents/property_cards/{filename}",
                "doc_type": doc_type,
                "doc_subtype": doc_subtype,
                "title": f"Property Card - {apn}",
                "extracted_apn": apn,
                "normalized_apn": apn,
                "apn_confidence": "high",
                "linked_parcel_id": apn,
                "link_method": "apn_exact_match",
                "link_confidence": "high",
                "requires_manual_review": False
            })
            doc_counter += 1

        # Process covenants
        for filename in parcel_docs.get('covenants', []):
            doc_type, doc_subtype = classify_document(filename)
            instrument = extract_instrument_number(filename)
            date_filed = extract_covenant_date(filename)
            url = build_covenant_url(instrument) if instrument else None

            documents.append({
                "doc_id": f"DOC_{doc_counter:06d}",
                "filename": filename,
                "filepath": f"/documents/covenants/{filename}",
                "doc_type": doc_type,
                "doc_subtype": doc_subtype,
                "title": f"Restrictive Covenant - {apn}",
                "extracted_apn": apn,
                "normalized_apn": apn,
                "apn_confidence": "high",
                "instrument_number": instrument,
                "date_filed": date_filed,
                "document_url": url,
                "linked_parcel_id": apn,
                "link_method": "apn_exact_match",
                "link_confidence": "high",
                "requires_manual_review": False
            })
            doc_counter += 1

        # Process aerials
        for filename in parcel_docs.get('aerials', []):
            doc_type, doc_subtype = classify_document(filename)
            documents.append({
                "doc_id": f"DOC_{doc_counter:06d}",
                "filename": filename,
                "filepath": f"/documents/aerials/{filename}",
                "doc_type": "aerial",
                "doc_subtype": "aerial_image",
                "title": f"Aerial Image - {apn}",
                "extracted_apn": apn,
                "normalized_apn": apn,
                "apn_confidence": "high",
                "linked_parcel_id": apn,
                "link_method": "apn_exact_match",
                "link_confidence": "high",
                "requires_manual_review": False
            })
            doc_counter += 1

        # Process permits
        for filename in parcel_docs.get('permits', []):
            doc_type, doc_subtype = classify_document(filename)
            documents.append({
                "doc_id": f"DOC_{doc_counter:06d}",
                "filename": filename,
                "filepath": f"/documents/permits/{filename}",
                "doc_type": "permit",
                "doc_subtype": "building_permit",
                "title": f"Permit - {apn}",
                "extracted_apn": apn,
                "normalized_apn": apn,
                "apn_confidence": "high",
                "linked_parcel_id": apn,
                "link_method": "apn_exact_match",
                "link_confidence": "high",
                "requires_manual_review": False
            })
            doc_counter += 1

    return {
        "_schema_version": "1.0",
        "_description": "Document index for the Homebody Document Portal. All documents are indexed here with metadata for search and parcel linking.",
        "_generated": datetime.now().isoformat(),
        "_total_documents": len(documents),
        "documents": documents,
        "doc_types": {
            "permit": {
                "subtypes": ["building_permit", "electrical_permit", "plumbing_permit", "mechanical_permit", "demolition_permit"],
                "icon": "Building and Construction.png",
                "color": "#6b8e4e"
            },
            "property_card": {
                "subtypes": ["assessor_card", "property_record"],
                "icon": "Property Detail Report .png",
                "color": "#6b8fa3"
            },
            "deed": {
                "subtypes": ["warranty_deed", "quitclaim_deed", "trust_deed"],
                "icon": "Recorded Docs.png",
                "color": "#c9a86c"
            },
            "covenant": {
                "subtypes": ["restrictive_covenant", "hoa_rules", "easement"],
                "icon": "Legal.png",
                "color": "#c0392b"
            },
            "survey": {
                "subtypes": ["boundary_survey", "site_plan", "topographic"],
                "icon": "Surveyers adn Engineers.png",
                "color": "#9b59b6"
            },
            "aerial": {
                "subtypes": ["aerial_image", "satellite", "drone"],
                "icon": "Aerial.png",
                "color": "#3498db"
            },
            "inspection": {
                "subtypes": ["building_inspection", "final_inspection", "code_violation"],
                "icon": "Municipal.png",
                "color": "#f39c12"
            }
        },
        "matching_rules": {
            "apn_patterns": [
                "^(\\d{11})$",
                "^(\\d{3})[-_](\\d{2})[-_](\\d{3})[-_](\\d{2})[-_](\\d{3})$",
                "^([A-Z0-9]{13,15})$"
            ],
            "permit_patterns": [
                "^(\\d{4})(BL|EL|PL|ME)(\\d{5,6})$",
                "^(T)(\\d{4})[-_](\\d{5})$"
            ]
        }
    }


def build_parcels_summary(source_data, docs_index):
    """Build parcel-keyed document summary."""
    # Build a lookup from apn to documents
    docs_by_apn = {}
    for doc in docs_index['documents']:
        apn = doc['linked_parcel_id']
        if apn not in docs_by_apn:
            docs_by_apn[apn] = []
        docs_by_apn[apn].append(doc)

    parcels = {}

    for apn, parcel_docs in source_data.items():
        # Count documents by type
        property_card_count = len(parcel_docs.get('property_cards', []))
        covenant_count = len(parcel_docs.get('covenants', []))
        aerial_count = len(parcel_docs.get('aerials', []))
        permit_count = len(parcel_docs.get('permits', []))
        total = property_card_count + covenant_count + aerial_count + permit_count

        if total == 0:
            continue

        # Get document details from docs_index
        apn_docs = docs_by_apn.get(apn, [])

        # Build documents_by_type structure
        documents_by_type = {
            "permit": {"count": 0, "docs": []},
            "property_card": {"count": 0, "docs": []},
            "covenant": {"count": 0, "docs": []},
            "deed": {"count": 0, "docs": []},
            "survey": {"count": 0, "docs": []},
            "aerial": {"count": 0, "docs": []},
            "inspection": {"count": 0, "docs": []}
        }

        for doc in apn_docs:
            doc_type = doc['doc_type']
            if doc_type in documents_by_type:
                documents_by_type[doc_type]['count'] += 1
                documents_by_type[doc_type]['docs'].append({
                    "doc_id": doc['doc_id'],
                    "title": doc['title'],
                    "filename": doc['filename'],
                    "filepath": doc['filepath'],
                    "date": doc.get('date_filed'),
                    "document_url": doc.get('document_url')
                })

        parcels[apn] = {
            "apn": apn,
            "total_documents": total,
            "last_updated": datetime.now().strftime('%Y-%m-%d'),
            "documents_by_type": documents_by_type,
            "has_dadu_permit": permit_count > 0,
            "has_covenant": covenant_count > 0,
            "has_aerial": aerial_count > 0
        }

    return {
        "_schema_version": "1.0",
        "_description": "Parcel-keyed document summary for fast rendering in Property Report Card and parcel detail views. Keyed by normalized APN.",
        "_generated": datetime.now().isoformat(),
        "_total_parcels": len(parcels),
        "_document_counts": {
            "property_cards": sum(1 for p in parcels.values() if p['documents_by_type']['property_card']['count'] > 0),
            "covenants": sum(1 for p in parcels.values() if p['has_covenant']),
            "aerials": sum(1 for p in parcels.values() if p['has_aerial']),
            "permits": sum(1 for p in parcels.values() if p['has_dadu_permit'])
        },
        "parcels": parcels
    }


def main():
    print(f"Loading source data from {INPUT_FILE}...")
    with open(INPUT_FILE, 'r') as f:
        source_data = json.load(f)

    print(f"Found {len(source_data)} parcels in source data")

    print("Building docs_index.json...")
    docs_index = build_docs_index(source_data)
    print(f"Created {docs_index['_total_documents']} document records")

    print("Building parcels_docs_summary.json...")
    parcels_summary = build_parcels_summary(source_data, docs_index)
    print(f"Created {parcels_summary['_total_parcels']} parcel summaries")

    print(f"Writing {DOCS_INDEX_OUTPUT}...")
    with open(DOCS_INDEX_OUTPUT, 'w') as f:
        json.dump(docs_index, f, indent=2)

    print(f"Writing {PARCELS_SUMMARY_OUTPUT}...")
    with open(PARCELS_SUMMARY_OUTPUT, 'w') as f:
        json.dump(parcels_summary, f, indent=2)

    print("Done!")
    print(f"\nSummary:")
    print(f"  Documents indexed: {docs_index['_total_documents']}")
    print(f"  Parcels with documents: {parcels_summary['_total_parcels']}")
    print(f"  Parcels with covenants: {parcels_summary['_document_counts']['covenants']}")
    print(f"  Parcels with aerials: {parcels_summary['_document_counts']['aerials']}")


if __name__ == "__main__":
    main()
