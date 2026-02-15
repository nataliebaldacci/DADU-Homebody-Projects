# HOMEBODY BUILDER / CASTLEHOLD DADU PLATFORM: COMPREHENSIVE PROJECT BRIEFING

**For:** New AI development assistant with zero prior context
**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Date:** February 13, 2026
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/
**Repo:** GitHub Pages static site (repo name: DADU-Homebody-Projects)

---

## 1. WORKING CONTEXT

I'm working in `/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects` and the repo is at https://github.com/nataliebaldacci/DADU-Homebody-Projects. The live site is at https://nataliebaldacci.github.io/DADU-Homebody-Projects/. I am working on fixing my links and finishing my website.

I am a Vanderbilt Law School J.D. candidate (Class of 2026) with dual master's degrees in Real Estate Development and Urban Planning from Columbia. This platform doubles as coursework for Professor Lehrman's "Networks, Law, and Entrepreneurial Strategy" class, demonstrating how building permit infrastructure creates network effects scalable across U.S. municipalities. I start at Paul Hastings' Real Estate team in NYC Fall 2026.

---

## 2. WHAT THE PLATFORM IS

**Homebody Builder** is the consumer-facing product name for a DADU (Detached Accessory Dwelling Unit) planning and eligibility platform for Nashville-Davidson County. It aggregates fragmented public data (parcel records, building permits, restrictive covenants, zoning codes, building footprints, assessor records) into a single web application that homeowners, contractors, designers, investors, and municipal staff can use to understand what can be built, where, by whom, and at what cost.

**Brand architecture (these are two distinct layers, never collapsed into one):**
- **Homebody Builder** = the consumer-facing product. This is what homeowners and contractors see. Tagline: "Nashville DADU planning made clear." This name appears on the homepage, tool pages, and user-facing content.
- **Castlehold** = the authority/data layer underneath. Tagline: "DADU Zoning & Buildability Intelligence." This name appears on reports, data attribution, legal/municipal pages, the About page, and the footer. Think of it like how "Powered by Castlehold" appears on Homebody Builder products.

**How this shows up in practice:**
- Homepage: "Homebody Builder / Nashville's DADU Planning & Eligibility Tool / Powered by Castlehold"
- Reports and data pages: "Parcel data, zoning analysis, and eligibility determinations provided by Castlehold"
- Legal/municipal pages: "Castlehold / Real Estate Zoning & Eligibility Infrastructure"

The platform name in the GitHub repo is "DADU-Homebody-Projects" and some page titles still say "Homebody Projects" (the older name before the brand was finalized). The current homepage says "Homebody Projects" in the footer, which should become "Homebody Builder" or "Castlehold" depending on context.

---

## 3. THE LEGISLATION DRIVING THE PLATFORM

Nashville's **BL2025-1007** (effective December 12, 2025) expanded DADU eligibility to **67,707 parcels** in the Urban Services District. Key rules:

| Criterion | Requirement |
|-----------|-------------|
| Zoning | R or RS zones only |
| Urban Services District (USD) | By-right construction (no special approval needed) |
| General Services District (GSD) | Requires overlay district approval |
| Lot under 10,000 SF | Max 700 SF living area / 750 SF footprint |
| Lot 10,000 SF or more | Max 850 SF living area / 1,000 SF footprint |
| Height | Cannot exceed principal structure |
| Owner occupancy | Required (owner must live in principal dwelling or the DADU) |

---

## 4. KEY STATISTICS

| Metric | Value |
|--------|-------|
| Total Nashville parcels in dataset | 285,512 |
| BL2025-1007 eligible parcels (USD) | 67,707 |
| Historic Metro DADU permits | 827 |
| Total permits in cleaned dataset | 4,700+ (up to 6,822 in some versions) |
| Third-party permit records | 1,800+ |
| Unique contractors in permit data | 393 |
| Legal citations in code database | 111 |
| Parcels with restrictive covenants | 43,000+ |
| Building footprints with height data | 327,000+ |
| PropertyShark confirmed 2-unit properties | 6,800+ |
| ADU detection accuracy (multi-indicator) | 98.9% |

