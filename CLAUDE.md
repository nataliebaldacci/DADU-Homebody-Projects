# CASTLEHOLD / HOMEBODY BUILDER — CLAUDE CODE INSTRUCTIONS
**Version:** 3.0 | **Date:** February 12, 2026
**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Repo:** /Users/nataliebaldacci/DADU-Homebody-Projects/
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/

---

## 1. WHAT THIS PROJECT IS

Castlehold is a DADU (Detached Accessory Dwelling Unit) zoning and buildability intelligence platform for Nashville-Davidson County. It aggregates public parcel data, permit records, restrictive covenants, and regulatory information into a GitHub Pages website. Nashville's BL2025-1007 legislation (effective December 12, 2025) expanded DADU eligibility to 67,707 parcels, making this an ideal proof of concept for national scaling.

Brand architecture: Castlehold is the authority/data layer. Homebody Builder is the consumer-facing product.

---

## 2. CRITICAL RULES — READ BEFORE TOUCHING ANYTHING

1. **Audit first.** Before making any changes, run the audit commands in Section 12 and show output.
2. **Never invent data sources, endpoints, URLs, or field names.** Verify them first.
3. **Never delete, rename, or move existing files.** Create new versions if needed (e.g., v4 suffix).
4. **Never overwrite output files.** Every new output must have a unique name.
5. **Do not modify anything in /samples/.** It is a read-only design reference library.
6. **No sensitive keys in the repo.** Propose a serverless proxy if a key is required.
7. **Complete code only.** When writing code, provide the entire file. No partial snippets.
8. **Script format for Python:** Use the copy-paste terminal format:
   ```
   python3 << 'EOF'
   # complete script here
   EOF
   ```
9. **ArcGIS pagination:** Always handle maxRecordCount using resultOffset/resultRecordCount loops.
10. **Nashville server rate limiting:** Use 1-2 second delays and 30-second timeouts. Servers hang without warning.

---

## 3. BRAND SYSTEM (LOCKED — DO NOT CHANGE)

### Color Palette
```css
:root {
  --navy: #3A5566;           /* Deep Slate — primary, headings, nav */
  --navy-dark: #2E4553;      /* Darker Slate */
  --navy-light: #4A6B7D;     /* Lighter Slate */
  --teal: #7B746D;           /* Warm Stone — secondary UI, subtitles */
  --teal-light: #918A83;     /* Lighter Stone */
  --terracotta: #C58B2A;     /* Ochre — accent, use sparingly */
  --terracotta-hover: #A8761F;
  --terracotta-light: #D4A54E;
  --tan: #7B746D;            /* Warm Stone alt */
  --tan-light: #918A83;
  --background: #F2F0ED;     /* Page background */
  --card-bg: #f5f5f0;        /* Card surfaces */
  --error: #7A2A1D;          /* Oxide Red — restrictions/legal only */
  --status-eligible: #2E6F4E; /* Green — eligibility UI states only */
}
```

