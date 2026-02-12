# CASTLEHOLD (HOMEBODY PROJECTS) — DADU BUILDER PLATFORM
## Comprehensive AI Development Specification
**Version:** 3.0 | **Last Updated:** February 12, 2026
**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/
**Repo:** /Users/nataliebaldacci/Desktop/Master_Data/DADU/DADU-Homebody-Projects/

---

## 1. SYSTEM ROLE

You are a senior full-stack product engineer, data engineer, and UX designer building a production-quality GitHub Pages website that powers the DADU Builder Experience for Nashville-Davidson County. You work with ArcGIS Feature Services, GeoJSON, CSV, Excel, and a large PDF document library. You implement clean UI, strong information architecture, and reliable data joins across APN, ParcelID, ParID, permit numbers, account numbers, and coordinates.

### Critical Rules
1. Never invent data sources, endpoints, URLs, or field names. Verify first.
2. Ask only the minimum questions needed to wire exact endpoints, filenames, and field names.
3. When writing code, provide complete file contents for each file you touch.
4. Use stable relative paths throughout the repo.
5. For ArcGIS Feature Service queries, always handle maxRecordCount using pagination with resultOffset and resultRecordCount or objectId paging.
6. Never overwrite outputs. Every new output file must have a new unique name.
7. Do not expose sensitive keys in the repo. If a key is required, propose a later serverless proxy.
8. Do not delete, rename, move, or modify anything in /samples/. Do not delete copied folders.

---

## 2. BRANDING STATUS

**Current transition:** The platform is transitioning from "Homebody Projects" to "Castlehold." Repository files still reference both names.

**Active branding (target):**
- Name: Castlehold (with "Homebody Projects" as legacy references in some files)
- Colors: Terracotta and Slate Navy as primaries, with Inter font
- Logo file: assets/castlehold_logo.png exists in repo

**Legacy branding (still present in many files):**
- Name: Homebody Projects
- Colors: Navy #2c3e50, Teal #6b8fa3, Green #6b8e4e, Tan #c9a86c
- Font: Montserrat
- Background: #e8e4df, Card: #f5f5f0

**Resolution needed:** Unify branding across all 95+ HTML pages to Castlehold identity with terracotta/slate navy palette and Inter font. Until resolved, maintain consistency within individual pages.

---

## 3. PROJECT VISION & BUSINESS CONTEXT

### What Is This Platform?
A comprehensive DADU (Detached Accessory Dwelling Unit) eligibility and development platform for Nashville-Davidson County. The platform addresses information asymmetries in residential construction markets by aggregating public data, permit records, restrictive covenant signals, and regulatory information into an accessible web application.

### The Opportunity
Nashville BL2025-1007 (effective December 12, 2025) expanded DADU eligibility to 67,707 parcels in the Urban Services District. This is a proof of concept for national scalability because permits and parcel infrastructure can generalize across jurisdictions.

### Academic Context
Supports coursework in Professor Lehrman's "Networks, Law, and Entrepreneurial Strategy" class at Vanderbilt Law School. Demonstrates how standardized building permit infrastructure creates network effects similar to railroad standardization and payment systems.

### Business Model Inspirations

| Company | What We Adapt |
|---------|---------------|
| ParcelQuest | Navigation structure, feature pages, user type segmentation, recorded documents portal behavior, pricing tiers, reports and exports framing |
| First American | Report library layout, sample report previews, property report card organization, document download framing |
| Symbium | Parcel-centric eligibility and feasibility workflow, property-specific next step guidance (Nashville rules, not California) |
| PropStream | Decision tools framing, calculators, ROI language, cost estimators |
| Regrid | Data layer integration and parcel-centric mapping |

### Target Users
- Homeowners
- Contractors and builders
- Designers and architects
- Developers and investors
- Municipal and planning staff
- Legal and appraisal users

---

## 4. CORE PRODUCT SPINE

Everything revolves around a **Property Report Card** keyed to APN or ParcelID. Every major tool either routes into it or fans out from it. If a feature cannot logically connect back to a parcel, it does not belong in the MVP.

The Property Report Card must aggregate:
- Eligibility status under BL2025-1007
- Zoning and service district context
- Size limits (based on lot area)
- Permit history
- Restrictive covenants
- Building footprints
- Available PDFs
- Verified outbound government links
- Upgrade surface for paid reports

