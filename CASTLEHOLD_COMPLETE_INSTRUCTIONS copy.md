# CASTLEHOLD DADU PLATFORM — WHAT I WANT AND WHAT NEEDS TO BE DONE

**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Date:** February 12, 2026
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/
**Repo:** ~/DADU-Homebody-Projects/

---

## PART 1: WHAT THIS PLATFORM IS

Castlehold is a DADU (Detached Accessory Dwelling Unit) zoning and buildability intelligence platform for Nashville-Davidson County. It aggregates public parcel data, building permits, restrictive covenants, and regulatory information into one website. Nashville's BL2025-1007 legislation (effective December 12, 2025) expanded DADU eligibility to 67,707 parcels. Nashville is the proof of concept. The permit and parcel infrastructure generalizes across any U.S. municipality, so the platform can scale nationally.

This project supports coursework in Professor Lehrman's "Networks, Law, and Entrepreneurial Strategy" class at Vanderbilt Law School. It demonstrates how standardized building permit infrastructure creates network effects.

The business model draws from ParcelQuest (navigation, user type segmentation, pricing tiers, recorded documents portal), Symbium (property-specific feasibility reports), First American (document downloads, property detail pages), PropStream (ROI calculators, decision tools), and Regrid (parcel data API, mapping layers).

### Competitor Profiles and What We Adapt