---

## 5. TECHNICAL ARCHITECTURE

### Hosting
- **Static website** on GitHub Pages (client-side JavaScript only, no server)
- **ArcGIS Online** feature layers hosted under vanderbilt.maps.arcgis.com and services3.arcgis.com
- **ArcGIS Experience Builder** for some embedded interactive maps (iframe)
- **Local data processing** in Python on my Mac using ~/dadu_env virtual environment

### Core Datasets

| Dataset | Records | Key Fields |
|---------|---------|------------|
| tn_davidson.csv | 284,000 | APN, address, zoning, lot size |
| Building_Footprints.geojson | 327,000+ | Height, sqft, building type |
| Parcels_with_Building_Characteristics (ArcGIS) | 285,512 | Structures, YearBuilt, footprints |
| Parcels with Covenants.xlsx | 43,000+ | Covenant URLs, recording info |
| DADU_All_Permits_Cleaned.csv | 4,700-6,822 | Permit number, contractor, cost, date |
| historic_dadu_permits_actual.csv | 827 | Metro permits 2017-2025 |
| PropertyShark_2Unit_SFR_Clean.csv | 6,800+ | Confirmed 2-unit properties |
| assessor_accounts_20260114.csv | Maps APN to ACCOUNTNUMBER | Cross-reference for property card URLs |

### ArcGIS Feature Services (CORS-friendly, use these NOT maps.nashville.gov)

| Layer | URL |
|-------|-----|
| DADU_Eligibility_ENHANCED | services3.arcgis.com/58WV6GqBWodG9Kll/... (161,703 parcels) |
| DADU_All_Permits_Final | services3.arcgis.com/58WV6GqBWodG9Kll/... (4,700+ permits) |
| Building Footprints | services3.arcgis.com/58WV6GqBWodG9Kll/... (327K+ features) |
| Parcels_with_Restrictive_Covenants | services3.arcgis.com/58WV6GqBWodG9Kll/... (43,710 parcels) |
| Covenant Links (with PDF URLs) | services3.arcgis.com/58WV6GqBWodG9Kll/... |

**Important:** Nashville's own ArcGIS servers (maps.nashville.gov) block CORS from GitHub Pages. Always use the Vanderbilt-hosted mirrors on services3.arcgis.com. Always paginate ArcGIS queries (services have maxRecordCount limits of 100-2000).

### External Link Templates (for Property Report Cards)

```
Parcel Viewer:      https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}
Print Record:       https://maps.nashville.gov/ParcelViewer/PrintRecord.html?pin={PIN}
Permit Docs:        https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}
Permit by Parcel:   https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={APN}
ePermits:           https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}
Assessor:           https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}
Property Cards:     https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
```

### Local PDF Libraries (thousands of downloaded documents)

| Folder | Contents |
|--------|----------|
| Permit_PDFs_Downloaded/ | Site plans, permit documents |
| Property_Cards_2_Assessor/ | Assessor property cards |
| Property_Cards_Downloaded/ | Additional property cards |
| Restrictive_Covenants/ | Covenant PDFs from Register of Deeds |

### ADU Detection: Five Combined Indicators

| Indicator | Records | Description |
|-----------|---------|-------------|
| regrid_2plus_bldgs | 67,000 | Properties with 2+ buildings per Regrid |
| county_permit | 827 | Metro Nashville DADU permits |
| 3rdparty_permit | 1,800 | RE Data/RealtyTrac permit records |
| fraction_B | 10,000 | "Fraction B" secondary address pattern |
| covenant | 1,100 | Restrictive covenant filings |

Combined, these five indicators achieve 98.9% detection accuracy against PropertyShark's confirmed 2-unit properties.

---

## 6. BRANDING (LOCKED, DO NOT CHANGE)

### Color Palette

