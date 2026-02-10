#!/usr/bin/env python3
import re
from pathlib import Path

REPO = Path("/Users/nataliebaldacci/Desktop/Master_Data/DADU/DADU_Homebody/GitHub_Repo")

# Pages that should have parcel data
PAGES_TO_CHECK = [
    "index.html",
    "property_search.html",
    "dadu_eligibility_map.html",
    "dadu_opportunity_explorer_v2.html",
    "dadu_near_me_v2.html",
    "am_i_eligible.html",
    "nashville_permit_explorer_v3.html",
    "contractor_dashboard.html",
    "dadu_property_viewer_v3.html",
]

print("=" * 80)
print("LIVE PARCEL DATA PAGES")
print("=" * 80)

for page in PAGES_TO_CHECK:
    filepath = REPO / page
    if not filepath.exists():
        print(f"\n✗ {page} - FILE NOT FOUND")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for parcel data references
    parcel_refs = re.findall(r'["\']([^"\']*(?:parcels|eligibility)[^"\']*\.(?:json|geojson))["\']', content)
    permit_refs = re.findall(r'["\']([^"\']*permit[^"\']*\.(?:json|geojson))["\']', content)
    
    # Check for Leaflet map
    has_map = 'leaflet' in content.lower() or 'L.map' in content
    
    # Check for interactive features
    has_search = 'search' in content.lower() and ('input' in content.lower() or 'filter' in content.lower())
    has_filters = 'filter' in content.lower() and ('checkbox' in content.lower() or 'radio' in content.lower() or 'select' in content.lower())
    
    if parcel_refs or permit_refs:
        print(f"\n✓ {page}")
        if has_map:
            print(f"  🗺️  Interactive Map: YES")
        if parcel_refs:
            print(f"  📊 Parcel Data: {', '.join(set(parcel_refs)[:2])}")
        if permit_refs:
            print(f"  🏗️  Permit Data: {', '.join(set(permit_refs)[:2])}")
        if has_search:
            print(f"  🔍 Search: YES")
        if has_filters:
            print(f"  🎛️  Filters: YES")
    else:
        print(f"\n⚠️  {page} - No parcel/permit data found")

print("\n" + "=" * 80)
