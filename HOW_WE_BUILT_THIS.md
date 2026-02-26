# How We Built Homebody Projects

**A complete reference for how this website was designed, built, and maintained.**
**Author:** Natalie Baldacci, Vanderbilt Law School J.D. 2026
**Built with:** Claude Code (Anthropic) + Canva + ArcGIS Online
**Deployed on:** GitHub Pages (static, client-side only)
**Live:** https://nataliebaldacci.github.io/DADU-Homebody-Projects/

---

## What This Is

Homebody Projects is a DADU (Detached Accessory Dwelling Unit) eligibility and planning platform for Nashville-Davidson County. It aggregates public parcel data, permit records, restrictive covenants, and regulatory information into a static website. Nashville's BL2025-1007 legislation (effective December 12, 2025) expanded DADU eligibility to 67,707 parcels.

**Two brand layers:**
- **Homebody Projects / Homebody Builder** = consumer-facing (nav, pages, tools)
- **Castlehold** = data/authority layer (reports, footer "Powered by" lines, About page)

---

## Architecture

### Stack
- **Frontend:** Vanilla HTML/CSS/JavaScript (no frameworks)
- **Hosting:** GitHub Pages (static files, no server)
- **Maps:** ArcGIS JavaScript SDK + Esri Feature Services (Vanderbilt ArcGIS Online)
- **Data:** JSON files served from `/data/` folder, ArcGIS REST API queries
- **Design:** Canva (custom icons), hand-coded SVG refinements via Claude Code
- **Version Control:** Git/GitHub, single `main` branch

### Why No Framework
GitHub Pages serves static files. All data loading is client-side via `fetch()` to ArcGIS REST endpoints or local JSON files. No build step, no bundler, no npm. Every HTML page is self-contained with inline `<style>` and `<script>` blocks plus shared CSS/JS includes.

### Shared Components
```
homebody_shared.css    — Global stylesheet with :root CSS variables
homebody_header.js     — Shared nav component (THE source of truth for navigation)
homebody_header.html   — Static header template (must match .js)
js/arcgis-services.js  — Shared ArcGIS service URL registry
```

Every page includes:
```html
<link rel="stylesheet" href="homebody_shared.css">
<div id="site-header"></div>
<script src="homebody_header.js"></script>
```

The nav is injected by `homebody_header.js` into the `#site-header` div on page load.

---

## Design System

### Color Palette (Locked)

The palette is architectural and muted. No bright/saturated colors. No traffic-light styling. One accent color only.

**Core Darks:**
| Name | Hex | Role |
|------|-----|------|
| True Dark Anchor | `#2F3A45` | Hero gradient base, footer, selected footprint |
| Deep Slate (Brand) | `#3A5566` | Nav, headings, brand authority, parcel strokes |
| Gray Azure | `#4C5C66` | Alternate dark, active permit markers |
| Medium Slate | `#496778` | Hover states, secondary elements |

**Mid Neutrals:**
| Name | Hex | Role |
|------|-----|------|
| Warm Stone | `#7B746D` | Secondary text, pill borders, dots in icons |
| Warm Muted UI | `#A59D8B` | Mid-tone, muted UI elements |

**Single Accent:**
| Name | Hex | Role |
|------|-----|------|
| Wheat | `#CBB279` | CTA buttons, stat numbers, highlights |

**Neutrals:**
| Name | Hex | Role |
|------|-----|------|
| Cream | `#E1D4BB` | Body text on dark backgrounds |
| Linen | `#F0EBE1` | Section backgrounds, icon circle backgrounds |
| Warm Light | `#F2F0ED` | Page background |
| Off-White | `#F5F5F0` | Card surfaces |

**Functional (Map Status):**
| Status | Hex | Description |
|--------|-----|-------------|
| Eligible | `#406A64` | Muted slate-teal |
| Conditional | `#918A83` | Gray |
| Not Eligible | `#B58676` | Muted clay |

**BANNED:** `#003039` (reads as green), any neon/bright/saturated colors, terracotta, sage, teal, ochre.