**Primary:**
| Name | Hex | Role |
|------|-----|------|
| Deep Slate | #3A5566 | Nav background, hero overlay, dark backgrounds, primary headings |
| Medium Slate | #496778 | Hover states, secondary elements, step number circles |
| Lighter Slate | #4A6B7D | Tertiary elements |

**Secondary:**
| Name | Hex | Role |
|------|-----|------|
| Warm Stone | #7B746D | Secondary text, outline pill borders |
| Lighter Stone | #918A83 | Borders |

**Accent:**
| Name | Hex | Role |
|------|-----|------|
| Wheat | #CBB279 | CTA buttons, stat numbers, announcement bar, highlights |
| Ochre | #C58B2A | Small accent moments (use sparingly) |

**Neutrals:**
| Name | Hex | Role |
|------|-----|------|
| Cream | #E1D4BB | Body text on dark backgrounds, card light surfaces |
| Linen | #F0EBE1 | Section backgrounds, stats bar background |
| Light Gray | #E2E2E0 | Card borders, dividers |
| Dark Warm Gray | #706F6C | Small labels, captions |
| Warm Light | #F2F0ED | Page background |
| Off-White | #f5f5f0 | Card surfaces |

**Functional (UI status only, NOT for nav or branding):**
| Name | Hex | Role |
|------|-----|------|
| Green | #2E6F4E | Eligibility badges only |
| Amber | #D4A017 | Conditional status only |
| Oxide Red | #7A2A1D | Restrictions/warnings only |

**BANNED COLOR: #003039.** Do NOT use this anywhere. It reads as green on screen and is not part of the palette. Find and replace every instance of #003039 with #3A5566 across the entire repo. This color was mistakenly introduced by a previous AI session and keeps reappearing.

**DO NOT USE:** #003039, terracotta, sage, teal, or any color not listed above.

**Font:** Inter (primary), system sans-serif fallback. Headlines use Source Serif 4 (or Georgia fallback), weight 700, italic.

**Logo:** Use assets/icons/ADU.png (the house icon), NOT the old castle SVG. Brand text "Homebody Projects" next to the logo in white, Inter weight 700.

### Old Colors Still Present in Some Pages (Need Replacing)

| Old | Replace With |
|-----|-------------|
| #003039 | #3A5566 (Deep Slate) — BANNED, replace everywhere |
| #2c3e50 | #3A5566 (Deep Slate) |
| #34495e | #4A6B7D (Lighter Slate) |
| #1a252f | #2E4553 or #3A5566 |
| #6b8fa3 | #7B746D (Warm Stone) |
| #6b8e4e | #3A5566 (Deep Slate) |
| #c9a86c | #CBB279 (Wheat) |
| #e8e4df | #F2F0ED (Warm Light) |
| #B55A3C | #C58B2A (Ochre) |

**IMPORTANT NOTE FOR NEW AI ASSISTANTS:** Multiple older instruction files in this project reference #003039 as "Midnight" and list it as the primary color. Those instructions are WRONG and OUTDATED. The correct primary dark is #3A5566 Deep Slate. If you see #003039 in any instruction file, CSS variable, or HTML file, replace it with #3A5566. Do not trust any document that lists #003039 as part of the palette.

---

## 7. NAVIGATION STRUCTURE (LOCKED)

### Top Bar Layout

```
HOMEBODY PROJECTS LOGO (ADU.png) | EXPLORE ▾ | BUILD ▾ | DATA ▾ | PRICING | 🔍 | My Projects | Get Started →
```

Nav bar: background #3A5566 (Deep Slate), height 64px, Inter font.
Nav links: color #E1D4BB (Cream), weight 600, 14px. Hover: color white, background #496778.
Get Started button: background #CBB279 (Wheat), color #3A5566, weight 700, rounded 8px. Hover: #D4A54E.

### EXPLORE Dropdown (3 columns)

**Learn:** What is a DADU?, DADU History, Building Requirements, Zoning Standards, Code & Legislation, Permit Process Timeline

**Discover:** Eligibility Map, Property Search, DADUs Near Me, Opportunity Explorer

