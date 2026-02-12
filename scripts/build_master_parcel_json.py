#!/usr/bin/env python3
"""
Build master_parcel_data.json — the single JSON file powering
Castlehold property reports, document lookups, and permit displays.

Join logic:
  confirmed_dadu_permits.csv  (APN)
    → Parcels_Dual_Cards_With_URLs.csv  (APN → ACCOUNTNUMBER, Card2 URLs, structures)
    → permits_adu_accessory_enriched.csv  (APN + PermitNumber → broader permit history)
    → dadu_trade_permits.csv  (parent_permit_number → trade sub-permits)
    → gdrive_docs_index.json  (APN → Google Drive PDF links)
"""

import csv
import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# ── Paths ──
BASE = Path("/Users/nataliebaldacci/DADU-Homebody-Projects")
DADU = BASE / "DADU"
FF = DADU / "FINAL_FINAL"

CONFIRMED_PERMITS = FF / "confirmed_dadu_permits.csv"
DUAL_CARDS = FF / "Parcels_Dual_Cards_With_URLs.csv"
PERMITS_ENRICHED = FF / "permits_adu_accessory_enriched.csv"
TRADE_PERMITS = DADU / "DADU_Trade_Permits" / "dadu_trade_permits.csv"
GDRIVE_INDEX = BASE / "data" / "gdrive_docs_index.json"
OUTPUT = BASE / "data" / "master_parcel_data.json"


def normalize_apn(apn):
    """Normalize APN to 11 digits, zero-padded."""
    if not apn:
        return None
    cleaned = re.sub(r'[^0-9]', '', str(apn))
    if not cleaned or len(cleaned) < 5:
        return None
    if len(cleaned) <= 11:
        return cleaned.zfill(11)
    return cleaned[:11]


def safe_float(val):
    """Convert to float, return None on failure."""
    try:
        v = float(val)
        return v if v == v else None  # NaN check
    except (ValueError, TypeError):
        return None


def safe_int(val):
    """Convert to int, return None on failure."""
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return None


def epoch_to_date(epoch_str):
    """Convert epoch milliseconds to YYYY-MM-DD."""
    try:
        ts = int(float(epoch_str)) / 1000
        return datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    except (ValueError, TypeError):
        return None