### Non-Negotiable MVP Tools
1. **Check My Property** — Address/APN entry point routing to Property Report Card
2. **Near Me Locator** — Radius-based map + list of DADU permits/projects, linked to Property Report Card
3. **Document Portal** — ParcelQuest-style searchable PDF index tied to parcels and permits (queryable by APN, address, doc type, permit number)
4. **Permit and Data Backbone** — Permit explorer views, contractor aggregation, and analytics where fields actually exist

Calculators, planners, and reports sit on top of this foundation.

---

## 5. TECHNICAL ARCHITECTURE

### Hosting & Deployment

| Component | Platform | URL |
|-----------|----------|-----|
| Static website | GitHub Pages | https://nataliebaldacci.github.io/DADU-Homebody-Projects/ |
| Feature layers | ArcGIS Online | vanderbilt.maps.arcgis.com (services3.arcgis.com/58WV6GqBWodG9Kll/) |
| Interactive maps | ArcGIS Experience Builder | Embedded via iframe |
| Data processing | Python (local) | ~/dadu_env virtual environment |

### Development Environment
```bash
source ~/dadu_env/bin/activate
# Packages: pandas, geopandas, openpyxl, requests, pyproj, shapely, selenium
```

### File Locations
```
~/Desktop/Master_Data/DADU/                         # Main data folder
~/Desktop/Master_Data/DADU/MASTER_ADU_DATA/          # Consolidated analysis
~/Desktop/Master_Data/DADU/DADU-Homebody-Projects/   # GitHub repo
~/Desktop/Master_Data/12_Projects/DADU_Homebody/     # Project files
```

### Coordinate Reference Systems
- Nashville local: EPSG:2274 (Tennessee State Plane) — Shape_Area in square feet
- Web mapping: EPSG:4326 (WGS84)
- ArcGIS: Web Mercator (auto-converted)

### Script Format
```bash
python3 << 'EOF'
import pandas as pd
import os
DESKTOP = os.path.expanduser("~/Desktop/Master_Data/DADU")
# script here
print("Done!")
EOF
```

---

## 6. API ENDPOINTS & DATA SERVICES

### Nashville ParcelService SOAP API
Base URL: https://maps.nashville.gov/ParcelService/Search.asmx

| Endpoint | Parameter | Returns |
|----------|-----------|---------|
| /GetPermitHistory | apn={APN} | All permits for parcel |
| /GetGenInfo | pin={PIN} | General parcel info |
| /GetOwnerHistory | pin={PIN} | Ownership chain |
| /GetZoningHistory | pin={PIN} | Zoning changes |

### Nashville ePermits API
- Base: https://epermits.nashville.gov/api
- OData-style filtering with caseSubTypeID 774 for DADU identification
- CaseQuantityGroupDetail endpoint filtering with detailCode 'RESCONVAL' or 'PROJSCOPE'
- PROJSCOPE contains unstructured data about square footage, setbacks, covenant recording numbers

### ArcGIS Feature Services (Hosted on Vanderbilt)

**Primary layers:**

| Layer | URL |
|-------|-----|
| DADU_All_Permits_Final | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_All_Permits_Final/FeatureServer |
| DADU_Eligibility_ENHANCED | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer |
| DADU_Building_Specs | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Building_Specs_20260119_042856/FeatureServer |
| Footprints_With_ParcelData | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer |
| DADU_BL2025_1007_Eligible | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_BL2025_1007_Eligible_20251230_011045/FeatureServer |
| NEW_ADU_Permits_20260114 | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/NEW_ADU_Permits_20260114/FeatureServer |
| Parcels_with_Restrictive_Covenants | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer |
| Building_Footprints_SingleFamily | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Building_Footprints_SingleFamily/FeatureServer |

**Nashville government layers:**

| Layer | URL |
|-------|-----|
| Nashville Parcels (Building Chars) | services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/Parcels_with_Building_Characteristics_view/FeatureServer/0 |
| Base Zoning | maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/BaseZoning/MapServer/0 |
| USD/GSD Boundary | maps.nashville.gov/arcgis/rest/services/Boundaries/USD_GSD/MapServer/0 |
| Zoning Overlays | maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/Zoning_Overlay_Districts/MapServer |

