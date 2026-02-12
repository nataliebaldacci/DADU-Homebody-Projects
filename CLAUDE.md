# CLAUDE.md — Castlehold DADU Codebase Guide

## Project Overview

**Castlehold** is a Nashville-Davidson County DADU (Detached Accessory Dwelling Unit) zoning intelligence platform. It provides property owners, contractors, designers, and municipal staff with eligibility checking, permitting guidance, building requirements, and market analysis for DADUs under BL2025-1007.

This is a **static HTML/CSS/JavaScript web application** with no build tools, no bundler, and no package manager. All processing happens client-side in the browser.

## Tech Stack

- **Frontend:** Vanilla HTML, CSS, JavaScript (no frameworks)
- **Mapping:** Leaflet 1.9.4 + MarkerCluster 1.5.3 (loaded via CDN)
- **GIS Backend:** ArcGIS REST Feature Services (Vanderbilt-hosted + Nashville Metro)
- **Typography:** Montserrat (Google Fonts)
- **Data Processing:** Python 3 scripts in `/scripts/`
- **No npm, no TypeScript, no build step, no bundler**

## Repository Structure

```
/
├── *.html                    # ~110 HTML pages (all root-level)
├── homebody_header.html      # CRITICAL: shared navigation header (single source of truth)
├── homebody_header.js        # Header generation utility
├── homebody_shared.css       # Castlehold design system (CSS variables + shared styles)
├── index.html                # Homepage with eligibility checker
├── property_search.html      # Advanced parcel search & map
├── js/
│   └── arcgis-services.js    # ArcGIS REST API utilities (service URLs + query functions)
├── assets/
│   ├── castlehold-logo.png   # Brand logo
│   └── icons/                # 25+ navigation icons (PNG)
├── data/
│   ├── docs_index.json       # Document metadata (8MB)
│   ├── ordinance_index.json  # Legislation index
│   └── *.md                  # Matching rules documentation
├── scripts/
│   ├── build_document_indices.py
│   ├── build_gdrive_index.py
│   ├── build_ordinance_index.py
│   └── download_permit_pdfs.py
├── MASTER_ADU_DATA/
│   ├── parcels_eligibility_lite.json  # 22MB - all Nashville parcels
│   ├── PDF_Database_By_APN.json       # PDF-to-parcel mapping
│   ├── permits_for_map.json           # Permit locations
│   └── contractors_ranked.json        # Contractor rankings
├── sample_reports/            # 10 HTML report templates
├── *.geojson                  # Large spatial datasets (50-87MB each)
├── *.json                     # Pre-processed parcel/permit data (9-22MB each)
├── *.py                       # Root-level utility scripts
└── .gitignore
```

## Critical Files — Do Not Modify Without Care

| File | Why |
|------|-----|
| `homebody_header.html` | Shared header loaded by all 34+ pages. Changes propagate everywhere. |
| `homebody_shared.css` | Design system tokens. Changing CSS variables affects the entire site. |
| `js/arcgis-services.js` | Central ArcGIS service URL registry. All map pages depend on this. |

## Development Setup

```bash
# Serve locally (required for fetch/CORS to work)
python -m http.server 8000

# Open in browser
# http://localhost:8000/index.html
```

There is **no build step**. Edit HTML/CSS/JS files directly and refresh the browser. Do not introduce build tools, bundlers, or package managers without explicit approval.

## Shared Header System

All pages load the shared header via JavaScript fetch injection:

```html
<div id="homebody-header-container"></div>
<script>
    fetch('homebody_header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('homebody-header-container').innerHTML = data;
        });
</script>
```

**To update navigation**, edit only `homebody_header.html`. Changes automatically appear on all pages.

**To add a new page:**
1. Create the HTML file in the root directory
2. Add the header injection snippet above at the start of `<body>`
3. If the page belongs in navigation, add it to `homebody_header.html`

Pages in `sample_reports/` use a relative path: `fetch('../homebody_header.html')`.

## Navigation Architecture (Locked)

The navigation structure is intentionally locked. The four main sections are:

- **EXPLORE** — Learn (6 items), Discover (4 items), By Role (5 items)
- **BUILD** — Plan (3), Design (1), Calculate (4), Hire (1), File (4)
- **DATA** — Activity (3), Reports (7), Records (6)
- **PRICING** — Direct link (no dropdown)

Header actions: Search → `property_search.html`, My Projects → `project_planner.html`, Get Started → `am_i_eligible.html`

