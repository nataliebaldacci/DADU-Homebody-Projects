# HOMEBODY PROJECTS — CLAUDE CODE INSTRUCTIONS
**Version:** 5.0 | **Date:** February 14, 2026
**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Repo:** /Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects
**GitHub:** https://github.com/nataliebaldacci/DADU-Homebody-Projects
**Live Site:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/

---

## 1. WHAT THIS PROJECT IS

Homebody Projects is a DADU (Detached Accessory Dwelling Unit) eligibility and planning platform for Nashville-Davidson County. It aggregates public parcel data, permit records, restrictive covenants, and regulatory information into a GitHub Pages website. Nashville's BL2025-1007 legislation (effective December 12, 2025) expanded DADU eligibility to 67,707 parcels, making this an ideal proof of concept for national scaling.

**Brand architecture (two layers, never collapsed):**
- **Homebody Projects / Homebody Builder** = the consumer-facing product. This is what homeowners and contractors see. Appears on homepage, tool pages, nav bar, and all user-facing content.
- **Castlehold** = the authority/data layer underneath. Appears on reports, data attribution, legal/municipal pages, About page, and footer "Powered by" lines.

**What the user sees:** "Homebody Projects" in the nav, "Homebody Builder" on product pages, "Powered by Castlehold" in the footer and on reports.

---

## 2. CRITICAL RULES — READ BEFORE TOUCHING ANYTHING

1. **Audit first.** Before making any changes, run the audit commands in Section 12 and show output.
2. **Never invent data sources, endpoints, URLs, or field names.** Verify them first.
3. **Never delete, rename, or move existing files unless directly asked.** Create new versions if needed (e.g., v4 suffix).
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
11. **NEVER USE EMOJI FOR ICONS.** No 🏠 🔍 📊 🏡 🔨 📐 ⚖️ or any other emoji anywhere on the site. Always use the PNG icons from assets/icons/. If an icon doesn't exist, use text only. This is absolute.
12. **Always use ADU.png for the logo.** The logo is assets/icons/ADU.png with "Homebody Projects" text. Never use the castle logo, never use an emoji house.

---

## 3. BRAND SYSTEM (LOCKED — DO NOT CHANGE)

### Color Palette

**Core Darks:**
| Name | Hex | Role |
|------|-----|------|
| True Dark Anchor | #2F3A45 | Hero gradient base, footer, overlay panels, selected footprint fill |
| Deep Slate (Brand) | #3A5566 | Nav background, headings, brand authority color, parcel boundary stroke |
| Gray Azure | #4C5C66 | Alternate dark, icons, active permit markers |
| Medium Slate | #496778 | Hover states, secondary elements, step number circles |
| Lighter Slate | #4A6B7D | Tertiary elements |

**Secondary / Mid Neutrals:**
| Name | Hex | Role |
|------|-----|------|
| Dark Warm Gray | #706F6C | Captions, small labels |
| Warm Stone | #7B746D | Secondary text, pill borders, hover footprint fill, small cluster markers |
| Lighter Stone | #918A83 | Borders, conditional map status |
| Warm Muted UI | #A59D8B | Mid-tone warm gray, muted UI, background footprint fill, in-review markers |

**Accent:**
| Name | Hex | Role |
|------|-----|------|
| Wheat | #CBB279 | Primary CTA buttons, stat numbers, announcement bar, highlights |

Wheat is the ONLY accent. No ochre, no secondary golds. One accent keeps the system disciplined.

**Neutrals:**
| Name | Hex | Role |
|------|-----|------|
| Cream | #E1D4BB | Body text on dark backgrounds, card light surfaces |
| Light Gray | #E2E2E0 | Card borders, dividers, unknown/out-of-scope map status |
| Linen | #F0EBE1 | Section backgrounds, stats bar background, icon circle backgrounds |
| Soft Canvas | #F3EEEA | Soft panels, filter containers, cards on warm backgrounds |
| Warm Light | #F2F0ED | Page background |
| Off-White | #F5F5F0 | Card surfaces |

**Functional / Map Status (muted, architectural, NOT traffic-light colors):**
| Name | Hex | Role |
|------|-----|------|
| Eligible | #406A64 | Eligible parcels on map, eligibility badges |
| Conditional | #918A83 | Conditional zoning (gray area = literally gray). Reuses Lighter Stone. |
| Not Eligible | #B58676 | Restricted parcels. Muted clay/brick. Nashville-appropriate. |
| Unknown | #E2E2E0 | Out of scope or unknown status. Reuses Light Gray. |

**Map Layer Hierarchy (value-shift system, same hue family, darker = selected):**
| Layer | Fill | Opacity | Stroke | Width | Notes |
|-------|------|---------|--------|-------|-------|
| Background footprints | #A59D8B | 0.55 | None | — | Recedes visually |
| Hover footprint | #7B746D | 0.75 | None | — | Slightly darker on hover |
| Selected footprint | #2F3A45 | 0.90 | #FFFFFF | 2px | Pops clearly with white edge |
| Parcel boundary | — | — | #2F3A45 dashed (6,4) | 2.5px | Crisp architectural line |
| Eligible outline | — | — | #406A64 | 1.5px | Subtle status on parcel edge |
| Conditional outline | — | — | #918A83 | 1.5px | Neutral status outline |
| Not eligible outline | — | — | #B58676 | 1.5px | Restrictive status outline |

Eligibility shows as a subtle outline on the parcel, NOT by recoloring the footprint. Footprint fill stays in the slate family and uses value shift for hierarchy.

**Cluster Markers (no neon, no traffic colors):**
| Size | Fill | Text |
|------|------|------|
| Small (2-9) | #7B746D (Warm Stone) | White |
| Medium (10-49) | #3A5566 (Deep Slate) | White |
| Large (50+) | #2F3A45 (True Dark) | White |

**Permit Status Point Markers:**
| Status | Hex | Notes |
|--------|-----|-------|
| Completed | #406A64 | Same as eligible |
| Active | #4C5C66 | Gray Azure |
| In Review | #A59D8B | Warm Muted UI |

### BANNED COLORS

**#003039 is BANNED.** It reads as green on screen. Replace every instance with #3A5566.

**DO NOT USE:** #003039, #2E6F4E (old eligible green), #6b8fa3, #6b8e4e, #D4A017 (old amber), #C58B2A (old ochre), #7A2A1D (old oxide red), terracotta, sage, teal, or any neon/traffic-light colors.

**DO NOT USE bright/saturated functional colors.** No neon green, candy red, construction-cone orange, or saturated yellow anywhere on maps or UI. All status colors must be muted and architectural.

### CSS Variables
```css
:root {
  /* Core Darks */
  --dark-anchor: #2F3A45;
  --slate: #3A5566;
  --slate-azure: #4C5C66;
  --slate-mid: #496778;
  --slate-light: #4A6B7D;
  /* Secondary / Mid */
  --gray-warm: #706F6C;
  --stone: #7B746D;
  --stone-light: #918A83;
  --stone-muted: #A59D8B;
  /* Accent */
  --wheat: #CBB279;
  /* Neutrals */
  --cream: #E1D4BB;
  --gray-light: #E2E2E0;
  --linen: #F0EBE1;
  --canvas: #F3EEEA;
  --background: #F2F0ED;
  --card-bg: #F5F5F0;
  /* Functional / Map */
  --eligible: #406A64;
  --conditional: #918A83;
  --not-eligible: #B58676;
  --unknown: #E2E2E0;
}
```

**NOTE:** Some older CSS files use variable names like --navy, --teal, --terracotta, --ochre, --error. These names are legacy. Map them to the correct current values. There is NO navy, teal, terracotta, or ochre in the palette.

### Old Colors to Find and Replace
| Old Hex | Replace With | What Changed |
|---------|-------------|-------------|
| #003039 | #3A5566 | BANNED "Midnight" to Deep Slate |
| #2E6F4E | #406A64 | Old eligible green to muted slate-teal |
| #34495e | #4A6B7D | Nav hover to Lighter Slate |
| #1a252f | #2F3A45 | Dark backgrounds to True Dark Anchor |
| #6b8fa3 | #7B746D | Old teal to Warm Stone |
| #6b8e4e | #3A5566 | Old green accent to Slate |
| #c9a86c | #CBB279 | Old tan to Wheat |
| #e8e4df | #F2F0ED | Background lightened |
| #B55A3C | #CBB279 | Old terracotta to Wheat |
| #C58B2A | #CBB279 | Old ochre to Wheat (accent consolidated) |
| #D4A017 | #918A83 | Old amber to Conditional gray |
| #7A2A1D | #B58676 | Old oxide red to Not Eligible clay |