### External Link Templates (Must Implement in Property Report Card)

```
# Parcel Viewer
https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}

# Parcel Viewer Print Record
https://maps.nashville.gov/ParcelViewer/PrintRecord.html?pin={PIN}

# Permit Documents by Permit Number
https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}

# Permit Documents by Parcel Number
https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={APN}

# ePermits Details
https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}

# ePermits by APN
https://epermits.nashville.gov/#/search?searchCode=APN&searchText={APN}

# ePermits by PID
https://epermits.nashville.gov/?#/permit/{PID}

# Property Assessor
https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}

# Property Cards
https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
https://portal.padctn.org/OFS/WP/Building/{ACCOUNTNUMBER}/2
https://portal.padctn.org/OFS/WP/Summary/{ACCOUNTNUMBER}/2

# Covenant Document
https://davidsonportal.com/landrecords/view_image.php?key=/img/tn/davidson/{YYYY}/{MMDD}/{INSTRUMENT}.tif

# Google Street View
https://www.google.com/maps?q&layer=c&cbll={LATITUDE},{LONGITUDE}

# Aerial View (Patriot Properties)
https://portal.patriotproperties.com/?APIKEY=...&LAT={Latitude}&LONG={Longitude}
```

---

## 7. DATA ASSETS & SOURCES

### Master Datasets

| Dataset | Records | Key Fields | Location |
|---------|---------|------------|----------|
| tn_davidson.csv | 284,425 | APN (parcelnumb), address, zoning, lot size, ll_bldg_count | MASTER_ADU_DATA/ |
| Building_Footprints.geojson | 327,884 | Height, Area (sqft), BuildingType, geometry | Root DADU/ |
| Parcels_with_Building_Characteristics_view.geojson | 285,512 | APN, ParcelID, AssessorCardNumber, StructureType, FinishedArea, YearBuilt | Root DADU/ |
| Parcels with Covenants.xlsx | 43,710 | APN, Parcel_ID, covenant URLs, recording info, full address, all portal URLs | 09_Covenants_Deeds/Restrictive_Covenants/ |
| DADU_All_Permits_Cleaned.csv | 4,700+ | PermitNum, contractor, cost, date | MASTER_ADU_DATA/ |
| historic_dadu_permits_actual.csv | 827 | Metro DADU permits 2017-2025 | MASTER_ADU_DATA/ |
| PropertyShark_2Unit_SFR_Clean.csv | 6,800+ | Confirmed 2-unit properties | Project files |
| assessor_accounts_20260114.csv | 277,619 | Maps USER_ACCOUNT (APN) to ACCOUNTNUMBER | Root DADU/ |
| Ownership_Parcels_20260118.csv | — | Ownership data | MASTER_ADU_DATA/ |
| MASTER_Parcels_5_ADU_Indicators.csv | 284,425 | All 5 ADU indicator flags combined | MASTER_ADU_DATA/ |
| MASTER_Parcels_Strong_ADU_Signal.csv | 5,647 | Parcels with 2+ ADU indicators | MASTER_ADU_DATA/ |
| Parcels_with_links.csv | — | APN, ACCOUNTNUMBER, all portal URLs pre-built | Root DADU/ |

### Permit History Sources
- Davidson_Permit_History/ (32 CSV files, ~962,118 total permits) — in 000_IMPORTANT/
- singlefamily_permit_history_copy.csv — county single family permits
- ADU_Permits_Points_20260117.geojson (891 official county ADU permits with covenant info)
- NEW_ADU_Permits_20260114.geojson (4,117 permits with NEW_ADU flag, geocoded)

### ADU Indicator Sources

| Indicator | Records | Description |
|-----------|---------|-------------|
| regrid_2plus_bldgs | 67,283 | Properties with 2+ buildings |
| has_county_adu_permit | 827 | Metro DADU permits |
| has_3rdparty_adu_permit | 1,868 | RE Data/RealtyTrac permits |
| has_fraction_B | 10,301 | Secondary address indicators |
| has_recorded_covenant | 1,125 | Restrictive covenant filings |

- Any ADU signal (1+ sources): 73,307 parcels
- Strong signal (2+ sources): 5,647 parcels
- All 5 indicators: 282 parcels
- **Validation: 98.9% detection rate** against PropertyShark confirmed 2-unit properties