Developer/Investor is intentionally excluded from user types. Do not add it.

## Castlehold Design System

### CSS Variables (defined in `homebody_shared.css`)

```css
/* Brand Colors */
--navy: #3A5566;           /* Primary — Deep Slate */
--navy-dark: #2E4553;
--navy-light: #4A6B7D;
--terracotta: #C58B2A;     /* Accent — Ochre (buttons, CTAs) */
--terracotta-hover: #A8761F;
--tan: #7B746D;            /* Secondary — Warm Stone */
--background: #F2F0ED;     /* Page background */
--card-bg: #f5f5f0;
--error: #7A2A1D;          /* Oxide Red */
--status-eligible: #2E6F4E;

/* Castle Logo Colors */
/* Left castle (DADU): #D4C5A9, Right castle (main): #3A5566 */
/* Ground: #7B746D, Windows/doors: #F2F0ED */
```

### Conventions

- Use CSS variables from `:root` — never hardcode hex colors
- Font: `'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`
- Standard button classes: `.btn-primary` (terracotta), `.btn-secondary` (navy), `.btn-outline`
- Card pattern: `.card` with `.card-header` and `.card-title`
- Badge classes: `.badge-eligible`, `.badge-not-eligible`, `.badge-conditional`
- Border radius tokens: `--radius` (8px), `--radius-lg` (12px), `--radius-xl` (16px)
- Shadow tokens: `--shadow-sm`, `--shadow`, `--shadow-lg`, `--shadow-xl`

## ArcGIS Service Layer

All GIS service URLs are centralized in `js/arcgis-services.js`. Key services:

| Service Key | Description |
|-------------|-------------|
| `eligibility` | DADU eligibility for all Nashville parcels |
| `allPermits` | All DADU permits |
| `newPermits` | Recent ADU permits |
| `buildingSpecs` | Building specifications |
| `existingDADUs` | Secondary structures on SFH parcels |
| `sfhParcels` | Single-family home parcels |
| `parcelsWithCovenants` | Parcels with restrictive covenants |
| `zoningOverlays` | Nashville official zoning overlays |

Query patterns used throughout:
- `queryArcGISService(url, options)` — generic query
- `queryByBounds(url, bounds, options)` — map viewport queries
- `queryByPoint(url, lat, lng, tolerance)` — click-based queries
- `queryByAddress(address)` — address search
- `queryAllFeatures(url, options, onProgress)` — paginated fetch for large datasets

## Data Files

### JSON (pre-processed, committed to repo)

| File | Size | Purpose |
|------|------|---------|
| `parcels_eligibility_lite.json` | 22MB | All Nashville parcels + eligibility flags |
| `parcels_scored_v2.json` | 20MB | Parcels with opportunity scores |
| `permits_with_apn.json` | 13MB | Permits linked to parcel IDs |
| `permits_light.json` | 9.4MB | Lighter permit dataset |
| `contractor_data_enhanced.json` | 1MB | Contractor metrics |
| `MASTER_ADU_DATA/parcels_eligibility_lite.json` | 22MB | Core eligibility data (used by map pages) |

### GeoJSON (large, some gitignored)

Large GeoJSON files (50-87MB) are used for map rendering. Check `.gitignore` before adding new ones. The gitignored files include: `building_footprints_light.geojson`, `dadu_eligibility_master.geojson`, `eligibility_by_right.geojson`, `eligibility_data.geojson`, `eligibility_points.geojson`, `eligibility_usd.geojson`, and `*.csv`.

### Data Processing Scripts

Run from repository root:
```bash
python scripts/build_document_indices.py   # Rebuild docs_index.json
python scripts/build_gdrive_index.py       # Rebuild Google Drive index
python scripts/build_ordinance_index.py    # Rebuild ordinance_index.json
python scripts/download_permit_pdfs.py     # Download permit PDFs
```

## Key Pages

### Core Interactive (fully functional with live data)

| Page | Purpose | Primary Data |
|------|---------|-------------|
| `index.html` | Homepage — "Can I build a DADU?" | `parcels_eligibility_lite.json` |
| `property_search.html` | Advanced parcel search + map | Eligibility + permits |
| `dadu_opportunity_explorer_v2.html` | Investment opportunity scoring | `parcels_scored_v2.json` |
| `nashville_permit_explorer_v3.html` | Permit analytics & trends | `permits_with_apn.json` |
| `contractor_dashboard.html` | Contractor performance metrics | `contractor_data_enhanced.json` |

