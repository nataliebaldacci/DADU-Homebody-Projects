#!/usr/bin/env python3
import re
from pathlib import Path

REPO = Path("/Users/nataliebaldacci/Desktop/Master_Data/DADU/DADU_Homebody/GitHub_Repo")

PAGES_TO_CHECK = [
    ("index.html", "Homepage with eligibility checker"),
    ("property_search.html", "Property search with map"),
    ("dadu_eligibility_map.html", "Interactive eligibility map"),
    ("dadu_opportunity_explorer_v2.html", "Opportunity explorer with scoring"),
    ("dadu_near_me_v2.html", "Find DADUs near location"),
    ("am_i_eligible.html", "Eligibility wizard"),
    ("nashville_permit_explorer_v3.html", "Permit explorer"),
    ("contractor_dashboard.html", "Contractor analytics"),
]

print("=" * 80)
print("LIVE PARCEL DATA PAGES IN YOUR GITHUB REPO")
print("=" * 80)

live_pages = []

for page, description in PAGES_TO_CHECK:
    filepath = REPO / page
    if not filepath.exists():
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for data references
    parcel_refs = re.findall(r'["\']([^"\']*(?:parcels|eligibility)[^"\']*\.(?:json|geojson))["\']', content)
    permit_refs = re.findall(r'["\']([^"\']*permit[^"\']*\.(?:json|geojson))["\']', content)
    
    has_map = 'leaflet' in content.lower() or 'L.map' in content
    has_data = bool(parcel_refs or permit_refs)
    
    if has_data:
        live_pages.append({
            'page': page,
            'desc': description,
            'map': has_map,
            'parcel': bool(parcel_refs),
            'permit': bool(permit_refs),
            'data_files': list(set(parcel_refs + permit_refs))[:3]
        })

for i, p in enumerate(live_pages, 1):
    print(f"\n{i}. {p['page']}")
    print(f"   {p['desc']}")
    features = []
    if p['map']:
        features.append("Interactive Map")
    if p['parcel']:
        features.append("Parcel Data")
    if p['permit']:
        features.append("Permit Data")
    print(f"   Features: {', '.join(features)}")
    if p['data_files']:
        print(f"   Data: {p['data_files'][0]}")

print(f"\n{'=' * 80}")
print(f"TOTAL: {len(live_pages)} pages with live parcel/permit data")
print("=" * 80)