**User Types:** Homeowner, Contractor, Designer/Architect, Municipal/Agency, Legal/Appraiser

### BUILD Dropdown (5 sections)

**Plan:** Project Planner, Interactive Checklist, Draw DADU on Parcel
**Design:** Site Plan Finder, Downloads
**Calculate:** Cost Estimator, ROI Calculator, Size Calculator, Property Tax Calculator
**Hire:** Contractor Marketplace
**File:** Forms Wizard, Owner Occupancy, STR Permit

### DATA Dropdown (3 sections)

**Activity:** Permit Dashboard, Contractor Dashboard, Market Trends
**Reports:** Eligibility, Property Intelligence, Project, Contractor, Market Analysis, Area Analysis
**Records:** Permit Explorer, Site Plans, Property Card, Recorded Docs, Covenants, Zoning Docs

### PRICING = Direct link, no dropdown

### Key Routes
- Search icon → property_search.html
- My Projects → project_planner.html (placeholder)
- Get Started → am_i_eligible.html

---

## 8. CURRENT STATE OF THE SITE

### What Exists and Works
The site is live at https://nataliebaldacci.github.io/DADU-Homebody-Projects/ with approximately **95-99 HTML pages**. Shared components include:
- `homebody_shared.css` (global stylesheet with CSS variables for the locked palette)
- `homebody_header.js` (shared nav component injected via `<div id="site-header"></div>`)
- `homebody_header.html` (shared header template)

### Page Inventory (approximate)

**Homepage:** index.html (Homebody Projects branded, hero with aerial Nashville photo, search bar, stats, tool cards, footer)

**Maps & Explorers (~20 files):** dadu_eligibility_map.html, parcel_footprint_map.html, property_search.html, dadu_explorer (v1-v3), dadu_near_me (v1-v2 + locator), dadu_property_viewer_v3.html, dadu_property_explorer (v1-v3), dadu_opportunity_explorer_v2.html, adu_opportunity_explorer.html, nashville_permit_explorer_v3.html, adu_permit_map.html, secondary_structures_map.html

**Calculators & Planning (~8 files):** roi_calculator.html, project_cost_estimator.html, property_tax_calculator.html, size_calculator.html, project_checklist.html, project_planner.html, draw_dadu_on_parcel.html, site_plan_downloads.html

**Reports & Pricing (~5 files):** eligibility_report.html, project_report.html, dadu_reports_store.html, reports_pricing.html, homebody_pricing.html

**Legal & Forms (~5 files):** determine_forms_required.html, legal_form_filler.html, restrictive_covenants_v2.html, dadu_documents_portal.html, pdf_database_lookup.html

**Dashboards (~4 files):** contractor_dashboard.html, permit_activity_dashboard.html, nashville_permit_analytics.html, contractor_marketplace.html

**Learn & Reference (~14 files):** what_is_dadu.html, dadu_building_requirements.html, dadu_design_standards.html, dadu_zoning_standards.html, permit_process_timeline.html, dadu_history.html, owner_occupancy.html, short_term_rental_permit.html, str_permit.html, trade_permits.html, overlay-districts.html, dadu_code_legislation_v3.html, dadu_legal_citations.html, dadu_legislation.html

**User/Feature Pages (~6 files):** user-homeowners.html, user-types.html, features.html, feature-documents.html, feature-eligibility-map.html, feature-property-search.html

**Contractor (~3 files):** contractor_advertising.html, dadu_contractors_infographic.html, designer_resources.html

**Other (~7 files):** about_platform_infographic.html, dadu_resources.html, legal_resources.html, market_trends.html, municipal_dashboard.html, homebody_dadu_pricing.html, property_report.html

**10+ older/duplicate versions** exist but should not be linked in navigation or deleted.

---

## 9. ACTIVE CLEANUP WORK IN PROGRESS

Before building new features, I am actively cleaning up the codebase and datasets. A new AI assistant should know this context so it does not re-introduce problems or work on files that are being deprecated.

