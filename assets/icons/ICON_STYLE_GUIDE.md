# Homebody Projects Icon Style Guide
**Version:** 1.0 | **Date:** February 26, 2026

---

## Design System: ParcelQuest Two-Color Icons

All icons on the Homebody Projects platform follow the **ParcelQuest two-color system** -- a geometric, architectural icon style using filled shapes (not thin strokes) with signature diminishing dot clusters.

---

## Color Palette for Icons

### Primary Colors (used in every icon)

| Color | Hex | Role | Usage |
|-------|-----|------|-------|
| **Deep Slate** | `#3A5566` | Structural / Primary | All main shapes, outlines, fills, text lines, document bodies |
| **Warm Stone** | `#7B746D` | Decorative / Dots | Diminishing dot columns, scattered accent dots |

### Cutout / Negative Space

| Color | Hex | Role | Usage |
|-------|-----|------|-------|
| **Off-White** | `#F5F5F0` | Interior fill | Inner rectangles, window cutouts, document interiors |

### Display Backgrounds

| Color | Hex | Role | Usage |
|-------|-----|------|-------|
| **Linen** | `#F0EBE1` | Icon circle bg | 72px circle behind icon in nav dropdowns and cards |
| **Warm Light** | `#F2F0ED` | Page background | Page background color |
| **Off-White** | `#F5F5F0` | Card surface | Card backgrounds |

### Colors NOT Used in Icons

| Color | Hex | Why Not |
|-------|-----|---------|
| Eligible | `#406A64` | Map status color only |
| Not Eligible | `#B58676` | Map status color only |
| Any bright/neon color | -- | BANNED site-wide |

---

## Icon Color Scales (6 Options)

You can produce any icon in multiple color scales depending on context. The shapes stay the same, only colors change.

### Scale 1: Standard (ParcelQuest Original)
| Element | Color | Hex |
|---------|-------|-----|
| Structural fills | Deep Slate | `#3A5566` |
| Dots | Warm Stone | `#7B746D` |
| Cutouts | Off-White | `#F5F5F0` |

**Use for:** Nav dropdown icons, card icons on light backgrounds. This is the default.

### Scale 2: Light + Slate Outline
| Element | Color | Hex |
|---------|-------|-----|
| Fills | Warm Muted UI | `#A59D8B` |
| Outlines/strokes | Deep Slate | `#3A5566` |
| Dots | Warm Muted UI | `#A59D8B` |
| Cutouts | Off-White | `#F5F5F0` |

**Use for:** Secondary icons, softer sections, paired alongside Standard scale to create visual hierarchy.

### Scale 3: Warm Monochrome
| Element | Color | Hex |
|---------|-------|-----|
| Everything | Warm Muted UI | `#A59D8B` |
| Cutouts | Off-White | `#F5F5F0` |

**Use for:** Decorative icons, watermark-style, background elements, subtle section headers. This matches the Canva-generated icon style.

### Scale 4: Stone Duo
| Element | Color | Hex |
|---------|-------|-----|
| Structural fills | Warm Stone | `#7B746D` |
| Dots | Lighter Stone | `#918A83` |
| Cutouts | Off-White | `#F5F5F0` |

**Use for:** Mid-tone backgrounds, neutral/muted contexts where Deep Slate feels too heavy.

### Scale 5: Cream on Dark (for dark backgrounds)
| Element | Color | Hex |
|---------|-------|-----|
| Structural fills | Cream | `#E1D4BB` |
| Dots | Warm Muted UI | `#A59D8B` |
| Background | Deep Slate | `#3A5566` |

**Use for:** Icons on dark sections (hero, footer, dark cards). The Cream reads clearly against #3A5566.

### Scale 6: Wheat on Dark (accent, use sparingly)
| Element | Color | Hex |
|---------|-------|-----|
| Structural fills | Wheat | `#CBB279` |
| Dots | Cream | `#E1D4BB` |
| Background | True Dark | `#2F3A45` |

**Use for:** Featured/highlighted icons on dark backgrounds. Use sparingly since Wheat is the accent color.

### Quick Color Swap Guide for Canva

When making icons in Canva, use these hex codes:

| Scale | Main Shape Color | Dot/Detail Color |
|-------|-----------------|------------------|
| Standard | `#3A5566` | `#7B746D` |
| Light + Outline | `#A59D8B` (fill) + `#3A5566` (outline) | `#A59D8B` |
| Warm Mono | `#A59D8B` | `#A59D8B` |
| Stone Duo | `#7B746D` | `#918A83` |
| Cream on Dark | `#E1D4BB` | `#A59D8B` |
| Wheat on Dark | `#CBB279` | `#E1D4BB` |

---

## SVG Structure Template