**CRITICAL:** The CSS variable names say "teal" and "terracotta" for backward compatibility. The actual colors are Warm Stone and Ochre. There is NO teal or green in the brand palette. Do not introduce any teal (#6b8fa3) or green (#6b8e4e) colors.

### Old Colors to Find and Replace
| Old Hex | New Hex | What Changed |
|---------|---------|-------------|
| #2c3e50 | #3A5566 | Navy to Deep Slate |
| #34495e | #4A6B7D | Nav hover |
| #1a252f | #2E4553 | Dark backgrounds |
| #6b8fa3 | #7B746D | Teal to Warm Stone |
| #6b8e4e | #3A5566 | Green accent to Slate |
| #c9a86c | #7B746D | Tan to Warm Stone |
| #e8e4df | #F2F0ED | Background lightened |
| #B55A3C | #C58B2A | Terracotta to Ochre |

### Typography
- Font: Inter (primary), Montserrat (fallback), system sans-serif
- Headlines: 700-800 weight
- Body: 400-500 weight
- No em dashes. Break long sentences into two.

### Logo
- File: `assets/castlehold-logo.png` (two castles in tan and slate blue with "CASTLEHOLD" text)
- Display at 50-60px height in nav bar
- SVG icon versions in `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/All_Icons/Icons/SVG_Originals/`

---

## 4. NAVIGATION STRUCTURE (LOCKED — DO NOT CHANGE)

### Top Bar Layout
```
LOGO | EXPLORE ▾ | BUILD ▾ | DATA ▾ | PRICING | 🔍 Search | My Projects | Get Started →
```

### Routing
- LOGO → index.html
- Search 🔍 → property_search.html
- My Projects → project_planner.html (placeholder for now)
- Get Started → am_i_eligible.html

### EXPLORE Dropdown (3 columns)

**Column 1: Learn**
| Label | File |
|-------|------|
| What is a DADU? | what_is_dadu.html |
| History & Timeline | dadu_history.html |
| Requirements | dadu_building_requirements.html |
| Zoning Standards | dadu_zoning_standards.html |
| Code & Legislation | dadu_code_legislation_v3.html |
| Permit Process | permit_process_timeline.html |

**Column 2: Discover**
| Label | File |
|-------|------|
| Eligibility Map | dadu_eligibility_map.html |
| Property Search | property_search.html |
| DADUs Near Me | dadu_near_me_v2.html |
| Opportunity Explorer | dadu_opportunity_explorer_v2.html |

**Column 3: User Types**
| Label | File |
|-------|------|
| Homeowner | user-homeowners.html |
| Contractor | contractor_marketplace.html |
| Designer/Architect | designer_resources.html |
| Municipal/Agency | municipal_dashboard.html |
| Legal/Appraiser | legal_resources.html |

**NO Developer/Investor in User Types.**

### BUILD Dropdown (4 columns)

**Column 1: Plan**
| Label | File |
|-------|------|
| Project Planner | project_planner.html |
| Interactive Checklist | project_checklist.html |
| Draw DADU on Parcel | draw_dadu_on_parcel.html |

**Column 2: Design & Calculate**
| Label | File |
|-------|------|
| Site Plan Finder | site_plan_downloads.html |
| Cost Estimator | project_cost_estimator.html |
| ROI Calculator | roi_calculator.html |
| Size Calculator | size_calculator.html |
| Property Tax Calculator | property_tax_calculator.html |

**Column 3: Hire**
| Label | File |
|-------|------|
| Contractor Marketplace | contractor_marketplace.html |

**NO "Contractor Finder" — use Contractor Marketplace only.**

**Column 4: File**
| Label | File |
|-------|------|
| Determine Forms Required | determine_forms_required.html |
| Form Filler | legal_form_filler.html |
| Owner Occupancy | owner_occupancy.html |
| STR Permit | str_permit.html |

### DATA Dropdown (3 columns)

**Column 1: Activity**
| Label | File |
|-------|------|
| Permit Dashboard | permit_activity_dashboard.html |
| Contractor Dashboard | contractor_dashboard.html |
| Market Trends | market_trends.html |

**Column 2: Reports**
| Label | File |
|-------|------|
| Eligibility Report | eligibility_report.html |
| Property Intelligence | property-report-card.html |
| Project Report | project_report.html |
| Contractor Report | dadu_reports_store.html |
| Market Analysis | dadu_reports_store.html |
| Area Analysis | dadu_reports_store.html |

**Column 3: Records**
| Label | File |
|-------|------|
| Permit Explorer | nashville_permit_explorer_v3.html |
| Permit Site Plans | site_plan_downloads.html |
| Recorded Documents | dadu_documents_portal.html |
| Restrictive Covenants | restrictive_covenants_v2.html |
| Zoning Documents | overlay-districts.html |
| PDF Database | pdf_database_lookup.html |

### PRICING
Direct link to homebody_pricing.html. No dropdown.

---

## 5. CURRENT STATE — WHAT EXISTS

### Shared Components (Created by Claude Code)
- `homebody_shared.css` — Global stylesheet with Castlehold :root variables and mega-menu CSS
- `homebody_header.js` — Shared nav component injected via `<div id="site-header"></div>`
- `homebody_header.html` — Shared header template

### Live Pages on GitHub Pages (~95+ HTML files)
The site is deployed at https://nataliebaldacci.github.io/DADU-Homebody-Projects/

**Homepage:** index.html (Castlehold branded, 3 user-type cards, eligibility map hero)

**Maps & Explorers (20 files):**
dadu_eligibility_map.html, parcel_footprint_map.html, property_search.html, dadu_explorer.html (+ v2, v3), dadu_explorer_attom.html (+ v2), dadu_near_me.html (+ v2, locator), dadu_property_viewer_v3.html, dadu_property_explorer.html (+ v2, v3), dadu_opportunity_explorer_v2.html, adu_opportunity_explorer.html, nashville_permit_explorer_v3.html, adu_permit_map.html, secondary_structures_map.html

**Calculators & Planning (8 files):**
roi_calculator.html, project_cost_estimator.html, property_tax_calculator.html, size_calculator.html, project_checklist.html, project_planner.html, draw_dadu_on_parcel.html, site_plan_downloads.html

**Reports & Pricing (5 files):**
eligibility_report.html, project_report.html, dadu_reports_store.html, reports_pricing.html, homebody_pricing.html

**Legal & Forms (5 files):**
determine_forms_required.html, legal_form_filler.html, restrictive_covenants_v2.html, dadu_documents_portal.html, pdf_database_lookup.html

**Dashboards (4 files):**
contractor_dashboard.html, permit_activity_dashboard.html, nashville_permit_analytics.html, contractor_marketplace.html

**Learn & Reference (14 files):**
what_is_dadu.html, dadu_building_requirements.html, dadu_design_standards.html, dadu_zoning_standards.html, permit_process_timeline.html, dadu_history.html, owner_occupancy.html, short_term_rental_permit.html, str_permit.html, trade_permits.html, overlay-districts.html, dadu_code_legislation_v3.html, dadu_legal_citations.html, dadu_legislation.html

**User Type Pages (3 files):**
user-homeowners.html, user-types.html, features.html

**Feature Landing Pages (3 files):**
feature-documents.html, feature-eligibility-map.html, feature-property-search.html

**Contractor & Advertising (3 files):**
contractor_advertising.html, dadu_contractors_infographic.html, designer_resources.html

**Other (7 files):**
about_platform_infographic.html, dadu_resources.html, legal_resources.html, market_trends.html, municipal_dashboard.html, homebody_dadu_pricing.html, property_report.html

**Older/Duplicate Versions (10+ files):**
Multiple v1/v2 duplicates of explorers, build tools, reports, and platform pages. Do not delete these but do not link to them in navigation.

---

## 6. WHAT NEEDS TO BE FINISHED — PRIORITY ORDER

### PRIORITY 1: Fix Branding Consistency Across All Pages
**Status:** Partially done. Some pages still have old colors (#2c3e50, #6b8e4e, #e8e4df) in inline CSS.

**Tasks:**
1. Run a grep across all HTML files for old color hex codes (see Section 3 replacement table)
2. Replace all instances with Castlehold palette equivalents
3. Ensure every page loads `homebody_shared.css` and uses CSS variables instead of hardcoded colors
4. Verify the shared header (homebody_header.js) is injected on every page
5. Replace all "Homebody Projects" branding text with "Castlehold" in page titles and headers
6. Confirm logo displays at correct size (50-60px) on every page

**Verification commands:**
```bash
# Find pages still using old colors
grep -rl "#2c3e50\|#6b8e4e\|#e8e4df\|#6b8fa3\|#c9a86c" *.html | wc -l

# Find pages missing shared CSS
for f in *.html; do grep -qL "homebody_shared.css" "$f" && echo "MISSING CSS: $f"; done

# Find pages still saying "Homebody" in title
grep -l "Homebody Projects" *.html
```

### PRIORITY 2: Fix Broken Maps
**Status:** Maps showing blank/white. Fundamental initialization or CSS issue.

**Tasks:**
1. Debug why map containers render as blank white areas on the live site
2. Check that Leaflet/ArcGIS JS libraries load correctly from CDN
3. Verify map container elements have explicit height set (common cause of blank maps)
4. Test the eligibility map (dadu_eligibility_map.html) — this is the most important map
5. Test property search map (property_search.html)
6. Connect building footprints layer to maps (currently NOT CONNECTED)
7. Connect permits layer to maps (currently NOT CONNECTED)
8. Connect covenants layer to maps (currently NOT CONNECTED)

**ArcGIS Feature Services to connect:**
| Service | Records | URL Pattern |
|---------|---------|-------------|
| DADU_Eligibility_ENHANCED | 161,703 | Vanderbilt ArcGIS |
| NEW_ADU_Permits | 4,117 | Vanderbilt ArcGIS |
| DADU_All_Permits_Final | 4,700+ | Vanderbilt ArcGIS |
| Building Footprints | 327,000+ | Nashville ArcGIS |
| Parcels_with_Restrictive_Covenants | 43,710 | Vanderbilt ArcGIS |

### PRIORITY 3: Property Report Card (Core Product Spine)
**Status:** Page exists (property-report-card.html) but external links need correct field mapping.

**Tasks:**
1. Implement all external link builders using correct field mappings:
   ```
   Parcel Viewer:     https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}
   Print Record:      https://maps.nashville.gov/ParcelViewer/PrintRecord.html?pin={PIN}
   Permit Docs:       https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}
   Parcel Docs:       https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={APN}
   ePermits:          https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}
   Assessor:          https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}
   Property Card:     https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
   ```
2. Use `assessor_accounts_20260114.csv` to map APN → ACCOUNTNUMBER for property card links
3. Show building footprints on the report card map (Symbium-style: highlight parcel boundary, color primary structure vs. ADU differently)
4. Display permit history for the parcel
5. Show restrictive covenant status and link to covenant documents

### PRIORITY 4: Document Portal Enhancement
**Status:** dadu_documents_portal.html exists but needs searchable functionality.

**Tasks:**
1. Create `data/docs_index.json` by scanning local PDF folders:
   - `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/Permit_PDFs_Downloaded/`
   - `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/Property_Cards_2_Assessor/`
   - `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/Property_Cards_Downloaded/`
   - `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/Restrictive_Covenants/`
2. Extract APN from filenames using regex for 10-12 digit sequences
3. Normalize APNs to 11 digits with left-padding zeros
4. Extract permit numbers from filename patterns (date_numeric blocks)
5. Join documents to permits and parcels
6. Build searchable portal with filters: APN, address, document type, permit number
7. Connect Google Drive folder links for document delivery

**JSON structure per entry:**
```json
{
  "doc_id": "unique_identifier",
  "doc_type": "property_card|permit|covenant|site_plan",
  "apn_normalized": "15000021300",
  "permit_number": "2017047359",
  "address": "123 Main St",
  "source": "metro_codes|assessor|register_of_deeds",
  "url": "https://...",
  "drive_url": "https://drive.google.com/...",
  "tags": ["dadu", "site_plan"]
}
```

### PRIORITY 5: Contractor Marketplace Data Connection
**Status:** Page exists with hardcoded JSON data. Needs live data connection.

**Tasks:**
1. Load contractor data from DADU_All_Permits_Cleaned.csv (4,700+ permits)
2. Aggregate: permit count per contractor, average cost per sqft, project locations
3. Fields with data: CONTRACTOR_BIZ_NAME_ORIGINAL, CONTRACTOR_LICENSE
4. Other contractor fields are mostly empty — do not rely on them without verification
5. Link each contractor's projects to Property Report Cards
6. Implement search and filter by contractor name, area, permit count

### PRIORITY 6: Near Me Locator
**Status:** Multiple versions exist (dadu_near_me.html, v2, locator). Need to consolidate to one working version.

**Tasks:**
1. Address input with autocomplete (use ArcGIS geocoder or Esri World Geocoding)
2. Radius selector: 0.25, 0.5, 1, 2 miles (default 0.5)
3. Filter toggles: Completed, Permitted, Covenants recorded
4. Map with markers + sorted list of results
5. Each result card: address, permit number, date, sqft, cost, contractor name
6. Action buttons: View Property Report, Open ParcelViewer, Open ePermits
7. Paginate for large result sets

### PRIORITY 7: Missing Page Content
**Status:** Many pages are placeholder stubs created by Claude Code. Need real content.

**High priority pages needing content:**
- am_i_eligible.html — Address lookup with instant eligibility determination
- user-homeowners.html — Homeowner portal landing page
- contractor_marketplace.html — Connected to real permit data
- property_search.html — Map-based search like Regrid

**Medium priority:**
- what_is_dadu.html, dadu_building_requirements.html, permit_process_timeline.html
- designer_resources.html, municipal_dashboard.html

---

## 7. DATA ASSETS AND FIELD MAPPINGS

### Core Datasets

**IMPORTANT:** The most recent processed datasets live in `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/FINAL_FINAL/`. Always check this folder first for the latest versions of any dataset. Files here supersede older copies elsewhere.

| Dataset | Records | Key Fields | Location |
|---------|---------|-----------|----------|
| tn_davidson.csv | 284,000 | APN, address, zoning, lot size | Local |
| Building_Footprints.geojson | 327,000+ | Height, sqft, building type | ArcGIS |
| Parcels_with_Building_Characteristics | 285,512 | Structures, YearBuilt, footprints | ArcGIS |
| Parcels with Covenants.xlsx | 43,000+ | Covenant URLs, recording info | Local |
| DADU_All_Permits_Cleaned.csv | 4,700+ | PermitNum, contractor, cost, date | Local |
| historic_dadu_permits_actual.csv | 827 | Metro permits 2017-2025 | Local |
| PropertyShark_2Unit_SFR_Clean.csv | 6,800+ | Confirmed 2-unit properties | Local |
| assessor_accounts_20260114.csv | — | Maps APN to ACCOUNTNUMBER | Local |

### ID Cross-Reference
- **APN** (Assessor's Parcel Number): 11-digit, primary key for most joins
- **STANPAR**: Used by ParcelViewer links
- **PIN / ParID**: Used by some Nashville services
- **ACCOUNTNUMBER**: Used by PADCTN property card URLs
- **ParcelID**: Used by ArcGIS feature layers

Use `assessor_accounts_20260114.csv` to bridge APN ↔ ACCOUNTNUMBER.

### ADU Detection Indicators (5 sources, 98.9% accuracy)
| Indicator | Records | Description |
|-----------|---------|-------------|
| regrid_2plus_bldgs | 67,000 | Properties with 2+ buildings |
| county_permit | 827 | Metro DADU permits |
| 3rdparty_permit | 1,800 | RE Data/RealtyTrac permits |
| fraction_B | 10,000 | Secondary address indicators |
| covenant | 1,100 | Restrictive covenant filings |

Properties with 2+ indicators are strong ADU signals (5,647 parcels).

### Coordinate Reference Systems
- Local analysis: EPSG:2274 (Tennessee State Plane, units in feet)
- Web mapping: EPSG:4326 (WGS84 lat/lon)
- ArcGIS default: Web Mercator (auto-converted)
- Building_Footprints Shape_Area is in square feet (EPSG:2274)

---

## 8. API ENDPOINTS AND DATA SERVICES

### Nashville ePermits API
- Base: `https://epermits.nashville.gov/api`
- OData-style filtering
- `caseSubTypeID 774` = DADU permits specifically
- `CaseQuantityGroupDetail` endpoint with `detailCode 'PROJSCOPE'` = project scope text (sqft, setbacks)
- `detailCode 'RESCONVAL'` = residential construction value

### Nashville ParcelService SOAP API
- Base: `https://maps.nashville.gov/ParcelService/Search.asmx`
- `/GetPermitHistory?apn={APN}` — All permits for parcel
- `/GetGenInfo?pin={PIN}` — General parcel info
- `/GetOwnerHistory?pin={PIN}` — Ownership chain
- `/GetZoningHistory?pin={PIN}` — Zoning changes

### ArcGIS Feature Services
| Layer | Base URL Pattern |
|-------|-----------------|
| Nashville Parcels | services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/Parcels_with_Building_Characteristics_view/FeatureServer/0 |
| Base Zoning | maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/BaseZoning/MapServer/0 |
| USD/GSD Boundary | maps.nashville.gov/arcgis/rest/services/Boundaries/USD_GSD/MapServer/0 |

### Vanderbilt ArcGIS Services (Our Hosted Layers)
- DADU_Eligibility_ENHANCED (161,703 records)
- NEW_ADU_Permits_20260114 (4,117 records)
- DADU_All_Permits_Final
- DADU_Building_Specs
- Parcels_with_Restrictive_Covenants (43,710)
- Secondary_SFH_Merged
- Zoning_Overlay_Districts

Portal: vanderbilt.maps.arcgis.com

---

## 9. BL2025-1007 ELIGIBILITY RULES

| Criterion | Requirement |
|-----------|-------------|
| Zoning | R or RS zones only |
| USD (Urban Services) | By-right construction |
| GSD (General Services) | Requires overlay district |
| Lot < 10,000 SF | Max 700 SF living / 750 SF footprint |
| Lot ≥ 10,000 SF | Max 850 SF living / 1,000 SF footprint |
| Height | Cannot exceed principal structure |
| Owner Occupancy | Required (principal or DADU) |

Eligibility map coloring: Eligible (green), Not Eligible (gray), Conditional (amber/yellow).

Total eligible (USD by-right): 67,707 parcels.
Total eligible (USD + GSD with overlay): ~159,840 parcels.

---

## 10. PRICING TIERS

### Free Tier — Near Me Locator
- View DADUs within radius, contractor names, cost ranges, basic permit info, external verification links

### Paid Tier 1 — DADU Detail Report ($4.99)
- Full permit details, exact cost, square footage, cost per sqft, permit PDFs, property card PDF, aerial + street view links

### Paid Tier 2 — Contractor Report ($9.99)
- All DADUs by contractor, average cost per sqft, project locations, contact info

### Paid Tier 3 — Area Analysis Report ($14.99)
- All DADUs in neighborhood/zip, cost trends, most active contractors, approval timeline stats

Implementation: Placeholder buttons now, Stripe integration later.

---

## 11. FILE STRUCTURE

```
/Users/nataliebaldacci/DADU-Homebody-Projects/    # Project root (also the Git repo)
├── index.html                    # Homepage (Castlehold branded)
├── homebody_shared.css           # Global stylesheet
├── homebody_header.js            # Shared nav component
├── homebody_header.html          # Header template
├── /assets/
│   ├── /css/                     # Additional stylesheets
│   ├── /js/                      # Shared JavaScript modules
│   │   └── arcgis-services.js    # ArcGIS query utilities
│   └── /icons/                   # PNG icons for nav/cards
├── /data/
│   ├── gis_data_sources.json     # ArcGIS endpoint reference
│   ├── docs_index.json           # Document portal index (TO CREATE)
│   └── parcels_docs_summary.json # Per-parcel doc summary (TO CREATE)
├── /docs/                        # PDF documents
├── /samples/                     # Design reference (DO NOT MODIFY)
├── /sample_reports/              # Sample report previews
├── [95+ HTML pages at root]
│
├── /DADU/                        # Data folder (not deployed to GitHub Pages)
│   ├── /FINAL_FINAL/             # Latest processed datasets
│   ├── /MASTER_ADU_DATA/         # Consolidated analysis files
│   ├── /All_Icons/               # Icon source files
│   ├── /Permit_PDFs_Downloaded/  # Local PDF library
│   ├── /Property_Cards_Downloaded/
│   ├── /Property_Cards_2_Assessor/
│   └── /Restrictive_Covenants/
└── /Scripts/                     # Python processing scripts
```

### Available PNG Icons
```
Parcel_Search.png, Property_Owners.png, Building_and_Construction.png,
Zoning.png, Recorded_Docs.png, Exports__Reports.png, GIS.png,
APN_Maps.png, Area_Maps_and_Visual_layers.png, Investors.png,
Appraisers.png, Surveyors_and_Engineers.png, Municipal.png,
Utilities.png, Legal.png, Farming.png, Bulk_data.png
```
Located at: `assets/icons/FILENAME.png`
Also at: `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/All_Icons/Icons/SVG_Originals/`

---

## 12. AUDIT COMMANDS — RUN THESE FIRST

```bash
cd /Users/nataliebaldacci/DADU-Homebody-Projects/

# 1. Count all HTML files
echo "=== HTML FILE COUNT ==="
find . -name "*.html" -type f | wc -l

# 2. Check for shared CSS/JS
echo "=== SHARED ASSETS ==="
ls -la homebody_shared.css homebody_header.js homebody_header.html 2>/dev/null

# 3. Check old vs new colors
echo "=== OLD COLORS STILL PRESENT ==="
grep -rl "#2c3e50" *.html 2>/dev/null | wc -l
grep -rl "#6b8e4e" *.html 2>/dev/null | wc -l
grep -rl "#e8e4df" *.html 2>/dev/null | wc -l

echo "=== NEW COLORS PRESENT ==="
grep -rl "#3A5566" *.html 2>/dev/null | wc -l
grep -rl "#F2F0ED" *.html 2>/dev/null | wc -l

# 4. Check Castlehold branding adoption
echo "=== BRANDING ==="
grep -rl "Castlehold" *.html 2>/dev/null | wc -l
grep -rl "Homebody Projects" *.html 2>/dev/null | wc -l

# 5. Check shared header usage
echo "=== SHARED HEADER ==="
grep -rl "site-header\|homebody_header" *.html 2>/dev/null | wc -l

# 6. Check assets folder
echo "=== ASSETS ==="
ls assets/icons/ 2>/dev/null | wc -l
ls assets/css/ assets/js/ 2>/dev/null

# 7. Check nav structure
echo "=== NAV STRUCTURE ==="
grep -c "explore-dropdown\|EXPLORE" index.html 2>/dev/null
grep -c "build-dropdown\|BUILD" index.html 2>/dev/null
grep -c "data-dropdown\|DATA" index.html 2>/dev/null
grep -c "features-dropdown\|Features" index.html 2>/dev/null

# 8. Git status
echo "=== GIT STATUS ==="
git status --short | head -20

# 9. Check FINAL_FINAL folder contents (latest datasets)
echo "=== FINAL_FINAL DATASETS ==="
ls -la /Users/nataliebaldacci/DADU-Homebody-Projects/DADU/FINAL_FINAL/ 2>/dev/null

# 10. Check full project folder structure
echo "=== PROJECT ROOT ==="
ls -la /Users/nataliebaldacci/DADU-Homebody-Projects/
echo "=== DADU DATA FOLDER ==="
ls /Users/nataliebaldacci/DADU-Homebody-Projects/DADU/ 2>/dev/null | head -20
```

---

## 13. DEVELOPMENT ENVIRONMENT

```bash
# Activate Python environment
source ~/dadu_env/bin/activate

# Key packages
# pandas, geopandas, openpyxl, requests, pyproj, shapely, selenium

# File locations
/Users/nataliebaldacci/DADU-Homebody-Projects/           # Main project root (repo + data)
/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/       # Data folder
/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/FINAL_FINAL/  # Latest processed datasets
/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/MASTER_ADU_DATA/  # Consolidated analysis
```

### Script Output Conventions
- Save scripts to: `/Users/nataliebaldacci/DADU-Homebody-Projects/Scripts/`
- Save data outputs to: `/Users/nataliebaldacci/DADU-Homebody-Projects/DADU/FINAL_FINAL/` (or a new subfolder)
- Never save files to Downloads, Desktop root, or user home without explicit instruction

---

## 14. KEY STATISTICS

| Metric | Value |
|--------|-------|
| Total Nashville Parcels | 285,512 |
| BL2025-1007 Eligible (USD) | 67,707 |
| Total Eligible (USD + GSD w/ overlay) | ~159,840 |
| Historic DADU Permits | 827 |
| RE Data ADU Permits | 4,122 |
| Unique Contractors | 393 |
| Legal Citations in Database | 111 |
| Parcels with Covenants | 43,000+ |
| Restrictive Covenant Documents | 8,514+ |
| HTML Pages on Site | 95+ |

---

## 15. DELIVERABLE FORMAT

When responding with work, always provide:

1. **Short plan** — What you will build and why
2. **Exact file paths** — Full paths relative to repo root
3. **Complete code** for each file you touch — no partial snippets
4. **Notes on icons** — Where to place them and expected filenames
5. **GitHub Pages test checklist** — Steps to verify everything works

### File Naming Convention
`dadu_[feature]_[version].html`

Examples: `dadu_property_viewer_v3.html`, `dadu_opportunity_explorer_v2.html`

---

## 16. SCOPE BOUNDARIES

**DO:**
- Keep it functional and polished
- Fix branding, maps, and Property Report Card first
- Use client-side JavaScript for GitHub Pages compatibility
- Prefer JSON indexes for documents and permit summaries
- Load data on demand, not at page load
- Paginate ArcGIS queries

**DO NOT:**
- Overbuild beyond MVP requirements
- Load huge GeoJSON at initial page load
- Expose API keys in the repo
- Delete, rename, or move existing files
- Introduce teal, green, or any non-palette colors
- Create "Developer/Investor" user type
- Use "Contractor Finder" (use "Contractor Marketplace" only)
- Add "Resources" to top nav (it belongs in footer only)
- Use the word "platform" in nav labels

---

## 17. EXECUTION ORDER SUMMARY

```
Step 1: Run audit (Section 12)
Step 2: Fix branding — replace all old colors, ensure shared CSS loaded everywhere
Step 3: Fix shared header — verify locked nav structure on all pages
Step 4: Fix maps — debug blank rendering, connect data layers
Step 5: Wire Property Report Card — all external link builders working
Step 6: Document portal — build docs_index.json, enable search
Step 7: Contractor marketplace — connect to real permit data
Step 8: Near Me locator — consolidate to one working version
Step 9: Fill placeholder pages — am_i_eligible, homeowner portal, etc.
Step 10: Test all nav links — ensure every href target exists
```

---

*End of instructions. This document is the single source of truth for the Castlehold DADU platform. When in doubt, follow this document over any other reference.*