def main():
    parcels = {}  # APN → parcel dict

    # ═══════════════════════════════════════════
    # 1. Load confirmed DADU permits (primary seed)
    # ═══════════════════════════════════════════
    print(f"Loading confirmed DADU permits from {CONFIRMED_PERMITS}")
    permit_count = 0
    with open(CONFIRMED_PERMITS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            apn = normalize_apn(row.get('APN', ''))
            if not apn:
                continue

            if apn not in parcels:
                parcels[apn] = {
                    'address': '',
                    'parcelId': '',
                    'accountNumber': '',
                    'cx': None,
                    'cy': None,
                    'structures': {},
                    'card2_images': {},
                    'permits': [],
                    'tradePermits': [],
                    'documents': {},
                    'urls': {}
                }

            p = parcels[apn]

            # Use address from permit if we don't have one yet
            addr = (row.get('ADDRESS') or row.get('LOCATION') or '').strip()
            if addr and not p['address']:
                p['address'] = addr

            pid = (row.get('ParcelID') or '').strip()
            if pid and not p['parcelId']:
                p['parcelId'] = pid

            # Coordinates
            cx = safe_float(row.get('CX'))
            cy = safe_float(row.get('CY'))
            if cx and cy and not p['cx']:
                p['cx'] = cx
                p['cy'] = cy

            # Build permit entry
            case_number = (row.get('CASE_NUMBER') or '').strip()
            permit_entry = {
                'number': case_number,
                'type': (row.get('CASE_TYPE_DESC') or '').strip(),
                'subType': (row.get('SUB_TYPE_DESC') or '').strip(),
                'status': (row.get('STATUS_CODE') or '').strip(),
                'dateAccepted': epoch_to_date(row.get('DATE_ACCEPTED')),
                'dateIssued': epoch_to_date(row.get('DATE_ISSUED')),
                'dateFinal': epoch_to_date(row.get('FINALDATE')),
                'value': safe_float(row.get('CONSTVAL')),
                'sqft': safe_int(row.get('BLDG_SQ_FT')),
                'scope': (row.get('SCOPE') or '').strip(),
                'contact': (row.get('CONTACT') or '').strip(),
                'source': 'confirmed_dadu',
                'epermitsUrl': (row.get('epermits') or '').strip()
            }

            # Avoid duplicate permits
            existing_numbers = {pp['number'] for pp in p['permits']}
            if case_number and case_number not in existing_numbers:
                p['permits'].append(permit_entry)
                permit_count += 1

    print(f"  Loaded {permit_count} permits across {len(parcels)} parcels")

    # ═══════════════════════════════════════════
    # 2. Join Parcels_Dual_Cards_With_URLs
    # ═══════════════════════════════════════════
    print(f"\nJoining dual card data from {DUAL_CARDS}")
    joined_cards = 0
    with open(DUAL_CARDS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            apn = normalize_apn(row.get('APN', ''))
            if not apn or apn not in parcels:
                continue

            p = parcels[apn]
            joined_cards += 1

            # Account number (critical for property card URLs)
            acct = (row.get('ACCOUNTNUMBER') or '').strip()
            if acct:
                p['accountNumber'] = acct

            # Parcel ID
            pid = (row.get('ParcelID') or '').strip()
            if pid:
                p['parcelId'] = pid

            # Card 1 (primary structure)
            st1 = (row.get('StructureType1') or '').strip()
            if st1:
                p['structures']['card1'] = {
                    'type': st1,
                    'area': safe_int(row.get('FinishedArea1')),
                    'exterior': (row.get('Exterior1') or '').strip(),
                    'yearBuilt': safe_int(row.get('YearBuilt1')),
                    'footprintArea': safe_float(row.get('Shape__Area1'))
                }

            # Card 2 (secondary structure / potential DADU)
            st2 = (row.get('StructureType2') or '').strip()
            if st2:
                p['structures']['card2'] = {
                    'type': st2,
                    'area': safe_int(row.get('FinishedArea2')),
                    'exterior': (row.get('Exterior2') or '').strip(),
                    'yearBuilt': safe_int(row.get('YearBuilt2')),
                    'footprintArea': safe_float(row.get('Shape__Area2'))
                }

            # Card 2 images
            photo = (row.get('Card2_Photo_URL') or '').strip()
            sketch = (row.get('Card2_Sketch_URL') or '').strip()
            if photo or sketch:
                p['card2_images'] = {}
                if photo:
                    p['card2_images']['photo'] = photo
                if sketch:
                    p['card2_images']['sketch'] = sketch

            # Build URLs
            p['urls']['summary'] = (row.get('Summary_URL') or '').strip()
            p['urls']['propertyCard'] = (row.get('PropertyCard_URL') or '').strip()
            p['urls']['card2Summary'] = (row.get('Card2_Summary_URL') or '').strip()
            p['urls']['card2BuildingPrint'] = (row.get('Card2_BuildingPrint_URL') or '').strip()

            # Standard external URLs
            if acct:
                p['urls']['propertyCardPdf'] = f"https://portal.padctn.org/OFS/WP/Print/{acct}"
            if pid:
                p['urls']['parcelViewer'] = f"https://maps.nashville.gov/ParcelViewer/?parcelID={pid}"
            p['urls']['assessor'] = f"https://davidson-tn-citizen.comper.info/template.aspx?propertyID={apn}"
            p['urls']['parcelDocs'] = f"https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={apn}"

    print(f"  Joined {joined_cards} parcels with dual card data")

    # ═══════════════════════════════════════════
    # 3. Enrich with broader permit history
    # ═══════════════════════════════════════════
    print(f"\nEnriching with broader permit history from {PERMITS_ENRICHED}")
    enriched_count = 0
    with open(PERMITS_ENRICHED, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            apn = normalize_apn(row.get('APN', ''))
            if not apn or apn not in parcels:
                continue

            p = parcels[apn]
            permit_num = (row.get('PermitNumber') or '').strip()
            if not permit_num:
                continue

            # Check if we already have this permit
            existing_numbers = {pp['number'] for pp in p['permits']}
            if permit_num in existing_numbers:
                continue

            permit_entry = {
                'number': permit_num,
                'type': (row.get('PermitType') or '').strip(),
                'subType': (row.get('PermitSubType') or '').strip(),
                'dateIssued': (row.get('DateIssued') or '').strip(),
                'location': (row.get('Location') or '').strip(),
                'purpose': (row.get('Purpose') or '').strip()[:200],  # Truncate long scope text
                'contractor': (row.get('Contractor') or '').strip(),
                'value': safe_float(row.get('Value')),
                'status': (row.get('Status') or '').strip(),
                'matchKeyword': (row.get('MATCH_KEYWORD') or '').strip(),
                'sqft': safe_int(row.get('BLDG_SQ_FT')),
                'source': 'enriched'
            }

            # Use address from enriched if we don't have one
            loc = (row.get('Location') or '').strip()
            if loc and not p['address']:
                p['address'] = loc

            p['permits'].append(permit_entry)
            enriched_count += 1

    print(f"  Added {enriched_count} additional permits from enriched data")

    # ═══════════════════════════════════════════
    # 4. Join trade permits
    # ═══════════════════════════════════════════
    print(f"\nJoining trade permits from {TRADE_PERMITS}")
    # Build lookup: parent_permit_number → list of trade permits
    # Then match to our parcels via permit numbers
    trade_by_parent = defaultdict(list)
    with open(TRADE_PERMITS, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            parent_num = (row.get('parent_permit_number') or '').strip()
            if not parent_num:
                continue
            trade_entry = {
                'number': (row.get('trade_permit_number') or '').strip(),
                'parentPermit': parent_num,
                'type': (row.get('trade_type') or '').strip(),
                'description': (row.get('trade_description') or '').strip(),
                'applicant': (row.get('applicant') or '').strip(),
                'status': (row.get('status') or '').strip(),
                'issuedDate': (row.get('issued_date') or '').strip()[:10],  # Just date part
                'address': (row.get('address') or '').strip()
            }
            trade_by_parent[parent_num].append(trade_entry)

    print(f"  Loaded {sum(len(v) for v in trade_by_parent.values())} trade permits for {len(trade_by_parent)} parent permits")

    # Match trade permits to parcels
    trade_matched = 0
    for apn, p in parcels.items():
        for permit in p['permits']:
            pnum = permit['number']
            if pnum in trade_by_parent:
                p['tradePermits'].extend(trade_by_parent[pnum])
                trade_matched += len(trade_by_parent[pnum])

    print(f"  Matched {trade_matched} trade permits to parcels")

    # ═══════════════════════════════════════════
    # 5. Merge Google Drive document links
    # ═══════════════════════════════════════════
    docs_merged = 0
    if GDRIVE_INDEX.exists():
        print(f"\nMerging Google Drive documents from {GDRIVE_INDEX}")
        with open(GDRIVE_INDEX, 'r') as f:
            gdrive = json.load(f)

        gdrive_parcels = gdrive.get('parcels', {})
        for apn, p in parcels.items():
            if apn in gdrive_parcels:
                p['documents'] = gdrive_parcels[apn]
                doc_count = sum(len(v) for v in gdrive_parcels[apn].values() if isinstance(v, list))
                docs_merged += doc_count

        print(f"  Merged {docs_merged} documents for parcels in index")
    else:
        print(f"\n  WARNING: {GDRIVE_INDEX} not found, skipping document merge")

    # ═══════════════════════════════════════════
    # 6. Build permit URL links for each permit
    # ═══════════════════════════════════════════
    for apn, p in parcels.items():
        for permit in p['permits']:
            pnum = permit.get('number', '')
            if pnum and not permit.get('epermitsUrl'):
                permit['epermitsUrl'] = f"https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={pnum}"

    # ═══════════════════════════════════════════
    # 7. Clean up empty fields and write output
    # ═══════════════════════════════════════════
    # Remove empty structures, card2_images, tradePermits
    for apn, p in parcels.items():
        if not p['structures']:
            del p['structures']
        if not p.get('card2_images'):
            if 'card2_images' in p:
                del p['card2_images']
        if not p['tradePermits']:
            del p['tradePermits']
        if not p['documents']:
            del p['documents']
        # Clean up empty URL entries
        p['urls'] = {k: v for k, v in p['urls'].items() if v}

    # Summary stats
    has_permits = sum(1 for p in parcels.values() if p.get('permits'))
    has_structures = sum(1 for p in parcels.values() if p.get('structures'))
    has_card2 = sum(1 for p in parcels.values() if p.get('card2_images'))
    has_trades = sum(1 for p in parcels.values() if p.get('tradePermits'))
    has_docs = sum(1 for p in parcels.values() if p.get('documents'))
    total_permits = sum(len(p.get('permits', [])) for p in parcels.values())
    total_trades = sum(len(p.get('tradePermits', [])) for p in parcels.values())

    output = {
        '_schema_version': '1.0',
        '_description': 'Master parcel data powering Castlehold property reports',
        '_generated': datetime.now().isoformat(),
        '_stats': {
            'total_parcels': len(parcels),
            'parcels_with_permits': has_permits,
            'parcels_with_structures': has_structures,
            'parcels_with_card2_images': has_card2,
            'parcels_with_trade_permits': has_trades,
            'parcels_with_documents': has_docs,
            'total_permits': total_permits,
            'total_trade_permits': total_trades,
            'total_documents': docs_merged
        },
        'parcels': parcels
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w') as f:
        json.dump(output, f, indent=2)

    size_mb = OUTPUT.stat().st_size / 1024 / 1024
    print(f"\n{'='*50}")
    print(f"MASTER PARCEL DATA BUILT SUCCESSFULLY")
    print(f"{'='*50}")
    print(f"  Output: {OUTPUT}")
    print(f"  File size: {size_mb:.2f} MB")
    print(f"  Total parcels: {len(parcels)}")
    print(f"  With permits: {has_permits}")
    print(f"  With structures: {has_structures}")
    print(f"  With Card2 images: {has_card2}")
    print(f"  With trade permits: {has_trades}")
    print(f"  With GDrive docs: {has_docs}")
    print(f"  Total permits: {total_permits}")
    print(f"  Total trade permits: {total_trades}")
    print(f"  Total documents: {docs_merged}")


if __name__ == '__main__':
    main()