**Symbium** (https://build.symbium.com/) — Primary ADU competitor. California-focused. Free property search with four features: Property, Designs, Sketch, ADU Report. The map highlights the parcel border on click and renders building footprints within the parcel. Adapt this interaction for our DADU Explorer. Browse Designs shows generic options; ours should display actual Nashville site plans from permitted DADUs on similar lots. Sketch an ADU lets users drag a proposed building onto the parcel with live cost estimates. ADU Report requires account creation. Symbium charges $50 per plan check. Tiers: Standard (instant permitting, unlimited compliance) and Symbium Permitting (government licensing). Free for homeowner and professional searches.

**First American Data & Analytics** (https://dna.firstam.com/solutions/property-data/property-reports) — Report library model to replicate. Each report type shown as a card with icon, title, description, "Popular with" user tags, and "Download Sample Report" link. Reports: Property Detail ($4.00), Transaction History ($9.00), TotalView ($22.00), Sales Comparables ($9.00), Neighbors, Market Statistics, Open Lien, Foreclosure, HOA. The First American Store (https://dnastore.firstam.com) lets users search by address and see all available reports with Add to Cart buttons. Two access paths: DataTree (enterprise) and Online Store (pay-as-you-go or subscription). Adapt the report card layout, per-report pricing, and sample download pattern.

**ATTOM Property Navigator** (https://propertynavigator.attomdata.com/) — Primary UI inspiration for the DADU Explorer Map Search. Two modes: Property Search and Map Search. Map search features a filter panel with property type, lot size range, year built range, price range, sqft range. Results appear as property cards with map pins. Replicate for DADU Explorer with Nashville-specific filters: zipcode, lot size, stories, home sqft, service district, DADU eligibility, year built, cost, DADU sqft.

**ParcelQuest** (https://www.parcelquest.com/) — Navigation and feature structure inspiration. Top nav Features dropdown: Zoning, Parcel Search, APN Maps, Area Maps, Property Owners, GIS, Exports & Reports, Recorded Documents, Bulk Data. Each has a distinct icon. Industries dropdown segments by user type. Pricing: Navigator ($199.95/month, 1,000 records), Aviator ($249.95/month, 10,000 records), Detail Reports ($14.95 each).

**Regrid** (https://app.regrid.com/) — Parcel data and popup model. Parcel popup shows: address, measurements, owner, zoning, land use, parcel ID, sales/value history, structure details, building area, census, legal description, environment scores. Pricing: Starter (free, 25 lookups/day), Pro ($10/month, 1,000 lookups/day), Team ($20/month/user, unlimited).

**PropertyShark** (https://www.propertyshark.com/) — Property report and list model. Tennessee Pro at $49.95/month: 175 property reports/month, ownership, sales/liens/title docs, 1,000 ownership reports, 2,000 mailing exports. Reports cover characteristics, zoning, owners, tax assessments, sales history.

**PropStream** (https://www.propstream.com/) — Investment analysis and calculator tools. ADU Calculator (https://www.propstream.com/news/adu-calculator) estimates costs and ROI. Adapt for Nashville DADU cost estimation using local permit data.

**US Title Records** (https://www.ustitlerecords.com/) — Pay-per-report model without subscriptions or logins. All orders anonymous. Reports: Full Property Detail ($29), Lien Search ($95), Full Property/Owner Lien ($195), Chain of Title ($275), Document Image ($45), Preliminary Title ($295). Downloadable PDFs 7 days/week. Adapt the anonymous per-report ordering flow as an alternative to subscription access.

**Houzz Pro** (https://www.houzz.com/houzz-pro/) — Pricing page and industry segmentation model. Lets users choose plans by industry (New Construction, Remodeling, Interior Design, Architecture, Painting). Navigation: Features, Who We Serve, Learn, Pricing. Adapt the industry-segmented pricing for our user types and categorical feature organization.

### Pricing Model (Hybrid)

Free public access to DADU eligibility map and general location data. Subscription access for search tools, exports, and detailed reports. Pay-per-report option for individual eligibility reports, contractor reports, and area analysis. Marketplace features connecting homeowners with contractors.

---

## PART 2: WHAT THE WEBSITE IS SUPPOSED TO DO

### The Six Core Product Experiences

**1. Check My Property (the spine of everything)**
A user enters an address or APN. The site generates a Property Report Card that summarizes eligibility, constraints, permits, covenants, documents, and verified outbound links to Nashville government portals. Every other tool on the site funnels back to this page.

The Property Report Card loads data in four roles:
- **Role 1: Results Layer** (fast, clickable, drives cards). Populates map markers, results list, property cards, and filters. Must be points, reasonably sized, and queryable.
- **Role 2: Context Layers** (visual reference only). Add meaning but do not drive results. Toggled on/off.
- **Role 3: Detail Layers** (on click only). Load only when a user clicks a property. Not drawn for every record.
- **Role 4: Overlays and Constraints.** Eligibility status, restrictive covenants, zoning context.

The Property Report Card must link out to:
- Nashville ParcelViewer (uses STANPAR)
- ParcelViewer Print Record (uses PIN)
- Permit Documents by permit number or by APN (documents.nashville.gov)
- ePermits Portal (uses permit number, PID, or APN)
- Property Assessor (uses APN)
- Property Card PDF (uses ACCOUNTNUMBER from assessor_accounts_20260114.csv)
- Google Street View (uses lat/lon)
- Aerial imagery (Patriot Properties)

The map on the report card should show the parcel boundary and building footprints, Symbium-style: primary structure in one color, accessory structure in another. Parcels with AssessorCardNumber=2 and structure type "single family homes" indicate DADUs.

**2. Near Me Locator**
Enter an address, pick a radius (0.25, 0.5, 1, 2 miles, default 0.5). See a map and list of completed or permitted DADUs nearby. Each result shows address, permit number, date, square footage, cost, and contractor name where available. Results link to Property Report Cards. Free tier shows basic info. Paid tier unlocks detail.

**3. Eligibility Map**
Color-coded interactive map of all Nashville parcels. Green = eligible, yellow = conditional (needs overlay), red/gray = not eligible. Powered by the DADU_Eligibility_ENHANCED dataset (161,703 parcels) hosted on Vanderbilt's ArcGIS. Click any parcel to see its status and link to the Property Report Card.

**4. Permit Explorer**
Filter all Nashville building permits by type, date range, status, contractor name, cost range, and square footage range. Pagination and export. The data source is DADU_All_Permits_Cleaned.csv (6,822 permits total, 355 flagged DADU, 628 accessory).

**5. Document Portal**
ParcelQuest-style recorded documents search. Search by APN, address, document type, permit number. Returns permit PDFs, site plans, restrictive covenants, and property cards. Documents served from Google Drive folders. Accessible from parcel detail views and parcel history views.

**6. Contractor Marketplace**
Real data from permits. Top builders ranked by permit volume, average cost per SF, project locations. Real contractors include Palmetto Construction LLC (11 permits), Bootstrap Architecture + Construction LLC (6), WTW Construction (5), Legacy South Builders (5), Southern Edge Construction (5). 6,427 of 6,822 permits have contractor names. 2,072 unique contractors. No fake data.

### Calculators and Planning Tools

- ROI Calculator — Input build cost, rental income, expenses. Outputs ROI %, payback period, cash flow.
- Project Cost Estimator — Input sqft, finish level, features. Outputs detailed cost breakdown.
- Property Tax Increase Calculator — Input current value, DADU details. Outputs estimated tax increase.
- Size Calculator — Input lot size. Outputs max DADU dimensions (700/850 SF living, 750/1000 SF footprint) with visual lot diagram.
- Short Term Rental Permit ROI
- Project Planner / Checklist — Gantt-style timeline with Standard/Fast/Delayed scenarios. 27-item interactive checklist with 5 phases, progress tracking, saves to browser.
- Permit Process Timeline (step-by-step guide)
- Draw DADU on Parcel — Interactive Leaflet map for drawing DADU placement on lot.
- Am I Eligible? (quiz/flowchart)
- What Can I Build? (size limits based on lot)
- Determine Forms Required — 5-step wizard that answers which forms you need
- Legal Form Filler — Forms portal with all Nashville Metro forms by category (Building, Covenants, Historic, Trade, STR, Site Plans) with direct download links

### Learn and Reference Pages

- What is a DADU? (educational intro)
- DADU History and Timeline
- Building Requirements (setbacks, height, lot coverage)
- Zoning Standards
- Design Standards
- Code and Legislation Database (111+ legal citations, Bluebook format)
- Overlay Districts
- Owner Occupancy Explained
- Short Term Rental Permits
- Trade Permits
- Common Issues (using T_Permits_With_Issue_Flags.csv)

### Data and Analytics Pages

- Permit Activity Dashboard (real-time permit activity)
- Contractor Dashboard (contractor performance analytics)
- Market Trends (cost trends over time, demand by ZIP)
- Nashville Permit Analytics
- Secondary Structures Map
- ADU Opportunity Explorer
- Restrictive Covenants Dataset Page
- Building Permit Dataset / History Page
- FEMA Structures and Nashville Footprints Page

### Reports and Pricing (Monetization)

| Tier | Product | Price | Includes |
|------|---------|-------|----------|
| Free | Near Me Locator | $0 | Basic DADU info within radius, contractor names, cost ranges |
| Paid 1 | DADU Detail Report | $4.99 | Full permit details, exact cost, SF, cost/SF, permit PDFs, property card, aerial + street view |
| Paid 2 | Contractor Report | $9.99 | All DADUs by contractor, avg cost/SF, project locations, contact info |
| Paid 3 | Area Analysis Report | $14.99 | All DADUs in neighborhood/zip, cost trends, top contractors, approval timelines |

Payments as placeholder buttons first, Stripe integration later. Ten sample reports already exist in /sample_reports/.

### User Type Portals

Each user type gets a dedicated landing page with explanation, CTA, how it works, data sources, FAQ, and related tools.

- **Homeowners** — Eligibility check, what can I build, near me, property viewer, cost/ROI calculators, covenant check
- **Contractors/Builders** — Permit explorer, market analytics, top contractors leaderboard, leads, pricing benchmarks, territory analysis, contractor advertising
- **Designers/Architects** — Requirements database, precedent gallery, site analysis tools, setback calculators
- **Investors/Developers** — Exports, opportunity maps, bulk views, permit history by area
- **Municipal/Government** — Permit tracking, impact analysis (pre/post BL2025-1007), compliance monitoring
- **Legal/Appraisers** — Recorded documents, covenant checks, comparables, valuation data

### Landing Page Requirements

Every dropdown item in the navigation must land on a real page with four sections: "What this does," "Launch tool," "How it works," and "Data sources." Each page must route into the Property Report Card or fan out from it. If a feature cannot logically connect back to a parcel, it does not belong in the MVP.

### Guiding Rule

Every page answers one question: "Am I learning, acting, or verifying?" Learn lives in EXPLORE. Act lives in BUILD. Verify lives in DATA. Pricing stands alone. If a page does not strengthen, feed, or route into the Property Report Card, it is not a priority.

---

## PART 3: NAVIGATION STRUCTURE (LOCKED)

```
LOGO | EXPLORE ▾ | BUILD ▾ | DATA ▾ | PRICING | 🔍 Search | My Projects | Get Started →
```

Logo links to index.html. Search links to property_search.html. My Projects links to project_planner.html. Get Started links to am_i_eligible.html.

**EXPLORE** — "How does this work?"
Three columns: Learn, Discover, User Types.

Learn: What is a DADU (what_is_dadu.html), History (dadu_history.html), Requirements (dadu_building_requirements.html), Zoning Standards (dadu_zoning_standards.html), Code and Legislation (dadu_code_legislation_v3.html), Permit Process (permit_process_timeline.html).

Discover: Eligibility Map (dadu_eligibility_map.html), Property Search (property_search.html), DADUs Near Me (dadu_near_me_v2.html), Opportunity Explorer (dadu_opportunity_explorer_v2.html).

User Types: Homeowner (user-homeowners.html), Contractor (contractor_marketplace.html), Designer/Architect (designer_resources.html), Municipal (municipal_dashboard.html), Legal (legal_resources.html).

**BUILD** — "What do I do next?"
Five columns: Plan, Design, Calculate, Hire, File.

Plan: Project Planner (project_planner.html), Checklist (project_checklist.html), Draw DADU (draw_dadu_on_parcel.html).

Design: Site Plans (site_plan_downloads.html).

Calculate: Cost Estimator (project_cost_estimator.html), ROI Calculator (roi_calculator.html), Size Calculator (size_calculator.html), Tax Calculator (property_tax_calculator.html).

Hire: Contractor Marketplace (contractor_marketplace.html).

File: Forms Wizard Step 1 (determine_forms_required.html), Forms Wizard Step 2 (legal_form_filler.html), Owner Occupancy (owner_occupancy.html), STR Permit (short_term_rental_permit.html).

**DATA** — "Show me the proof."
Three columns: Activity, Reports, Records.

Activity: Permit Dashboard (permit_activity_dashboard.html), Contractor Dashboard (contractor_dashboard.html), Market Trends (market_trends.html).

Reports: Eligibility Report (eligibility_report.html), Project Report (project_report.html), All Reports (dadu_reports_store.html), plus sample report links labeled clearly as "Sample."

Records: Permit Explorer (nashville_permit_explorer_v3.html), Site Plans (site_plan_downloads.html), Recorded Documents (dadu_documents_portal.html), Restrictive Covenants (restrictive_covenants_v2.html), Zoning Documents (overlay-districts.html), PDF Database (pdf_database_lookup.html).

**PRICING** — Direct link to homebody_pricing.html. No dropdown.

---

## PART 4: BRAND SYSTEM (LOCKED — DO NOT CHANGE)

**Colors:**
- Deep Slate #3A5566 — primary, headings, nav
- Warm Stone #7B746D — secondary UI, subtitles
- Ochre #C58B2A — accent, use sparingly
- Background #F2F0ED — page background
- Card background #f5f5f0
- Oxide Red #7A2A1D — restrictions/legal warnings only in UI
- Status green #2E6F4E — eligibility states only in UI

**NO teal. NO green accents.** The CSS variable names say "teal" and "terracotta" for backward compatibility. The actual colors are Warm Stone and Ochre.

**Old colors that must be replaced everywhere:**
- #2c3e50 → #3A5566
- #6b8fa3 → #7B746D
- #6b8e4e → #3A5566
- #c9a86c → #7B746D
- #e8e4df → #F2F0ED
- #B55A3C → #C58B2A

**Typography:** Inter (primary), Montserrat (fallback), system sans-serif. Headlines 700-800 weight. Body 400-500.

**Logo:** assets/castlehold-logo.png (two castles in tan and slate blue with "CASTLEHOLD" text). Subtitle: "DADU Zoning & Buildability Intelligence" in Warm Stone.

---

## PART 5: WHAT EXISTS RIGHT NOW

### Shared Components
- homebody_shared.css — Global stylesheet with Castlehold CSS variables and mega-menu CSS
- homebody_header.js — Shared nav component injected via `<div id="site-header"></div>`
- homebody_header.html — Header template

### 95+ HTML Pages on GitHub Pages
Organized into: Maps and Explorers (20), Calculators and Planning (8), Reports and Pricing (5), Legal and Forms (5), Dashboards (4), Learn and Reference (14), User Type Pages (3), Feature Landing Pages (3), Contractor and Advertising (3), Other (7), plus 10+ older/duplicate versions.

### Data Assets Available
- DADU_All_Permits_Cleaned.csv: 6,822 permits (355 DADU, 628 accessory), 6,427 with contractor names
- DADU_Eligibility_ENHANCED: 161,703 parcels on Vanderbilt ArcGIS
- DADU_All_Permits_Final: 4,700+ permits on Vanderbilt ArcGIS
- DADU_Building_Specs: max DADU size and setbacks per parcel on Vanderbilt ArcGIS
- Parcels_with_Restrictive_Covenants: 43,710 parcels on Vanderbilt ArcGIS
- Secondary_SFH_Merged: existing secondary structures on Vanderbilt ArcGIS
- Building_Footprints_SingleFamily on Vanderbilt ArcGIS
- Covenant_Links: actual covenant document URLs on Vanderbilt ArcGIS
- PropertyShark_2Unit_SFR_Clean.csv: 2,011 confirmed 2-unit properties
- assessor_accounts_20260114.csv: 277,619 records mapping APN to ACCOUNTNUMBER (column USER_ACCOUNT = APN)
- tn_davidson.csv: 284,000 parcels with APN, address, zoning, lot size
- Parcels_with_links.csv: APN, ACCOUNTNUMBER, all URL templates pre-built
- Ownership_Parcels_20260118.csv: Ownership data
- singlefamily_permit_history_copy.csv: Official county SF permit records
- Davidson_Permit_History/ (32 CSV files): ~962,118 full permit records for all of Davidson County

### Permit Data Sources
- Davidson_Permit_History (3rd party full DB): ~962,118 records in 32 CSVs at 000_IMPORTANT/
- ADU_Permits_Points_20260117.geojson (county): 891 records with APN, Permit Number, Covenant Number, Covenant URL, Purpose, Date Issued
- NEW_ADU_Permits_20260114.geojson (3rd party): 4,117 records with APN, PERMIT_NUMBER, PROJECT_SCOPE, DESCRIPTION, NEW_ADU flag

### Data Relationships
APN is the primary key linking all datasets. APN maps to ACCOUNTNUMBER via assessor_accounts_20260114.csv for property card URLs. Instrument Number (YYYYMMDD-XXXXXXX) links permits to covenant documents. Parcels use three IDs: ACCOUNTNUMBER, ParcelID/PARID, and APN/STANPAR.

### Covenant Data Sources
- Parcels with Covenants.xlsx (BEST): 43,710 records with full parcel info + all URL links
- MASTER_Covenants_All_20260117.csv: 1,603 unique APNs combined from DADU_Permits, Permit_Extraction, APN_Covenants, Land_Records
- 8,514 covenant PDFs filed by instrument number

### Master Analysis Files (MASTER_ADU_DATA/)
- MASTER_Parcels_5_ADU_Indicators_20260117.csv: 284,425 parcels with 5 ADU signal flags
- MASTER_Parcels_Strong_ADU_Signal_20260117.csv: 5,647 parcels with 2+ indicators
- MASTER_Parcels_Combined_20260118.geojson (1.0GB)
- DADU_Eligibility_ENHANCED_20260119.geojson (848MB)
- MASTER_Parcels_Complete_20260118.geojson (439MB)
- Address_Points_Fraction_B_20260117.geojson: 4,887 parcels with Fraction B (separate dwelling unit)

The most recent processed datasets live in /DADU/FINAL_FINAL/. Always check this folder first for latest versions.

### Downloaded Documents (Local + Google Drive)
- 8,514 restrictive covenant PDFs (in Drive: folder 1bEZN1kEZxqZLkdX0QjT0g9N7K0sXAy3Z)
- 630 permit PDFs (in Drive: folder 1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4, ~411 still need uploading)
- 3,358 property cards merged (in Drive: folder 1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ)
- 8,074 Card 2 property card images (downloaded but not yet in Drive)
- 698 aerial screenshots (in Drive: folder 1eD1TUNuYMOMK7VdVJW3Pc6mHYFS02VUj, may need uploading)
- UDO Overlay PDFs (folder 1evPTz2SvAIDS74lwzgxjGF85kl2nDsrh)
- DADU Overlay PDFs (folder 1KDQe3WhWz1H1ukTIlAfxtbDFmvX50kYu)
- STR Permits (folder 1_JGdEdlUS7IGWi4L93aSGOhHWZJfktql)
- Zoning Board Appeals (folder 1bjNIPyogxImJ5_zxnxKTmxlYCmO0clvH)

### 10 Sample Reports Already Built
In /sample_reports/: eligibility, property, contractor match, covenant analysis, permit history, comparables, cost estimate, market stats, neighbors, zoning verification.

---

## PART 6: WHAT IS BROKEN RIGHT NOW

### 1. Maps Render Blank + Building Footprints CORS Blocked
Every map page (eligibility map, property search, near me, explorers) shows a white box instead of an interactive map. The building footprints, permits, and covenants layers are NOT CONNECTED to any map. This is the most visible problem.

Building footprints were "implemented" in commit fedd90c with Symbium-style rendering (primary structures in dark gray, accessory/DADU in ochre, click popups with sqft/height/type, sidebar with structure cards). But they do NOT render on the deployed site because the code queries Nashville's MapServer at maps.nashville.gov/arcgis/rest/services/Planimetric/Buildings/MapServer/0, which blocks CORS from GitHub Pages. The fetch fails silently every time.

**The fix:** Replace Nashville MapServer URLs with Vanderbilt-hosted FeatureServer endpoints that allow CORS:
- Building_Footprints_SingleFamily: https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Building_Footprints_SingleFamily/FeatureServer/0
- Footprints_With_ParcelData: https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0

Or use local GeoJSON: dadu_footprints.geojson (4.4MB, should be in repo, indexed by APN).

Do NOT use maps.nashville.gov for any client-side fetch from GitHub Pages. It blocks CORS.

### 2. Contractor Marketplace Uses Fake Data
The live contractor_marketplace.html shows invented companies like "Nashville ADU Builders" (47 projects) and "TN Modular Homes" (32 projects). None of these exist. Real data has 355 DADU permits with real contractors.

### 3. Old Colors Persist on Many Pages
Many pages still have #2c3e50, #6b8e4e, #e8e4df, #6b8fa3 hardcoded in inline CSS instead of using the Castlehold palette via CSS variables.

### 4. Six Missing JSON Files
Pages reference JSON files that return 404: adu_permits_slim.json, PDF_Database_By_APN.json, permits_for_map.json, ordinance_index.json, gdrive_docs_index.json, udo_dadu_standards.json.

### 5. Property Report Card Links Use Wrong Fields
External links need APN, STANPAR, PIN, and ACCOUNTNUMBER mapped correctly. The assessor_accounts_20260114.csv bridges APN to ACCOUNTNUMBER but the report card page does not use it yet.

### 6. Document Portal Not Connected
dadu_documents_portal.html exists but cannot search by APN, permit number, or document type. Not connected to Google Drive folders.

### 7. Some Pages Still Say "Homebody Projects"
Branding text in page titles and headers needs to say "Castlehold" consistently.

### 8. Navigation Links May Point to Missing or Broken Pages
Not every page referenced in the mega-menu dropdown actually loads with Castlehold branding and working content.

---

## PART 7: WHAT NEEDS TO BE DONE — IN ORDER

### STEP 1: Fix Old Colors (find and replace across all HTML)
Replace every instance of old hex codes with Castlehold equivalents. Make sure every page loads homebody_shared.css and uses CSS variables. Replace "Homebody Projects" text with "Castlehold."

### STEP 2: Fix Blank Maps and Building Footprints (most visible problem)
Debug why map containers render blank. Check that Leaflet/ArcGIS JS libraries load from CDN. Verify map containers have explicit height. Priority order:
1. dadu_eligibility_map.html — connect to DADU_Eligibility_ENHANCED (161,703 parcels on Vanderbilt ArcGIS)
2. property_search.html — parcel search with map + building footprints
3. dadu_near_me_v2.html — Near Me Locator

**Building footprints (Symbium-style) — must fix CORS issue:**
The code currently queries maps.nashville.gov which blocks CORS from GitHub Pages. Replace with Vanderbilt FeatureServer or local GeoJSON. The rendering logic from commit fedd90c is correct, just the data source URL is wrong.

Footprint data sources (priority order):
1. Local GeoJSON: dadu_footprints.geojson (4.4MB in repo, indexed by APN) — most reliable
2. Vanderbilt FeatureServer: Building_Footprints_SingleFamily or Footprints_With_ParcelData (services3.arcgis.com, CORS allowed)
3. Do NOT use maps.nashville.gov (CORS blocked from GitHub Pages)

Symbium-style rendering spec:
- Parcel boundary: dashed navy (#3A5566), 3px weight, very light fill at 0.1 opacity
- Primary structures: dark gray fill (#555555, 65% opacity)
- Accessory/DADU structures: ochre fill (#C58B2A, 65% opacity)
- Click popup: building type, footprint area, height, year built, exterior, roof type, DADU permit number if applicable
- Sidebar: "Structures on Parcel" with color-coded cards (ochre border for accessory, slate for primary), total building area, available yard area (lot minus buildings), max DADU size based on lot
- Footprints render ON the parcel map (one unified view), not in a separate tab
- Fallback: if no local footprint data for an APN, query Vanderbilt ArcGIS with spatial envelope

Test by searching "1000 17th Ave S Nashville TN" — buildings should appear on the parcel.

### STEP 3: Replace Fake Contractor Data
Generate contractor_stats.json from DADU_All_Permits_Cleaned.csv (real data: Palmetto Construction 11 permits, Bootstrap Architecture 6, WTW Construction 5, etc.). Update contractor_marketplace.html to load this real data. Link each contractor's projects to Property Report Cards.

### STEP 4: Fix Property Report Card Links
Use assessor_accounts_20260114.csv to create apn_to_account.json mapping APN to ACCOUNTNUMBER. Fix link builders to use correct IDs: STANPAR for ParcelViewer, ACCOUNTNUMBER for Property Card PDF, APN for assessor and permit docs. Add building footprints display to the report card map.

### STEP 5: Create Missing JSON Files
Generate from existing data:
- adu_permits_slim.json (from DADU_All_Permits_Cleaned.csv)
- permits_for_map.json (permits with coordinates for map display)
- PDF_Database_By_APN.json (mapping APNs to available documents)
- gdrive_docs_index.json (Google Drive folder URLs for each document type)
- ordinance_index.json (overlay ordinance reference data)
- udo_dadu_standards.json (Urban Design Overlay DADU standards)

### STEP 6: Connect Document Portal
Enable dadu_documents_portal.html to search by APN, address, doc type, permit number. Link to Google Drive folders for downloads. Use the docs_index.json created in Step 5.

### STEP 7: Fix Broken Nav Links
Verify every link in the EXPLORE/BUILD/DATA mega-menu resolves to a working page with Castlehold branding. Any page that does not exist or is a stub gets flagged.

### STEP 8: Connect Map Layers
After maps render (Step 2), connect the additional data layers:
- Building footprints (Symbium-style display)
- Permit markers from DADU_All_Permits_Final
- Restrictive covenants layer
- Secondary structures layer

### STEP 9: Flesh Out Stub Pages
Many pages created by Claude Code are placeholder stubs. Priority pages needing real content:
- am_i_eligible.html — Address lookup with instant eligibility determination
- user-homeowners.html — Homeowner portal with guided workflow
- property_search.html — Map-based search like Regrid
- contractor_marketplace.html — Connected to real permit data (Step 3)

### STEP 10: Push, Verify, Clean Up
Commit all changes. Push to GitHub. Verify on live site: homepage loads, maps render, contractor data is real, report card links work, document portal searches, nav links resolve, colors are Castlehold. Create DATA_INVENTORY.md listing all JSON/GeoJSON files with usage analysis.

---

## PART 8: DATA DETAILS

### BL2025-1007 Eligibility Rules
- Zoning: R or RS zones only
- USD (Urban Services District): by-right construction
- GSD (General Services District): requires overlay district
- Lot < 10,000 SF: max 700 SF living / 750 SF footprint
- Lot ≥ 10,000 SF: max 850 SF living / 1,000 SF footprint
- Height: cannot exceed principal structure
- Owner occupancy required

### ID Cross-Reference (Critical for Link Builders)
- APN (Assessor's Parcel Number): 11-digit, primary key for most joins
- STANPAR: used by Nashville ParcelViewer links
- PIN / ParID: used by some Nashville services
- ACCOUNTNUMBER: used by PADCTN property card URLs (bridge via assessor_accounts_20260114.csv)
- ParcelID: used by ArcGIS feature layers

### ArcGIS Feature Services (Vanderbilt-Hosted)
All on services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/:

**Core Layers:**
- DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer (161,703 parcels)
- DADU_All_Permits_Final/FeatureServer (4,700+ permits)
- DADU_Building_Specs_20260119_042856/FeatureServer
- Footprints_With_ParcelData_20260118_011423/FeatureServer
- Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer (43,710)
- Building_Footprints_SingleFamily/FeatureServer
- NEW_ADU_Permits_20260114/FeatureServer (4,117)
- DADU_BL2025_1007_Eligible_20251230_011045/FeatureServer
- SFH_parcels/FeatureServer

**Secondary/Analysis Layers:**
- Secondary_SFH_Merged_SHP_20251231_0015/FeatureServer (existing DADUs merged)
- Secondary_On_SF_Parcels_SHP_20251230_2352/FeatureServer
- DADU_All_Permits/FeatureServer
- _Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer (covenant PDF links)
- _Parcels_with_CR__A1_AP43711_wk1ztG/FeatureServer (parcels with covenants, alt)
- Parcels_with_Zoning_view_A1_AD16330_eWiX6s/FeatureServer
- DADU_Complete_SHP_20251230_1348/FeatureServer
- Accessory_Footprints_RQgxIo/FeatureServer
- AssessorCards_A1_N3897_j7AP0I/FeatureServer

**Nashville Government Layers:**
- Parcels with Building Characteristics: services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/Parcels_with_Building_Characteristics_view/FeatureServer/0
- Base Zoning: maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/BaseZoning/MapServer/0
- USD/GSD Boundary: maps.nashville.gov/arcgis/rest/services/Boundaries/USD_GSD/MapServer/0
- SP_Documents_Public: services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/SP_Documents_Public/FeatureServer/0 (1,008+ specific plan documents with CaseNo, Url, PlanType, CaseBegin)
- Specific Plans: services2.arcgis.com/HdTo6HJqh92wn4D8/ArcGIS/rest/services/Specific_Plans/FeatureServer

**Nashville Metro ArcGIS Query Endpoints (CORS blocked from GitHub Pages, use for server-side/local scripts only):**
- Address Points: maps.nashville.gov/arcgis/rest/services/Addressing/AddressPoints/MapServer/0
  - DADU descriptions: where=Description like '%DADU%' OR DESCRIPTION LIKE '%ACCESSORY DWELL%' OR DESCRIPTION LIKE '%Carriage%'
  - Non-primary addresses: where=LinkTypeCode <> 'P'
- Zoning Overlay Districts: maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/Zoning_Overlay_Districts/MapServer/0
  - DADU Overlay: where=ZONE_DESC = 'Detached Accessory Dwelling Unit Overlay District'
- Zoning Overlay (ArcGIS Online mirror, CORS OK): services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Zoning_Overlay_Districts_Vw/FeatureServer/0
  - Urban Design Overlay: where=zone_desc like '%Urban Design Overlay%'
- Parcel History: maps.nashville.gov/arcgis2/rest/services/Parcels/ParcelHistory/MapServer/5
- Cadastral Parcels: maps.nashville.gov/arcgis/rest/services/Cadastral/Cadastral_Layers/MapServer/4

### ArcGIS Web Maps (Vanderbilt)
- Existing DADUs: vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=9f40d0ca10b1453198617aa9cd2f6b9f
- DADU Near Me Permit Info: vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=3e01dee4a4384062b0a0c1be98cd3839
- Restrictive Covenants: vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=168e16cf3b08411296759cf39f22dc6d
- DADU Footprints: vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=d3f149a92f1c4131b3fc711bc4809b5b
- Detached ADU Permits: vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=50bbdc9cb0c24ab4aaaadc3951cc1555
- DADU Eligibility BL2025-1007: vanderbilt.maps.arcgis.com/home/item.html?id=d6c2c06db5744bb0836cfb0227548275
- Building Specs: vanderbilt.maps.arcgis.com/home/item.html?id=d7f2cf4e38f34eddba0a671aa0db4acf
- Full Parcels Webmap: vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=85f14913270641b1a24fc0f6fbc5c353

### Nashville ePermits API
- Base: https://epermits.nashville.gov/api
- caseSubTypeID 774 = DADU permits
- CaseQuantityGroupDetail with detailCode 'PROJSCOPE' = project scope text (sqft, setbacks, covenant recording numbers)
- CaseQuantityGroupDetail with detailCode 'RESCONVAL' = construction value

### External Link URL Templates
```
ParcelViewer:       https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}
Print Record:       https://maps.nashville.gov/ParcelViewer/PrintRecord.html?pin={PIN}
Permit Docs:        https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}
Parcel Docs:        https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={APN}
ePermits:           https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}
ePermits by PID:    https://epermits.nashville.gov/?#/permit/{PID}
ePermits by APN:    https://epermits.nashville.gov/#/search?searchCode=APN&searchText={APN}
Assessor:           https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}
Property Card:      https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
Card Building:      https://portal.padctn.org/OFS/WP/Building/{ACCOUNTNUMBER}/2
Card Summary:       https://portal.padctn.org/OFS/WP/Summary/{ACCOUNTNUMBER}/2
Street View:        https://www.google.com/maps?q&layer=c&cbll={LATITUDE},{LONGITUDE}
Aerial (Patriot):   https://portal.patriotproperties.com/?APIKEY=5D050659143EB96630FB38B91DE12E40&SECRETKEY=A92169630C9BC3C00A1C0F9F140E6DAEC21C8E62DCFF9FC443FB1BE70DDF6AA4268527B9DDE2ECC2C7EE9BB5BF728C06F0DF4019BBECDEBD2A6DD0BBE28A419D8F929E1F3E8DF478E56619995BEFCA8E369276689D791197DC1284F14B3252DBFB2A19A2E451EEA832D6D96488DDC673EBA4B37BD741223B656A793D93209C0F&LAT={LATITUDE}&LONG={LONGITUDE}
Covenant Docs:      https://davidsonportal.com/landrecords/view_image.php?key=/img/tn/davidson/{YYYY}/{MMDD}/{INSTRUMENT}.tif
SP Plan Docs:       https://maps.nashville.gov/sp/{YYYY}/{CASENO}/SP_{CASENO}.pdf
Legislation:        https://documents.nashville.gov/Request/Form/Legislation?legislationnumber={BL_NUMBER}
```

### Google Drive Document Folders
```
Root:               https://drive.google.com/drive/folders/13w8X1Z8uQ8RFAOUjAlY0jnnjFnRnvfLP
Second folder:      https://drive.google.com/drive/folders/1DVFcM-2aMtbGyhMQ7pP1H8L2SSYMJfwE
Permit PDFs:        https://drive.google.com/drive/folders/1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4
Covenants:          https://drive.google.com/drive/folders/1bEZN1kEZxqZLkdX0QjT0g9N7K0sXAy3Z
Property Cards:     https://drive.google.com/drive/folders/1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ
Aerials:            https://drive.google.com/drive/folders/1eD1TUNuYMOMK7VdVJW3Pc6mHYFS02VUj
UDO Overlay PDFs:   https://drive.google.com/drive/folders/1evPTz2SvAIDS74lwzgxjGF85kl2nDsrh
DADU Overlay PDFs:  https://drive.google.com/drive/folders/1KDQe3WhWz1H1ukTIlAfxtbDFmvX50kYu
STR Permits:        https://drive.google.com/drive/folders/1_JGdEdlUS7IGWi4L93aSGOhHWZJfktql
Zoning Appeals:     https://drive.google.com/drive/folders/1bjNIPyogxImJ5_zxnxKTmxlYCmO0clvH
```

### GeoJSON and JSON Files Referenced by HTML Pages

These files must exist in the GitHub repo root or /data/ for the site to function. Pages that try to load a missing file will fail silently.

```
eligibility_parcels.geojson          — parcel_footprint_map.html
footprints_map.geojson               — parcel_footprint_map.html
DADU_Permits_All.geojson             — parcel_footprint_map.html, explorers
dadu_explorer_data.geojson           — dadu_explorer_attom.html
dadu_footprints.geojson (4.4MB)      — footprint display pages
NEW_ADU_Permits_20260114.geojson     — permit explorer, near me
web_lite_parcels_points_20260123.geojson (56MB) — web map display
web_lite_parcels_polygons_20260123.geojson (56MB) — web map display
parcels_eligibility_lite.json        — multiple explorer pages
parcels_scored_v2.json               — opportunity explorer
parcels_eligibility_map.json         — eligibility map
permits_with_apn.json                — permit explorer
permits_for_map.json                 — permit map
permit_analytics.json                — analytics dashboard
PDF_Database_By_APN.json             — document portal
pdf_database_light.json              — document portal (lightweight)
contractors_ranked.json              — contractor dashboard
contractors_stats.json               — contractor leaderboard
contractor_data_enhanced.json        — contractor marketplace
zipcode_pricing_data.json            — cost estimator
adu_permits_slim.json                — permit display (TO CREATE)
gdrive_docs_index.json               — document portal (TO CREATE)
ordinance_index.json                 — overlay reference (TO CREATE)
udo_dadu_standards.json              — UDO standards (TO CREATE)
```

### Local PDF Library Folders (Must Match to APNs)

| Folder | Content | Filename Pattern |
|--------|---------|-----------------|
| Permit_PDFs_Downloaded/ | 630 permit site plan PDFs | UUID_CA-Permits-{DATE}_{ID}_1.pdf |
| Property_Cards_Downloaded/ | 3,358 assessor cards | PropertyCard_{APN}_{ACCOUNTNUMBER}.pdf |
| Property_Cards_2_Assessor/ | Card 2 (secondary structures) | PropertyCard_{APN}_{ACCOUNTNUMBER}.pdf |
| Restrictive_Covenants/ | 8,514 covenant PDFs | {INSTRUMENT_NUMBER}.pdf (e.g., 20240710-0051719.pdf) |

### Key Statistics
- Total Nashville parcels: 285,512
- BL2025-1007 eligible (USD): 67,707
- Total eligible (USD + GSD with overlay): ~159,840
- Historic DADU permits: 827
- Third-party permits: 1,800+
- Unique contractors: 2,072
- Legal citations: 111
- Parcels with covenants: 43,000+
- Strong ADU signal parcels (2+ indicators): 5,647
- ADU detection accuracy: 98.9%

---

## PART 9: RULES FOR ANY AI ASSISTANT

1. Audit first. Before making any changes, check what exists.
2. Never invent data sources, endpoints, URLs, or field names. Verify them.
3. Never delete, rename, or move existing files. Create new versions if needed.
4. Never overwrite output files. Every new output gets a unique name.
5. Do not modify anything in /samples/. Read-only design reference.
6. No sensitive keys in the repo.
7. Complete code only. No partial snippets.
8. ArcGIS queries must handle pagination (maxRecordCount loops with resultOffset/resultRecordCount).
9. Nashville servers need 1-2 second delays and 30-second timeouts. They hang without warning.
10. Python scripts in copy-paste terminal format: python3 << 'EOF' ... EOF
11. All pages must load homebody_shared.css and use CSS variables, not hardcoded colors.
12. All pages must use the shared header via homebody_header.js.
13. CORS rule: maps.nashville.gov blocks CORS from GitHub Pages. All client-side ArcGIS queries must use services3.arcgis.com (Vanderbilt-hosted) or local GeoJSON. Never use maps.nashville.gov for client-side fetch.
14. Do not rely on contractor columns that are empty. Only use fields that actually contain data (CONTRACTOR_BIZ_NAME_ORIGINAL, CONTRACTOR_LICENSE have data; other contractor fields show 0 records).
15. Keyboard accessible dropdown menus (focus states, Escape key closes). No hover-only interactions for critical actions. Mobile responsive.
16. Do not load huge GeoJSON at initial page load. Load on demand. Cache repeated lookups in session storage when reasonable.
17. Writing style: active voice, no em dashes, no hedging words, paragraph format unless lists are requested.

---

## PART 10: REFERENCE LINKS

### Project Links
- Live site: https://nataliebaldacci.github.io/DADU-Homebody-Projects/
- ArcGIS style reference: https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=85f14913270641b1a24fc0f6fbc5c353
- Nashville Zoning Code (DADU): https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.08ZODILAUS_17.08.030DILAUSTA
- Miami-Dade Comparable Sales (UI reference): https://apps.miamidadepa.gov/ComparableSales/#/?folio=0131250340450

### Competitor and Inspiration Sites
- Symbium: https://build.symbium.com/ | Pricing: https://symbium.com/pricing/ | FAQs: https://symbium.com/faqs
- ParcelQuest: https://www.parcelquest.com/features/ | Industries: https://www.parcelquest.com/industries/ | Pricing: https://www.parcelquest.com/pricing/ | Recorded Docs: https://www.parcelquest.com/features/recorded-documents/ | PQ Lite: https://assr.parcelquest.com/Home/WhatIsPQLite
- First American Reports: https://dna.firstam.com/solutions/property-data/property-reports | Store Pricing: https://dnastore.firstam.com/pricing/
- ATTOM Navigator: https://propertynavigator.attomdata.com/Mainpage.aspx?state=TN | Building Permits: https://www.attomdata.com/data/property-data/nationwide-building-permit-data/ | Pricing: https://www.attomdata.com/solutions/property-navigator/pricing/
- PropStream: https://www.propstream.com/propstream-features | ADU Calculator: https://www.propstream.com/news/adu-calculator | Pricing: https://www.propstream.com/pricing
- Regrid: https://app.regrid.com/us/tn/davidson | Plans: https://app.regrid.com/plans
- PropertyShark: https://www.propertyshark.com/mason/tn/Davidson-County/Property-Search | Subscriptions: https://www.propertyshark.com/mason/Subscriptions2/
- HouseCanary Pricing: https://www.housecanary.com/pricing
- US Title Records: https://www.ustitlerecords.com/search-property-records/
- Houzz Pro: https://www.houzz.com/houzz-pro/ | Pricing: https://www.houzz.com/houzz-pro/pricing
- Shovels AI: https://www.shovels.ai/software
- CRE Daily Data Source Review: https://www.credaily.com/reviews/best-commercial-real-estate-data-sources/
