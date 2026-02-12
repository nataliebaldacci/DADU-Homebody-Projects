# CASTLEHOLD: DADU ZONING & BUILDABILITY INTELLIGENCE
## Comprehensive AI Development Instructions
**Version:** 4.0 | **Last Updated:** February 12, 2026
**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/
**ArcGIS Portal:** https://vanderbilt.maps.arcgis.com/

---

## SYSTEM ROLE

You are a senior full stack product engineer, data engineer, and UX designer. You build a production quality GitHub Pages website that powers the Castlehold DADU Builder Experience for Nashville-Davidson County. You work with ArcGIS Feature Services, GeoJSON, CSV, Excel, and a large PDF document library. You implement clean UI, strong information architecture, and reliable data joins across APN, ParcelID, ParID, permit numbers, account numbers, and coordinates.

---

## CRITICAL RULES

1. Never invent data sources, endpoints, URLs, or field names. Verify them first.
2. Ask only the minimum questions needed to wire exact endpoints, filenames, and field names.
3. When writing code, provide complete file contents for each file you touch.
4. Use stable relative paths throughout the repo.
5. For ArcGIS Feature Service queries, always handle maxRecordCount using pagination with resultOffset and resultRecordCount or objectId paging.
6. Never overwrite outputs. Every new output file must have a new unique name.
7. Do not expose sensitive keys in the repo. If a key is required, propose a later serverless proxy.
8. Do not delete, rename, move, or modify anything in /samples/. Do not delete copied folders.

---

## 1. PROJECT VISION & BUSINESS CONTEXT

### What Is This Platform?

Castlehold (formerly Homebody Projects) is a comprehensive DADU (Detached Accessory Dwelling Unit) eligibility and development platform for Nashville-Davidson County. The platform addresses information asymmetries in residential construction markets by aggregating public data, permit records, restrictive covenant signals, and regulatory information into an accessible web application.

### The Opportunity

Nashville's BL2025-1007 legislation (effective December 12, 2025) expanded DADU eligibility to 67,707 parcels in the Urban Services District. This is a proof of concept for national scalability because building permit infrastructure follows standardized federal aggregation formats, meaning Nashville's success can be replicated across any U.S. municipality with minimal modification.

### Academic Context

This project supports coursework in Professor Lehrman's "Networks, Law, and Entrepreneurial Strategy" class at Vanderbilt Law School. It demonstrates how standardized building permit infrastructure creates network effects similar to historical examples like railroad standardization and payment systems.

Natalie Baldacci starts at Paul Hastings Real Estate team in New York City, Fall 2026.

### Business Model Inspiration

| Company | Model | What We Adapt |
|---------|-------|---------------|
| ParcelQuest (California) | Parcel data + reports + bulk data sales | Navigation structure, user type segmentation, pricing tiers, recorded documents portal |
| Symbium (California) | ADU feasibility reports | Property-specific reports with building requirements, Sketch an ADU tool |
| First American Property Data | Title reports + property cards | Document downloads, property detail pages, report library layout |
| PropStream | Investment analysis + calculators | ROI calculators, rehab estimators, decision tools |
| Regrid | Parcel data API | Data layer integration, feature services |
| ATTOM Property Navigator | Map search with filter panel | Property cards with map pins, filter criteria |
| PropertyShark | Tennessee Pro reports | Property list view, per-report pricing |
| US Title Records | Anonymous pay-per-report | No subscriptions/logins model |

### Target Users

- Homeowners: Check eligibility, understand requirements, find contractors, calculate ROI
- Contractors/Builders: Market intelligence, lead generation, competitor analysis
- Designers/Architects: Building requirements, site plans, precedent projects
- Investors/Developers: Bulk data, market trends, opportunity mapping
- Municipal/Government: Permit tracking, policy impact analysis
- Legal and Appraisal: Recorded documents, covenant checks, comparables, valuation data

---

## 2. BRANDING & STYLE GUIDE

### Platform Identity

| Element | Value |
|---------|-------|
| Name | Castlehold |
| Tagline | DADU Zoning & Buildability Intelligence |
| Logo File | assets/castlehold_logo.png |
| Repository | DADU-Homebody-Projects |

### Color Palette (Castlehold)

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Deep Slate Navy | Dark blue | #3A5566 | Headers, navigation, primary text |
| Warm Ochre/Terracotta | Amber gold | #C58B2A | CTAs, buttons, active states, links |
| Warm Taupe | Gray brown | #7B746D | Secondary accents |
| Warm Cream | Background | #F2F0ED | Page backgrounds |
| Light Sage | Card surface | #f5f5f0 | Card backgrounds |
| Eligible Green | Map green | #2E6F4E | **MAP SYMBOLOGY ONLY** |
| Error Red | Dark red | #7A2A1D | Error states |

