# HOMEBODY PROJECTS — CLAUDE CODE INSTRUCTIONS
**Version:** 4.0 | **Date:** February 14, 2026
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
- **File:** `assets/icons/ADU.png` (house icon)
- Display at ~42px height in nav bar
- Brand text "Homebody Projects" next to the logo: white, Inter, weight 700
- **DO NOT USE** the old castle logo (castlehold-logo.png) or castle SVG

---

## 4. NAVIGATION STRUCTURE

### Top Bar Layout
```
HOMEBODY PROJECTS LOGO (ADU.png) | EXPLORE ▾ | DASHBOARD ▾ | FEATURED TOOLS ▾ | WHO WE SERVE ▾ | RESOURCES ▾ | PRICING | ABOUT | [Am I Eligible? →]
```

Nav bar: background #3A5566, height 64px, Inter font.
Nav links: color #E1D4BB, weight 600, 14px. Hover: color white, background #496778.
Logo: ADU.png at ~42px height, far left, with "Homebody Projects" text.
"Am I Eligible?" button: far right, background #CBB279, text #3A5566, weight 700, border-radius 8px. Links to am_i_eligible.html. This is the primary CTA visible on every page.

### Dropdown Icon Style
Each dropdown item with an icon should show the PNG icon at 32-40px, clearly visible next to the label. Icons sit in a #F0EBE1 (Linen) circle background, 48px diameter. The previous version made icons too small and hard to see. Make them prominent.

### Routing
- LOGO → index.html
- PRICING → homebody_dadu_pricing.html (no dropdown)
- ABOUT → about.html (no dropdown)

---

### EXPLORE Dropdown

**Section: INTERACTIVE MAP** (Icon: Area_Maps_and_Visual_layers.png)

| Label | Icon | File |
|-------|------|------|
| Property Search | Parcel_Search.png | property_search.html |
| Eligibility Map | Zoning.png | dadu_eligibility_map.html |
| DADUs Near Me | Neighbors.png | dadu_near_me_v2.html |