### Typography
- **Body:** Inter (primary), system sans-serif fallback
- **Headlines:** Source Serif 4 (or Georgia), weight 700, italic
- No Montserrat (was removed in branding sweep)

### Logo
- `assets/icons/ADU.png` — primary dark house icon
- `assets/icons/ADU_Light.svg` — white variant for dark nav
- `assets/icons/ADU_MultiColors.svg` — multicolor variant (currently used in nav)
- Never use the old castle logo

---

## Icon System (ParcelQuest Style)

### Design Philosophy

All custom nav icons follow ParcelQuest's two-color style. The key insight:

> **Dots REPLACE content where lines/text would normally be.** They don't just decorate. Dots ARE the information — replacing text lines, grid cells, labels, and data rows. This is what makes the icons distinctive.

### Icon Specs
- **Viewbox:** 28x28
- **File size:** ~1-2KB per SVG
- **Colors:** Exactly 3:
  - `#3A5566` (Deep Slate) — structural shapes, outlines, fills
  - `#7B746D` (Warm Stone) — dots (content replacement)
  - `#F5F5F0` (Off-White) — cutouts, negative space
- **No emoji anywhere on the site.** This is absolute.

### Version History

4 dot-style versions were created for comparison:

| Version | Approach |
|---------|----------|
| V1 | Full detail + 2-column diminishing dots outside figure |
| V2 | Full detail + small 4-dot cluster outside |
| V3 | Dots placed inside figures as texture/fill |
| V4 | Dots replace lines/text content (true PQ style) |
| V5 | Custom hybrids combining best elements |

User selected mostly V3 (dots as internal texture) and V4 (dots replace content), with two V5 hybrids (Permit Approval, Project Report).

### Icon Inventory (38 custom SVGs)

All icons live in `assets/icons/`. Version folders (`_v2/`, `_v3/`, `_v4/`, `_v5/`) are preserved for reference.

**Nav icons (every item has a unique icon):**
```
Property_Owners.svg         — Homeowners
Building_and_Construction.svg — Contractors (only use)
Surveyors_and_Engineers.svg — Designers & Architects
Municipal.svg               — Municipal & Agencies
Legal.svg                   — Legal Professionals
Area_Maps_and_Visual_layers.svg — Interactive Maps (col header)
Zoning.svg                  — Eligibility Map
Parcel Search.svg           — Property Search
ADU.png                     — Existing DADUs
Permit_Explorer.svg         — Permit Explorer Map
Neighbors.svg               — DADUs Near Me
Dashboard.svg               — Dashboards (col header)
Permit_Activity.svg         — Permit Activity
Contractor_Marketplace.svg  — Contractor Marketplace
Cost_Market.png             — Market Trends (Canva export)
Permit_Analytics.svg        — Permit Analytics
Project_Planner.svg         — Plan My Project (col header)
Build_DADU.svg              — Build My DADU
Checklist_.svg              — Planning Hub
Draw_DADU.svg               — Draw DADU on Parcel
Permit_Timeline.svg         — Permit Process Timeline
Appraisers.svg              — All Calculators
Form_Wizard.svg             — Form Wizard
Exports__Reports.svg        — Research (col header) + Report Generator
Permit_Site_Plans.svg       — Find Site Plans
External_Links.svg          — External Links
Document_Database.svg       — PDF Database
Find_Contractor.svg         — Find a Contractor
Recorded_Docs.svg           — Learn (col header)
What_is_DADU.svg            — What is a DADU?
General_Requirements.svg    — General Requirements
Eligibility_Check.svg       — Eligibility Flowchart
DADU_History.svg            — DADU History
Legislation.svg             — Code & Legislation
GIS.svg                     — ArcGIS Maps
Permit_Approval.svg         — Permits & Forms (col header)
Owner_Occupancy.svg         — Owner Occupancy
STR_Permit.svg              — Short Term Rental Permit
Trade_Permits.svg           — Required Trade Permits
Zoning_Documents.svg        — Overlay Districts
Restrictive_Covenants.svg   — Restrictive Covenants
Overlay_Design_Standards.svg — Design Standards
```