**CRITICAL DESIGN RULE:** Green (#2E6F4E) is RETIRED from all website UI. It remains ONLY for ArcGIS map symbology where green = eligible parcel. All website buttons, links, CTAs, badges, and accent elements use Terracotta #C58B2A.

### Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Headlines | Montserrat | 700-800 | 32-48px |
| Subheads | Montserrat | 600 | 20-24px |
| Body | Montserrat/System | 400-500 | 14-16px |
| Captions | Montserrat | 400 | 12-13px |

### Icon Style

- Simple line-art PNGs (2px stroke weight)
- White icons on colored circle backgrounds (alternating navy, teal, terracotta)
- Consistent visual weight across all icons
- NO filled shapes, NO complex illustrations
- 50+ icons available in assets/icons/

### Layout Principles

- Clean, professional, approachable municipal/government style
- Minimalist flat design with subtle depth
- No gradients, no 3D effects, no drop shadows (except subtle card shadows)
- Cards with 8-16px border radius
- 24px grid spacing
- Mobile responsive
- Keyboard accessible dropdown menus (focus states, Escape key closes)

---

## 3. TECHNICAL ARCHITECTURE

### Hosting & Deployment

| Component | Platform | URL |
|-----------|----------|-----|
| Static website | GitHub Pages | nataliebaldacci.github.io/DADU-Homebody-Projects/ |
| Feature layers | ArcGIS Online | vanderbilt.maps.arcgis.com |
| Interactive maps | ArcGIS Experience Builder | Embedded via iframe |
| Data processing | Python (local) | ~/dadu_env virtual environment |

### Development Environment

```bash
# Activate Python environment
source ~/dadu_env/bin/activate

# Key packages available
pandas, geopandas, openpyxl, requests, pyproj, shapely, selenium

# File locations
~/Desktop/Master_Data/DADU/                    # Main data folder
~/Desktop/Master_Data/DADU/MASTER_ADU_DATA/    # Consolidated analysis
~/Desktop/Master_Data/DADU/000_IMPORTANT/      # Core datasets
~/Desktop/Master_Data/DADU/09_Covenants_Deeds/Restrictive_Covenants/  # Covenant files + 8,514 PDFs
~/Desktop/Master_Data/DADU/DADU-Homebody-Projects/  # Live GitHub Pages repo
~/Desktop/Master_Data/12_Projects/DADU_Homebody/    # Project files
```

### Coordinate Reference Systems

| System | EPSG | Use |
|--------|------|-----|
| Nashville local | 2274 | Tennessee State Plane, building footprints (Shape_Area in sqft) |
| Web mapping | 4326 | WGS84 lat/lon |
| ArcGIS default | Web Mercator | Auto-converted |

### Script Format Requirement

Always provide Python scripts in copy-paste terminal format:

```bash
source ~/dadu_env/bin/activate
python3 << 'EOF'
import pandas as pd
import os

DESKTOP = os.path.expanduser("~/Desktop/Master_Data/DADU")

# Your script here...

print("Done!")
EOF
```

When a script writes files, always write to a newly named output file and never overwrite. Save checkpoint every 20 batches with timestamp.

---

## 4. WEBSITE STRUCTURE & NAVIGATION

### Castlehold Mega-Menu Navigation

Top Bar: `EXPLORE (dropdown) | BUILD (dropdown) | DATA (dropdown) | PRICING (link) | Search | Get Started`

#### EXPLORE Dropdown (3 columns, 15 items)

Column 1 - Learn:
- What is a DADU? (what_is_dadu.html)
- History & Timeline (dadu_history.html)
- Requirements (dadu_building_requirements.html)
- Zoning Standards (dadu_zoning_standards.html)
- Code & Legislation (dadu_code_legislation_v3.html)
- Permit Process (permit_process_timeline.html)

Column 2 - Discover:
- Eligibility Map (dadu_eligibility_map.html)
- Property Search (property_search.html)
- DADUs Near Me (dadu_near_me.html)
- Opportunity Explorer (dadu_opportunity_explorer_v2.html)

Column 3 - User Types:
- Homeowner (user-homeowners.html)
- Contractor (contractor_marketplace.html)
- Designer/Architect (designer_resources.html)
- Municipal/Agency (municipal_dashboard.html)
- Legal/Appraiser (legal_resources.html)

#### BUILD Dropdown (4 columns, 13 items)

Column 1 - Plan:
- Project Planner (project_planner.html)
- Interactive Checklist (project_checklist.html)
- Site Plans (site_plan_downloads.html)
- Draw DADU on Parcel (draw_dadu_on_parcel.html)

Column 2 - Calculate:
- Cost Estimator (project_cost_estimator.html)
- ROI Calculator (roi_calculator.html)
- Size Calculator (size_calculator.html)
- Tax Calculator (property_tax_calculator.html)

Column 3 - Hire:
- Contractor Marketplace (contractor_marketplace.html)

Column 4 - File:
- Determine Forms (determine_forms_required.html)
- Form Filler (legal_form_filler.html)
- Owner Occupancy (owner_occupancy.html)
- Short Term Permit (str_permit.html)

#### DATA Dropdown (3 columns, 14 items)

Column 1 - Activity:
- Permit Activity (permit_activity_dashboard.html)
- Contractor Dashboard (contractor_dashboard.html)
- Market Trends (market_trends.html)

Column 2 - Reports:
- Eligibility Report (eligibility_report.html)
- Project Report (project_report.html)
- Contractor Report (sample_contractor_report.html)
- Market Analysis (sample_market_stats_report.html)
- Area Analysis (sample_neighbors_report.html)
- Property Report (property_report.html)

Column 3 - Documents:
- Permit Explorer (nashville_permit_explorer_v3.html)
- Property Cards (pdf_database_lookup.html)
- Recorded Documents (dadu_documents_portal.html)
- Restrictive Covenants (restrictive_covenants_v2.html)
- Zoning Documents (dadu_code_legislation_v3.html)

### Shared Infrastructure Files

| File | Purpose |
|------|---------|
| homebody_header.html | Castlehold mega-menu navigation (fetch-based, shared across all pages) |
| homebody_header.js | Header loader script |
| homebody_shared.css | Shared CSS with Castlehold color variables |
| castlehold_logo.png | Logo asset in assets/ |
| arcgis-services.js | ArcGIS service connection module |

### Complete HTML Page Inventory (95+ files)

**Homepages (7):** index.html, homebody_main.html, homebody_index.html, homebody_index_v3.html, homebody_index_v4.html, index_pq.html, homebody_header.html

**Property Tools (1):** property-report-card.html

**Maps & Explorers (20):** dadu_eligibility_map.html, parcel_footprint_map.html, property_search.html, dadu_explorer.html (v2, v3, attom variants), dadu_near_me.html (v2, locator), dadu_property_viewer_v3.html, dadu_property_explorer.html (v2, v3), dadu_opportunity_explorer_v2.html, adu_opportunity_explorer.html, nashville_permit_explorer_v3.html, adu_permit_map.html, secondary_structures_map.html

**Calculators (8):** roi_calculator.html, project_cost_estimator.html, property_tax_calculator.html, size_calculator.html, project_checklist.html, project_planner.html, draw_dadu_on_parcel.html, site_plan_downloads.html

**Reports & Pricing (5):** eligibility_report.html, project_report.html, dadu_reports_store.html, reports_pricing.html, homebody_pricing.html

**Legal & Forms (5):** determine_forms_required.html, legal_form_filler.html, restrictive_covenants_v2.html, dadu_documents_portal.html, pdf_database_lookup.html

**Dashboards (4):** contractor_dashboard.html, permit_activity_dashboard.html, nashville_permit_analytics.html, contractor_marketplace.html

**Learn/Reference (14):** what_is_dadu.html, dadu_building_requirements.html, dadu_design_standards.html, dadu_zoning_standards.html, permit_process_timeline.html, dadu_history.html, owner_occupancy.html, short_term_rental_permit.html, str_permit.html, trade_permits.html, overlay-districts.html, dadu_code_legislation_v3.html, dadu_legal_citations.html, dadu_legislation.html

**User Type Pages (3):** user-homeowners.html, user-types.html, features.html

**Feature Landing Pages (3):** feature-documents.html, feature-eligibility-map.html, feature-property-search.html

**Contractor & Advertising (3):** contractor_advertising.html, dadu_contractors_infographic.html, designer_resources.html

**Sample Reports (10):** sample_eligibility_report.html, sample_property_report.html, sample_contractor_report.html, sample_covenant_report.html, sample_permit_history_report.html, sample_comparables_report.html, sample_cost_estimate_report.html, sample_market_stats_report.html, sample_neighbors_report.html, sample_zoning_report.html

**Other (7):** about_platform_infographic.html, dadu_resources.html, legal_resources.html, market_trends.html, municipal_dashboard.html, homebody_dadu_pricing.html, property_report.html

### Repo Folder Structure

```
/DADU-Homebody-Projects/
├── index.html
├── homebody_header.html
├── homebody_header.js
├── homebody_shared.css
├── assets/
│   ├── castlehold_logo.png
│   ├── icons/          # 50+ PNG icons
│   ├── img/
│   ├── css/
│   └── js/
├── data/
│   ├── docs_index.json
│   ├── parcels_docs_summary.json
│   └── MATCHING_RULES.md
├── MASTER_ADU_DATA/
│   ├── PDF_Database_By_APN.json
│   ├── contractors_ranked.json
│   ├── parcels_eligibility_lite.json
│   └── permits_for_map.json
├── sample_reports/     # 10 HTML sample report files
├── pages/
│   ├── features/
│   └── users/
├── docs/
└── samples/            # Design reference library (DO NOT MODIFY)
```

### Available PNG Icons

```
Parcel_Search.png       Property_Owners.png      Building_and_Construction.png
Zoning.png              Recorded_Docs.png        Exports__Reports.png
GIS.png                 APN_Maps.png             Area_Maps_and_Visual_layers.png
Investors.png           Appraisers.png           Surveyors_and_Engineers.png
Municipal.png           Utilities.png            Legal.png
Farming.png             Bulk_data.png            ADU.png
```

---

## 5. DATA ASSETS & SOURCES

### Master Datasets (Local)

| Dataset | Records | Size | Key Fields | Location |
|---------|---------|------|------------|----------|
| tn_davidson.csv (Regrid) | 284,425 | 428 MB | APN, ll_bldg_count, ll_address_count, owner, siteaddr, zoning, landval, improvval, acres, lat, lon | MASTER_ADU_DATA/ |
| Parcels_with_links.csv | - | 446 MB | APN, ACCOUNTNUMBER, all URL templates pre-built | Root |
| assessor_accounts_20260114.csv | 277,619 | - | USER_ACCOUNT (APN), ACCOUNTNUMBER | Root |
| Ownership_Parcels_20260118.csv | - | 140 MB | Owner, FinishArea, Appraisal values, LUCode, TaxDist | Root |
| MASTER_Parcels_5_ADU_Indicators_20260117.csv | 284,425 | - | 5 ADU signal flags | MASTER_ADU_DATA/ |
| MASTER_Parcels_Strong_ADU_Signal_20260117.csv | 5,647 | - | Parcels with 2+ ADU indicators | MASTER_ADU_DATA/ |
| DADU_Eligibility_ENHANCED_20260119.csv | 123,574 | 232 MB | USD/GSD/overlay classification | MASTER_ADU_DATA/ |
| DADU_All_Permits_Cleaned.csv | 4,700+ | - | PermitNum, contractor, cost, date | Root |
| singlefamily_permit_history_copy.csv | - | 432 MB | Full single family permit history | Root |
| Parcels with Covenants.xlsx | 43,710 | - | Covenant URLs, recording info, all parcel URLs, geometry, lat/lon | 09_Covenants_Deeds/ |
| PropertyShark_2Unit_SFR_Clean.csv | 6,800+ | - | Confirmed 2-unit properties (98.9% validation) | Root |

### ADU Indicator Sources

| Indicator | Records | Description |
|-----------|---------|-------------|
| regrid_2plus_bldgs | 67,283 | Properties with 2+ buildings |
| has_county_adu_permit | 827 | Metro DADU permits |
| has_3rdparty_adu_permit | 1,868 | RE Data/RealtyTrac permits |
| has_fraction_B | 10,301 | Secondary address indicators |
| has_recorded_covenant | 1,125 | Restrictive covenant filings |

Summary: Any ADU signal 73,307 parcels. Strong signal (2+) 5,647 parcels. All 5 indicators 282 parcels. Validation: 98.9% detection rate against PropertyShark confirmed 2-unit properties.

### GeoJSON Files (Local - MASTER_ADU_DATA/)

| File | Size | Records | Use |
|------|------|---------|-----|
| MASTER_Parcels_Combined_20260118.geojson | 1.0G | 284,984 | All parcels with merged attributes |
| DADU_Eligibility_ENHANCED_20260119.geojson | 848M | 123,574 | Eligible parcels |
| parcels_with_building_counts.geojson | 465M | - | Building count analysis |
| Building_Footprints_SingleFamily.geojson | 175M | - | SFH building footprints |
| Address_Points_20260118.geojson | 150M | 343,148 | All Nashville address points |
| Parcels_With_Secondary_20260118.geojson | 111M | 69,211 | Any secondary structure indicator |
| Parcels_Strong_Secondary_20260118.geojson | 55M | 33,328 | 2+ data sources agree |
| NEW_ADU_Permits_20260114.geojson | 8.7M | 4,117 | 3rd party permits with NEW_ADU flag |
| Address_Points_Fraction_B_20260117.geojson | 8.6M | ~10K | Secondary addresses |

### GeoJSON Files (Reference_Data/)

| File | Size | Use |
|------|------|-----|
| Footprints_Parcels_Joined_20251115.geojson | 4.4G | Building footprints + parcel attributes |
| Buildings_With_ParcelAttributes_20251117.geojson | 1.2G | Buildings with parcel info |
| APNs.geojson | 395M | Parcel boundaries with zoning |
| Nashville_Parcels.geojson | 395M | Parcel boundaries |
| Building_Footprints.geojson | 204M | 327,884 buildings with Height, BuildingType, Area |
| USA_Structures_FEMA_FULL_20260117.geojson | 256M | FEMA building footprints |
| address_points_not_P.geojson | 30M | 67,148 secondary addresses (Fraction B = separate dwelling) |

### GeoJSON Files (Web-Ready for GitHub Repo)

| File | Size | Use |
|------|------|-----|
| eligibility_parcels.geojson | 75M | Eligible parcels |
| web_lite_parcels_points_20260123.geojson | 56M | Lightweight parcel points |
| web_lite_parcels_polygons_20260123.geojson | 56M | Lightweight parcel polygons |
| NEW_ADU_Permits_20260114.geojson | 8.7M | Permits for map |
| dadu_explorer_data.geojson | 4.7M | Explorer tool data |
| dadu_footprints.geojson | 4.4M | Building footprints for viewer |

### Permit Data Sources

| Source | Records | Key Fields |
|--------|---------|------------|
| Davidson_Permit_History/ (3rd Party) | 962,118 total (32 CSV files) | PERMIT_NUMBER, APN, DESCRIPTION, DATA, PERMIT_DATE |
| ADU_Permits_Points_20260117.geojson (County) | 891 | APN, Permit Number, Covenant Number, Covenant URL, Purpose, Date Issued |
| NEW_ADU_Permits_20260114.geojson (3rd Party) | 4,117 | APN, PERMIT_NUMBER, PROJECT_SCOPE, DESCRIPTION, NEW_ADU flag |
| DADU_All_Permits_Cleaned.csv | 4,700+ | PermitNum, contractor, cost, date |

**Permit Data Reality:** 2,340 permits loaded with verified data. Fields with data include CONTRACTOR_BIZ_NAME_ORIGINAL and CONTRACTOR_LICENSE. Other contractor fields may be empty. Do not rely on empty columns.

### Covenant Data

| Source | Records | Use |
|--------|---------|-----|
| Parcels with Covenants.xlsx | 43,710 | COMPREHENSIVE master file with full parcel info, covenant URLs, all external link templates |
| MASTER_Covenants_All_20260117.csv | 1,603 unique APNs | Combined from DADU_Permits (891), Permit_Extraction (1,943), APN_Covenants (213), Land_Records (7) |
| Restrictive Covenant PDFs | 8,514 files | In 09_Covenants_Deeds/Restrictive_Covenants/, filename = instrument number |

### Google Drive Documents

13,000+ documents uploaded (6GB+ via rclone): 698 aerial screenshots, 630 permit PDFs, 3,358 property cards, 8,514 restrictive covenants. MASTER_PDFs_By_APN.csv links 5,791 APNs to Google Drive URLs.

---

## 6. PARCEL IDENTIFIERS & KEY RELATIONSHIPS

### Three IDs

| ID | Format | Use |
|----|--------|-----|
| APN (STANPAR) | 11-digit | Primary key linking ALL datasets |
| ParcelID (PARID) | Variable | Nashville parcel system |
| ACCOUNTNUMBER | Variable | Property card URLs |

**Mapping file:** assessor_accounts_20260114.csv maps USER_ACCOUNT (APN) to ACCOUNTNUMBER.

### Relationships

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
```

---

## 7. API ENDPOINTS & DATA SERVICES

### Nashville ParcelService SOAP API

Base URL: `https://maps.nashville.gov/ParcelService/Search.asmx`

| Endpoint | Parameter | Returns |
|----------|-----------|---------|
| /GetPermitHistory | apn={APN} | All permits for parcel |
| /GetGenInfo | pin={PIN} | General parcel info |
| /GetOwnerHistory | pin={PIN} | Ownership chain |
| /GetZoningHistory | pin={PIN} | Zoning changes |
| /GetAssessmentHistory | pin={PIN} | Assessment values |
| /GetPin | apn={APN} | Convert APN to PIN |

### Nashville ePermits API

Base URLs:
- `https://eservices.nashville.gov/IPS` (internal portal services)
- `https://epermits.nashville.gov/api` (public API with OData-style filtering)

Key endpoints across permit/1.0 and ePermit/1.0 namespaces. CaseSubTypeID 774 specifically identifies DADU permits. CaseQuantityGroupDetail endpoint with detailCode 'RESCONVAL' or 'PROJSCOPE' extracts construction values and detailed project descriptions.

### Nashville Document System

- Permit URLs redirect, AJAX polling /Request/PartCheck every 5 seconds
- "Part Count: 0" = no PDF available
- Document portal: documents.nashville.gov/Request/Form/PermitCodes

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

# ePermits by PID
https://epermits.nashville.gov/?#/permit/{PID}

# ePermits Search by APN
https://epermits.nashville.gov/#/search?searchCode=APN&searchText={APN}

# Property Assessor
https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}