Eligibility Map note: Full parcel map colored by eligibility status (Eligible = #406A64 outline, Conditional = #918A83 outline, Not Eligible = #B58676 outline).

**Section: DOCUMENT DATABASE** (Icon: Recorded_Docs.png)

| Label | Icon | File |
|-------|------|------|
| Approved Site Plans | — | site_plan_downloads.html |
| Design Documents | — | dadu_documents_portal.html |
| DADU Footprint Cards | — | footprint_cards.html |

---

### DASHBOARD Dropdown

| Label | Icon | File |
|-------|------|------|
| Permit Activity | — | permit_activity_dashboard.html |
| Contractor Marketplace | Building_and_Construction.png | contractor_marketplace.html |
| Upcoming DADU Legislation | Legal.png | dadu_legislation.html |

---

### FEATURED TOOLS Dropdown

**Section: Report Generators** (Icon: Exports__Reports.png)

| Label | File |
|-------|------|
| Property Detail Report | property-report-card.html |
| Eligibility Report | eligibility_report.html |
| Contractor Report | dadu_reports_store.html |

**Section: Interactive Planners**

| Label | File |
|-------|------|
| Project Planner | project_planner.html |
| Interactive Checklist | project_checklist.html |

**Section: Form Wizard**

| Label | File |
|-------|------|
| Determine Forms Required | determine_forms_required.html |
| Form Filler | legal_form_filler.html |

**Section: PROJECT CALCULATORS** (Icon: Appraisers.png)

| Label | File |
|-------|------|
| Project Cost Estimator | project_cost_estimator.html |
| DADU Size Calculator | size_calculator.html |
| ROI Calculator | roi_calculator.html |
| Property Tax Calculator | property_tax_calculator.html |

---

### WHO WE SERVE Dropdown

| Label | Icon | File |
|-------|------|------|
| Homeowners | Property_Owners.png | user-homeowners.html |
| Contractors | Building_and_Construction.png | contractor_marketplace.html |
| Designers / Architects | Surveyors_and_Engineers.png | designer_resources.html |
| Municipal & Local Agencies | Municipal.png | municipal_dashboard.html |
| Legal Professionals | Legal.png | legal_resources.html |

---

### RESOURCES Dropdown

| Label | File |
|-------|------|
| What is a DADU? | what_is_dadu.html |
| General Requirements | dadu_building_requirements.html |
| Metro Code & Legislation | dadu_code_legislation_v3.html |
| Zoning Standards and Documents | dadu_zoning_standards.html |
| Short Term Rental Permit | str_permit.html |
| Owner Occupancy Requirements | owner_occupancy.html |

---

### PRICING
Direct link to homebody_dadu_pricing.html. No dropdown.

### ABOUT
Direct link to about.html. No dropdown.

---

## 5. CURRENT STATE — WHAT EXISTS

### Shared Components
- `homebody_shared.css` — Global stylesheet with :root color variables
- `homebody_header.js` — Shared nav component injected via `<div id="site-header"></div>`
- `homebody_header.html` — Shared header template

### Live Pages (~95+ HTML files)
The site is deployed at https://nataliebaldacci.github.io/DADU-Homebody-Projects/

**Homepage:** index.html

**Maps & Explorers (20 files):**
dadu_eligibility_map.html, parcel_footprint_map.html, property_search.html, dadu_explorer.html (+ v2, v3), dadu_explorer_attom.html (+ v2), dadu_near_me.html (+ v2, locator), dadu_property_viewer_v3.html, dadu_property_explorer.html (+ v2, v3), dadu_opportunity_explorer_v2.html, adu_opportunity_explorer.html, nashville_permit_explorer_v3.html, adu_permit_map.html, secondary_structures_map.html

**Calculators & Planning (8 files):**
roi_calculator.html, project_cost_estimator.html, property_tax_calculator.html, size_calculator.html, project_checklist.html, project_planner.html, draw_dadu_on_parcel.html, site_plan_downloads.html

**Reports & Pricing (5 files):**
eligibility_report.html, project_report.html, dadu_reports_store.html, reports_pricing.html, homebody_dadu_pricing.html

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
Multiple v1/v2 duplicates. Do not delete these but do not link to them in navigation.

---

## 6. WHAT NEEDS TO BE FINISHED — PRIORITY ORDER

### PRIORITY 1: Fix Branding Consistency Across All Pages
**Status:** Partially done. Many pages still have old colors and wrong brand names.

**Tasks:**
1. Find and replace BANNED color #003039 with #3A5566 in every file
2. Find and replace all old colors (see Section 3 replacement table)
3. Ensure every page loads `homebody_shared.css` and uses CSS variables
4. Verify the shared header (homebody_header.js) is injected on every page
5. Replace "CASTLEHOLD" with "Homebody Projects" in nav bars and page titles
6. Replace castle logo references with `assets/icons/ADU.png`
7. Castlehold name stays ONLY on reports, data attribution, legal pages, and footer "Powered by" line

**Verification commands:**
```bash
# Find BANNED color
grep -rl "#003039" --include="*.html" --include="*.css" --include="*.js" . | wc -l

# Find old colors
grep -rl "#2c3e50\|#6b8e4e\|#e8e4df\|#6b8fa3\|#c9a86c" *.html | wc -l

# Find pages missing shared CSS
for f in *.html; do grep -qL "homebody_shared.css" "$f" && echo "MISSING CSS: $f"; done

# Find pages still saying CASTLEHOLD in nav/title
grep -l "CASTLEHOLD" *.html
```

### PRIORITY 2: Fix Broken Maps
**Status:** ArcGIS layer URLs have been migrated (see below). Maps may still render blank due to CSS/height issues or basemap changes. Test each page.

**COMPLETED — ArcGIS Layer Migration (Feb 2026):**
14 files updated to use new Feb 2026 ArcGIS feature services. Zero old service URLs remain in any .html or .js file.

| Old Service | New Service | Type |
|-------------|-------------|------|
| DADU_Eligibility_ENHANCED_20260119 | Eligibility_Enhanced_Polygons_20260213 | Polygons, 96 fields |
| DADU_Building_Specs_20260119 | Building_Specs_Polygons_20260213 | Polygons, 45 fields |
| Footprints_With_ParcelData_20260118 | Footprints_Trimmed_20260213 | Polygons, 54 fields |
| Building_Footprints_SingleFamily | Footprints_Trimmed_20260213 | Polygons, 54 fields |

Shared registry (`js/arcgis-services.js`) now includes all 6 new services including Parcels_Building_Info_20260213 (89 fields) and eligibility_parcels (lightweight).

**Files touched:** am_i_eligible, property-report-card, dadu_eligibility_map, property_search, permit_explorer, dadu_property_viewer_v3, dadu_symbium_map, dadu_build_tool, dadu_build_explorer_v2, dadu_property_report, dadu_explorer_attom_v2, homebody_index_map, footprints_proof_of_concept, dadu_build_tool_backup

**STILL TO DO:**
1. Verify maps actually render on the live site (not just that URLs are correct)
2. Check that map containers have explicit height set
3. Check that Leaflet/ArcGIS JS libraries load from CDN
4. Confirm basemaps were not changed (a previous session changed them without permission)
5. Test the eligibility map (dadu_eligibility_map.html) — most important map
6. Test property search map (property_search.html)
7. DO NOT change basemaps without asking

### PRIORITY 3: Property Report Card (Core Product Spine)
**Status:** Page exists (property-report-card.html) but external links need correct field mapping.

**Tasks:**
1. Implement all external link builders:
   ```
   Parcel Viewer:     https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}
   Print Record:      https://maps.nashville.gov/ParcelViewer/PrintRecord.html?pin={PIN}
   Permit Docs:       https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}
   Parcel Docs:       https://documents.nashville.gov/Request/Form/PermitCodes?parcelnumber={APN}
   ePermits:          https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}
   Assessor:          https://davidson-tn-citizen.comper.info/template.aspx?propertyID={APN}
   Property Card:     https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
   ```
2. Use `assessor_accounts_20260114.csv` to map APN → ACCOUNTNUMBER
3. Show building footprints on the report card map
4. Display permit history for the parcel
5. Show restrictive covenant status and link to covenant documents

### PRIORITY 4: Document Portal Enhancement
**Status:** dadu_documents_portal.html exists but needs working search.

**Tasks:**
1. Create `data/docs_index.json` by scanning local PDF folders
2. Extract APN from filenames using regex for 10-12 digit sequences
3. Normalize APNs to 11 digits with left-padding zeros
4. Build searchable portal with filters: APN, address, document type, permit number

### PRIORITY 5: Contractor Marketplace Data Connection
**Status:** Page exists with hardcoded data. Needs live data connection.

**Tasks:**
1. Load contractor data from DADU_All_Permits_Cleaned.csv
2. Aggregate: permit count per contractor, average cost per sqft, project locations
3. Fields with data: CONTRACTOR_BIZ_NAME_ORIGINAL, CONTRACTOR_LICENSE
4. Other contractor fields are mostly empty — do not rely on them

### PRIORITY 6: Near Me Locator
**Status:** Multiple versions exist. Need to consolidate to one working version.

### PRIORITY 7: Missing Page Content
**Status:** Many pages are placeholder stubs. Need real content.

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
| Cost Estimator | Exports__Reports.png | Estimate build costs by size, finish level, and site conditions. | project_cost_estimator.html |
| Contractor Directory | Building_and_Construction.png | Connect to vetted builders specializing in ADUs on your sized lot. | contractor_marketplace.html |

Each card: #f5f5f0 background, #E2E2E0 border, icon in #F0EBE1 circle, heading #3A5566, body #706F6C, "Learn More →" link

### SECTION 3: ALL-IN-ONE PLATFORM FEATURES
- **Background:** white
- **Heading:** "All-In-One DADU Platform Features" — #3A5566, serif, italic
- **Feature grid (cards or icon+text blocks):**

| Feature | Icon | Link |
|---------|------|------|
| Explore Interactive Maps | Area_Maps_and_Visual_layers.png | dadu_eligibility_map.html |
| Planning Projects | — | project_planner.html |
| Form Wizard | — | determine_forms_required.html |
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
| Municipal | Municipal.png | Permit tracking, policy analysis, compliance monitoring. | municipal_dashboard.html |
| Legal Professionals | Legal.png | Covenant research, title issues, zoning compliance, and legal citations database. | legal_resources.html |

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
| Recorded Documents | dadu_documents_portal.html |
| Permits & Site Plans | site_plan_downloads.html |
| Direct External Links to Metro Code | (external Nashville links) |
| Codes and Legislation | dadu_code_legislation_v3.html |
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

| Tool | Description |
|------|-------------|
| ROI Calculator | Return on investment based on build cost and rental income |
| Project Cost Estimator | Estimate by size, finish level, and site conditions |
| Property Tax Increase Calculator | Estimate property tax impact of DADU |
| Size Calculator | Max DADU size based on lot (< 10K SF = 700/750; ≥ 10K = 850/1,000) |
| Short Term Rental Permit ROI | ROI if used as short-term rental |
| Project Planner / Checklist | Step-by-step project management |
| Permit Process Timeline | Step-by-step permitting guide |
| Draw DADU on Parcel | Visual placement tool |
| Am I Eligible? | Address-based eligibility check/flowchart |
| What Can I Build? | Size limits based on lot and zoning |
| Determine Forms Required | Forms wizard step 1 |
| Legal Form Filler | Forms wizard step 2 |

### Learn and Reference Pages

| Page | Content |
|------|---------|
| What is a DADU? | Educational introduction |
| DADU History & Timeline | Legislative history |
| Building Requirements | Setbacks, height, lot coverage |
| Zoning Standards | R, RS, SP zone rules |
| Design Standards | Overlay design requirements |
| Code & Legislation Database | 111+ legal citations, Bluebook format |
| Overlay Districts | UDO, DADU, SP overlays with ordinance links |
| Owner Occupancy | Requirement explanation and forms |
| Short Term Rental Permits | STR eligibility for DADUs |
| Trade Permits | Required trade permits for construction |
| Common Issues | Flag patterns from T_Permits_With_Issue_Flags.csv |

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

Each user type gets a dedicated landing page with explanation, CTA, how it works, data sources, FAQ, and related tools:

| User Type | Core Needs |
|-----------|-----------|
| Homeowners | Eligibility check, what can I build, near me, property viewer, cost/ROI calculators, covenant check |
| Contractors/Builders | Permit explorer, market analytics, top contractors leaderboard, leads, pricing benchmarks, territory analysis |
| Designers/Architects | Requirements database, precedent gallery, site analysis tools, setback calculators |
| Municipal/Government | Permit tracking, impact analysis (pre/post BL2025-1007), compliance monitoring |
| Legal/Appraisers | Recorded documents, covenant checks, comparables placeholder, valuation data |

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

**February 14, 2026 — Updated navigation to EXPLORE | DASHBOARD | FEATURED TOOLS | WHO WE SERVE | RESOURCES | PRICING | ABOUT**

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
├── homebody_header.js            # Shared nav component
├── homebody_header.html          # Header template
├── /assets/
│   ├── /css/                     # Additional stylesheets
│   ├── /js/                      # Shared JavaScript modules
│   └── /icons/                   # PNG icons for nav/cards (ADU.png is here)
├── /data/                        # JSON indexes, local GeoJSON
├── /docs/                        # PDF documents
├── /samples/                     # Design reference (DO NOT MODIFY)
├── /sample_reports/              # Sample report previews
├── [95+ HTML pages at root]
├── /DADU/                        # Data folder
│   ├── /FINAL_FINAL/             # Latest processed datasets
│   ├── /MASTER_ADU_DATA/         # Consolidated analysis files
│   ├── /All_Icons/               # Icon source files
│   ├── /Permit_PDFs_Downloaded/
│   ├── /Property_Cards_Downloaded/
│   ├── /Property_Cards_2_Assessor/
│   └── /Restrictive_Covenants/
└── /Scripts/                     # Python processing scripts
```

### Available PNG Icons
Path: `/Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects/assets/icons/`
Web path: `assets/icons/FILENAME.png`
**EMOJI ARE BANNED SITE-WIDE.** If no PNG exists, use text only.
Make icons prominent. Previous AI session made them too small.
```
ADU.png, Parcel_Search.png, Property_Owners.png, Building_and_Construction.png,
Zoning.png, Recorded_Docs.png, Exports__Reports.png, GIS.png,
APN_Maps.png, Area_Maps_and_Visual_layers.png, Investors.png,
Appraisers.png, Surveyors_and_Engineers.png, Municipal.png,
Utilities.png, Legal.png, Farming.png, Bulk_data.png
```

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

# 9. Nav structure on index.html
echo "=== NAV STRUCTURE ==="
grep -c "EXPLORE\|explore" index.html 2>/dev/null
grep -c "DASHBOARD\|dashboard" index.html 2>/dev/null
grep -c "FEATURED TOOLS\|featured-tools" index.html 2>/dev/null
grep -c "WHO WE SERVE\|who-we-serve" index.html 2>/dev/null
grep -c "RESOURCES\|resources" index.html 2>/dev/null
grep -c "PRICING\|pricing" index.html 2>/dev/null
grep -c "ABOUT\|about" index.html 2>/dev/null

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
| HTML Pages on Site | 95+ |

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
- Use "Contractor Finder" (use "Contractor Marketplace" only)
- Change basemaps on any map page without explicit permission
- Load GeoJSON files from the repo for map rendering (use live ArcGIS layers instead)

---

## 16. EXECUTION ORDER

```
Step 1:  Run audit (Section 12) — show output before doing anything
Step 2:  Kill #003039 — replace with #3A5566 in every file
Step 3:  Fix branding — replace old colors, CASTLEHOLD → Homebody Projects, castle logo → ADU.png
Step 4:  Fix shared header — verify locked nav on all pages
Step 5:  Fix maps — debug blank rendering, connect data layers
Step 6:  Wire Property Report Card — all external link builders working
Step 7:  Document portal — build docs_index.json, enable search
Step 8:  Contractor marketplace — connect to real permit data
Step 9:  Near Me locator — consolidate to one working version
Step 10: Fill placeholder pages
Step 11: Test all nav links — ensure every href target exists
```

---

*End of instructions. This is the single source of truth. When in doubt, follow this document. If you see #003039 anywhere, replace it with #3A5566.*