### Canva vs Hand-Coded Icons

Some icons were designed in Canva and exported. Canva SVG exports are bloated (270-315KB due to C2PA certificate metadata, 20+ clipPaths). Two approaches:

1. **PNG export** — Use for complex Canva designs (e.g., Cost_Market.png)
2. **Hand-coded SVG** — Recreate the design in clean SVG (~1-2KB). Better for simple shapes.

SVGO only reduces Canva SVGs by ~7%, so hand-coding or PNG is always preferred.

---

## Navigation Structure

The nav is defined in `homebody_header.js`. This is the SINGLE SOURCE OF TRUTH. `homebody_header.html` is a static mirror that must stay in sync.

### Layout
```
LOGO | WHO WE SERVE ▾ | EXPLORE ▾ | BUILD ▾ | RESOURCES ▾ | PRICING | ABOUT | [Am I Eligible? →]
```

- **WHO WE SERVE:** `dropdown-single` (flat list, 5 items)
- **EXPLORE:** `mega-menu-2` (2 columns: Interactive Maps + Dashboards)
- **BUILD:** `mega-menu-2` (2 columns: Plan My Project + Research)
- **RESOURCES:** `mega-menu-2` (2 columns: Learn + Permits & Forms)
- **PRICING:** direct link
- **ABOUT:** direct link

### Dropdown Icon Style
Each item shows an SVG/PNG icon at 32-40px in a `#F0EBE1` (Linen) circle background, 48px diameter.

---

## Data Architecture

### Local JSON Files (in `/data/`)
| File | Size | Records | Purpose |
|------|------|---------|---------|
| `apn_to_account.json` | 6.6MB | 277K | APN → ACCOUNTNUMBER mapping |
| `gdrive_docs_index.json` | 8.9MB | 18,782 docs | Google Drive document index |
| `contractor_stats.json` | 179KB | 370 contractors | Contractor statistics |
| `master_parcel_data.json` | 6.4MB | 868 parcels | Master parcel dataset |
| `address_search_index.json` | — | — | Address typeahead |
| `adu_permits_slim.json` | — | — | Slim ADU permit data |

### ArcGIS Feature Services
All map data comes from Vanderbilt's ArcGIS Online at `services3.arcgis.com/58WV6GqBWodG9Kll/`. These are CORS-friendly from GitHub Pages.

**Critical:** `maps.nashville.gov` is CORS-blocked from GitHub Pages. Use local JSON or Vanderbilt ArcGIS endpoints instead.

Key layers:
- **Eligibility:** DADU_Eligibility_ENHANCED (161,703 records, TABLE — no geometry)
- **Parcels:** Eligibility_Enhanced_Polygons (has geometry)
- **Permits:** DADU_All_Permits_MERGED_v2 (point + polygon)
- **Footprints:** Footprints_With_ParcelData (building outlines)
- **Covenants:** Parcels_with_Restrictive_Covenants (43,711 parcels)

Always paginate ArcGIS queries (handle maxRecordCount with resultOffset/resultRecordCount loops).

### Nashville External Links
```
Parcel Viewer:  https://maps.nashville.gov/ParcelViewer/?parcelID={STANPAR}
Permit Docs:    https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}
ePermits:       https://epermits.nashville.gov/?#/?searchCode=PRMT={PERMIT_NUMBER}
Property Card:  https://portal.padctn.org/OFS/WP/Print/{ACCOUNTNUMBER}
```

---

## Build Process (How It Was Made)

### Phase 1: Data Foundation (January 2026)
1. Extracted 327,829 building footprints from Nashville ArcGIS
2. Cross-referenced 5 ADU indicator sources across 284,425 parcels (98.9% accuracy)
3. Downloaded 8,514 restrictive covenant PDFs, 630 permit PDFs, 3,358 property cards
4. Built eligibility dataset: 67,707 eligible parcels
5. Uploaded all datasets to Vanderbilt ArcGIS Online