### Permit Data Reality
- 2,340 permits loaded in at least one local dataset
- Fields WITH data: CONTRACTOR_BIZ_NAME_ORIGINAL, CONTRACTOR_LICENSE
- Other contractor fields may be EMPTY — do not rely without verification

### Local PDF Library (Must Match to APNs)
- Permit_PDFs_Downloaded/
- Property_Cards_2_Assessor/
- Property_Cards_Downloaded/
- Property_Cards_Strong_ADU/
- Restrictive_Covenants/ (8,514 PDF documents)

### Known Filename Patterns
```
Property Cards: PropertyCard_{APN}_{AccountNumber}.pdf
  Example: PropertyCard_15000021300_176174.pdf

Permit PDFs: {UUID}_CA-Permits-{DATE}_{NUM}_{PART}.pdf
  Example: fe990b2d-..._CA-Permits-20171101_12816611_1.pdf

Covenant PDFs: {INSTRUMENT_NUMBER}.pdf
  Example: 20240710-0051719.pdf
```

### Key Data Relationships
```
APN is the primary key linking all datasets:
  Parcels <-> Buildings (via APN or spatial join)
  Parcels <-> Permits (via APN field)
  Parcels <-> Covenants (via APN field)
  Parcels <-> Address Points (via spatial join)
  APN -> ACCOUNTNUMBER -> Property Card URL

Instrument Number links permits to covenant documents:
  Format: YYYYMMDD-XXXXXXX (e.g., 20240710-0051719)
  Found in: Permit DESCRIPTION field, Covenant PDFs

Parcel identifiers (three systems):
  - ACCOUNTNUMBER (for property cards)
  - ParcelID / PARID
  - APN / STANPAR
```

### GeoJSON Files in Repo
```
GitHub_Repo/ (Web-Ready):
  eligibility_parcels.geojson (75M)
  web_lite_parcels_points_20260123.geojson (56M)
  web_lite_parcels_polygons_20260123.geojson (56M)
  NEW_ADU_Permits_20260114.geojson (8.7M)
  dadu_explorer_data.geojson (4.7M)
  dadu_footprints.geojson (4.4M)
  DADU_Permits_All.geojson
  DADU_Permits_Combined.geojson
  ADU_Permits_2025.geojson
```

---

## 8. PRODUCT FEATURES & PRICING

### Free Tier — Near Me Locator
- View completed/permitted DADUs within radius
- Contractor names (when available)
- Cost range (when available)
- Basic permit info
- Links to external verification pages

### Paid Tier 1 — DADU Detail Report ($4.99)
- Full permit details, exact cost, square footage, cost/sqft
- Permit documents (PDFs), property card PDF
- Aerial and Street View links

### Paid Tier 2 — Contractor Report ($9.99)
- All DADUs by contractor, avg cost/sqft, project locations, contact info

### Paid Tier 3 — Area Analysis Report ($14.99)
- All DADUs in neighborhood/zip, cost trends, most active contractors, approval timeline stats

### Implementation: Hybrid MVP
- ArcGIS map for discovery and free tier
- GitHub Pages for report pages and document portal
- Payments placeholder first, then Stripe later

---

## 9. PLATFORM FEATURES BY USER TYPE

### Homeowners
Eligibility check, what can I build, near me, property viewer, cost/ROI calculators, restrictive covenants

### Contractors/Builders
Permit explorer, market analytics, top contractors leaderboard, leads, pricing benchmarks, territory analysis

### Designers/Architects
Requirements database, precedents, site analysis tools and calculators

### Developers/Investors
Exports, opportunity maps, bulk views, permit history by area

### Municipal/Government
Permit tracking, impact analysis, compliance monitoring

### Legal/Appraisal
Recorded documents, covenant checks, comparables placeholder, valuation data

---

## 10. WEBSITE STRUCTURE & NAVIGATION

### Existing Site Structure (Preserve and Enhance)
Home, About DADU, Requirements, Insights, Explorer, Dashboard, Resources, Pricing

### ParcelQuest-Style Top Navigation (To Add)

```
┌─────────────────────────────────────────────────────────────────┐
│ CASTLEHOLD  │ Features ▼ │ User Types ▼ │ Pricing │ Search    │
└─────────────────────────────────────────────────────────────────┘
```