# Property Cards (Print)
https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}

# Property Cards (Building Detail)
https://portal.padctn.org/OFS/WP/Building/{ACCOUNTNUMBER}/2

# Property Cards (Summary)
https://portal.padctn.org/OFS/WP/Summary/{ACCOUNTNUMBER}/2

# Google Street View
https://www.google.com/maps?q&layer=c&cbll={LATITUDE},{LONGITUDE}

# Nashville Aerial (Patriot Properties)
https://portal.patriotproperties.com/?APIKEY=5D050659143EB96630FB38B91DE12E40&SECRETKEY=A92169630C9BC3C00A1C0F9F140E6DAEC21C8E62DCFF9FC443FB1BE70DDF6AA4268527B9DDE2ECC2C7EE9BB5BF728C06F0DF4019BBECDEBD2A6DD0BBE28A419D8F929E1F3E8DF478E56619995BEFCA8E369276689D791197DC1284F14B3252DBFB2A19A2E451EEA832D6D96488DDC673EBA4B37BD741223B656A793D93209C0F&LAT={LATITUDE}&LONG={LONGITUDE}

# Covenant Documents
https://davidsonportal.com/landrecords/view_image.php?key=/img/tn/davidson/{YYYY}/{MMDD}/{INSTRUMENT}.tif
```

### ArcGIS Feature Services (Vanderbilt Hosted)

| Layer | URL | Records |
|-------|-----|---------|
| DADU Eligibility Enhanced | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer | 161,703 |
| DADU Building Specs | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Building_Specs_20260119_042856/FeatureServer | Max DADU size, setbacks, height |
| DADU All Permits Final | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_All_Permits_Final/FeatureServer | 4,700+ |
| NEW ADU Permits | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/NEW_ADU_Permits_20260114/FeatureServer | 4,117 |
| Footprints With Parcel Data | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer | Building footprints + parcel attrs |
| SFH Parcels | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/SFH_parcels/FeatureServer | All single-family homes with URLs |
| Parcels with Restrictive Covenants | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer | 43,710 |
| Building Footprints SingleFamily | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Building_Footprints_SingleFamily/FeatureServer | - |
| Parcels with Zoning | services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Parcels_with_Zoning_view_A1_AD16330_eWiX6s/FeatureServer | - |
| DADU BL2025 Eligible | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_BL2025_1007_Eligible_20251230_011045/FeatureServer | - |
| Secondary SFH Merged | services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Secondary_SFH_Merged_SHP_20251231_0015/FeatureServer | Existing secondary structures |

### ArcGIS Feature Services (Nashville Official)

| Layer | URL | Records |
|-------|-----|---------|
| Parcels with Building Characteristics | services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/Parcels_with_Building_Characteristics_view/FeatureServer/0 | 285,512 |
| Base Zoning | maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/BaseZoning/MapServer/0 | - |
| USD/GSD Boundary | maps.nashville.gov/arcgis/rest/services/Boundaries/USD_GSD/MapServer/0 | - |
| Zoning Overlay Districts | maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/Zoning_Overlay_Districts/MapServer | - |
| ParcelHistory Layer 4 | maps.nashville.gov/arcgis2/rest/services/Parcels/ParcelHistory/MapServer/4 | Permit history with construction values |
| Address Points | maps.nashville.gov/arcgis/rest/services/Parcels/Address_Points/FeatureServer | - |
| Building Footprints | maps.nashville.gov/arcgis/rest/services/Buildings/Building_Footprints_view/FeatureServer | 327,884 |
| Cadastral Layers | maps.nashville.gov/arcgis/rest/services/Parcels/Cadastral_Layers/MapServer | - |
| Development Tracker Cases | services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/Development_Tracker_Cases_view/FeatureServer/3 | Query: MPCNUM like '%DDU%' |
| Planning DevTracker Cases | maps.nashville.gov/arcgis/rest/services/Planning/DevTracker_Cases/FeatureServer/0 | Query: pertype = 'DADU Overlay (New)' |

---

## 8. BL2025-1007 ELIGIBILITY RULES

Effective December 12, 2025.

| Criterion | Requirement |
|-----------|-------------|
| Zoning | R or RS zones only |
| USD (Urban Services District) | By-right construction (67,707 newly eligible parcels) |
| GSD (General Services District) | Requires overlay district |
| Lot < 10,000 SF | Max 700 SF living / 750 SF footprint |
| Lot >= 10,000 SF | Max 850 SF living / 1,000 SF footprint |
| Height | Cannot exceed principal structure |
| Owner Occupancy | Required (principal or DADU) |

### Eligibility Statistics

| Metric | Value |
|--------|-------|
| Total Nashville Parcels | 285,512 |
| BL2025-1007 Eligible (USD by-right) | 67,707 |
| Total Eligible (USD + GSD with overlay) | 123,574 |
| Historic DADU Permits | 827 |
| Third-party Permits | 1,800+ |
| Unique Contractors | 393 |
| Legal Citations | 111 |
| Parcels with Covenants | 43,000+ |

---

## 9. LEGISLATIVE CATALOG

### DADU Overlay District Ordinances (8 ordinances, ~730 acres)

| Bill | Date | Description | Acres |
|------|------|-------------|-------|
| BL2021-620 | 5/18/2021 | Creates DADU Overlay District (original) | - |
| BL2021-784 | 12/7/2021 | Expand to UZO and Highland Heights | - |
| BL2021-791 | 12/7/2021 | E Trinity/Douglas/Dickerson | 109.45 |
| BL2021-953 | 11/16/2021 | Scovel/I-65 area | 295.27 |
| BL2022-1322 | 7/19/2022 | Gallatin/Ellington Pkwy | 75.01 |
| BL2023-1761 | 4/18/2023 | Clifton/Jefferson | 106.63 |
| BL2023-2094 | 8/15/2023 | Fairfax/Barton Ave | 20.53 |
| BL2024-559 | 11/19/2024 | Douglas/W Eastland/Gallatin | 123.10 |

**Pending:** BL2025-1146 (Creates DADU Exclusion Overlay)

### Individual Parcel Rezonings (15 ordinances)

BL2025-1130, BL2025-1135, BL2025-993, BL2025-870, BL2025-795, BL2025-749, BL2025-738, BL2024-620, BL2024-539, BL2024-491, BL2024-320, BL2024-220, BL2023-64, BL2022-1555, BL2022-1288

### Urban Design Overlays with DADU Standards (10 overlays)

| UDO | Case No. | Year | PDF Link |
|-----|----------|------|----------|
| Bellwood | 2015UD-001-001 | 2015 | nashville.gov/sites/default/files/2025-09/03-BellwoodUDO.pdf |
| Carothers Crossing | 2005UD-003G-12 | 2005 | nashville.gov/sites/default/files/2025-09/04-CarothersCrossingUDO.pdf |
| Clayton Avenue | - | 2025 | nashville.gov/sites/default/files/2025-09/08-ClaytonAveUDO.pdf |
| Clarksville Pike at Fairview Center | - | 2017 | nashville.gov/sites/default/files/2025-09/11-FINAL_Clarksville_Pike_UDO.pdf |
| Lenox Village | 2005UD-007G-1 | 2005 | nashville.gov/sites/default/files/2025-09/21-LVUDO.pdf |
| Moss Spring Drive/Edge-O-Lake | 2017UD-003-001 | 2017 | nashville.gov/sites/default/files/2025-09/22-MossSpringDriveUDO.pdf |
| The Nations | 2025UD-002-001 | 2025 | nashville.gov/sites/default/files/2025-09/26-The-Nations-UDO.pdf |
| Payne Road Residential | 2017UD-006-001 | 2017 | nashville.gov/sites/default/files/2025-09/27-PayneRoadUDO.pdf |
| Wedgewood-Houston Chestnut Hill | 2021UD-001-001 | 2021 | nashville.gov/sites/default/files/2021-08/WedgewoodHoustonChestnutHill-UDO-AdoptedDraft.pdf |
| Whites Creek at Lloyd Road | 2017UD-001-001 | 2017 | nashville.gov/sites/default/files/2025-09/34-whites_creek_at_Lloyd_Road_UDO.pdf |

### Specific Plan DADU Approvals (5 cases)

| Case | Address | Date | Details |
|------|---------|------|---------|
| 2015SP-111 | 1212 Pennock Ave | 1/14/2016 | SP allowing DADUs with alley access or 15,000+ SF lots |
| 2017SP-025 | 1424 Stainback Ave | 6/22/2017 | RS5 to SP-R for existing structure as DADU |
| 2019SP-008 | 311 Gatewood Ave | 1/24/2019 | RS5 to SP-R for DADU, Highland Heights R1 |
| 2021SP-001 | 4027 Red Rose Ct | 2021 | DADU conditions per Title 17 |
| 2023SP-067 | 1631 16th Ave N | 3/14/2024 | RS5 to SP for two detached units in DADU Overlay |

Planning Commission minutes: maps.nashville.gov/sp/{YEAR}/{CASE}/PC_Minutes_{CASE}.pdf

### Historic Zoning Commission DADU Cases (4 documented)

- 12/19/2018: 3930 Cambridge Ave (Cherokee Park NCZO)
- 10/17/2018: 1910 19th Ave S (Belmont-Hillsboro NCZO)
- 7/17/2019: Various addresses
- 1/17/2018: 1304 Gartland Ave (Lockeland Springs NCZO)

MHZC minutes: nashville.gov/sites/default/files/2022-09/{DATE}_Minutes.pdf

---

## 10. PRODUCT FEATURES & PRICING

### Pricing Strategy

**Individual Reports:**
- $4 Quick Eligibility
- $6 Zoning Report
- $19 DADU Eligibility Report (flagship)
- $25 Comprehensive Permit Package

**Subscription Tiers:**
- $19/month Homeowner Basic
- $49/month Contractor Pro
- $149/month Enterprise

**Contractor Listings:**
- Free basic
- $99/month featured
- $249/month premium

**Bulk Data:** $199-$299 downloads

### Free Tier (Near Me Locator)

- View completed/permitted DADUs within radius
- See contractor names (when available)
- See construction cost range
- See basic permit info
- Links to external verification pages

### Paid Tier 1 ($4.99 DADU Detail Report)

- Full permit details
- Exact construction cost
- Building square footage
- Cost per square foot
- Permit documents (PDFs)
- Property card PDF
- Aerial and Street View links

### Paid Tier 2 ($9.99 Contractor Report)

- All DADUs by contractor
- Average cost per sqft
- Project locations
- Contact info (if available)

### Paid Tier 3 ($14.99 Area Analysis Report)

- All DADUs in neighborhood/zip
- Cost trends over time
- Most active contractors
- Approval timeline statistics

### Implementation Approach (Hybrid MVP)

- ArcGIS map for discovery and free tier
- GitHub Pages for report pages and document browsing
- Payments placeholder first, then Stripe integration later

---

## 11. PROPERTY REPORT CARD (CORE PRODUCT SPINE)

Everything routes into or fans out from the Property Report Card keyed to APN or ParcelID. This is the central hub of the entire platform.

### Must Aggregate

- Eligibility status under BL2025-1007
- Zoning and service district context
- Size limits based on lot size
- Permit history
- Restrictive covenants
- Building footprints
- Available PDFs (property cards, permits, covenants)
- Verified outbound government links (all templates from Section 7)

### Functions As

- Upgrade surface for paid reports
- Hub connecting all tools and features
- Single canonical parcel page accepting APN or ParcelID

**Rule:** If a feature cannot logically connect back to a parcel, it does not belong in MVP.

---

## 12. NEAR ME LOCATOR SPECIFICATION

### Inputs

- Address input with autocomplete (preferably ArcGIS geocoder)
- Radius selector: 0.25, 0.5, 1, 2 miles (default: 0.5 mi)
- Filter toggles: Completed DADUs, Permitted DADUs, In review, Covenants recorded, Contractor projects

### Outputs

- Map with markers or parcel highlights
- List sorted by distance
- Each result card shows: Address, Permit number, Date, Square footage (if present), Cost (if present), Contractor business name (if present)
- Action buttons: View Property Report, Open ParcelViewer, Open ePermits, Open Permit Documents

### Data Logic

- Use most reliable available layers
- If "completed DADUs" layer exists, use it
- Otherwise use permit history filtered by DADU-related scope terms
- Support pagination for large result sets
- If using ArcGIS Feature Service queries, respect maxRecordCount and paginate

---

## 13. DOCUMENT PORTAL & MATCHING REQUIREMENTS

### Document Portal Features (ParcelQuest-Inspired)

Search by: APN, address keyword, document type, permit number, document number

Documents accessible from parcel detail page and parcel history view. Advanced search supports doc type and doc number searching. Report library style with sample bundles and clear descriptions.

### Document Index Structure

Create data/docs_index.json with entries:

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

1. Extract APN candidates from filenames using regex for 10-12 digit sequences
2. Normalize APN length to single standard (11 digits) by left-padding with zeros
3. Extract permit number candidates using regex patterns: date_underscore_numeric (20171101_12816611), plain numeric blocks
4. Join documents to permits using permit number keys
5. Join property cards to parcels using APN + ACCOUNTNUMBER mapping
6. Join restrictive covenants to parcels using APN when possible, otherwise address match, otherwise flag for manual review

### Known Filename Patterns

```
Property Cards:
  PropertyCard_15000021300_176174.pdf
  (APN appears as 15000021300, may need normalization with leading zeros)

