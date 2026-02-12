# CLAUDE CODE TASK: Build the Permit Explorer + Wire Documents + Fix Map Layers

**Author:** Natalie Baldacci
**Date:** February 12, 2026
**Repo:** ~/DADU-Homebody-Projects/
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/

---

## WHAT I NEED BUILT

I need a **Permit Explorer** page that displays all DADU permits on an interactive map, with each permit linking to its documents (site plan PDFs, property card images, permit PDFs) and external Nashville portals. I also need the eligibility map layers, building footprint layers, and restrictive covenant layers actually rendering on the site. Right now most map pages show blank white boxes.

This is ONE task with FOUR connected pieces:

1. **Permit Explorer map page** with all permits plotted, filterable, and linked to documents
2. **Document wiring** so permit PDFs, property cards, site plans, and covenant PDFs are accessible from permit cards and property reports
3. **Eligibility map layers** (green/yellow/red parcels) actually rendering
4. **Restrictive covenants map layer** integrated into the site

---

## CASTLEHOLD BRANDING (LOCKED — USE EXACTLY THESE COLORS)

```css
:root {
  --midnight: #003039;    /* Primary dark — nav bars, headers, hero backgrounds */
  --graphite: #3E4A4F;    /* Secondary dark — body text, secondary headers */
  --steel:    #537188;    /* Mid-tone — secondary text, icon backgrounds, borders */
  --wheat:    #CBB279;    /* Accent — CTAs, highlights, stat numbers, hover states */
  --cream:    #E1D4BB;    /* Light surface — card backgrounds, light accents */
  --linen:    #F0EBE1;    /* Page background — body background, dropdown panels */
}
```

| Name | Hex | Role |
|------|-----|------|
| Midnight | `#003039` | Primary dark: nav, headers, hero |
| Graphite | `#3E4A4F` | Secondary dark: text, subheaders |
| Steel Blue | `#537188` | Mid-tone: borders, icon bg, secondary text |
| Wheat | `#CBB279` | Accent: CTAs, highlights, stat numbers |
| Cream | `#E1D4BB` | Light surface: cards, light accents |
| Linen | `#F0EBE1` | Background: page bg, dropdowns |

**Font:** Inter (primary), system sans-serif fallback
**Logo text:** CASTLEHOLD
**DO NOT USE:** terracotta, sage, green, ochre, orange, teal, or any color not listed above.

---

## PIECE 1: PERMIT EXPLORER PAGE

### Data Source
Primary: `DADU_All_Permits_Cleaned.csv` (6,822 permits, in the repo root)
ArcGIS: `DADU_All_Permits_Final` at https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_All_Permits_Final/FeatureServer/0

### What the Page Must Do
- Display ALL permits as markers on a Leaflet map (use the ArcGIS FeatureServer, NOT Nashville MapServer which blocks CORS)
- Color-code markers by status. Use these Castlehold-compatible marker colors:
  - Completed/DONE = `#2E6F4E` (status green, used only for eligibility/completion indicators)
  - Issued/Active = `#537188` (Steel Blue)
  - Expired = `#CBB279` (Wheat)
  - Revoked = `#7A2A1D` (Oxide Red, restriction indicator only)
- Clicking a permit marker opens a popup or sidebar card showing:
  - Address
  - Permit number
  - Status
  - Date issued / date completed
  - Contractor name (CONTRACTOR_BIZ_NAME_ORIGINAL field)
  - Cost (if available)
  - Square footage (if available)
  - Cost per SF (calculated if both cost and SF exist)
- Each permit card must have action buttons:
  - **View Site Plan PDF** → links to the permit PDF if we have one (from Google Drive folder `1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4` or from documents.nashville.gov)
  - **View Property Card** → links to property card image (from Google Drive folder `1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ`) OR to PADCTN portal at `https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}` using the APN-to-ACCOUNTNUMBER mapping from `assessor_accounts_20260114.csv`
  - **Open in ePermits** → `https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}`
  - **View Permit Documents** → `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}`
  - **Open ParcelViewer** → `https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}`
  - **View Property Report** → links to property_search.html?apn={APN} or the Property Report Card page