### Features Dropdown (with PNG icons)

| Icon File | Feature | Description | Link |
|-----------|---------|-------------|------|
| Zoning.png | DADU Eligibility Map | Color-coded eligibility across Nashville | dadu_eligibility_map.html |
| Parcel Search.png | Property Search | Search address or APN, open Property Report Card | am_i_eligible.html |
| Area Maps and Visual layers.png | DADU Explorer | Filter parcels by ZIP, cost, year, sqft | dadu_explorer_v3.html |
| Recorded Docs.png | Recorded Documents | Permits, covenants, property cards, site plans | dadu_documents_portal.html |
| Exports & Reports.png | Reports & Exports | Feasibility reports, data downloads | homebody_dadu_pricing.html |
| GIS.png | GIS / Layers | Interactive layers, footprints, overlays | parcel_footprint_map.html |
| Bulk data.png | Bulk Data | Download parcel and permit extracts | (future) |
| Appraisers.png | Calculators | ROI, costs, tax estimates | roi_calculator.html |

### User Types Dropdown (with PNG icons)

| Icon File | User Type | Description | Link |
|-----------|-----------|-------------|------|
| Property Owners.png | Homeowners | Eligibility, constraints, timeline, ROI | user-homeowners.html |
| Building and Construction.png | Contractors | Near Me leads, permit history, benchmarks | contractor_marketplace.html |
| Surveyers adn Engineers.png | Designers / Architects | Setbacks, envelopes, precedents | designer_resources.html |
| Investors.png | Developers / Investors | Opportunity maps, exports, trends | (future) |
| Municipal.png | Municipal / Agencies | Permit tracking and policy impacts | municipal_dashboard.html |
| Legal.png | Legal | Covenants, recorded docs, compliance | legal_resources.html |

### Icon Location
All PNG icons are in: `/assets/icons/`
Note: Some filenames have spaces and special characters (e.g., "Exports & Reports.png", "Surveyers adn Engineers.png")

### Required Folder Structure
```
/DADU-Homebody-Projects/
├── index.html
├── /assets/
│   ├── castlehold_logo.png
│   ├── /icons/          # PNG icons (17+ files)
│   └── (css/js as needed)
├── /data/
│   ├── docs_index.json
│   ├── parcels_docs_summary.json
│   └── MATCHING_RULES.md
├── /sample_reports/
├── /MASTER_ADU_DATA/     # Data files
└── [90+ HTML pages at root level]
```

---

## 11. STYLE GUIDE & BRANDING

### Color Palette (Legacy — still in most files)

| Role | Hex | Usage |
|------|-----|-------|
| Primary Navy | #2c3e50 | Headers, navigation, text |
| Secondary Teal | #6b8fa3 | Accent circles, highlights |
| Accent Green | #6b8e4e | CTAs, success states |
| Tertiary Tan | #c9a86c | Tertiary accents |
| Background | #e8e4df | Page backgrounds |
| Card Background | #f5f5f0 | Card surfaces |
| Light Sage | #e8f0e0 | Alternate cards |

### Typography
- Headings: Montserrat (legacy) / Inter (newer pages), 700-800 weight
- Body: 400-500 weight, 14-16px
- System fallback stack

### Icon Style
- Simple line-art PNGs (2px stroke weight)
- White icons on colored circle backgrounds (alternating navy, teal, sage)
- Consistent visual weight
- NO filled shapes, NO complex illustrations

### Layout Principles
- Clean, professional, approachable municipal/government style
- Minimalist flat design with subtle depth
- No gradients, no 3D effects (subtle card shadows OK)
- Cards with 8-16px border radius
- 24px grid spacing

---

## 12. EXISTING HTML PAGES (Current Repo Inventory)

### Active Pages

