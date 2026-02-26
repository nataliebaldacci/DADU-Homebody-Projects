# Icon Session Summary — February 26, 2026

## What Was Accomplished

### ParcelQuest-Style Icon System (Sessions 3-4)

Replaced all Lucide/generic icons across the Homebody Projects nav with custom-designed SVGs matching ParcelQuest's two-color icon style.

**Key design principle discovered:** ParcelQuest puts dots WHERE LINES/TEXT WOULD NORMALLY BE. Dots replace content (text lines, grid cells, labels, data rows) — they don't just decorate. This is what makes PQ icons distinctive.

### Icon Versions Created

4 version folders were created so we could compare approaches:

| Version | Folder | Style | Dots Approach |
|---------|--------|-------|---------------|
| V1 | `assets/icons/` (original) | Full detail + 2-column diminishing dots outside figure | Dots are decoration outside the icon |
| V2 | `assets/icons/_v2/` | Full detail + small 4-dot cluster outside | Reduced decoration, still outside |
| V3 | `assets/icons/_v3/` | Dots placed inside figures as texture/fill | Dots become internal texture |
| V4 | `assets/icons/_v4/` | Dots replace lines/text content (PQ style) | Dots ARE the content — replace text, grid lines, data |
| V5 | `assets/icons/_v5/` | Hybrid combinations of best elements | Custom per icon |

### User's Final Selections (24 icons)

| Icon | Selected Version | Notes |
|------|-----------------|-------|
| Checklist_ | V3 | |
| Dashboard | V3 | V1/V2 saved to `_saved/` for Contractor Marketplace |
| Draw_DADU | V3 | |
| Eligibility_Check | V3 | |
| Permit_Explorer | V3 | |
| Claims | V3 | |
| homeowner | V3 | |
| DADU_History | V3 | |
| STR_Permit | V3 | |
| Permit_Site_Plans | V3 | |
| Project_Planner | V3 | |
| Area_Analysis | V3 | |
| Permit_Analytics | V3 | |
| Document_Database | V4 | |
| Legislation | V4 | |
| Owner_Occupancy | V4 | |
| Restrictive_Covenants | V4 | |
| Overlay_Design_Standards | V4 | |
| Zoning_Documents | V4 | User noted "needs work" — may revisit |
| Permit_Approval | V5 | Hybrid: v4 dot-text + stamp handle (left) + check circle (right) |
| Project_Report | V5 | Hybrid: v2 layout (header/house/chart) + v4 dot rows, no outside dots |
| Permit_Activity | V1 | Keep original |
| Project_Checklist | V1 | Keep original |
| Draw_on_Parcel | Reworked | V1 arrows + detail inside, removed outside dots, added yard dot texture |

### New Icons Created

| Icon | Purpose |
|------|---------|
| `What_is_DADU.svg` | House with question mark — for "What is a DADU?" nav item |
| `Valuations.svg` | House + price tag (hand-coded from Canva design 4) |

### Nav Fixes Applied (homebody_header.js)

**Duplicate icon resolutions:**
| Nav Item | Before (duplicate) | After (unique) |
|----------|-------------------|----------------|
| Eligibility Map | `Area Maps and Visual layers.svg` (same as col header) | `Zoning.svg` |
| Code & Legislation | `Legal.svg` (same as Legal Professionals) | `Legislation.svg` |
| PDF Database | `Recorded_Docs.svg` (same as External Links + Learn header) | `Document_Database.svg` |
| What is a DADU? | `ADU.png` (same as Existing DADUs) | `What_is_DADU.svg` |

**Label changes:**
- "STR Permit" → "Short Term Rental Permit"

**Column header icon changes:**
- Learn column: `ADU.png` → `Recorded_Docs.svg`
- Permits & Forms column: `Legal.svg` → `Permit_Approval.svg`

**Previously committed (Session 3):**
- Permit Analytics: `Enhanced Transaction History Report .svg` → `Permit_Analytics.svg`
- DADU History: `Timeline.svg` → `DADU_History.svg`
- Owner Occupancy: `homeowner.svg` → `Owner_Occupancy.svg`
- Trade Permits: `Renewals.png` → `Renewals.svg`

---

## Color Palette (for icon design)

All custom SVG icons use exactly 3 colors:

| Color | Hex | Usage in Icons |
|-------|-----|---------------|
| Deep Slate | `#3A5566` | Primary structural shapes, outlines, fills |
| Warm Stone | `#7B746D` | Dots (PQ-style content replacement) |
| Off-White | `#F5F5F0` | Cutouts, negative space, inner fills |

Icon template: 28x28 viewBox, ~1-2KB per SVG.

The full site palette is documented in CLAUDE.md Section 3.

---

## Remaining Icon Work

### Still Needs Unique Icons (from nav audit)

These items still share icons with other nav items:

| Nav Item | Currently Uses | Shared With |
|----------|---------------|-------------|
| Build My DADU | `Building_and_Construction.svg` | Contractors, Contractor Marketplace, Find a Contractor, General Requirements |
| Contractor Marketplace | `Building_and_Construction.svg` | (5 items share this icon) |
| Find a Contractor | `Building_and_Construction.svg` | |
| General Requirements | `Building_and_Construction.svg` | |
| Form Wizard | `Eligibility_Check.svg` | Eligibility Flowchart |
| External Links | `Recorded_Docs.svg` | Learn column header |
| Permit Process Timeline | `Permit_Approval.svg` | Permits & Forms column header |

`Building_and_Construction.svg` is the worst offender — used 5 times. Dashboard V1/V2 are saved at `_saved/Dashboard_v1.svg` and `_saved/Dashboard_v2.svg` for potential Contractor Marketplace use.

### Icons User May Revisit
- **Zoning_Documents** — User said "needs work, can we use a PQ one?" Using V4 for now.
- **Draw_on_Parcel** — Reworked with V1's arrows but user hasn't confirmed the new version yet.
- **Valuations** — Hand-coded version; user preferred Canva design. May need PNG export replacement.
- **Investments** — Still using original PNG, no custom SVG version created yet.

---

## File Structure

```
assets/icons/
├── [24 active custom SVGs]     ← User-selected final versions
├── _v2/                        ← 23 icons, reduced outside dots
├── _v3/                        ← 24 icons, dots inside as texture
├── _v4/                        ← 24 icons, dots replace content (PQ style)
├── _v5/                        ← 2 hybrid icons (Permit_Approval, Project_Report)
├── _saved/                     ← Dashboard V1/V2 saved for future use
├── _preview/                   ← Canva exports and work-in-progress
├── [original ParcelQuest SVGs] ← Property_Owners.svg, Municipal.svg, etc.
└── [PNG icons]                 ← ADU.png, Claims.png, Investments.png, Renewals.png
```

## Utility Pages (not in nav, for development only)
- `icon_compare.html` — Side-by-side V1/V2/V3/V4 comparison grid
- `icon_mockups.html` — V5 hybrid mockup preview
- `icon_preview.html` — Full icon inventory with status

## Git Commits (this session)
- `499247c` — Finalize PQ-style icons: apply user-selected versions, fix nav duplicates
- `16a0363` — (Prior session) Update nav icons: Permit_Analytics.svg, DADU_History.svg