### Duplicate Page Cleanup
The repo accumulated ~99 HTML files over many development sessions, with significant duplication. Many pages have "_1" suffix duplicates (created by git merge conflicts or accidental copies), and multiple version chains exist (v1, v2, v3) where only the latest version should be linked in navigation. I have identified approximately 17 "_1" duplicate files safe to delete and am working through version pairs (e.g., dadu_property_portal_v2.html vs v3, nashville_permit_explorer_v2 vs v3) to pick canonical pages and archive the rest.

**Rules for the new assistant:**
- Do not link to any "_1" suffix files in navigation.
- Do not delete old versions, but do not link to them either. Only link to the canonical (latest) version of each page.
- If you create a new version of a page, use the next version number suffix (e.g., if v3 exists, create v4).
- The goal is roughly 40-50 canonical pages in the nav, not 99.

### Dataset Cleanup and Fixes
Several datasets need repair or consolidation:
- The permits dataset exists in multiple versions (DADU_All_Permits_Cleaned.csv at 4,700+ records, a 6,822-record version, historic_dadu_permits_actual.csv at 827 records, and a master permits file with 31,876 records including non-DADU permits). These need clear delineation so the platform knows which file to use for which purpose.
- Contractor data fields are inconsistent. CONTRACTOR_BIZ_NAME_ORIGINAL and CONTRACTOR_LICENSE have data, but other contractor fields are empty. Do not build features that depend on empty columns without verifying data exists first.
- The ArcGIS feature layers and the local CSV files sometimes have different record counts for the same data. The ArcGIS layers are the canonical source for the live site; the CSVs are for local analysis.
- Building footprint data and parcel data use different parcel ID formats (APN, STANPAR, ParcelID, ParID) that must be joined carefully with normalization (zero-padding, format matching).

### Git/Merge Conflict Recovery
The repo went through a period where Claude Code attempted to update 100+ files simultaneously, which caused merge conflicts and broken pushes. Some pages may still contain merge conflict markers (<<<<<<, ======, >>>>>>) in their HTML. The current state is mostly recovered, but any page that looks broken should be checked for conflict artifacts before debugging the actual code.

## 10. WHAT NEEDS TO BE FINISHED (PRIORITY ORDER)