### Typography
- **Body font:** Inter (primary), system sans-serif fallback
- **Headline font:** Source Serif 4 (or Georgia fallback), weight 700, italic
- Headlines: 700-800 weight
- Body: 400-500 weight
- No em dashes. Break long sentences into two.

### Logo
- **Nav logo:** `assets/icons/ADU_Light.svg` (light/white house icon for dark nav background)
- **General logo:** `assets/icons/ADU.png` (dark house icon for light backgrounds, dropdown items)
- Display at ~42px height in nav bar
- Brand text "Homebody Projects" next to the logo: white, Inter, weight 700
- **DO NOT USE** the old castle logo (castlehold-logo.png) or castle SVG

---

## 4. NAVIGATION STRUCTURE (LIVE — Updated Feb 14, 2026)

The nav is implemented in `homebody_header.js` (source of truth) and `homebody_header.html` (static mirror). Both files must stay in sync.

### Top Bar Layout
```
HOMEBODY PROJECTS LOGO (ADU.png) | WHO WE SERVE ▾ | EXPLORE ▾ | BUILD ▾ | DATA ▾ | RESOURCES ▾ | PRICING | ABOUT | [Am I Eligible? →]
```

Nav bar: background #3A5566, height 64px, Inter font.
Nav links: color #E1D4BB, weight 600, 14px. Hover: color white, background #496778.
Logo: ADU.png at ~42px height, far left, with "Homebody Projects" text.
"Am I Eligible?" button: far right, background #CBB279, text #3A5566, weight 700, border-radius 8px. Links to am_i_eligible.html. This is the primary CTA visible on every page.

### Dropdown Icon Style
Each dropdown item shows an SVG/PNG icon at 32-40px, clearly visible next to the label. Icons sit in a #F0EBE1 (Linen) circle background, 48px diameter. Make them prominent.

### Routing
- LOGO → index.html
- PRICING → homebody_dadu_pricing.html (no dropdown)
- ABOUT → about_platform.html (no dropdown)

---

### WHO WE SERVE Dropdown (mega-menu-2, two columns)

**Column 1: User Portals** (Icon: Property_Owners.svg)

| Label | Icon | File |
|-------|------|------|
| Homeowners | Property_Owners.svg | homeowner_portal.html |
| Contractors | Building_and_Construction.svg | contractor_portal.html |
| Designers & Architects | Surveyors_and_Engineers.svg | designer_portal.html |

**Column 2: Professional** (Icon: Municipal.svg)

| Label | Icon | File |
|-------|------|------|
| Municipal & Agencies | Municipal.svg | user-homeowners.html |
| Legal Professionals | Legal.svg | dadu_contractors_infographic.html |
| Advertise With Us | Building_and_Construction.svg | contractor_portal.html#advertise |

---

### EXPLORE Dropdown (mega-menu-2, two columns)

**Column 1: Interactive Maps** (Icon: Area_Maps_and_Visual_layers.svg)

| Label | Icon | File |
|-------|------|------|
| Eligibility Map | Zoning.svg | dadu_eligibility_map.html |
| Property Search | Parcel Search.svg | property_search.html |
| DADUs Near Me | Neighbors.svg | dadu_near_me_v2.html |
| Opportunity Explorer | Area_Maps_and_Visual_layers.svg | dadu_opportunity_explorer_v2.html |
| Permit Explorer Map | Permit_Explorer.svg | permit_explorer.html |
| Parcel Footprint Map | APN Maps.svg | parcel_footprint_map.html |
| ADU Permit Map | Permit_Activity.svg | adu_permit_map.html |
| Overview Map | GIS.svg | homebody_index_map.html |

**Column 2: Dashboards** (Icon: Permit_Activity.svg)

| Label | Icon | File |
|-------|------|------|
| Permit Activity | Permit_Activity.svg | permit_activity_dashboard.html |
| Contractor Marketplace | Building_and_Construction.svg | contractor_marketplace.html |
| Market Trends | Investments.png | market_trends.html |
| Permit Analytics | Enhanced Transaction History Report .svg | nashville_permit_analytics.html |

---

### BUILD Dropdown (mega-menu-4, four columns)

**Column 1: Project Planner** (Icon: Project_Planner.svg)

| Label | Icon | File |
|-------|------|------|
| Project Planner | Project_Planner.svg | project_planner_hub.html |

Note: project_planner_hub.html is the hub page that links to: project_checklist.html, draw_dadu_on_parcel.html, permit_process_timeline.html, and project_planner.html. Those sub-pages are no longer in the nav individually.

**Column 2: Calculators** (Icon: Appraisers.svg)

| Label | Icon | File |
|-------|------|------|
| All Calculators | Appraisers.svg | dadu_calculators.html |

**Column 3: Form Wizard** (Icon: Claims.png)

| Label | Icon | File |
|-------|------|------|
| Form Wizard | Claims.png | form_wizard.html |

Note: `form_wizard.html` is the unified replacement for the deleted `determine_forms_required.html` and `legal_form_filler.html`.

**Column 4: Hire** (Icon: Building_and_Construction.svg)

| Label | Icon | File |
|-------|------|------|
| Find a Contractor | Building_and_Construction.svg | contractor_dashboard.html |

---

### DATA Dropdown (mega-menu-2, two columns)

**Column 1: Report Generator** (Icon: Exports__Reports.svg)

| Label | Icon | File |
|-------|------|------|
| Eligibility Report | Claims.png | eligibility_report.html |
| Project Report | Exports__Reports.svg | project_report.html |
| Neighbors Report | Neighbors.svg | neighbors_report.html |
| Market Report | Market Statistics Report .svg | dadu_reports_store.html |
| Property Report Card | Property Detail Report .svg | property-report-card.html |

**Column 2: Document Database** (Icon: Recorded_Docs.svg)

| Label | Icon | File |
|-------|------|------|
| Site Plans & Permits | Permit_Site_Plans.svg | site_plan_downloads.html |
| External Links | Recorded_Docs.svg | dadu_resources.html |
| Restrictive Covenants | Restrictive_Covenants.svg | restrictive_covenants_v2.html |
| PDF Database | Recorded_Docs.svg | pdf_database_lookup.html |

---

### RESOURCES Dropdown (mega-menu-2, two columns)

**Column 1: Learn** (Icon: ADU.png)

| Label | Icon | File |
|-------|------|------|
| What is a DADU? | ADU.png | what_is_dadu.html |
| General Requirements | Building_and_Construction.svg | dadu_requirements_overview.html |
| Eligibility Flowchart | Zoning.svg | dadu_eligibility_flowchart.html |
| DADU History | Recorded_Docs.svg | dadu_history.html |
| Code & Legislation | Legislation.svg | dadu_code_legislation_v5.html |

**Column 2: Permits & Forms** (Icon: Legal.svg)

| Label | Icon | File |
|-------|------|------|
| Owner Occupancy | Owner_Occupancy.svg | owner_occupancy.html |
| STR Permit | STR_Permit.svg | str_permit.html |
| Required Trade Permits | Renewals.png | trade_permits.html |
| Overlay Districts | Zoning_Documents.svg | overlay-districts.html |
| Design Standards | Overlay_Design_Standards.svg | dadu_design_standards.html |

---

### PRICING
Direct link to homebody_dadu_pricing.html. No dropdown.

### ABOUT
Direct link to homebody_dadu_pricing.html#about. No dropdown.

---

## 5. CURRENT STATE — WHAT EXISTS (Updated Feb 14, 2026)

### Shared Components
- `homebody_shared.css` — Global stylesheet with :root color variables
- `homebody_header.js` — Shared nav component (source of truth for navigation)
- `homebody_header.html` — Static header template (must match homebody_header.js)
- `js/arcgis-services.js` — Shared ArcGIS service registry