### UI Styling for Permit Explorer
- Nav bar: `background: var(--midnight)` with `color: var(--linen)`
- Page background: `var(--linen)`
- Sidebar/filter panel: `background: white` or `var(--cream)` with `border: 1px solid rgba(62,74,79,.12)`
- Cards: white background, `border-radius: 16px`, subtle shadow `0 10px 25px rgba(0,0,0,.06)`
- Action buttons: `background: var(--wheat); color: var(--midnight)` for primary, `background: transparent; border: 1px solid var(--steel)` for secondary
- Stats bar numbers: `color: var(--wheat)` on dark background or `color: var(--midnight)` on light
- Filter labels: `color: var(--graphite)`
- Headings: `color: var(--midnight); font-family: Inter`

### Filters (sidebar or top bar)
- Permit status (Completed, Issued, Expired, All)
- Date range (year picker or slider)
- Cost range (slider or presets: Under $100K, $100-200K, $200-300K, $300K+)
- Square footage range (Under 500, 500-750, 750-1000, 1000+)
- Contractor name (searchable dropdown of real contractors from the data)
- Address search (text input that filters or geocodes)

### Stats Bar
Show summary stats that update as filters change:
- Total permits shown
- Average cost
- Average square footage
- Average cost per SF
- Most active contractor in filtered set

### Sort Options for List View
- Newest first / Oldest first
- Highest cost / Lowest cost
- Largest / Smallest

### File Name
`permit_explorer.html` (new file, do not overwrite any existing files)

---

## PIECE 2: WIRE IN THE DOCUMENTS

### Document Sources

**Permit PDFs (site plans):**
- Google Drive folder: `1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4`
- 630 permit PDFs downloaded
- Filename pattern: `{uuid}_CA-Permits-{date}_{id}_{page}.pdf`
- Also available at: `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}`

**Property Cards:**
- Google Drive folder: `1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ` (3,358 merged cards)
- Card 2 images: 8,074 downloaded (not yet in Drive)
- Filename pattern: `PropertyCard_{APN}_{ACCOUNTNUMBER}.pdf`
- Also available at: `https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}`
- Mapping file: `assessor_accounts_20260114.csv` (column USER_ACCOUNT = APN, column ACCOUNTNUMBER = account number)

**Restrictive Covenants:**
- Google Drive folder: `1bEZN1kEZxqZLkdX0QjT0g9N7K0sXAy3Z` (8,514 PDFs)
- Filename pattern: instrument number as filename (e.g., `20240710-0051719.pdf`)
- ArcGIS layer with links: https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer/0

**UDO Overlay PDFs:**
- Google Drive folder: `1evPTz2SvAIDS74lwzgxjGF85kl2nDsrh`

**DADU Overlay PDFs:**
- Google Drive folder: `1KDQe3WhWz1H1ukTIlAfxtbDFmvX50kYu`

**Aerial Screenshots:**
- Google Drive folder: `1eD1TUNuYMOMK7VdVJW3Pc6mHYFS02VUj` (698 screenshots)

### What Must Happen

1. **Create a document index JSON** (`data/docs_index.json`) that maps each permit's APN to its available documents. Structure:
```json
{
  "09500021900": {
    "permit_pdfs": [
      {"filename": "...", "drive_url": "https://drive.google.com/file/d/{FILE_ID}/view", "nashville_url": "https://documents.nashville.gov/..."}
    ],
    "property_cards": [
      {"filename": "PropertyCard_09500021900_123456.pdf", "drive_url": "...", "padctn_url": "https://portal.padctn.org/OFS/WP/Print/123456"}
    ],
    "covenants": [
      {"instrument": "20240710-0051719", "drive_url": "...", "register_url": "..."}
    ],
    "aerials": [{"drive_url": "..."}],
    "overlay_docs": [{"type": "UDO", "drive_url": "..."}, {"type": "DADU", "drive_url": "..."}]
  }
}
```

2. **For permit PDFs we don't have locally**, the permit card should link to Nashville's document portal: `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}` as fallback.

3. **For property cards**, use the APN-to-ACCOUNTNUMBER mapping to generate the PADCTN URL as primary link: `https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}`. Google Drive link as secondary.

4. **Overlay documents** (UDO and DADU overlay design PDFs) should appear in the Document Portal and in Property Report Cards for parcels in overlay zones. These are general reference documents, not parcel-specific. They should appear in a "Zoning & Overlay Documents" section.

5. **Connect the Document Portal** (`dadu_documents_portal.html`) to actually search and filter by APN, address, document type, and permit number using the docs_index.json.