### PRIORITY 1: Branding Consistency
Many pages still use old hex colors (#2c3e50, #6b8e4e, #e8e4df, and the banned #003039) in inline CSS. Every page needs to load homebody_shared.css and use CSS variables. User-facing page titles should say "Homebody Projects" or "Homebody Builder." The Castlehold name appears only on reports, data attribution, legal pages, and the footer "Powered by" line. The shared header must appear consistently on every page with the ADU.png house icon (not the castle logo).

### PRIORITY 2: Fix Broken Maps
Multiple map pages render as blank white boxes on the live site. Common causes include Leaflet/ArcGIS JS libraries not loading, map containers missing explicit height, or initialization errors. The eligibility map (dadu_eligibility_map.html) is the highest priority. Building footprints, permit markers, and covenant layers are NOT yet connected to most map pages.

### PRIORITY 3: Property Report Card (Core Product Spine)
This is the central product page. Every other page funnels here. A user enters an address or APN and the page generates a report covering: eligibility status, zoning constraints, lot size limits, DADU size maximums, existing permits, covenant flags, available documents, and verified outbound links to Nashville government portals (ParcelViewer, ePermits, assessor, property cards). The page exists (property-report-card.html) but the external links need correct field mapping and the document wiring is incomplete.

### PRIORITY 4: Permit Explorer
Display all DADU permits on a Leaflet map with color-coded markers by status. Each permit card should show address, permit number, date, contractor, cost, and link to permit documents. Filter by status, date range, contractor, and cost range. Data source: DADU_All_Permits_Final ArcGIS FeatureServer.

### PRIORITY 5: Document Wiring
Individual permit PDFs, property card images, site plan PDFs, and covenant PDFs need to be linked to specific parcels and permits. A docs_index.json file maps documents to APNs. The document portal (dadu_documents_portal.html) needs working search and filter against this index.

### PRIORITY 6: Contractor Marketplace
Real contractor data from permits aggregated into profiles showing permit count, average cost per square foot, project locations, and contact info. Ranked by activity. Links back to Property Report Cards for each project.

### PRIORITY 7: Pricing and Payments
Tiered report pricing: Free (Near Me locator), $4.99 (Detail Report), $9.99 (Contractor Report), $14.99 (Area Analysis). Stripe integration is planned but not yet implemented. Placeholder pricing pages exist.

---

## 11. PRODUCT FEATURES BY USER TYPE

**Homeowners:** Eligibility check, size calculator, cost estimator, DADUs near me, property viewer, covenant check, contractor matching, ROI calculator.

**Contractors/Builders:** Permit explorer, market analytics, top contractors leaderboard, project leads, pricing benchmarks, territory analysis, contractor profile pages.

**Designers/Architects:** Building requirements database, precedent gallery, site analysis tools, setback calculators, height limit tools.

**Investors/Developers:** Parcel data exports, permit history by area, opportunity maps (eligible parcels without existing ADUs).

**Municipal/Government:** Permit tracking dashboard, pre/post BL2025-1007 impact analysis, compliance monitoring.

**Legal/Appraisal:** Recorded documents portal, covenant checks, comparables (placeholder), valuation outputs.

---

## 12. PRICING TIERS

| Tier | Price | Includes |
|------|-------|----------|
| Free | $0 | Near Me locator, basic permit info, contractor names, cost ranges, external links |
| Detail Report | $4.99 | Full permit details, exact cost, square footage, cost/SF, permit PDFs, property card, aerial + street view |
| Contractor Report | $9.99 | All DADUs by contractor, average cost/SF, project locations, contact info |
| Area Analysis | $14.99 | All DADUs in neighborhood/zip, cost trends, most active contractors, approval timeline stats |

Competitive benchmarks: ParcelQuest charges $7.95-$19.95 per report, PropStream charges $99/month.

---

## 13. BUSINESS MODEL INSPIRATIONS

| Company | What We Adapt |
|---------|---------------|
| ParcelQuest (California) | Navigation structure, feature pages, user type segmentation, pricing tiers, recorded documents portal |
| Symbium (California) | Parcel-centric eligibility workflow, property-specific next-step guidance |
| First American Property Data | Report library layout, sample previews, property report card organization |
| PropStream | Decision tools framing, calculators, ROI language |
| Regrid | Data layer integration, parcel-centric mapping |

---

## 14. CRITICAL DEVELOPMENT RULES

1. **Never invent data sources, endpoints, URLs, or field names.** Verify before implementing.
2. **Never overwrite outputs.** Every new file gets a unique name (use version suffixes like _v2, _v3).
3. **Use stable relative paths** throughout the repo.
4. **Paginate all ArcGIS queries** (handle maxRecordCount using resultOffset/resultRecordCount or objectId paging).
5. **Do not modify the /samples/ folder.** It contains design reference screenshots and competitor patterns.
6. **Do not expose API keys** in the repo. Propose serverless proxy for anything requiring secrets.
7. **Do not load huge GeoJSON at page load.** Load on demand via spatial queries or user interaction.
8. **Client-side JavaScript only.** GitHub Pages has no server-side processing.
9. **Python scripts** for data processing should be provided as complete copy-paste terminal commands using the `python3 << 'EOF'` pattern. Never ask me to edit a script manually.
10. **Always add checkpoint saves** (every 20 batches) to permit download scripts. Save progress incrementally.

---

## 15. WRITING AND STYLE PREFERENCES

- **Active voice only.** No passive constructions.
- **No em dashes.** Break long sentences into two sentences instead.
- **No hedging** ("somewhat," "arguably," "it seems that").
- **No bullet points** unless I specifically request a summary or list. Write in full paragraphs.
- **Concise.** Cut unnecessary words. "Although" not "despite the fact that." "During" not "in the course of."
- **Specific, not abstract.** Concrete terms over vague language.
- **Legal citations** in Bluebook format with full URLs.
- **No interpretive gloss** ("demonstrating that," "this shows that").

---

## 16. MY DEVELOPMENT ENVIRONMENT

- Mac with Python 3
- Virtual environments: dadu_env, Whisper_env
- Key packages: pandas, geopandas, openpyxl, requests, pyproj, shapely, selenium
- Data folder: ~/Desktop/Master_Data/DADU/
- Master analysis folder: ~/Desktop/Master_Data/DADU/MASTER_ADU_DATA/
- Scripts save to: ~/Desktop/Master_Data/Scripts/
- Outputs save to: ~/Desktop/Master_Data/[new project-specific folder]/
- Coordinate systems: EPSG:2274 (Tennessee State Plane) for local analysis, EPSG:4326 (WGS84) for web

---

## 17. WHAT I AM NOW TRYING TO DO

I am actively developing the Homebody Builder platform toward a functional MVP. The work has two tracks running simultaneously: cleanup of accumulated technical debt, and building toward the core product.

### Track 1: Cleanup (Active Right Now)

1. **Cleaning up duplicate HTML pages.** The repo has ~99 HTML files but only ~40-50 are canonical. I am identifying and archiving "_1" duplicates, picking winners from version chains (v1/v2/v3), and ensuring only canonical pages appear in navigation. Do not create new pages for features that already have a working page.

2. **Fixing datasets.** The permits data exists in multiple overlapping files with different record counts and column structures. Contractor data has many empty fields that previous development sessions incorrectly assumed had data. I am consolidating to canonical dataset versions and documenting which file to use for which purpose.

3. **Recovering from merge conflicts.** A previous Claude Code session tried to update 100+ files simultaneously, causing git merge conflicts. Some pages may still contain conflict markers. Any broken page should be checked for conflict artifacts before debugging logic.

4. **Purging the banned color #003039.** A previous AI session introduced #003039 across many pages and instruction files, labeling it "Midnight." This color reads as green on screen and is banned from the entire palette. The correct primary dark is #3A5566 Deep Slate. Every instance of #003039 must be replaced with #3A5566 across all HTML, CSS, and JS files in the repo. Several instruction files in the project (CASTLEHOLD_CLAUDE_CODE_INSTRUCTIONS.md, CLAUDE.md, castlehold_homepage_flat.html, permit_explorer prompts) still list #003039 as the primary color. Those references are outdated and wrong.

### Track 2: Building the MVP

1. **Getting the Homebody Projects / Homebody Builder branding fully consistent** across all canonical pages (replacing old colors including banned #003039, ensuring shared CSS and header load everywhere, swapping castle logo for ADU.png house icon).

2. **Making the maps actually render** on the live site. The eligibility map, permit explorer map, and property search map currently show blank white boxes. This requires debugging Leaflet/ArcGIS JS library loading, ensuring map containers have explicit heights, and connecting the ArcGIS feature layers.

3. **Building the Property Report Card** as the core product spine that every other page links to. This page takes an address or APN input and generates a complete property intelligence report with eligibility, constraints, permits, covenants, documents, and outbound links to Nashville portals.

4. **Wiring documents to parcels** so that when a user views a property, they can access the specific permit PDFs, property cards, site plans, and covenant documents for that parcel.

5. **Building the Permit Explorer** as a searchable, filterable, map-based interface to all DADU permits with contractor info, costs, and document links.

6. **Completing the Contractor Marketplace** with real data from the permits dataset showing contractor rankings, average costs, project portfolios, and links to their work.

7. **Preparing academic deliverables** for Professor Lehrman's class demonstrating network effects theory, competitive pricing analysis, and national scalability frameworks.

The platform is a proof of concept for national scalability. Nashville is the first city. The infrastructure (permit data aggregation, parcel intelligence, document matching, contractor analytics) generalizes to any U.S. municipality that publishes building permits and parcel data.