### Data Files (in /data/)
- `apn_to_account.json` (6.6MB, 277K entries) — APN to ACCOUNTNUMBER mapping
- `gdrive_docs_index.json` (8.9MB, 18,782 docs / 8,804 parcels) — Google Drive document index v2.1
- `contractor_stats.json` (179KB, 370 contractors / 628 permits) — Contractor statistics
- `master_parcel_data.json` (6.4MB, 868 parcels with permits) — Master parcel dataset
- `address_search_index.json` — Address typeahead index
- `adu_permits_slim.json` — Slim ADU permit data
- `docs_index.json` — Local document index
- `legislation_links_database.json` — Legislation links
- `overlay_districts_index.json` — Overlay district data
- Plus several other supporting JSON/CSV files

### Logo Files (in assets/icons/)
- `ADU.png` — Primary logo (house icon, use everywhere)
- `ADU_Light.svg` — Light/white variant
- `ADU_Blue.svg` — Blue variant
- `ADU_Light.png` — Light PNG variant
- `ADU_MultiColors.svg` — Multicolor variant

### Live Pages (87 HTML files at root)
The site is deployed at https://nataliebaldacci.github.io/DADU-Homebody-Projects/

**Linked in Navigation (35 pages):**
These are the pages directly accessible from the nav dropdowns:

| Nav Section | Pages |
|-------------|-------|
| WHO WE SERVE | homeowner_portal.html, contractor_portal.html, designer_portal.html, user-homeowners.html, dadu_contractors_infographic.html |
| EXPLORE > Maps | dadu_eligibility_map.html, property_search.html, dadu_near_me_v2.html, dadu_opportunity_explorer_v2.html, permit_explorer.html, parcel_footprint_map.html, adu_permit_map.html, homebody_index_map.html |
| EXPLORE > Dashboards | permit_activity_dashboard.html, contractor_marketplace.html, market_trends.html, nashville_permit_analytics.html |
| BUILD | project_planner_hub.html, dadu_calculators.html, form_wizard.html, contractor_dashboard.html |
| DATA > Reports | eligibility_report.html, project_report.html, neighbors_report.html, dadu_reports_store.html, property-report-card.html |
| DATA > Docs | site_plan_downloads.html, dadu_resources.html, restrictive_covenants_v2.html, pdf_database_lookup.html |
| RESOURCES | what_is_dadu.html, dadu_requirements_overview.html, dadu_history.html, dadu_code_legislation_v5.html, owner_occupancy.html, str_permit.html, trade_permits.html, overlay-districts.html, dadu_design_standards.html |
| Direct links | homebody_dadu_pricing.html, am_i_eligible.html, about_platform.html, dadu_documents_portal.html (via Pricing page) |
| Homepage | index.html |

**Unlinked but Worth Keeping (17 pages):**
These have unique content not duplicated elsewhere:

| File | Purpose |
|------|---------|
| area_analysis_report.html | Unique area analysis report |
| contractor_advertising.html | Original advertising page (content merged into contractor_portal.html#advertise) |
| contractor_report.html | Unique contractor report |
| dadu_zoning_standards.html | Zoning standards (content merged into dadu_requirements_overview.html) |
| designer_resources.html | Designer resource content |
| draw_dadu_on_parcel.html | Visual DADU placement tool (linked from project_planner_hub.html) |
| feature-documents.html | Feature landing page (absorbed into about_platform.html) |
| feature-eligibility-map.html | Feature landing page (absorbed into about_platform.html) |
| features.html | Features overview (absorbed into about_platform.html) |
| permit_process_timeline.html | Step-by-step permitting guide (linked from project_planner_hub.html) |
| project_checklist.html | Interactive project checklist (linked from project_planner_hub.html) |
| project_planner.html | Original project planner |
| property_intelligence_report.html | Unique intelligence report |
| property_report.html | Original property report |
| size_calculator.html | Size calculator (removed from nav, may return) |
| user-types.html | User types overview (absorbed into about_platform.html) |
| zoning_documents.html | Zoning document content |

**Unlinked Duplicates (25 pages, candidates for deletion):**
These are older versions or duplicates with content covered by other pages:

am_i_eligible_compact.html, castlehold_homepage_flat.html, dadu_build_explorer.html, dadu_build_explorer_v2.html, dadu_build_tool.html, dadu_build_tool_backup.html, dadu_eligibility_checklist.html, dadu_eligibility_flowchart.html, dadu_explorer_attom.html, dadu_explorer_attom_v2.html, dadu_explorer_v2.html, dadu_near_me_locator.html, dadu_near_me_v3.html, dadu_platform.html, dadu_property_report.html, dadu_property_viewer_v3.html, dadu_report_connected.html, dadu_report_full.html, dadu_symbium_map.html, footprints_proof_of_concept.html, homebody_index.html, homebody_index_v3.html, homebody_index_v4.html, homebody_main.html, index_pq.html, nashville_permit_explorer_v3.html

**Previously Deleted (this session):**
about.html, about_platform_infographic.html, dadu_building_requirements.html, dadu_code_legislation_v3.html, dadu_code_legislation_v4.html, dadu_legislation.html, feature-property-search.html, footprint_cards.html, legal_resources.html, municipal_dashboard.html, project_cost_estimator.html, property_tax_calculator.html, roi_calculator.html, determine_forms_required.html, legal_form_filler.html

---

## 6. WHAT NEEDS TO BE FINISHED — PRIORITY ORDER

### COMPLETED (Feb 14, 2026)
- ✅ Navigation reorganized: WHO WE SERVE | EXPLORE | BUILD | DATA | RESOURCES | PRICING | ABOUT
- ✅ Shared header (homebody_header.js) updated with new nav structure
- ✅ homebody_header.html static template updated to match
- ✅ Logo fixed: ADU.png in nav, "Homebody Projects" branding
- ✅ Logo color variants added: ADU_Light.svg, ADU_Blue.svg, ADU_Light.png, ADU_MultiColors.svg
- ✅ Form Wizard consolidated: form_wizard.html replaces determine_forms_required.html + legal_form_filler.html
- ✅ 15 obsolete pages deleted (about.html, dadu_building_requirements.html, dadu_code_legislation_v3/v4, etc.)
- ✅ BANNED color #003039: 0 files (clean)
- ✅ GeoJSON files removed from git tracking (5.9GB cleaned)
- ✅ .gitignore updated: blanket *.geojson, *.csv, *.xlsx rules
- ✅ ArcGIS layer URLs migrated to Feb 2026 services (14 files)
- ✅ Shared ArcGIS registry created (js/arcgis-services.js)
- ✅ Phase 2 data files created: apn_to_account.json, gdrive_docs_index.json, contractor_stats.json, master_parcel_data.json
- ✅ Contractor advertising merged: content from contractor_advertising.html merged into contractor_portal.html#advertise
- ✅ Contractor pricing added to homebody_dadu_pricing.html (3 tiers: $29/$79/$149)
- ✅ Nav updated: "Advertise With Us" now links to contractor_portal.html#advertise (both header.js and header.html)
- ✅ contractor_portal.html fully rebranded: Inter font, CSS variables, SVG icons, fixed broken link to deleted page
- ✅ Eligibility flowchart made fully interactive: step-through wizard with YES/NO gates, collapsed summary bars with "Change Answer", progress bar, Step 5 informational with Continue button, Step 6 ends with Eligible result card + Property Report Card link, Show All toggle, Start Over, all 49 links preserved
- ✅ Three-page styling fix: trade_permits.html (title, Montserrat→Inter, CSS var fixes incl. green --terracotta bug), overlay-districts.html (title, Montserrat→Inter, removed banned colors --yellow/--red/purple, footer branding), contractor_dashboard.html (already correct, no changes needed)
- ✅ About page created: about_platform.html with 7 sections (Hero, What Is, Platform Features 12 cards, How It Works, Data Sources 6 cards, Built For Every User 4 portals, CTA). ABOUT nav updated from pricing#about to about_platform.html in both header.js and header.html. Absorbs: features.html, feature-documents.html, feature-eligibility-map.html, user-types.html
- ✅ 24 duplicate pages deleted (verified dadu_report_full.html aerial/street view already in property-report-card.html; kept dadu_resources.html as active nav page)
- ✅ Branding sweep complete: old palette colors replaced in 9 files, Montserrat→Inter in 30 files, 32 title tags fixed from Castlehold to Homebody Projects, 3 castle logo nav bars fixed, 8 footer brand spans fixed, 7 footer copyright lines fixed. Verified: 0 banned colors, 0 old colors, 0 Montserrat, 0 Castlehold in titles (except sample_reports/ which are allowed)

### PRIORITY 1: Delete Duplicate Pages
**Status:** DONE. 24 duplicate pages deleted. dadu_resources.html kept (active nav page).

### PRIORITY 2: Fix Branding Consistency Across All Pages
**Status:** DONE. All pages fixed. Verified 0 banned colors, 0 old palette colors, 0 Montserrat references, 0 Castlehold in page titles (only in sample_reports/ which is allowed).

### PRIORITY 3: Fix Broken Maps
**Status:** AUDITED. All 8 map pages verified: Leaflet 1.9.4 CDN loaded, map containers have proper height (calc(100vh) or flex chains), homebody_shared.css and homebody_header.js present, ArcGIS Feature Service URLs (CORS-friendly). No basemaps changed. Live site testing still recommended.

**Audit results (all 8 pages pass):**
- dadu_eligibility_map.html: height: calc(100vh - 80px) + min-height: 500px
- property_search.html: absolute positioning with parent calc(100vh - 75px)
- dadu_near_me_v2.html: height: 100% with flex parent
- dadu_opportunity_explorer_v2.html: flex:1 with parent calc(100vh - 75px)
- permit_explorer.html: flex chain from html(100%)→body(flex)→main→map, mobile 50vh
- parcel_footprint_map.html: height: calc(100vh - 75px)
- adu_permit_map.html: absolute with top:75px bottom:0
- homebody_index_map.html: proper flex tree with min-height:0

### PRIORITY 4: Property Report Card (Core Product Spine)
**Status:** Page enhanced in Phase 2 with apn_to_account.json, covenants, Nashville fallbacks. External links need verification.

**Tasks:**
1. Verify all external link builders work:
   ```
   Parcel Viewer:     https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}
   Print Record:      https://maps.nashville.gov/ParcelViewer/PrintRecord.html?pin={PIN}
   Permit Docs:       https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}
   Parcel Docs:       https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={APN}
   ePermits:          https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}
   Assessor:          https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}
   Property Card:     https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
   ```
2. Show building footprints on the report card map
3. Display permit history for the parcel
4. Show restrictive covenant status and link to covenant documents

### PRIORITY 5: Document Portal Enhancement
**Status:** dadu_documents_portal.html enhanced in Phase 2 with multi-search, filters, real stats. Uses gdrive_docs_index.json.

**Still needed:**
1. Verify search functionality works end-to-end
2. Test document linking to Google Drive
3. Verify all document types display correctly

### PRIORITY 6: Contractor Marketplace Data Connection
**Status:** Rewritten in Phase 2 using contractor_stats.json (370 contractors, 628 permits). Real data connected.

**Still needed:**
1. Verify data displays correctly on live site
2. Test search and filtering
3. Verify contractor detail views

### PRIORITY 7: Homepage (index.html)
**Status:** DONE. Fixed 7 broken links to deleted pages (determine_forms_required→form_wizard, municipal_dashboard→user-homeowners, legal_resources→dadu_contractors_infographic, dadu_code_legislation_v3→v5, dadu_building_requirements→dadu_requirements_overview, project_planner→project_planner_hub). Updated icons to match Section 6B spec. Fixed section background colors to #F2F0ED. All 22 links verified, all 18 icons verified.

### PRIORITY 8: Fill Placeholder Pages
**Status:** Many pages have basic content. Some may still be stubs.

### PRIORITY 9: Test All Nav Links
**Status:** All 41 nav target pages verified to exist. Need live testing to confirm they render correctly.

---

## 6B. HOMEPAGE IMPLEMENTATION SPEC (index.html)

### Reference Images
- **Style reference:** `ChatGPT Image Feb 12, 2026, 05_42_00 AM.png` in repo root. Match this look and feel.
- **Hero backdrop (KEEP this image, do not replace):** `ChatGPT Image Feb 12, 2026, 06_17_37 AM.png`
- Also available at: `assets/nashville-aerial-hero.png`

### Logo Swap
- Replace `assets/castlehold-logo.png` with `assets/icons/ADU.png`
- Replace any inline SVG castle logo with: `<img src="assets/icons/ADU.png" alt="Homebody Projects" style="height: 42px; width: auto;">`
- Replace "CASTLEHOLD" text with "Homebody Projects"
- Remove subtitle "DADU Zoning & Buildability Intelligence"

### Homepage Color Spec
```
Nav bar:        background #3A5566, text #E1D4BB, hover #496778
Hero overlay:   linear-gradient(rgba(58, 85, 102, 0.8), rgba(58, 85, 102, 0.9)) over backdrop image
Headline:       color #E1D4BB, serif font (Source Serif 4 or Georgia), weight 700, italic
Subtitle:       color #F0EBE1
Search bar:     white background, rounded, button #CBB279 with #3A5566 text
Stat numbers:   color #CBB279, font-weight 800
Stat labels:    color #E1D4BB, uppercase, letter-spacing 2px
Section bgs:    alternating #F2F0ED (warm light) and white
Cards:          background #f5f5f0, border 1px solid #E2E2E0
Card headings:  color #3A5566
Card body text: color #706F6C
Card icons:     PNG icons in 48px #F0EBE1 (Linen) circle backgrounds
Card links:     color #3A5566, "Learn More →"
Dark sections:  background #3A5566, text #E1D4BB, headline italic serif
CTA buttons:    background #CBB279, text #3A5566, font-weight 700, border-radius 8px
Footer:         background #3A5566, text #E1D4BB, links #918A83
```

---

### SECTION 1: HERO
- **Backdrop:** `ChatGPT Image Feb 12, 2026, 06_17_37 AM.png` (DO NOT REPLACE)
- **Overlay:** linear-gradient(rgba(58, 85, 102, 0.8), rgba(58, 85, 102, 0.9))
- **Headline:** "Build Your Nashville DADU with Confidence" — #E1D4BB, serif, 700, italic
- **Subtitle:** "The complete platform for DADU eligibility, permits, contractors, and market data. 67,707 eligible parcels. One powerful tool." — #F0EBE1
- **Search bar:** Address input with "Enter your Nashville address..." placeholder, "Check Eligibility" button (#CBB279 bg, #3A5566 text)
- **Stats row:**
  - 67,707 — ELIGIBLE PARCELS
  - 827+ — DADUS PERMITTED
  - 393 — ACTIVE CONTRACTORS
  - Numbers: #CBB279, font-weight 800. Labels: #E1D4BB, uppercase, letter-spacing 2px

### SECTION 2: EVERYTHING YOU NEED FOR YOUR DADU PROJECT
- **Background:** #F2F0ED
- **Heading:** "Everything You Need for Your DADU Project" — #3A5566, serif, italic
- **4 cards in a row:**

| Card | Icon | Description | Link |
|------|------|-------------|------|
| Am I Eligible? | Property_Owners.png | Instant eligibility check based on Nashville's BL2025-1007 zoning requirements. | am_i_eligible.html |
| Size Calculator | Appraisers.png | Calculate your maximum DADU size based on lot dimensions and zoning. | size_calculator.html |
| Cost Estimator | Exports__Reports.png | Estimate build costs by size, finish level, and site conditions. | dadu_calculators.html |
| Contractor Directory | Building_and_Construction.png | Connect to vetted builders specializing in ADUs on your sized lot. | contractor_marketplace.html |

Each card: #f5f5f0 background, #E2E2E0 border, icon in #F0EBE1 circle, heading #3A5566, body #706F6C, "Learn More →" link

### SECTION 3: ALL-IN-ONE PLATFORM FEATURES
- **Background:** white
- **Heading:** "All-In-One DADU Platform Features" — #3A5566, serif, italic
- **Feature grid (cards or icon+text blocks):**

| Feature | Icon | Link |
|---------|------|------|
| Explore Interactive Maps | Area_Maps_and_Visual_layers.png | dadu_eligibility_map.html |
| Planning Projects | — | project_planner_hub.html |
| Form Wizard | — | form_wizard.html |
| Document Portal | Recorded_Docs.png | dadu_documents_portal.html |
| Activity Dashboard | — | permit_activity_dashboard.html |
| Market Insights | — | market_trends.html |
| Contractors | Building_and_Construction.png | contractor_marketplace.html |

### SECTION 4: BUILT FOR YOUR NEEDS
- **Background:** #F2F0ED
- **Heading:** "Built For Your Needs" — #3A5566, serif, italic
- **Subheading:** "Specialized tools and data for every user type" — #706F6C
- **User type cards (larger, with PNG icons prominently displayed):**

| User Type | Icon | Description | Link |
|-----------|------|-------------|------|
| Homeowners | Property_Owners.png | Check your eligibility, understand requirements, estimate costs, and find qualified contractors. | user-homeowners.html |
| Contractors & Builders | Building_and_Construction.png | Find leads and market insights. | contractor_marketplace.html |
| Designers & Architects | Surveyors_and_Engineers.png | Building requirements, site analysis, precedent projects. | designer_resources.html |
| Municipal | Municipal.png | Permit tracking, policy analysis, compliance monitoring. | user-homeowners.html |
| Legal Professionals | Legal.png | Covenant research, title issues, zoning compliance, and legal citations database. | dadu_contractors_infographic.html |

Each card: "Get Started" button (#CBB279 bg, #3A5566 text)

### SECTION 5: PROFESSIONAL REPORTS
- **Background:** #3A5566 (dark section)
- **Heading:** "Professional Reports" — #E1D4BB, serif, italic
- **Report cards (on dark background):**

| Report | Link |
|--------|------|
| Eligibility Report | eligibility_report.html |
| Project Report | project_report.html |
| Neighbors Report | neighbors_report.html |
| Market Report | dadu_reports_store.html |

Cards: #f5f5f0 background on dark section, or white with subtle border

### SECTION 6: DATA & RESOURCES
- **Background:** #F2F0ED
- **Heading:** "Data & Resources" — #3A5566, serif, italic
- **Subheading:** "Access Nashville's most comprehensive DADU dataset" — #706F6C
- **Items:**

| Item | Link |
|------|------|
| Document Portal | dadu_documents_portal.html (accessed via Pricing page) |
| Permits & Site Plans | site_plan_downloads.html |
| Direct External Links to Metro Code | (external Nashville links) |
| Codes and Legislation | dadu_code_legislation_v5.html |
| DADU Guide | what_is_dadu.html |

### SECTION 7: CTA — READY TO BUILD YOUR DADU?
- **Background:** #3A5566 with aerial backdrop overlay (same treatment as hero)
- **Heading:** "Ready to Build Your DADU?" — #E1D4BB, serif, italic
- **Button:** "Check Eligibility Now" — #CBB279 bg, #3A5566 text, large, centered
- Links to: am_i_eligible.html

### SECTION 8: FOOTER
- **Background:** #3A5566
- **Text:** #E1D4BB
- **Links:** #918A83
- **Columns:**
  - Learn: Am I Eligible, Size Calculator, Cost Estimator
  - Features: Contractor Directory, Planning Resources, Pricing
  - Get in Touch: email, Contact, Sign in
- **Bottom row:** Privacy Policy | Terms, social icons (Twitter, LinkedIn)
- **"Powered by Castlehold"** in small text (this is the ONLY place Castlehold appears on the homepage)

---

### What NOT to Change on the Homepage
- Do not remove or replace the hero backdrop image
- Do not change basemaps on any embedded map
- Do not introduce any color not listed in Section 3 of this document
- Do not use #003039 anywhere (BANNED)

---

## 7. DATA ASSETS AND FIELD MAPPINGS

### Core Datasets

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

### Coordinate Reference Systems
- Local analysis: EPSG:2274 (Tennessee State Plane, units in feet)
- Web mapping: EPSG:4326 (WGS84 lat/lon)
- ArcGIS default: Web Mercator (auto-converted)

---

## 8. ARCGIS LAYERS AND DATA SERVICES

### CRITICAL: Use Live ArcGIS Layers, NOT Local GeoJSON
The site was loading GeoJSON files from the GitHub repo, which caused blank maps because the files are too large for client-side loading. **Replace all GeoJSON references with the live ArcGIS Feature Service URLs below.** All layers are hosted on Vanderbilt's ArcGIS Online at services3.arcgis.com (CORS-friendly). Do NOT use maps.nashville.gov endpoints from client-side code (CORS blocked from GitHub Pages).

### ArcGIS Authentication
```
ARCGIS_CLIENT_ID=Ofts9Gi1vx4gytIO
ARCGIS_CLIENT_SECRET=d567d643e2fb4fd4ae23c2201e9cd5a6
```
These are OAuth app credentials. A temporary token is required for each session. Ask for the token before making authenticated requests.

Portal: vanderbilt.maps.arcgis.com

### DO NOT CHANGE BASEMAPS
A previous session changed basemaps without permission. Do not switch basemap styles unless explicitly asked.

---

### Parcel Polygon Layers (All Parcels)
| Layer | URL |
|-------|-----|
| Eligibility Enhanced Polygons | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Eligibility_Enhanced_Polygons_20260213_065606/FeatureServer |
| Parcels with Building Info | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Parcels_Building_Info_20260213_070754/FeatureServer/0 |
| Building Specs Polygons | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Building_Specs_Polygons_20260213_065606/FeatureServer |
| Building Footprints SingleFamily | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Building_Footprints_SingleFamily/FeatureServer/0 |

### Eligible-Only Parcel Layers
| Layer | URL |
|-------|-----|
| DADU BL2025-1007 Eligible | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_BL2025_1007_Eligible_20251230_011045/FeatureServer/0 |
| DADU Complete SHP | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_Complete_SHP_20251230_1348/FeatureServer |

### Building Footprint Polygon Layers
| Layer | URL |
|-------|-----|
| Footprints With Parcel Data | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Footprints_With_ParcelData_20260118_011423/FeatureServer/0 |
| Footprints Trimmed | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Footprints_Trimmed_20260213_060215/FeatureServer |
| Building Footprints SingleFamily | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Building_Footprints_SingleFamily/FeatureServer |
| Accessory Footprints | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Accessory_Footprints_RQgxIo/FeatureServer |
| SF Footprints Flattened | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/SF_Footprints_Flattened_20251118_2/FeatureServer |

### Permit Data Layers
| Layer | URL |
|-------|-----|
| DADU All Permits MERGED v2 | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_All_Permits_MERGED_v2_20260213/FeatureServer |
| DADU Permits Combined | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_Permits_Combined/FeatureServer/0 |
| NEW ADU Permits (4,117 records) | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/NEW_ADU_Permits_20260114/FeatureServer/0 |
| DADU All Permits | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_All_Permits/FeatureServer/0 |
| DADU All Permits Final | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_All_Permits_Final/FeatureServer/0 |
| DADU Permit Type | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_Permit_Type_1bUTSV/FeatureServer |

### Point Layers
| Layer | Records | URL |
|-------|---------|-----|
| NEW ADU Permits Points | 4,117 | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/NEW_ADU_Permits_20260114/FeatureServer/0 |
| DADU Eligibility ENHANCED | 161,703 | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer |
| DADU All Permits Points | — | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_All_Permits/FeatureServer/0 |
| DADU All Permits Final Points | — | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_All_Permits_Final/FeatureServer/0 |
| DADU Building Specs | — | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Building_Specs_20260119_042856/FeatureServer |
| Existing DADUs Merged | — | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Secondary_SFH_Merged_SHP_20251231_0015/FeatureServer/0 |
| Secondary on SF Parcels | — | https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Secondary_On_SF_Parcels_SHP_20251230_2352/FeatureServer/0 |

### Restrictive Covenants Layers
| Layer | URL |
|-------|-----|
| Parcels with CR (43,711) | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Parcels_with_CR__A1_AP43711_wk1ztG/FeatureServer/0 |
| Parcels with Restrictive Covenants | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer/0 |
| Restrictive Covenant Links (PDFs) | https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer/0 |

### Web Maps (Vanderbilt ArcGIS Online)
| Map | URL |
|-----|-----|
| Existing DADUs | https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=9f40d0ca10b1453198617aa9cd2f6b9f |
| Building Specs | https://vanderbilt.maps.arcgis.com/home/item.html?id=d7f2cf4e38f34eddba0a671aa0db4acf |
| DADU Near Me | https://vanderbilt.maps.arcgis.com/home/item.html?id=3e01dee4a4384062b0a0c1be98cd3839 |
| DADU Permits (map 1) | https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=50bbdc9cb0c24ab4aaaadc3951cc1555 |
| DADU Permits (map 2) | https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=e07213bcf33748679b195c72ee421e42 |
| DADU Eligibility BL2025-1007 | https://vanderbilt.maps.arcgis.com/home/item.html?id=d6c2c06db5744bb0836cfb0227548275 |
| DADU Footprints | https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=d3f149a92f1c4131b3fc711bc4809b5b |
| Restrictive Covenants | https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=168e16cf3b08411296759cf39f22dc6d |

### Locators / Geocoding
| Service | URL |
|---------|-----|
| Nashville Address Points | https://maps.nashville.gov/arcgis/rest/services/Addressing/AddressPoints/MapServer/0/ |
| Nashville Locators | https://maps.nashville.gov/arcgis2/rest/services/Locators |

---

### Nashville ePermits API
- Base: `https://epermits.nashville.gov/api`
- `caseSubTypeID 774` = DADU permits specifically

### Nashville ParcelService SOAP API
- Base: `https://maps.nashville.gov/ParcelService/Search.asmx`
- `/GetPermitHistory?apn={APN}`
- `/GetGenInfo?pin={PIN}`
- `/GetOwnerHistory?pin={PIN}`

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

Eligibility map coloring: Eligible (#406A64), Not Eligible (#B58676), Conditional (#918A83).

---

## 10. PRICING TIERS

| Tier | Price | Includes |
|------|-------|----------|
| Free | $0 | Near Me locator, basic permit info, contractor names, cost ranges, external links |
| Detail Report | $4.99 | Full permit details, exact cost, sqft, cost/SF, permit PDFs, property card, aerial + street view |
| Contractor Report | $9.99 | All DADUs by contractor, average cost/SF, project locations, contact info |
| Area Analysis | $14.99 | All DADUs in neighborhood/zip, cost trends, most active contractors, approval timeline stats |

Implementation: Placeholder buttons now, Stripe integration later.

Sample report previews already built: eligibility, property, contractor match, covenant analysis, permit history, comparables, cost estimate, market stats, neighbors, zoning verification.

---

## 10B. COMPLETE PRODUCT CATALOG

### Core Product Experiences (the six things users come here to do)

1. **Check My Property (Property Report Card)** — The spine of the platform. A user enters an address or APN and gets a Property Report Card summarizing eligibility, constraints, permits, covenants, documents, and verified outbound links to Nashville government portals (ParcelViewer, ePermits, property assessor, document search). Every other tool on the site funnels back to this.

2. **Near Me Locator** — Enter an address, pick a radius (0.25, 0.5, 1, 2 miles), see a map + list of completed or permitted DADUs nearby. Each result shows address, permit number, date, square footage, cost, and contractor name where available. Results link to Property Report Cards. Free tier shows basic info; paid tier unlocks detail.

3. **Eligibility Map** — Color-coded interactive map of all 285,512 Nashville parcels: green (eligible), yellow (conditional/overlay needed), gray (not eligible). Powered by the DADU_Eligibility_ENHANCED dataset (161,703 parcels). Click any parcel to see status and link to the Property Report Card.

4. **Permit Explorer** — Filter all Nashville building permits by type, date range, status, contractor name, cost range, and square footage range. Pagination and export. PropStream-style decision tools.

5. **Document Portal** — ParcelQuest-style recorded documents search. Search by APN, address, document type, permit number. Returns permit PDFs, site plans, restrictive covenants, and property cards. Documents link to Google Drive folders for download. Accessible from parcel detail views and parcel history views.

6. **Contractor Marketplace** — Real data from permits showing top builders ranked by permit volume, average cost per SF, project locations, and contact info where available. Contractor profiles, leaderboard, pricing benchmarks.

### Calculators and Planning Tools

| Tool | File | Description |
|------|------|-------------|
| All Calculators Hub | dadu_calculators.html | Central hub linking to all calculator tools |
| Size Calculator | size_calculator.html | Max DADU size based on lot (< 10K SF = 700/750; ≥ 10K = 850/1,000) |
| Project Planner Hub | project_planner_hub.html | Step-by-step project management hub |
| Project Checklist | project_checklist.html | Interactive project checklist |
| Permit Process Timeline | permit_process_timeline.html | Step-by-step permitting guide |
| Draw DADU on Parcel | draw_dadu_on_parcel.html | Visual placement tool |
| Form Wizard | form_wizard.html | Unified forms wizard (replaced determine_forms_required + legal_form_filler) |
| Am I Eligible? | am_i_eligible.html | Address-based eligibility check/flowchart |

### Learn and Reference Pages

| Page | File | Content |
|------|------|---------|
| What is a DADU? | what_is_dadu.html | Educational introduction |
| General Requirements | dadu_requirements_overview.html | Setbacks, height, lot coverage, zoning standards (merged from dadu_zoning_standards.html) |
| DADU History | dadu_history.html | Legislative history |
| Code & Legislation | dadu_code_legislation_v5.html | 111+ legal citations, Bluebook format |
| Design Standards | dadu_design_standards.html | Overlay design requirements |
| Overlay Districts | overlay-districts.html | UDO, DADU, SP overlays with ordinance links |
| Owner Occupancy | owner_occupancy.html | Requirement explanation and forms |
| STR Permit | str_permit.html | STR eligibility for DADUs |
| Trade Permits | trade_permits.html | Required trade permits for construction |

### Data and Analytics Pages

| Page | Content |
|------|---------|
| Permit Activity Dashboard | Real-time permit activity tracking |
| Contractor Dashboard | Performance analytics by contractor |
| Market Trends | Cost trends over time, demand by ZIP |
| Nashville Permit Analytics | Costs, trends, demand analysis |
| Secondary Structures Map | Parcels with existing secondary buildings |
| ADU Opportunity Explorer | Eligible parcels without existing ADUs |
| DADU Activity Feed | Recent construction/permit activity |
| Restrictive Covenants Dataset | 43,000+ parcels with covenant data |
| Building Permit History | Complete permit records by area |

### User Type Portals

Each user type has a dedicated portal page linked from WHO WE SERVE:

| User Type | Portal Page | Nav Link | Core Needs |
|-----------|------------|----------|-----------|
| Homeowners | homeowner_portal.html | WHO WE SERVE > User Portals | Eligibility check, what can I build, near me, cost calculators, covenant check |
| Contractors | contractor_portal.html | WHO WE SERVE > User Portals | Permit explorer, market analytics, leads, pricing benchmarks |
| Designers/Architects | designer_portal.html | WHO WE SERVE > User Portals | Requirements database, site analysis tools, setback calculators |
| Municipal/Government | user-homeowners.html | WHO WE SERVE > Professional | Permit tracking, impact analysis, compliance monitoring |
| Legal/Appraisers | dadu_contractors_infographic.html | WHO WE SERVE > Professional | Recorded documents, covenant checks, valuation data |

**Additional pages in WHO WE SERVE > Professional:**
- "Advertise With Us" links to contractor_portal.html#advertise (advertising content merged into contractor portal)
- contractor_advertising.html still exists as a standalone page but is no longer linked from nav

**NOTE:** There is no Developer/Investor user type in the nav or on the site. If that content exists, it stays as a standalone page not linked from primary navigation.

---

## 10C. PROJECT BUILD HISTORY AND LOCAL DATA INVENTORY

### Build Timeline

**January 19, 2026 — Data Foundation**
- Extracted 327,829 building footprints from Nashville ArcGIS
- Cross-referenced 5 ADU indicator sources across 284,425 parcels (98.9% accuracy against PropertyShark)
- Created master analysis files: MASTER_Parcels_5_ADU_Indicators, MASTER_Parcels_Strong_ADU_Signal, MASTER_Covenants_All
- Downloaded 8,514 restrictive covenant PDFs, 630 permit PDFs, 698 aerials, 3,358 property cards
- Created PDF_Database_By_APN.json (73,375 APNs mapped to local file paths)
- Built eligibility dataset: 161,702 eligible parcels, 159,840 by-right in USD, 58,886 needing overlay in GSD

**January 23, 2026 — References and ArcGIS Upload**
- Created 12-sheet reference Excel (Legistar bills, overlay ordinances, Metro Code, ArcGIS endpoints)
- Uploaded datasets to ArcGIS Online: DADU_Eligibility_ENHANCED, All_Permits_Final, Building_Specs, Covenants, Footprints, Secondary structures
- Built DADU_Eligibility_ENHANCED_20260119.csv and DADU_Eligibility_FINAL_20260119.csv

**February 5-6, 2026 — Website Build (Claude Code Session 1)**
- Built 95+ HTML pages including homepage, contractor marketplace, dashboards, calculators
- Created mega-menu navigation structure

**February 10-11, 2026 — Castlehold Rebranding (Claude Code Session 2)**
- Locked nav, palette, shared components (homebody_header.js, homebody_shared.css)
- Built property report card with URL templates
- Discovered ePermits caseSubTypeID 774 = DADU permits
- Found PROJSCOPE contains square footage, setbacks, covenant recording numbers; RESCONVAL has construction values

**February 12, 2026 — Overlay Ordinances and Documentation**
- Extracted 247 overlay ordinances across 18 types from Nashville zoning code
- Created consolidated instructions document (CLAUDE.md)
- Audited live site: blank maps, fake contractor data, old colors, missing JSON files

**February 13, 2026 — ArcGIS Layer Migration**
- Migrated 14 files to Feb 2026 ArcGIS feature services
- Created shared registry (js/arcgis-services.js)

**February 14, 2026 — Navigation Reorganization and Cleanup (Claude Code Session 4)**
- Ran full site audit: 87 HTML files at root, 0 files with BANNED #003039
- Reorganized nav from EXPLORE | DASHBOARD | FEATURED TOOLS | WHO WE SERVE to intent-based: WHO WE SERVE | EXPLORE | BUILD | DATA | RESOURCES | PRICING | ABOUT
- Rewrote homebody_header.js and homebody_header.html with complete new nav structure
- Added mega-menu-2 CSS class to homebody_shared.css for 2-column dropdowns
- Fixed logo in shared header: ADU.png + "Homebody Projects" (was castle logo + "Castlehold")
- Added logo color variants: ADU_Light.svg, ADU_Blue.svg, ADU_Light.png, ADU_MultiColors.svg
- Consolidated Form Wizard: form_wizard.html replaces determine_forms_required.html + legal_form_filler.html
- Deleted 15 obsolete pages: about.html, about_platform_infographic.html, dadu_building_requirements.html, dadu_code_legislation_v3.html, dadu_code_legislation_v4.html, dadu_legislation.html, feature-property-search.html, footprint_cards.html, legal_resources.html, municipal_dashboard.html, project_cost_estimator.html, property_tax_calculator.html, roi_calculator.html, determine_forms_required.html, legal_form_filler.html
- Removed 5.9GB of GeoJSON files from git tracking (31 files), cleaned other junk files
- Updated .gitignore with blanket *.geojson, *.csv, *.xlsx rules
- Squashed 7 unpushed commits into one clean commit to resolve GitHub HTTP 400 (large file rejection)
- Identified 26 additional duplicate pages as candidates for deletion
- Verified all 41 nav target pages exist
- Updated CLAUDE.md to v5.0 with accurate current state

### Local Data Downloads (~/Desktop/Master_Data/DADU/)

| Folder | Files | Size |
|--------|-------|------|
| Permit_PDFs_Downloaded/ | 630 PDFs | 1.79 GB |
| Restrictive_Covenants/ | 8,514 PDFs | 1.43 GB |
| Property_Cards_ALL_Merged/ | 3,358 PDFs | ~6.9 GB |
| Card2_Images/ | 8,074 images | — |
| Aerial_PDFs/ | 698 PNGs | — |
| Davidson_Permit_History/ | 32 CSVs (962K permits) | 15.5 GB |
| MASTER_ADU_DATA/ | 125+ analysis files | — |

### Google Drive Document Folders

| Folder | Drive ID | Contents | Upload Status |
|--------|----------|----------|--------------|
| Permit PDFs | 1N_IpJaweqoFhbmBnYHjQJs1G1ItTQjC4 | 630 permit/site plan PDFs | ~219 uploaded, ~411 pending |
| Restrictive Covenants | 1bEZN1kEZxqZLkdX0QjT0g9N7K0sXAy3Z | 8,514 covenant PDFs | ✅ Complete |
| Property Cards | 1UGNXAbDE1RuXfzMc6Vk3YL2r1AlZMwLZ | 3,358 merged cards | ✅ Complete |
| Aerials | 1eD1TUNuYMOMK7VdVJW3Pc6mHYFS02VUj | 698 aerial screenshots | Pending |
| UDO Overlay PDFs | 1evPTz2SvAIDS74lwzgxjGF85kl2nDsrh | UDO overlay design docs | — |
| DADU Overlay PDFs | 1KDQe3WhWz1H1ukTIlAfxtbDFmvX50kYu | DADU overlay design docs | — |
| STR Permits | 1_JGdEdlUS7IGWi4L93aSGOhHWZJfktql | STR permit docs | — |
| Zoning Board Appeals | 1bjNIPyogxImJ5_zxnxKTmxlYCmO0clvH | ZBA decision docs | — |

### ADU Indicator Sources (Validation System)

| Indicator | Records | Description |
|-----------|---------|-------------|
| regrid_2plus_bldgs | 67,000 | Properties with 2+ buildings from Regrid |
| county_permit | 827 | Metro Nashville DADU permits |
| 3rdparty_permit | 1,800 | RE Data/RealtyTrac permit records |
| fraction_B | 10,000 | Secondary address indicators ("123B Main St") |
| covenant | 1,100 | Restrictive covenant filings mentioning secondary structures |

Combined 2+ indicators: 5,647 parcels with strong ADU signal. 98.9% detection rate against PropertyShark's confirmed 2-unit properties.

### ePermits API Discovery

- caseSubTypeID 774 = DADU permits
- PROJSCOPE field contains: square footage, setbacks, covenant recording numbers
- RESCONVAL field contains: construction cost values
- CaseQuantityGroupDetail endpoint returns detailed permit data

---

## 11. FILE STRUCTURE

```
/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects/
├── index.html                    # Homepage
├── homebody_shared.css           # Global stylesheet
├── homebody_header.js            # Shared nav component (SOURCE OF TRUTH for navigation)
├── homebody_header.html          # Static header template (must match .js)
├── CLAUDE.md                     # This file — project instructions
├── /assets/
│   ├── /css/                     # Additional stylesheets
│   ├── /js/                      # Shared JavaScript modules
│   └── /icons/                   # SVG + PNG icons for nav/cards (ADU.png logo is here)
├── /js/
│   └── arcgis-services.js        # Shared ArcGIS service URL registry
├── /data/                        # JSON indexes (apn_to_account, contractor_stats, etc.)
├── /docs/                        # PDF documents
├── /samples/                     # Design reference (DO NOT MODIFY)
├── /sample_reports/              # Sample report previews
├── [87 HTML pages at root]       # 42 linked, 11 unlinked keepers, 25 duplicate candidates
├── /DADU/                        # Data folder (130GB, in .gitignore)
│   ├── /FINAL_FINAL/             # Latest processed datasets
│   ├── /MASTER_ADU_DATA/         # Consolidated analysis files
│   ├── /All_Icons/               # Icon source files
│   ├── /Permit_PDFs_Downloaded/
│   ├── /Property_Cards_Downloaded/
│   ├── /Property_Cards_2_Assessor/
│   └── /Restrictive_Covenants/
├── /New_Icons/                   # New icon source files (Logo/ subfolder has variants)
└── /Scripts/                     # Python processing scripts
```

### Available Icons (SVG + PNG)
Path: `/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects/assets/icons/`
Web path: `assets/icons/FILENAME`
**EMOJI ARE BANNED SITE-WIDE.** If no icon exists, use text only.
Make icons prominent. Previous AI session made them too small.

**SVG Icons (preferred for nav, cards, UI):**
```
APN Maps.svg, Appraisers.svg, Area Maps and Visual layers.svg,
Area_Analysis.svg, Area_Maps_and_Visual_layers.svg,
Building and Construction.svg, Building_and_Construction.svg,
Bulk data.svg, Claims.png, Draw_on_Parcel.svg,
Enhanced Transaction History Report .svg, Exports & Reports.svg,
Exports__Reports.svg, GIS.svg, Home_Owner.svg, Investors.svg,
Legal.svg, Legislation.svg, Market Statistics Report .svg,
Municipal.svg, Neighbors.svg, Overlay_Design_Standards.svg,
Owner_Occupancy.svg, Parcel Search.svg, Permit_Activity.svg,
Permit_Explorer.svg, Permit_Site_Plans.svg, Project_Checklist.svg,
Project_Planner.svg, Property Detail Report .svg,
Property Owners.svg, Property_Owners.svg,
Recordable Legal Report.svg, Recorded Docs.svg, Recorded_Docs.svg,
Restrictive_Covenants.svg, STR_Permit.svg,
Surveyers adn Engineers.svg, Surveyors_and_Engineers.svg,
Transaction History Report .svg, Utilities.svg, Valuations.png,
Zoning.svg, Zoning_Documents.svg
```

**PNG Icons:**
```
ADU.png (logo), Claims.png, Investments.png, Renewals.png, Valuations.png
```

**Logo Variants:**
```
ADU.png (primary), ADU_Light.svg, ADU_Blue.svg, ADU_Light.png, ADU_MultiColors.svg
```

Note: Some SVGs have both spaced names ("Property Owners.svg") and underscored names ("Property_Owners.svg"). The nav uses underscored versions.

---

## 12. AUDIT COMMANDS — RUN THESE FIRST

```bash
cd /Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects

# 1. Count all HTML files
echo "=== HTML FILE COUNT ==="
find . -name "*.html" -type f -not -path "./samples/*" | wc -l

# 2. Check for shared CSS/JS
echo "=== SHARED ASSETS ==="
ls -la homebody_shared.css homebody_header.js homebody_header.html 2>/dev/null

# 3. BANNED COLOR CHECK
echo "=== BANNED #003039 ==="
grep -rl "#003039" --include="*.html" --include="*.css" --include="*.js" . 2>/dev/null | wc -l

# 4. Old colors still present
echo "=== OLD COLORS ==="
grep -rl "#2c3e50\|#6b8e4e\|#e8e4df\|#6b8fa3" --include="*.html" --include="*.css" . 2>/dev/null | wc -l

# 5. Correct colors present
echo "=== CORRECT COLORS ==="
grep -rl "#3A5566" --include="*.html" --include="*.css" . 2>/dev/null | wc -l
grep -rl "#CBB279" --include="*.html" --include="*.css" . 2>/dev/null | wc -l

# 6. Branding
echo "=== BRANDING ==="
echo "CASTLEHOLD in nav/title:"
grep -rl "CASTLEHOLD" --include="*.html" . 2>/dev/null | wc -l
echo "Homebody Projects:"
grep -rl "Homebody Projects" --include="*.html" . 2>/dev/null | wc -l

# 7. Logo references
echo "=== LOGO ==="
echo "Castle logo:"
grep -rl "castlehold-logo" --include="*.html" . 2>/dev/null | wc -l
echo "ADU.png:"
grep -rl "ADU.png" --include="*.html" . 2>/dev/null | wc -l

# 8. Shared header usage
echo "=== SHARED HEADER ==="
grep -rl "site-header\|homebody_header" --include="*.html" . 2>/dev/null | wc -l

# 9. Nav structure check (via shared header)
echo "=== NAV STRUCTURE (homebody_header.js) ==="
grep -c "WHO WE SERVE\|who-we-serve" homebody_header.js 2>/dev/null
grep -c "EXPLORE\|explore" homebody_header.js 2>/dev/null
grep -c "BUILD\|build" homebody_header.js 2>/dev/null
grep -c "DATA\|data" homebody_header.js 2>/dev/null
grep -c "RESOURCES\|resources" homebody_header.js 2>/dev/null
grep -c "PRICING\|pricing" homebody_header.js 2>/dev/null
grep -c "ABOUT\|about" homebody_header.js 2>/dev/null

# 10. Map pages check
echo "=== MAP PAGES ==="
for f in dadu_eligibility_map.html property_search.html permit_explorer.html; do
  [ -f "$f" ] && echo "$f: EXISTS" || echo "$f: MISSING"
done

# 11. Merge conflict markers
echo "=== MERGE CONFLICTS ==="
grep -rl "<<<<<<\|>>>>>>" --include="*.html" . 2>/dev/null || echo "NONE"

# 12. Git status
echo "=== GIT ==="
git status --short | head -20
git log --oneline -5

# 13. GeoJSON references that need replacing with live ArcGIS layers
echo "=== GEOJSON REFS TO REPLACE ==="
grep -rl "\.geojson\|\.json.*FeatureCollection\|fetch.*\.geojson" --include="*.html" --include="*.js" . 2>/dev/null || echo "NONE"
```

---

## 13. DEVELOPMENT ENVIRONMENT

```bash
# Activate Python environment
source ~/dadu_env/bin/activate

# File locations
/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects/           # Repo root
/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects/DADU/      # Data folder
/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects/DADU/FINAL_FINAL/  # Latest datasets
```

---

## 14. KEY STATISTICS

| Metric | Value |
|--------|-------|
| Total Nashville Parcels | 285,512 |
| BL2025-1007 Eligible (USD) | 67,707 |
| Historic DADU Permits | 827 |
| RE Data ADU Permits | 4,122 |
| Unique Contractors | 393 |
| Legal Citations in Database | 111 |
| Parcels with Covenants | 43,000+ |
| HTML Pages on Site | 87 (36 linked in nav, 17 unlinked worth keeping, 25 duplicate candidates for deletion) |

---

## 15. SCOPE BOUNDARIES

**DO:**
- Keep it functional and polished
- Fix branding, maps, and Property Report Card first
- Use client-side JavaScript for GitHub Pages compatibility
- Load data on demand, not at page load
- Paginate ArcGIS queries

**DO NOT:**
- Use emoji for icons -- NEVER. Use PNG icons from assets/icons/ or plain text.
- Use any logo other than assets/icons/ADU.png
- Use #003039 anywhere (BANNED)
- Use ochre (#C58B2A), old amber (#D4A017), or old oxide red (#7A2A1D)
- Use neon, bright, or saturated colors on maps (no traffic-light styling)
- Use the castle logo (use ADU.png)
- Write "CASTLEHOLD" in nav bars or page titles (use "Homebody Projects")
- Introduce teal, green accent, terracotta, or any non-palette colors
- Load huge GeoJSON at initial page load
- Expose API keys in the repo
- Delete, rename, or move existing files
- Create "Developer/Investor" user type
- Nav label for contractor_dashboard.html is "Find a Contractor" in the BUILD dropdown. "Contractor Marketplace" stays as the label for contractor_marketplace.html in EXPLORE.
- Change basemaps on any map page without explicit permission
- Load GeoJSON files from the repo for map rendering (use live ArcGIS layers instead)

---

## 16. EXECUTION ORDER

```
Step 1:  ✅ DONE — Run audit (Section 12)
Step 2:  ✅ DONE — Kill #003039 (0 files remaining)
Step 3:  ✅ DONE — Fix shared header: nav reorganized, logo fixed, branding fixed
Step 4:  ✅ DONE — Delete obsolete pages (15 deleted), consolidated Form Wizard
Step 5:  ✅ DONE — Clean repo (5.9GB GeoJSON removed, .gitignore updated)
Step 6:  ✅ DONE — ArcGIS layer migration (14 files, js/arcgis-services.js registry)
Step 7:  ✅ DONE — Phase 2 data connections (contractor_stats, apn_to_account, gdrive_docs_index)
Step 8:  PENDING — Delete 26 identified duplicate pages (awaiting user confirmation)
Step 9:  ✅ DONE — Branding sweep complete (47 files: old colors, Montserrat→Inter, Castlehold→Homebody Projects titles)
Step 10: ✅ DONE — Map pages audited: all 8 have proper height, CDN libs, ArcGIS URLs
Step 11: PENDING — Test Property Report Card external links
Step 12: PENDING — Test Document Portal search end-to-end
Step 13: PENDING — Test Contractor Marketplace data display
Step 14: DONE — Homepage refreshed: 7 broken links fixed, icons updated, section backgrounds corrected
Step 15: PENDING — Fill placeholder/stub pages
Step 16: PENDING — Final testing: all nav links render correctly on live site
```

---

*End of instructions. Version 5.0 — Updated Feb 14, 2026. This is the single source of truth. When in doubt, follow this document. If you see #003039 anywhere, replace it with #3A5566. The navigation source of truth is homebody_header.js.*