### APN-to-ACCOUNTNUMBER Mapping
The file `assessor_accounts_20260114.csv` has these columns:
- `USER_ACCOUNT` = APN (the parcel number we use everywhere)
- `ACCOUNTNUMBER` = the account number needed for property card URLs

Create `data/apn_to_account.json` mapping APN → ACCOUNTNUMBER for use in link builders.

---

## PIECE 3: FIX ELIGIBILITY MAP LAYERS

### The Problem
The eligibility map should show green/yellow/red parcels. The data exists in multiple forms:
- Local GeoJSON files in the repo: `eligibility_green.geojson`, `eligibility_red.geojson`, `eligibility_yellow.geojson`, `eligibility_by_right.geojson`, `eligibility_usd.geojson`, `eligibility_points.geojson`
- ArcGIS FeatureServer: `DADU_Eligibility_ENHANCED` at https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer/0
- The `permits_data.geojson` file also exists locally

### What Must Happen
1. The eligibility map page (`dadu_eligibility_map.html`) must render with actual colored parcels
2. Use the ArcGIS FeatureServer as primary source (161,703 parcels, CORS-friendly from services3.arcgis.com)
3. Green = eligible (R/RS zoning in USD), Yellow = conditional (R/RS in GSD, needs overlay), Red/Gray = not eligible
4. Clicking a parcel shows: address, APN, zoning, lot size, eligibility status, max DADU size, and a "View Full Report" link
5. The local GeoJSON files can serve as fallback or for fast initial loading of simplified point data
6. Do NOT load all 161K parcels at once. Use ArcGIS spatial queries with the current map extent, or use the point GeoJSON for overview and polygon queries on click/zoom

### Eligibility Map Styling
- Use the Castlehold palette for all chrome (nav, panels, buttons, text)
- The map marker/parcel colors for eligibility status are functional, not brand colors:
  - Eligible: `#2E6F4E` (green)
  - Conditional: `#D4A017` (amber)
  - Not eligible: `#8B8B8B` (gray)
- Legend panel: `background: white; border-radius: var(--radius)`
- Info popups: `background: white` with `border-top: 3px solid var(--wheat)`

### Additional Map Layers to Connect
On the eligibility map or on dedicated map pages, also connect:
- **Building footprints**: https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Building_Footprints_SingleFamily/FeatureServer/0 or Footprints_With_ParcelData at https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0
- **Permit markers**: DADU_All_Permits_Final at https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_All_Permits_Final/FeatureServer/0
- Do NOT use maps.nashville.gov URLs (CORS blocked from GitHub Pages)

---

## PIECE 4: RESTRICTIVE COVENANTS MAP LAYER

### ArcGIS Layers Available
- Parcels with CR (parcel polygons): https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Parcels_with_CR__A1_AP43711_wk1ztG/FeatureServer/0
- Alternate parcels layer: https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer/0
- Covenant Links (points with PDF URLs): https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer/0

### Existing ArcGIS Web Map
https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=168e16cf3b08411296759cf39f22dc6d