### Placeholder Pages (under development)

These pages exist for navigation completeness but show "under development" messages:
`designer_resources.html`, `municipal_dashboard.html`, `legal_resources.html`, `contractor_marketplace.html`, `short_term_rental_permit.html`, `permit_activity_dashboard.html`, `market_trends.html`, `dadu_reports_store.html`, `pdf_database_lookup.html`

Replace placeholders with real functionality as features are built.

## Leaflet Map Pattern

Interactive map pages follow this pattern:

```javascript
// Initialize map
const map = L.map('map').setView([36.1627, -86.7816], 12);  // Nashville center
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '...'
}).addTo(map);

// Load GeoJSON overlay
L.geoJSON(data, {
    style: feature => ({ /* use CSS variables or eligibility-based colors */ }),
    onEachFeature: (feature, layer) => { layer.bindPopup(/* ... */); }
}).addTo(map);

// Marker clustering for dense points
const markers = L.markerClusterGroup();
markers.addTo(map);
```

## APN and Permit Number Formats

Nashville-specific formats (documented in `data/MATCHING_RULES.md`):

- **APN (Assessor's Parcel Number):** 11 digits, displayed as `XXX-XX-X-XXX-XX`
- **Permit numbers:** `2024BL12345` (Building), `2024EL12345` (Electrical), `T2024-12345` (Trade)

## Coding Conventions

- **No frameworks** — vanilla JavaScript only. Do not introduce React, Vue, jQuery, etc.
- **No build tools** — no webpack, vite, rollup, etc. Files are served directly.
- **All HTML pages are root-level** — do not create subdirectories for pages (except `sample_reports/`)
- **Inline `<style>` and `<script>` blocks** — most pages embed their CSS/JS. Only shared code goes in external files.
- **CDN for libraries** — Leaflet, MarkerCluster, and fonts are loaded from CDNs, not vendored locally.
- **ArcGIS queries return GeoJSON** — always request `f: 'geojson'` and `outSR: 4326`.
- **Console logging** — use `console.error()` for failures, keep `console.log()` minimal in production code.
- **Responsive design** — CSS Grid/Flexbox with mobile breakpoints at 768px and 1024px.

## Testing

There is no automated test framework. Testing is manual:

1. Open pages in browser via local HTTP server
2. Verify the shared header renders and dropdowns work
3. Test map interactions (zoom, click, search)
4. Verify navigation links resolve correctly
5. Run `python verify_links.py` to check all 45 navigation targets

## Common Tasks

### Updating a page's content
Edit the HTML file directly. The header is loaded dynamically — no need to touch it.

### Changing navigation
Edit `homebody_header.html` only. All 34+ pages pick up changes automatically.

### Adding a new ArcGIS data layer
1. Add the service URL to `ARCGIS_SERVICES` in `js/arcgis-services.js`
2. Use `queryArcGISService()` or helper functions to query it
3. Render results with Leaflet GeoJSON layer

### Rebuilding data indices
```bash
python scripts/build_document_indices.py
python scripts/build_ordinance_index.py
```

### Verifying site integrity
```bash
python verify_links.py          # Check all nav links
python check_live_pages.py      # Check page availability
```

## Existing Documentation

| File | Content |
|------|---------|
| `QUICK_REFERENCE.md` | Developer quick-start, color palette, nav structure |
| `IMPLEMENTATION_REPORT.md` | Detailed log of Castlehold rebranding implementation |
| `IMPLEMENTATION_SUMMARY.txt` | Executive summary of implementation |
| `PARCEL_DATA_PAGES.md` | Which pages use which data, live status |
| `data/MATCHING_RULES.md` | APN & permit number extraction rules (Python) |
| `data/DOCUMENT_MATCHING_RULES.md` | PDF document matching logic |
| `data/ARCGIS_ELIGIBILITY_SYMBOLOGY.md` | Map color/symbology rules |

## Things to Avoid

- Do not rename existing HTML files — URLs may be bookmarked or linked externally
- Do not delete files without checking if they are referenced by other pages
- Do not introduce server-side dependencies — this is a static site
- Do not hardcode colors — use CSS variables from the design system
- Do not add Developer/Investor to the navigation user types
- Do not modify the navigation structure without explicit approval (it is locked)
- Do not commit large GeoJSON files without checking `.gitignore`
- Do not use `file://` protocol for testing — use an HTTP server (fetch won't work otherwise)
