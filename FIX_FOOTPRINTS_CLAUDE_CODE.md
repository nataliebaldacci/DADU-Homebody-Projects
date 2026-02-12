# FIX BUILDING FOOTPRINTS — PASTE THIS INTO CLAUDE CODE

## THE ROOT CAUSE
Building footprints do not render on the deployed site. The code queries Nashville's 
MapServer (maps.nashville.gov) which blocks CORS from GitHub Pages. The fetch fails 
silently — no error shown, no footprints drawn.

## THE FIX
Replace ALL Nashville MapServer footprint URLs with the Vanderbilt-hosted FeatureServer.
This server returns `Access-Control-Allow-Origin: *` (verified).

### The working endpoint:
```
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0/query
```

### Why this one (not Building_Footprints_SingleFamily):
- Footprints_With_ParcelData has an **APN field** for direct filtering
- No spatial query needed — just `where=APN='09305019400'`
- Also has: Nash_BldgType, Nash_Area, Nash_Height, StructureType, YearBuilt, Exterior, 
  Nash_RoofType, AssessorCardNumber, Footprint_Rank, FinishedArea, FEMA_SqFt
- Building_Footprints_SingleFamily does NOT have APN — requires spatial query

### Query parameters that work:
```
where=APN='{APN}'
outFields=APN,Nash_BldgType,Nash_Area,Nash_Height,Nash_RoofType,StructureType,FinishedArea,YearBuilt,Exterior,AssessorCardNumber,Footprint_Rank,FEMA_SqFt
returnGeometry=true
outSR=4326
f=geojson
```

### Verified working example:
```
curl "https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0/query?where=APN%3D%2709305019400%27&outFields=*&returnGeometry=true&outSR=4326&f=geojson"
```
Returns GeoJSON FeatureCollection with polygon geometries.

## IMPLEMENTATION STEPS

### Step 1: Find and replace the broken URL
In property_search.html and dadu_property_viewer_v3.html, search for:
- `maps.nashville.gov/arcgis/rest/services/Planimetric/Buildings/MapServer`
- `maps.nashville.gov` (any building/footprint-related fetch)
- Any reference to `dadu_footprints.geojson` (local file may not be in the repo)

Replace with the Vanderbilt URL above.

### Step 2: Replace the query function
The footprint loading function should look like this:

```javascript
async function loadBuildingFootprints(apn) {
  const FOOTPRINTS_URL = 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0/query';
  
  const params = new URLSearchParams({
    where: `APN='${apn}'`,
    outFields: 'APN,Nash_BldgType,Nash_Area,Nash_Height,Nash_RoofType,StructureType,FinishedArea,YearBuilt,Exterior,AssessorCardNumber,Footprint_Rank,FEMA_SqFt',
    returnGeometry: 'true',
    outSR: '4326',
    f: 'geojson'
  });
  
  try {
    const resp = await fetch(`${FOOTPRINTS_URL}?${params}`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();
    
    if (!data.features || data.features.length === 0) {
      console.warn('No footprints found for APN:', apn);
      return;
    }
    
    // Deduplicate: keep only unique Footprint_Rank values
    // (Card 1 and Card 2 both appear but share same geometry)
    const seen = new Set();
    const unique = data.features.filter(f => {
      const rank = f.properties.Footprint_Rank;
      if (seen.has(rank)) return false;
      seen.add(rank);
      return true;
    });
    data.features = unique;
    
    // Add to map
    const footprintLayer = L.geoJSON(data, {
      style: function(feature) {
        const isAccessory = isAccessoryStructure(feature.properties);
        return {
          color: '#333333',
          weight: 2,
          fillColor: isAccessory ? '#C58B2A' : '#555555',  // ochre for accessory, dark gray for primary
          fillOpacity: 0.65
        };
      },
      onEachFeature: function(feature, layer) {
        const p = feature.properties;
        const isAcc = isAccessoryStructure(p);
        const area = p.Nash_Area ? Math.round(p.Nash_Area) : (p.FEMA_SqFt ? Math.round(p.FEMA_SqFt) : '—');
        
        layer.bindPopup(`
          <div style="font-family:Inter,system-ui,sans-serif;">
            <b style="color:${isAcc ? '#C58B2A' : '#3A5566'}">
              ${isAcc ? 'Accessory Structure' : 'Primary Structure'}
            </b><br>
            Type: ${p.Nash_BldgType || '—'}<br>
            Structure: ${p.StructureType || '—'}<br>
            Footprint: ${area} SF<br>
            Height: ${p.Nash_Height ? Math.round(p.Nash_Height) + ' ft' : '—'}<br>
            Year Built: ${p.YearBuilt ? Math.round(p.YearBuilt) : '—'}<br>
            Roof: ${p.Nash_RoofType || '—'}
          </div>
        `);
        
        layer.on('mouseover', function() { this.setStyle({ fillOpacity: 0.85, weight: 3 }); });
        layer.on('mouseout', function() { this.setStyle({ fillOpacity: 0.65, weight: 2 }); });
      }
    }).addTo(map);
    
    return footprintLayer;
    
  } catch (err) {
    console.error('Failed to load footprints:', err);
    return null;
  }
}

function isAccessoryStructure(props) {
  const rank = props.Footprint_Rank;
  if (rank && rank > 1) return true;
  const type = (props.Nash_BldgType || '').toLowerCase();
  return type.includes('minor') || type.includes('accessory') || type.includes('shed') || type.includes('garage');
}
```

### Step 3: Call it when a parcel is selected
Wherever the existing code handles parcel selection (after geocoding an address or 
clicking a parcel on the map), call `loadBuildingFootprints(apn)` with the parcel's APN.

The APN comes from whatever parcel lookup is already working — the eligibility layer, 
the geocoder result, or the clicked parcel feature.

### Step 4: Update sidebar with building summary
After footprints load, show in sidebar:
- Total buildings count (X primary, Y accessory)
- Total footprint area
- Available yard area (lot SF minus total footprint)
- Max DADU size (700 SF if lot < 10K; 850 SF if lot >= 10K)

### Step 5: Test and push
Test: Search "1000 17th Ave S Nashville TN" — buildings should render on the parcel.
Test: Search an APN directly like "09305019400" — should work.
Push to GitHub.

## CRITICAL RULES
1. Do NOT use maps.nashville.gov for ANY client-side fetch. CORS is blocked.
2. Do NOT rely on dadu_footprints.geojson existing in the repo (it may be gitignored due to size).
3. The Vanderbilt FeatureServer (services3.arcgis.com) DOES allow CORS. Use it.
4. Query by APN string, NOT spatial envelope. The APN field is on Footprints_With_ParcelData.
5. Deduplicate results — each physical building appears twice (Card 1 and Card 2).
6. Footprint_Rank=1 is the largest building (usually main house). Higher ranks are smaller structures.

## FILES TO MODIFY
- property_search.html
- dadu_property_viewer_v3.html
- Any other file that references Nashville buildings MapServer or dadu_footprints.geojson

## WHAT SUCCESS LOOKS LIKE
When a user searches an address or APN:
1. Parcel boundary appears (dashed outline)
2. Building footprints appear ON the parcel as filled polygons
3. Primary structures in dark gray, accessory/DADU in ochre
4. Click any building → popup with type, area, height, year built
5. Sidebar shows building summary with area calculations