### Phase 2: Website Build (February 5-6, 2026)
1. Built 95+ HTML pages using Claude Code
2. Created mega-menu navigation structure
3. Implemented shared header component (`homebody_header.js`)
4. Connected to ArcGIS Feature Services for live map data

### Phase 3: Branding & Polish (February 10-15, 2026)
1. Locked color palette (no traffic-light colors, architectural muted tones)
2. Replaced all Montserrat → Inter font references (30 files)
3. Fixed all old palette colors (9 files)
4. Fixed all Castlehold → Homebody Projects branding (32 titles)
5. Deleted 49 obsolete/duplicate pages (87 → 77 HTML files)
6. Removed 5.9GB of GeoJSON from git tracking
7. Created shared ArcGIS registry (`js/arcgis-services.js`)
8. Built Phase 2 data files (apn_to_account, contractor_stats, etc.)
9. Fixed all maps: eligibility toggles, existing DADUs gallery, near me
10. Connected dashboards to real ArcGIS data
11. Rewrote eligibility flowchart with homeowner-friendly questions

### Phase 4: Icon System (February 25-26, 2026)
1. Replaced all Lucide/generic icons with custom ParcelQuest-style SVGs
2. Created 4 version folders for comparison (V1-V4)
3. User selected favorites per icon
4. Created V5 hybrids for Permit Approval and Project Report
5. Eliminated all nav icon duplicates (every item has unique icon)
6. Created 7 new icons to resolve `Building_and_Construction.svg` being used 5x

---

## Key Rules for Future Work

1. **Never use emoji for icons.** Use SVG/PNG from `assets/icons/` or plain text.
2. **Never use `#003039`.** Replace with `#3A5566`.
3. **Never delete files** unless explicitly asked. Create new versions.
4. **`homebody_header.js` is the nav source of truth.** Always edit this file for nav changes.
5. **No GeoJSON in the repo.** Use live ArcGIS Feature Service URLs.
6. **No API keys in the repo.** Use serverless proxy if needed.
7. **Paginate ArcGIS queries.** Always handle maxRecordCount.
8. **Nashville servers rate limit.** Use 1-2 second delays, 30-second timeouts.
9. **Canva SVG exports are bloated.** Use PNG exports or hand-code clean SVGs.
10. **All map data from `services3.arcgis.com`** (Vanderbilt). Never `maps.nashville.gov` (CORS blocked).

---

## File Structure

```
/DADU-Homebody-Projects/
├── index.html                     # Homepage
├── homebody_shared.css            # Global stylesheet
├── homebody_header.js             # Shared nav (SOURCE OF TRUTH)
├── CLAUDE.md                      # Full project instructions (v5.2)
├── HOW_WE_BUILT_THIS.md          # This file
├── SESSION_ICONS_FEB26.md        # Icon session details
├── assets/
│   ├── icons/                     # All SVG + PNG icons
│   │   ├── _v2/ _v3/ _v4/ _v5/  # Icon version folders
│   │   └── _saved/               # Dashboard V1/V2 saved for future use
│   ├── css/                       # Additional stylesheets
│   └── js/                        # Shared JavaScript
├── js/
│   └── arcgis-services.js         # ArcGIS URL registry
├── data/                          # JSON data files
├── docs/                          # PDF documents
├── samples/                       # Design reference (READ ONLY)
├── sample_reports/                # Sample report previews
└── [77 HTML pages]                # 40 in nav, 37 unlinked/legacy
```

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Nashville Parcels | 285,512 |
| BL2025-1007 Eligible | 67,707 |
| Historic DADU Permits | 827 |
| Unique Contractors | 393 |
| HTML Pages on Site | 77 |
| Custom SVG Icons | 38+ |
| Data Files | 8+ JSON indexes |
| ArcGIS Feature Layers | 20+ |
| Pages Deleted (cleanup) | 49 |
| GeoJSON Removed | 5.9GB |

---

*Last updated: February 26, 2026*