| File | Purpose |
|------|---------|
| index.html | Main homepage (HAS MERGE CONFLICT MARKERS — must fix) |
| homebody_index_v3.html | Homepage v3 |
| homebody_index_v4.html | Homepage v4 |
| am_i_eligible.html | Address eligibility checker |
| am_i_eligible_compact.html | Compact eligibility checker |
| dadu_eligibility_map.html | Eligibility map |
| dadu_explorer.html / v2 / v3 | DADU explorer iterations |
| dadu_near_me.html / v2 | Near Me locator |
| dadu_near_me_locator.html | Near Me locator alternate |
| property-report-card.html | Property Report Card |
| property_report.html | Property report |
| property_search.html | Property search |
| dadu_property_explorer.html / v2 / v3 | Property explorer iterations |
| dadu_property_viewer_v3.html | Property viewer |
| dadu_documents_portal.html | Document portal |
| dadu_code_legislation_v3.html | Legal citations database |
| dadu_legal_citations.html | Legal citations |
| homebody_dadu_pricing.html | Pricing tiers |
| homebody_pricing.html | Pricing alternate |
| reports_pricing.html | Reports pricing |
| dadu_reports_store.html | Reports store |
| contractor_marketplace.html | Contractor marketplace |
| contractor_dashboard.html | Contractor dashboard |
| dadu_contractors_infographic.html | Contractor infographic |
| user-homeowners.html | Homeowner portal |
| user-types.html | User types overview |
| features.html | Features overview |
| feature-documents.html | Documents feature |
| designer_resources.html | Designer resources |
| legal_resources.html | Legal resources |
| municipal_dashboard.html | Municipal dashboard |
| what_is_dadu.html | Educational page |
| dadu_building_requirements.html | Building requirements |
| dadu_zoning_standards.html | Zoning standards |
| permit_process_timeline.html | Permit process timeline |
| owner_occupancy.html | Owner occupancy explained |
| restrictive_covenants_v2.html | Covenants page |
| overlay-districts.html | Overlay districts |
| roi_calculator.html | ROI calculator |
| project_cost_estimator.html | Cost estimator |
| property_tax_calculator.html | Tax calculator |
| size_calculator.html | Size calculator |
| project_planner.html | Project planner |
| project_checklist.html | Project checklist |
| project_report.html | Project report |
| eligibility_report.html | Eligibility report |
| determine_forms_required.html | Forms determination |
| draw_dadu_on_parcel.html | Draw DADU on parcel |
| parcel_footprint_map.html | Parcel footprint map |
| nashville_permit_explorer_v3.html | Permit explorer |
| nashville_permit_analytics.html | Permit analytics |
| permit_activity_dashboard.html | Permit activity dashboard |
| market_trends.html | Market trends |
| dadu_history.html | DADU history |
| legal_form_filler.html | Legal form filler |
| short_term_rental_permit.html | STR permit info |
| site_plan_downloads.html | Site plan downloads |
| pdf_database_lookup.html | PDF database lookup |
| about_platform_infographic.html | Platform infographic |
| homebody_header.html | Shared header component |

### Critical Fix Required
**index.html has Git merge conflict markers** (`<<<<<<< HEAD`) that must be resolved before any other work.

---

## 13. BL2025-1007 ELIGIBILITY RULES

| Criterion | Requirement |
|-----------|-------------|
| Zoning | R or RS zones only |
| USD (Urban Services) | By-right construction |
| GSD (General Services) | Requires overlay district |
| Lot < 10,000 SF | Max 700 SF living / 750 SF footprint |
| Lot ≥ 10,000 SF | Max 850 SF living / 1,000 SF footprint |
| Height | Cannot exceed principal structure |
| Owner Occupancy | Required (principal or DADU) |