### What Must Happen
1. Add a covenants layer toggle on the eligibility map or permit explorer (or both) so users can see which parcels have recorded covenants
2. Style covenant parcels with a distinct dashed border in `var(--wheat)` (#CBB279) so they're visible alongside the eligibility colors
3. Clicking a covenant parcel should show the instrument number and a link to the covenant PDF (from the Covenant Links layer which has URLs)
4. Alternatively, embed or iframe the existing ArcGIS web map if direct integration is too complex for a first pass
5. The covenants should also appear in Property Report Cards: when a user looks up a property, show whether it has a recorded restrictive covenant and link to the document

---

## CRITICAL TECHNICAL RULES

1. **CORS**: Only use services3.arcgis.com or services2.arcgis.com URLs for ArcGIS queries from GitHub Pages. Do NOT use maps.nashville.gov (CORS blocked). Do NOT use any Nashville MapServer endpoint for client-side fetch.
2. **Pagination**: ArcGIS FeatureServer queries have maxRecordCount limits (usually 1000-2000). Always paginate with resultOffset and resultRecordCount, or use objectId paging.
3. **No huge GeoJSON at page load**: Do not load all 161K parcels or 327K footprints at once. Use spatial queries with map extent, or load point data for overview and detail on interaction.
4. **File naming**: New files get new names. Do not overwrite existing files. Use pattern `dadu_[feature]_[version].html`.
5. **Branding**: Use Castlehold branding EXACTLY as specified in the CASTLEHOLD BRANDING section above. Midnight `#003039`, Graphite `#3E4A4F`, Steel Blue `#537188`, Wheat `#CBB279`, Cream `#E1D4BB`, Linen `#F0EBE1`. Font: Inter. Logo text: CASTLEHOLD. Do NOT use terracotta, sage, green, ochre, orange, teal, or any other colors not in the locked palette.
6. **No fake data**: All contractor names, costs, and permit details must come from DADU_All_Permits_Cleaned.csv or the ArcGIS permit layer. Do not invent any data.
7. **External links**: Always provide the Nashville portal fallback links even if we don't have a local PDF. The link templates are:
   - ParcelViewer: `https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}`
   - Permit Documents: `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}`
   - ePermits: `https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}`
   - Property Assessor: `https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}`
   - Property Card: `https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}`
8. **GitHub Pages compatible**: All client-side JavaScript. No server-side code. No API keys exposed.

---

## VANDERBILT ARCGIS LAYER URLS (CORS-FRIENDLY)

```
DADU_Eligibility_ENHANCED:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer/0

DADU_All_Permits_Final:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_All_Permits_Final/FeatureServer/0

DADU_Building_Specs:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Building_Specs_20260119_042856/FeatureServer/0

Building_Footprints_SingleFamily:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Building_Footprints_SingleFamily/FeatureServer/0

Footprints_With_ParcelData:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0

Parcels_with_Restrictive_Covenants:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer/0

Restrictive_Covenant_Links:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer/0

Parcels_with_CR:
https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Parcels_with_CR__A1_AP43711_wk1ztG/FeatureServer/0
```

---

## LOCAL GEOJSON FILES IN REPO

```
eligibility_red.geojson
eligibility_yellow.geojson
eligibility_green.geojson
permits_data.geojson
eligibility_by_right.geojson
eligibility_usd.geojson
eligibility_points.geojson
dadu_footprints.geojson (4.4MB)
```

---

## GOOGLE DRIVE DOCUMENT FOLDERS

| Folder | Drive ID | Contents |
|--------|----------|----------|
| Permit PDFs | 1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4 | 630 permit/site plan PDFs |
| Property Cards | 1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ | 3,358 merged property cards |
| Restrictive Covenants | 1bEZN1kEZxqZLkdX0QjT0g9N7K0sXAy3Z | 8,514 covenant PDFs |
| Aerials | 1eD1TUNuYMOMK7VdVJW3Pc6mHYFS02VUj | 698 aerial screenshots |
| UDO Overlay PDFs | 1evPTz2SvAIDS74lwzgxjGF85kl2nDsrh | UDO overlay design docs |
| DADU Overlay PDFs | 1KDQe3WhWz1H1ukTIlAfxtbDFmvX50kYu | DADU overlay design docs |
| STR Permits | 1_JGdEdlUS7IGWi4L93aSGOhHWZJfktql | STR permit docs |
| Zoning Board Appeals | 1bjNIPyogxImJ5_zxnxKTmxlYCmO0clvH | ZBA decision docs |

---

## DELIVERABLES

1. `permit_explorer.html` — Full permit explorer with map, filters, document links
2. `data/docs_index.json` — Document index mapping APNs to available PDFs
3. `data/apn_to_account.json` — APN to ACCOUNTNUMBER mapping for property card links
4. `data/contractor_stats.json` — Real contractor data from permits CSV
5. Fix `dadu_eligibility_map.html` to actually render colored parcels
6. Add restrictive covenants layer toggle to eligibility map
7. Connect `dadu_documents_portal.html` to search docs_index.json
8. Add overlay document sections (UDO/DADU overlay PDFs) to Document Portal and Property Report Cards

### For Each Deliverable Provide:
- Exact file path relative to repo root
- Complete code (no partial snippets)
- Notes on what data sources it connects to
- Test checklist (what to search, what should appear)

---

## PRIORITY ORDER

Start with the Permit Explorer page (Piece 1) because it's the most visible new feature. Then wire in documents (Piece 2) since the Permit Explorer needs document links. Then fix the eligibility map (Piece 3). Then add covenants (Piece 4). Each piece should work independently even if the others aren't done yet, using Nashville portal fallback links where local documents aren't available.
