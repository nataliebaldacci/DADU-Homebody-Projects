# TASK: Wire Document Images into Existing DADUs Map

The file `existing_dadus_map.html` shows completed DADU permits on a map but the popup cards have no photos, sketches, or document links. The data already exists in `data/gdrive_docs_index.json` (8,804 parcels). Wire it in.

## What gdrive_docs_index.json Contains

Structure: `{ "parcels": { "APN": { ... } } }`

Each parcel can have:

```json
{
  "property_cards": [{ "gdrive_url": "https://drive.google.com/file/d/.../view", "filename": "..." }],
  "assessor_cards": [{
    "type": "card2",
    "structure_type": "SINGLE FAMILY",
    "finished_area": "308",
    "card2_photo_url": "https://portal.padctn.org/OFS/WP/Image/GetPropertyImage?propertyID={ID}&card=2",
    "card2_sketch_url": "https://portal.padctn.org/OFS/WP/Image/GetSketchImage?propertyID={ID}&card=2",
    "card2_summary_url": "https://portal.padctn.org/OFS/WP/Summary/{ID}/2",
    "card2_buildingprint_url": "https://portal.padctn.org/OFS/WP/BuildingPrint/{ID}/2",
    "property_card_url": "https://portal.padctn.org/OFS/WP/Print/{ID}"
  }],
  "permits": [...],
  "covenants": [...]
}
```

4,238 parcels have Card2 photo and sketch URLs. 3,301 have property card PDFs. 2,370 have permit docs. 2,678 have covenants.

## What to Do

1. At page load, fetch `data/gdrive_docs_index.json` and store it as a lookup object (key = APN).

2. When a user clicks a DADU marker and the popup opens, look up that permit's APN in the docs index.

3. In the popup card, add these sections if data exists:

**Photo (from Card2):**
```html
<img src="{card2_photo_url}" alt="DADU Photo" style="width:100%; max-height:200px; object-fit:cover; border-radius:8px;">
```

**Sketch (from Card2):**
```html
<img src="{card2_sketch_url}" alt="Floor Plan Sketch" style="width:100%; max-height:180px; object-fit:contain; border-radius:8px; background:#f5f5f0;">
```

**Document Links row:**
- Property Card PDF → `property_card_url` or `property_cards[0].gdrive_url`
- Site Plan → `permits[0].gdrive_url` if exists, else `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT}`
- Covenant → `covenants[0].gdrive_url` if exists
- Card 2 Details → `card2_summary_url`

Style the links as small buttons in a row:
```css
.doc-link-btn {
  display: inline-block;
  padding: 4px 10px;
  font-size: 12px;
  border-radius: 4px;
  background: var(--linen, #F0EBE1);
  color: var(--slate, #3A5566);
  border: 1px solid rgba(62,74,79,.15);
  text-decoration: none;
  margin: 2px;
}
.doc-link-btn:hover { background: var(--wheat, #CBB279); color: white; }
```

4. If the APN has no docs in the index, show fallback links using URL patterns:
- Property Card: `https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}` (look up in `data/apn_to_account.json`)
- Permit Docs: `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT}`
- Street View: `https://www.google.com/maps?q&layer=c&cbll={LAT},{LON}`

5. Also load `data/apn_to_account.json` at page load for the account number lookups.

## APN Matching

The APN in the permit data might be formatted differently than in gdrive_docs_index.json. Try these lookups in order:
- Exact match
- Strip leading zeros and try again
- Pad to 11 digits with leading zeros and try again

## Important

- The gdrive_docs_index.json is ~9MB. Load it once at page init, not per popup.
- The Card2 photo/sketch URLs are Nashville server images. They load fast but may occasionally 404 for older properties. Add `onerror="this.style.display='none'"` on img tags.
- Do NOT change the map markers, filters, or data query. Only enhance the popup content.

## Branding
- Use Castlehold palette from homebody_shared.css
- No emoji
- Inter font

```bash
git add -A && git commit -m "Wire Card2 photos, sketches, and doc links into existing DADUs map popups" && git push origin main
```