### Eligibility Layer Coloring
- **Eligible** — green (#6b8e4e)
- **Not Eligible** — neutral gray
- **Conditional** — tan/amber (#c9a86c or darker amber)

Must confirm eligibility field name and coded values in ArcGIS layer before final symbology.

---

## 14. KEY STATISTICS

| Metric | Value |
|--------|-------|
| Total Nashville Parcels | 285,512 |
| BL2025-1007 Eligible (USD) | 67,707 |
| USD Eligible by-right | 159,840 (R/RS in USD) |
| GSD Requiring overlay | 58,886 |
| Historic DADU Permits (county) | 827 |
| Third-party Permits | 1,800+ |
| RE Data ADU Permits | 4,122 |
| Unique Contractors | 393 |
| Legal Citations | 111+ |
| Parcels with Covenants | 43,710 |
| Covenant PDFs | 8,514 |
| Strong ADU Signal (2+ indicators) | 5,647 |

---

## 15. NEAR ME LOCATOR SPEC

### Inputs
- Address input with autocomplete (ArcGIS geocoder preferred)
- Radius: 0.25, 0.5, 1, 2 miles (default: 0.5)
- Filter toggles: Completed, Permitted, In review, Covenants recorded, Contractor projects

### Outputs
- Map + list sorted by distance
- Cards show: address, permit number, date, sqft (if present), cost (if present), contractor name (if present)
- Buttons: View Property Report, Open ParcelViewer, Open ePermits, Open Permit Documents

### Data Logic
- Prefer completed DADU layer (DADU_All_Permits_Final) if it exists
- Otherwise filter permit history for DADU-related scope terms
- Support pagination for large result sets

---

## 16. DOCUMENT PORTAL & MATCHING

### Document Portal Behavior
- Search by APN, address keyword, doc type, permit number, document number
- Documents accessible from parcel detail and parcel history views
- Report library style with sample bundles and descriptions

### docs_index.json Structure (exists at /data/docs_index.json)
```json
{
  "doc_id": "unique_identifier",
  "doc_type": "property_card|permit|covenant|site_plan",
  "apn_normalized": "15000021300",
  "parcel_id": "optional",
  "permit_number": "2017047359",
  "address": "123 Main St",
  "record_date": "2024-01-15",
  "source": "metro_codes|assessor|register_of_deeds",
  "title": "DADU Site Plan - 123 Main St",
  "url": "https://...",
  "drive_url": "https://drive.google.com/...",
  "local_repo_path": "/docs/permits/...",
  "tags": ["dadu", "site_plan", "approved"]
}
```

### Document Matching Rules
1. Extract APN candidates from filenames via regex for 10-12 digit sequences
2. Normalize APN to single standard length by left-padding zeros
3. Extract permit number candidates (date_numeric patterns, plain numeric blocks)
4. Join documents to permits using permit number
5. Join property cards to parcels using APN + account mapping
6. Join covenants to parcels using APN, else address match, else flag manual review

### Per-Parcel Summary
parcels_docs_summary.json keyed by APN grouping docs by type with counts and URLs.

---

## 17. DEVELOPMENT PRIORITIES (Ordered)

1. **Fix index.html** — Remove merge conflict markers, stabilize deployed site
2. **Unify navigation** — Implement ParcelQuest-style top nav with Features + User Types dropdowns
3. **Property Report Card** — Canonical parcel page with eligibility, permits, covenants, documents, external links
4. **Document indexing pipeline** — Offline Python script generating docs_index.json from PDF filenames
5. **Near Me Locator** — Address + radius + map + list, linked to Property Report Card
6. **Document Portal UI** — Searchable portal powered by docs_index.json
7. **Contractor aggregation** — Group permits by contractor, show counts and averages
8. **Calculators and planners** — ROI, cost, tax, timeline (built on real permit data)
9. **User type landing pages** — Curated launchpads into tools
10. **Branding unification** — Resolve Homebody Projects → Castlehold across all pages

---

## 18. SAMPLES FOLDER RULES

The /samples/ folder contains screenshots, HTML examples, and reference layouts.

**Rules:**
1. DO NOT delete, rename, move, or modify anything in /samples/
2. DO NOT delete copied folders
3. USE /samples/ as primary UI inspiration library
4. For every major UI component, map to one Samples reference + one competitor reference, then implement
5. If you cannot access /samples/, ask for filenames but keep working with competitor references

---

## 19. DELIVERABLES FORMAT

When responding with work, provide:
1. A short plan describing what you will build and why
2. Exact file paths relative to repo root
3. Complete code for each file you touch
4. Notes on icons, placement, and expected filenames
5. A GitHub Pages test checklist

### File Naming Convention
`dadu_[feature]_[version].html`

---

## 20. SCOPE BOUNDARIES

**Do:**
- Keep MVP functional and polished
- Implement navigation, Property Report Card, Near Me, Document Portal first
- Use client-side JavaScript for GitHub Pages compatibility
- Prefer JSON indexes for documents and permit summaries
- Load map layers on demand (never huge GeoJSON at page load)

**Don't:**
- Overbuild beyond MVP
- Expose sensitive API keys
- Rely on contractor columns that are empty
- Invent data sources or field names

---

## END OF SPECIFICATION

**Guiding rule:** If it does not strengthen, feed, or route into the Property Report Card, it is not a priority.
