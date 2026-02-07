#!/usr/bin/env python3
"""
Build comprehensive ordinance index for DADU eligibility
Maps ordinances to PDF links for DADU Overlays, UDOs, and SPs
"""

import urllib.request
import json
import os
from datetime import datetime

BASE_URL = "https://maps.nashville.gov/arcgis2/rest/services/Parcels/ParcelHistory/MapServer/5/query"

def fetch_all_records(where_clause, fields="ZoneCode,OrdinanceNumber,CaseNumber,url,Description"):
    """Fetch all records with pagination"""
    all_records = []
    offset = 0
    batch_size = 100

    while True:
        params = f"where={where_clause}&outFields={fields}&resultOffset={offset}&resultRecordCount={batch_size}&f=json"
        url = f"{BASE_URL}?{urllib.parse.quote(params, safe='=&')}"

        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = json.load(response)
        except Exception as e:
            print(f"Error fetching offset {offset}: {e}")
            break

        features = data.get('features', [])
        if not features:
            break

        all_records.extend(features)
        offset += batch_size

        if not data.get('exceededTransferLimit', False):
            break
        if offset > 200000:
            break

    return all_records

def build_ordinance_map(records, zone_type):
    """Build map of ordinance -> details"""
    ordinances = {}
    parcel_map = {}

    for f in records:
        a = f['attributes']
        ord_num = a.get('OrdinanceNumber', '')
        parcel_id = a.get('ParcelID')
        case_num = a.get('CaseNumber', '')
        url = a.get('url', '')
        desc = a.get('Description', '')

        if not ord_num:
            continue

        if ord_num not in ordinances:
            ordinances[ord_num] = {
                'ordinance': ord_num,
                'case_number': case_num,
                'zone_type': zone_type,
                'description': desc[:200] if desc else '',
                'url': url,
                'parcel_count': 0
            }
        ordinances[ord_num]['parcel_count'] += 1

        # Map parcel to ordinance
        if parcel_id:
            if parcel_id not in parcel_map:
                parcel_map[parcel_id] = []
            parcel_map[parcel_id].append({
                'ordinance': ord_num,
                'case': case_num,
                'type': zone_type,
                'url': url
            })

    return ordinances, parcel_map

def main():
    print("Building DADU Ordinance Index...")
    print("=" * 50)

    all_ordinances = {}
    all_parcel_maps = {}

    # 1. DADU Overlays
    print("\n1. Fetching DADU Overlays...")
    dadu_records = fetch_all_records("ZoneCode='OV-DDU'")
    print(f"   Found {len(dadu_records)} DADU overlay parcels")
    dadu_ords, dadu_parcels = build_ordinance_map(dadu_records, 'DADU_OVERLAY')
    all_ordinances.update(dadu_ords)
    all_parcel_maps.update(dadu_parcels)

    # 2. Urban Design Overlays
    print("\n2. Fetching Urban Design Overlays...")
    udo_records = fetch_all_records("ZoneCode='UDO' OR ZoneCode LIKE '%UDO%'")
    print(f"   Found {len(udo_records)} UDO parcels")
    udo_ords, udo_parcels = build_ordinance_map(udo_records, 'UDO')
    all_ordinances.update(udo_ords)
    for pid, ords in udo_parcels.items():
        if pid in all_parcel_maps:
            all_parcel_maps[pid].extend(ords)
        else:
            all_parcel_maps[pid] = ords

    # 3. Specific Plans
    print("\n3. Fetching Specific Plans...")
    sp_records = fetch_all_records("ZoneCode='SP'")
    print(f"   Found {len(sp_records)} SP parcels")
    sp_ords, sp_parcels = build_ordinance_map(sp_records, 'SP')
    all_ordinances.update(sp_ords)
    for pid, ords in sp_parcels.items():
        if pid in all_parcel_maps:
            all_parcel_maps[pid].extend(ords)
        else:
            all_parcel_maps[pid] = ords

    # Add BL2025-1007 (USD by-right)
    all_ordinances['BL2025-1007'] = {
        'ordinance': 'BL2025-1007',
        'case_number': 'USD-BY-RIGHT',
        'zone_type': 'USD_BY_RIGHT',
        'description': 'DADU permitted by right in Urban Services District for R/RS zones',
        'url': 'https://documents.nashville.gov/Request/Form/Legislation?legislationnumber=BL2025-1007',
        'parcel_count': 67707  # Approximate USD eligible count
    }

    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total unique ordinances: {len(all_ordinances)}")
    print(f"Total parcels with overlay/SP data: {len(all_parcel_maps)}")

    by_type = {}
    for ord_data in all_ordinances.values():
        t = ord_data['zone_type']
        by_type[t] = by_type.get(t, 0) + 1

    print("\nBy type:")
    for t, count in sorted(by_type.items()):
        print(f"  {t}: {count} ordinances")

    # Build output
    output = {
        'generated': datetime.now().isoformat(),
        'stats': {
            'total_ordinances': len(all_ordinances),
            'total_parcels_mapped': len(all_parcel_maps),
            'by_type': by_type
        },
        'ordinances': all_ordinances,
        # Note: parcel_map is too large for client-side use
        # We'll query the API directly for parcel-specific lookups
    }

    # Save ordinances index (smaller file for client use)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, 'ordinance_index.json')
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nSaved to: {output_file}")
    print(f"File size: {os.path.getsize(output_file) / 1024:.1f} KB")

if __name__ == '__main__':
    import urllib.parse
    main()