Every icon follows this structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 28 28">
  <g>
    <!-- Main subject (left/center area, roughly 20x22 space) -->
    <g>
      <!-- Filled shapes in #3A5566 -->
    </g>

    <!-- Diminishing dots column 1 (right side) -->
    <g><circle fill="#7B746D" cx="24" cy="X" r="1.05"/></g>
    <g><circle fill="#7B746D" cx="24" cy="X" r="0.87"/></g>
    <g><circle fill="#7B746D" cx="24" cy="X" r="0.69"/></g>
    <g><circle fill="#7B746D" cx="24" cy="X" r="0.51"/></g>

    <!-- Diminishing dots column 2 (far right) -->
    <g><circle fill="#7B746D" cx="27" cy="X" r="0.87"/></g>
    <g><circle fill="#7B746D" cx="27" cy="X" r="0.69"/></g>
    <g><circle fill="#7B746D" cx="27" cy="X" r="0.51"/></g>
    <g><circle fill="#7B746D" cx="27" cy="X" r="0.38"/></g>
  </g>
</svg>
```

---

## Design Rules

### 1. ViewBox and Dimensions
- **Standard viewBox:** `0 0 28 28` (preferred) or `0 0 28 24`
- **Width/height attributes:** Match the viewBox
- **Main subject area:** Left 20px of the canvas (x: 0-20)
- **Dot columns:** Right 8px of the canvas (x: 22-28)

### 2. Shapes and Style
- **Use filled shapes**, not thin strokes
- Prefer `<rect>`, `<circle>`, `<path>` elements
- Use `rx` for rounded corners (typically 0.3-1.2)
- Each distinct element wrapped in its own `<g>` tag
- **No gradients, no shadows, no filters**
- **No thin-stroke line icons** (that is the Lucide style we are replacing)

### 3. Negative Space / Cutouts
- Create depth by layering: a #3A5566 filled shape with a slightly smaller #F5F5F0 shape inside
- Example: Document = outer #3A5566 rect + inner #F5F5F0 rect
- Example: Checkmark badge = outer #3A5566 circle + inner #F5F5F0 circle + #3A5566 checkmark path

### 4. Diminishing Dots Pattern
The signature element. Two columns of circles that decrease in radius:

**Column 1** (cx: 22-24.5):
- r="1.05" (largest)
- r="0.87"
- r="0.69"
- r="0.51" (smallest)
- Vertical spacing: ~3 units between centers

**Column 2** (cx: 25-27.5):
- r="0.87" (starts one size smaller)
- r="0.69"
- r="0.51"
- r="0.38" (smallest)
- Offset vertically from column 1 by ~1.5-2 units

Some icons also scatter a few extra #7B746D dots around the main subject for data-point effects (see Area_Analysis.svg).

### 5. File Size Target
- **Target:** Under 2KB per icon (most are 1-1.5KB)
- **Maximum:** 5KB
- If an SVG exceeds 5KB, simplify it
- The 288KB Checklist_.svg is an extreme example of what NOT to do

### 6. Opacity
- Use `opacity="0.3"` or `opacity="0.5"` sparingly for layered/stacked effects (e.g., a background document behind a foreground one)
- Main subject should always be full opacity

---

## Icon Subjects by Category

### Documents & Reports
| Icon | Subject | Key Elements |
|------|---------|-------------|
| Permit_Site_Plans | Blueprint | Document frame, floor plan lines, room divisions |
| Restrictive_Covenants | Locked document | Document with padlock, keyhole detail |
| Project_Report | Report with chart | Document with header bar, bar chart, text lines |
| Claims | Claim form | Document with folded corner, exclamation mark |
| Recorded_Docs | Filing | (Original ParcelQuest) |
| Exports__Reports | Reports | (Original ParcelQuest) |

### Charts & Data
| Icon | Subject | Key Elements |
|------|---------|-------------|
| Permit_Activity | Bar chart | 4 ascending bars on axis line |
| Dashboard | Monitor with chart | Screen frame, mini bar chart, trend line |
| Investments | Trend line | Axis lines, rising line with data points, arrow |
| Cost_Market | Dollar circle | Currency symbol in circle, trend arrow |
| Area_Analysis | Radar/target | Concentric circles, crosshairs, data points |

### Planning & Tools
| Icon | Subject | Key Elements |
|------|---------|-------------|
| Project_Planner | Gantt chart | Horizontal bars at different offsets, timeline |
| Project_Checklist | Clipboard | Board, clip, 3 check items (2 checked, 1 empty) |
| Checklist_ | Clipboard | Same concept, simpler execution |
| Draw_on_Parcel | Parcel + pencil | Dashed lot outline, DADU footprint, pencil, dimension arrows |
| Draw_DADU | Canvas + house | Drawing surface with grid, house sketch, pencil |

### Buildings & People
| Icon | Subject | Key Elements |
|------|---------|-------------|
| Eligibility_Check | House + badge | House shape, checkmark badge/circle |
| homeowner | House + person | House with windows/door, person silhouette below |
| Owner_Occupancy | House + key | House roof, key with circular head |
| Valuations | House + scale | House with dollar sign, balance scale |

### Permits & Process
| Icon | Subject | Key Elements |
|------|---------|-------------|
| Permit_Approval | Stamp + document | Document with text lines, approval stamp circle, stamp handle |
| Permit_Explorer | Search + documents | Document stack, magnifying glass |
| STR_Permit | Calendar | Calendar grid with cells, hanging tabs |
| Renewals | Cycle arrows | Circular renewal arrows, calendar element |
| Legislation | Gavel | Gavel head, handle, sound block base |

### Zoning & Maps
| Icon | Subject | Key Elements |
|------|---------|-------------|
| Zoning_Documents | Zone grid | 4-cell grid with different zone patterns |
| Overlay_Design_Standards | Layers | 3 stacked offset rectangles with opacity |
| Document_Database | Filing cabinet | 3-drawer cabinet with drawer pulls |

---

## Icon Inventory

### Status Legend
- **PQ Original** = From original ParcelQuest source files (do not modify)
- **Replaced** = Was Lucide, now hand-coded ParcelQuest style (live in assets/icons/)
- **Preview** = New alternative in assets/icons/_preview/ (not yet replacing original)
- **PNG** = Still a PNG file, SVG alternative available in _preview/

### Complete List

| Filename | Status | Size | Used In Nav |
|----------|--------|------|-------------|
| Property_Owners.svg | PQ Original | ~2KB | WHO WE SERVE |
| Legal.svg | PQ Original | ~2KB | WHO WE SERVE, RESOURCES |
| Municipal.svg | PQ Original | ~2KB | WHO WE SERVE |
| Building_and_Construction.svg | PQ Original | ~2KB | WHO WE SERVE, EXPLORE, BUILD |
| Zoning.svg | PQ Original | ~2KB | EXPLORE, RESOURCES |
| Exports__Reports.svg | PQ Original | ~2KB | DATA |
| Neighbors.svg | PQ Original | ~2KB | EXPLORE |
| Surveyors_and_Engineers.svg | PQ Original | ~2KB | WHO WE SERVE |
| GIS.svg | PQ Original | ~2KB | RESOURCES |
| Recorded_Docs.svg | PQ Original | ~2KB | DATA, RESOURCES |
| Parcel Search.svg | PQ Original | ~2KB | EXPLORE |
| Area_Maps_and_Visual_layers.svg | PQ Original | ~2KB | EXPLORE |
| Permit_Activity.svg | Replaced | ~1KB | EXPLORE |
| Permit_Site_Plans.svg | Replaced | ~1KB | DATA |
| Project_Planner.svg | Replaced | ~1KB | BUILD |
| Project_Checklist.svg | Replaced | ~1KB | BUILD |
| Restrictive_Covenants.svg | Replaced | ~1KB | DATA |
| STR_Permit.svg | Replaced | ~1KB | RESOURCES |
| Owner_Occupancy.svg | Replaced | ~1KB | RESOURCES |
| Overlay_Design_Standards.svg | Replaced | ~1KB | RESOURCES |
| Legislation.svg | Replaced | ~1KB | RESOURCES |
| Zoning_Documents.svg | Replaced | ~1KB | RESOURCES |
| Area_Analysis.svg | Replaced | ~1KB | -- |
| Draw_on_Parcel.svg | Replaced | ~1KB | BUILD |
| Permit_Explorer.svg | Preview available | 8.1KB | EXPLORE |
| Dashboard.svg | Preview available | 10.1KB | -- |
| Cost_Market.svg | Preview available | 7.7KB | -- |
| Eligibility_Check.svg | Preview available | 16.4KB | -- |
| Draw_DADU.svg | Preview available | 9.3KB | -- |
| homeowner.svg | Preview available | 8.7KB | -- |
| Permit_Approval.svg | Preview available | 6.4KB | -- |
| Project_Report.svg | Preview available | 7.7KB | -- |
| Checklist_.svg | Preview available | 288KB | -- |
| Document_Database.svg | Preview available | -- | -- |
| Claims.png | PNG, SVG preview | 7.5KB | BUILD |
| Renewals.png | PNG, SVG preview | 12.2KB | BUILD, RESOURCES |
| Investments.png | PNG, SVG preview | 11.5KB | EXPLORE |
| Valuations.png | PNG, SVG preview | 12.7KB | -- |
| ADU.png | Logo (keep as PNG) | -- | Nav, cards |

---

## How to Create New Icons

1. Start with the SVG template above (28x28 viewBox)
2. Sketch the main subject using only `#3A5566` filled shapes in the left 20px
3. Use `#F5F5F0` cutouts for interior detail / negative space
4. Add two diminishing dot columns on the right using `#7B746D`
5. Wrap each distinct element in `<g>` tags
6. Keep file size under 2KB
7. Test at 24px, 32px, 48px, and 64px sizes
8. Place in `assets/icons/` (or `assets/icons/_preview/` for review first)

---

## Canva AI Prompts

If generating icons via Canva AI, use this prompt template:

> Create a simple, geometric [SUBJECT DESCRIPTION] icon using ONLY two colors: Deep Slate (#3A5566) for the main structural shapes and Warm Stone (#7B746D) for small decorative dot clusters. The icon should use filled shapes (not thin outlines). Include a column of 4 diminishing circles in #7B746D on the right side of the icon, decreasing from large to small. White (#F5F5F0) can be used for interior cutout details. No gradients, no shadows, no other colors. Style: architectural, geometric, professional.

---

*This guide is the single source of truth for icon styling. When in doubt, reference the original ParcelQuest icons (Property_Owners.svg, Legal.svg, etc.) as the gold standard.*