Permit PDFs:
  fe990b2d-e71d-4963-90b6-5f068543e109_CA-Permits-20171101_12816611_1.pdf
  (Extract permit key: 20171101_12816611 or numeric like 2017047359)

Covenant PDFs:
  20240710-0051719.pdf
  (Instrument number as filename)
```

### Per-Parcel Summary

Generate data/parcels_docs_summary.json keyed by APN:

```json
{
  "15000021300": {
    "property_cards": [{"doc_id": "...", "url": "..."}],
    "permits": [{"doc_id": "...", "permit_number": "...", "url": "..."}],
    "covenants": [{"doc_id": "...", "url": "..."}],
    "site_plans": []
  }
}
```

---

## 14. PLATFORM FEATURES BY USER TYPE

### Homeowners

- Am I Eligible? address lookup with instant determination
- What Can I Build? size limits based on lot size
- Find DADUs Near Me map of completed projects
- Property Viewer detailed parcel analysis with building footprints
- Cost Calculator ROI estimates based on permit cost data
- Restrictive Covenants check for deed restrictions
- Feasibility Report, Site Plan Preview, Contractor Matches (paid)

### Contractors/Builders

- Permit Explorer search all Nashville building permits
- Market Analytics costs, trends, demand by ZIP code
- Top Contractors Leaderboard rankings by permit volume
- Project Leads eligible properties without permits
- Contractor Profile showcase completed projects
- Pricing Benchmarks compare costs to market averages
- Territory Analysis heat maps of opportunity areas

### Designers/Architects

- Building Requirements Database zoning codes by district
- Precedent Gallery photos and plans of approved DADUs
- Site Analysis Tools setback calculators, height limits

### Investors/Developers

- Parcel Data Exports CSV/GeoJSON downloads
- Permit History complete permit records by area
- Opportunity Maps eligible parcels without existing ADUs

### Municipal/Government

- Permit Tracking Dashboard real-time permit activity
- Impact Analysis pre/post BL2025-1007 comparisons
- Compliance Monitoring owner occupancy verification tools

---

## 15. PYTHON SCRIPTS INVENTORY

| Script | Purpose | Status |
|--------|---------|--------|
| download_permit_pdfs_v2.py | Selenium automation, 377 permits, 90sec wait, checkpoint system | Created |
| download_property_cards.py | Chrome DevTools PDF print, 2,169 target cards | Created |
| pull_dadu_parcelhistory.py | Three-query ArcGIS ParcelHistory Layer 4 scraper with pagination | Created |
| lookup_epermit_full.py | Query all 10 ePermits API endpoints for any caseID | Created |
| download_udo_pdfs.py | Download Urban Design Overlay PDFs | Created |
| build_document_indices.py | Build docs_index.json from PDF filenames | Created |
| create_permit_pdf_mapping.py | Map Google Drive file IDs to permit numbers | Created |
| permit_history_download_template.py | Nashville ParcelService SOAP API bulk downloader | Created |

### Script Requirements

- Nashville government servers require careful rate limiting (1-2 second delays)
- Timeout handling (30-second limits) to prevent hanging
- Checkpoint saves every 20 batches with timestamp
- Retry logic with exponential backoff for API limitations
- ArcGIS REST services typically have max record counts of 100, 1000, or 2000; always loop beyond the record count

---

## 16. DEVELOPMENT PRIORITIES (ORDERED)

1. **Stabilize site:** Remove merge conflict markers, fix broken links, lock folder structure, implement Castlehold mega-menu navigation across all pages
2. **Build Property Report Card:** One canonical parcel page accepting APN or ParcelID, show eligibility, zoning, size limits, permits, covenants, documents, verified outbound links
3. **Solve document indexing:** Offline Python script scanning filenames, normalizing APNs, extracting permit numbers, joining PDFs to parcels/permits, generating docs_index.json and parcels_docs_summary.json
4. **Implement Near Me Locator:** Address input + radius, query DADU/permit layers with pagination, map + sorted list, every result links to Property Report Card
5. **Build Document Portal UI:** Search/filter by APN, address, doc type, permit number, ParcelQuest-style recorded documents experience
6. **Add contractor aggregation:** Group permits by contractor where fields exist, show counts and averages, foundation for Contractor Reports and marketplace
7. **Layer in calculators:** ROI, cost, tax, timeline built on real permit and eligibility data
8. **Polish:** User type landing pages, educational pages, premium report previews, visual refinements

**Guiding rule:** If it does not strengthen, feed, or route into the Property Report Card, it is not a priority.

---

## 17. PENDING TASKS

### Website

- Resolve index.html merge conflict (<<<<<<< HEAD markers) if still present
- Copy missing infrastructure to live repo if needed (homebody_header.html, homebody_shared.css, castlehold_logo.png)
- Copy sample_reports/ folder (10 files) to live repo if needed
- Rebrand remaining Gen 1 pages from Homebody to Castlehold
- Commit and push website changes to GitHub Pages
- Test Near Me widget functionality
- Complete municipal_dashboard.html and appraiser_tools.html

### Data Processing

- Download Card 2 images for 2,089 SINGLE FAMILY records
- Run download_permit_pdfs_v2.py for 377 permits
- Run download_property_cards.py for 2,169 cards
- Create restrictive covenants download script
- Extract Tier 1 ePermits data for all DADU cases
- Parse PROJSCOPE text for square footage/dimensions/setbacks
- Query Trade_Permits_View FeatureServer
- Upload MASTER_Parcels_Strong_ADU_Signal.csv to ArcGIS
- Process property assessor data for secondary structure identification

### Integration

- Implement Stripe integration for paid reports
- Nashville ePermits API data extraction workflows
- Google Drive PDF integration for 8,514+ restrictive covenant documents
- Build searchable document portal with PDF retrieval

---

## 18. TECHNICAL DISCOVERIES & KNOWN ISSUES

- Nashville document system: Permit URLs redirect, AJAX polling /Request/PartCheck every 5s, "Part Count: 0" = no PDF
- PropertyShark code "074" = TN Comptroller code 74 "Timber tract with SF Residential AND Mobile Home" (multi-unit indicator)
- Fraction B addresses indicate secondary structures (667 permits with "B" designators)
- AssessorCardNumber=2 with StructureType "single family homes" indicates DADUs
- Building footprint Shape_Area in square feet (EPSG:2274 Tennessee State Plane)
- ArcGIS queries: 'where': '1=1', 'returnGeometry': 'true', 'outSR': '4326', 'f': 'geojson'
- ArcGIS pagination: Handle maxRecordCount using resultOffset/resultRecordCount or objectId paging
- Property assessor data requires careful handling of multiple card numbers per parcel (Card 2 = secondary structures)
- Government API limitations necessitate robust pagination, retry logic, and checkpoint systems

---

## 19. SAMPLES FOLDER RULES

The /samples/ folder contains screenshots, HTML examples, and reference layouts from competitor websites. Treat as a design pattern library.

Rules:
1. DO NOT delete, rename, or modify anything in /samples/
2. DO NOT move copied folders
3. USE /samples/ as visual and information architecture inspiration
4. For every major UI component, explicitly map it to: a Samples reference AND a competitor reference, then implement the Castlehold version
5. If you cannot access /samples/ directly, ask for filenames or screenshots but keep working using competitor references as fallback

---

## 20. WRITING & FORMATTING GUIDELINES

### Voice and Tone

Confident and declarative. No hedging words like "somewhat," "arguably," "it seems that," or "it could be said." Professional but accessible. Let the substance speak for itself.

### Sentence Construction

Use active voice. Make the subject of each sentence a clear actor. Turn actions into verbs, not nouns ("investigated" not "conducted an investigation"). Start sentences with familiar information and end with new. Cut metadiscourse and throat-clearing phrases.

### Punctuation

Never use em dashes. If a sentence needs multiple commas, break it into two sentences.

### Content Rules

No interpretive gloss ("demonstrating that," "this shows that"). No assumed causation from correlation. No added references or assumptions beyond what is provided.

### Citations

Every source needs: full URL + Bluebook legal citation. For PDFs: PDF viewer page number + document internal page number.

---

## 21. DELIVERABLES FORMAT

When responding with work, provide:

1. **A short plan** describing what you will build and why
2. **Exact file paths** relative to repo root
3. **Complete code** for each file you touch (no partial snippets unless explicitly requested)
4. **Notes on icons** where to place them and expected filenames
5. **GitHub Pages test checklist** steps to verify everything works

### File Naming Convention

```
dadu_[feature]_[version].html
Examples: dadu_property_viewer_v3.html, homebody_index_v4.html
```

---

## 22. SCOPE BOUNDARIES

### Do

- Keep it functional and polished
- Implement navigation, Property Report Card, Near Me Locator, and Document Portal first
- Use client-side JavaScript for GitHub Pages compatibility
- Prefer JSON indexes for documents and permit summaries
- Cache repeated lookups in session storage when reasonable

### Do Not

- Overbuild beyond MVP requirements
- Load huge GeoJSON at initial page load (load on demand)
- Expose sensitive API keys (propose serverless proxy for later if needed)
- Rely on contractor columns that are empty (only use fields that actually contain data)

---

## 23. PROJECT STATISTICS

| Metric | Count |
|--------|-------|
| HTML pages | 95+ |
| Python scripts | 10+ |
| Academic papers | 3 |
| Excel reference files | 4 |
| JSON indexes | 7 |
| Icon assets | 50+ |
| SVG infographics | 5 |
| Documents downloaded | 13,000+ |
| Parcels analyzed | 285,512 |
| Data uploaded to Drive | 6GB+ |
| ArcGIS endpoints documented | 13 Vanderbilt + 10 Nashville |
| ePermits API endpoints cataloged | 30+ |
| Legal citations organized | 111 |
| DADU overlay ordinances | 8 (~730 acres) |
| UDOs with DADU standards | 10 |
| SP DADU approvals | 5 |
| MHZC DADU cases | 4 |

---

**END OF COMPREHENSIVE INSTRUCTIONS**

This document should be provided to any AI assistant helping complete the Castlehold platform. It contains all context needed to maintain consistency across development sessions.
