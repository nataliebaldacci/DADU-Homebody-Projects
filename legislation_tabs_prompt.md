# Task: Reorganize dadu_code_legislation_v3.html into a tabbed layout

**File:** `dadu_code_legislation_v3.html`

First run: `git add -A && git commit -m "checkpoint before legislation page redesign"`

Then: `cp dadu_code_legislation_v3.html dadu_code_legislation_v4.html`

Work on the v4 copy ONLY.

## Problem

The current page is one giant scroll with 14 sections of tables. It's unusable. Reorganize into a **tabbed interface** so users click the tab they need instead of scrolling forever.

## New Tab Structure

### Tab 1: Current Law & Upcoming Legislation
- Start with the eligibility path explainer box from dadu_legislation.html:
  - USD (Urban Services District): By-right construction in R/RS/SP zones
  - GSD (General Services District): Requires DADU Overlay approval
  - Historic Districts: Additional MHZC review required
- BL2025-1007 (the big one) as a card with attachments (Substitute Text, Exhibit A, Gadd Amendment, Johnston Amendment) — each attachment gets a "Download PDF" button
- BL2025-1005 (RN/RL zoning districts) as a card
- BL2025-1006 (height regulations) as a card
- Upcoming: BL2025-1146 (DADU Exclusion Overlay) with a "Pending" tag
- Include the visual timeline from dadu_legislation.html showing the evolution: 2020 → 2021 → 2022 → 2023 → 2024 → 2025
- Also include the bill text PDF download cards from dadu_legislation.html (BL2024-559, BL2023-2094, BL2023-1761, BL2022-1322, BL2021-791/953, BL2021-635/BL2020-316) — each with "Download PDF" button linking to assets/legislation/*.pdf

### Tab 2: Metro Code Sections
- § 17.16.030(G) — the primary DADU regulation, with all 10 subsections listed
- Related code sections table (§ 17.04.060 Definitions, § 17.08.030 District Land Use, § 17.12.020 Bulk Tables, § 17.12.030 Setbacks, § 17.12.040(E) Accessory Buildings, § 17.40.105 Specific Plan, § 17.40.130 UDO)
- Each with its Municode link

### Tab 3: Historic & Overlays / Specific Plans
This tab has 4 sub-sections (use accordion or sub-tabs within this tab):

**DADU Overlay**
- DADU Overlay district plans and PDFs (DDU-001-001 through any others)
- Link to overlay-districts.html for map view

**Urban Design Overlay (UDO)**
- UDO districts with DADU-specific standards
- UDO document links

**Historic Overlay**
- MHZC design guidelines by neighborhood (Hillsboro-West End, Edgefield, Lockeland Springs, etc.)
- MHZC staff recommendations
- MHZC meeting minutes references

**Specific Plan Documents**
- SP rezoning documents that reference DADUs
- SP document table with SP number, location, link

### Tab 4: Legislative History
- Full Legistar bill archive table (all 62+ bills from 2011-2025)
- Withdrawn/Failed bills section
- This is the "deep archive" — users who need the full history come here

### Tab 5: Government & Administrative Resources
- Metro Codes Portal link (nashville.gov/departments/law/metro-codes)
- Nashville Planning Department links
- Planning Commission documents
- ArcGIS data service endpoints (Feature Service URLs)
- Errata & corrections

## Tab UI Styling

```css
.tab-nav {
  display: flex;
  background-color: #3a5566;
  border-radius: 8px 8px 0 0;
  overflow: hidden;
}

.tab-btn {
  padding: 14px 24px;
  background: transparent;
  border: none;
  color: #e2e2e0;
  font-family: Inter, sans-serif;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  white-space: nowrap;
  border-bottom: 3px solid transparent;
  transition: all 0.2s;
}

.tab-btn:hover {
  background-color: #496778;
  color: #ffffff;
}

.tab-btn.active {
  color: #ffffff;
  border-bottom-color: #cbb279;
  background-color: #496778;
}

.tab-content {
  display: none;
  padding: 24px;
  background-color: #ffffff;
  border: 1px solid #e2e2e0;
  border-top: none;
  border-radius: 0 0 8px 8px;
}

.tab-content.active {
  display: block;
}
```

## Accordion styling (for sub-sections within Tab 3):

```css
.accordion-header {
  background-color: #f0ebe1;
  padding: 12px 20px;
  cursor: pointer;
  font-family: Inter, sans-serif;
  font-weight: 700;
  font-size: 15px;
  color: #3a5566;
  border: 1px solid #e2e2e0;
  border-radius: 6px;
  margin-bottom: 4px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.accordion-header:hover {
  background-color: #e1d4bb;
}

.accordion-header .arrow {
  transition: transform 0.2s;
}

.accordion-header.open .arrow {
  transform: rotate(180deg);
}

.accordion-body {
  display: none;
  padding: 16px 20px;
  border: 1px solid #e2e2e0;
  border-top: none;
  border-radius: 0 0 6px 6px;
  margin-bottom: 12px;
}

.accordion-body.open {
  display: block;
}
```

## CRITICAL: LINK PRESERVATION

Before you start, extract EVERY SINGLE link from ALL FOUR of these source files:
- dadu_code_legislation_v3.html
- dadu_citations_complete.html
- dadu_legal_citations.html
- dadu_legislation.html

Run this first:
```
grep -ohP 'href="[^"]*"' dadu_code_legislation_v3.html dadu_citations_complete.html dadu_legal_citations.html dadu_legislation.html | sort -u > /tmp/all_legislation_links.txt
cat /tmp/all_legislation_links.txt | wc -l
```

Every link in that list MUST appear somewhere in the new v4 file. After building v4, run the same grep on it and diff against the original list. If ANY link is missing, add it back. Zero links lost.

This includes:
- Every Legistar bill link
- Every Municode code section link
- Every PDF download link (especially the assets/legislation/*.pdf files from dadu_legislation.html)
- Every ArcGIS endpoint URL
- Every Nashville.gov resource link
- Every MHZC guideline PDF link

## DESIGN REFERENCE: Use the styling from dadu_legislation.html

Open `dadu_legislation.html` and match its visual style. It uses:
- Card-based layout for each bill/document (not just flat tables)
- Each card has: bill number as heading, effective date, description paragraph, colored tags (e.g. "Amendment", "Overlay Standards", "Design Plan", "Original"), and action buttons ("Download PDF", "Metro Codes", etc.)
- Section headers use PNG icons from assets/icons/ (Legal.png, Zoning.png, Recorded Docs.png, etc.)
- Eligibility path explainer box at the top (USD by-right, GSD overlay, Historic MHZC)
- Visual timeline for legislative history
- Related resources cards at the bottom linking to other pages

Combine this card-based visual style WITH the tabbed navigation structure. So each tab's content uses cards and icons like dadu_legislation.html, not just raw tables.

Use tables only for the Legislative History tab (Tab 4) where you're showing 62+ bills — cards don't work for that volume. Everything else should be cards.

## Page header

Keep the same dark header style as other pages:
- Background: `#3a5566`
- Title: "NASHVILLE DADU CODE & LEGISLATION" in white
- Subtitle: "Comprehensive Reference Database | Updated January 2026" in `#e2e2e0`

## Card styling (for bill/document cards in Tabs 1, 2, 3, 5):

```css
.legislation-card {
  background: #ffffff;
  border: 1px solid #e2e2e0;
  border-radius: 10px;
  padding: 20px 24px;
  margin-bottom: 16px;
  transition: box-shadow 0.2s;
}

.legislation-card:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.legislation-card h3 {
  color: #3a5566;
  font-family: Inter, sans-serif;
  font-weight: 700;
  font-size: 18px;
  margin-bottom: 4px;
}

.legislation-card .effective-date {
  color: #7b746d;
  font-size: 13px;
  font-weight: 500;
  margin-bottom: 8px;
}

.legislation-card .description {
  color: #706f6c;
  font-size: 14px;
  line-height: 1.5;
  margin-bottom: 12px;
}

.tag {
  display: inline-block;
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 600;
  font-family: Inter, sans-serif;
  margin-right: 6px;
  margin-bottom: 8px;
}

.tag-amendment { background: #f0ebe1; color: #3a5566; }
.tag-overlay { background: #cbb279; color: #ffffff; }
.tag-design { background: #496778; color: #ffffff; }
.tag-original { background: #3a5566; color: #ffffff; }
.tag-passed { background: #2E6F4E; color: #ffffff; }
.tag-pending { background: #D4A017; color: #ffffff; }
.tag-failed { background: #8B8B8B; color: #ffffff; }

.card-actions {
  display: flex;
  gap: 10px;
  margin-top: 12px;
}

.card-btn {
  padding: 8px 16px;
  border-radius: 6px;
  font-family: Inter, sans-serif;
  font-weight: 600;
  font-size: 13px;
  text-decoration: none;
  cursor: pointer;
  border: none;
}

.card-btn-primary {
  background-color: #3a5566;
  color: #ffffff;
}

.card-btn-primary:hover {
  background-color: #496778;
}

.card-btn-secondary {
  background-color: transparent;
  color: #496778;
  border: 1px solid #496778;
}

.card-btn-secondary:hover {
  background-color: #f0ebe1;
}
```

## Section headers with icons (like dadu_legislation.html):

```css
.section-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.section-icon {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: #f0ebe1;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.section-icon img {
  width: 28px;
  height: 28px;
}

.section-header h2 {
  color: #3a5566;
  font-family: Inter, sans-serif;
  font-weight: 800;
  font-size: 22px;
  margin: 0;
}

.section-header .section-subtitle {
  color: #7b746d;
  font-size: 14px;
  margin: 0;
}
```

Use these icons from assets/icons/:
- Tab 1 (Current Law): Legal.png
- Tab 2 (Metro Code): Recorded Docs.png
- Tab 3 (Overlays): Zoning.png
- Tab 4 (History): APN Maps.png or Market Statistics Report .png
- Tab 5 (Resources): Municipal.png

## Table styling

```css
.legislation-table {
  width: 100%;
  border-collapse: collapse;
  font-family: Inter, sans-serif;
  font-size: 14px;
}

.legislation-table th {
  background-color: #f0ebe1;
  color: #3a5566;
  font-weight: 700;
  padding: 10px 12px;
  text-align: left;
  border-bottom: 2px solid #cbb279;
  font-size: 12px;
  text-transform: uppercase;
}

.legislation-table td {
  padding: 10px 12px;
  border-bottom: 1px solid #e2e2e0;
  color: #706f6c;
}

.legislation-table td a {
  color: #496778;
  font-weight: 600;
  text-decoration: none;
}

.legislation-table td a:hover {
  color: #3a5566;
  text-decoration: underline;
}

.legislation-table tr:hover {
  background-color: #f0ebe1;
}
```

## JavaScript for tabs (simple, no libraries):

```javascript
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.tab).classList.add('active');
  });
});

document.querySelectorAll('.accordion-header').forEach(header => {
  header.addEventListener('click', () => {
    header.classList.toggle('open');
    header.nextElementSibling.classList.toggle('open');
  });
});
```

## Content sources — merge ALL FOUR files

Pull content from ALL of these into v4:

1. **dadu_code_legislation_v3.html** — the main source. Has 14 sections of bills, code sections, MHZC guidelines, overlays, ArcGIS endpoints. Keep every row of every table.

2. **dadu_citations_complete.html** — check for any bills or links not already in v3. Add any missing ones.

3. **dadu_legal_citations.html** — has the detailed § 17.16.030(G) subsection breakdown and related code sections table with Municode links. Make sure Tab 2 (Metro Code) includes all of these.

4. **dadu_legislation.html** — has PDF download links for actual bill text that the others DON'T have:
   - assets/legislation/BL2024-559_ecba1856-82c4-4b1e-8443-b18670afba6a_MC-Legis20190722_105046_1.pdf
   - assets/legislation/BL2023-2094_d1cd7abf-c715-4d24-9177-81bfca915a9a_MC-Legis20190722_103360_1 (1).pdf
   - assets/legislation/BL2023-1761_f4446edd-69b0-4c2b-a96c-9df05f74de1a_MC-Legis20190722_102683_1.pdf
   - assets/legislation/BL2022-1322_cf0e252a-e3ac-4db8-91ef-1961f2954f80_MC-Legis20190722_101611_1.pdf
   - assets/legislation/BL2021-791_BL2021-953_4fda61a9-1aa2-4c97-8cc6-a98ff7d222e4_MC-Legis20190722_95726_1.pdf
   - assets/legislation/BL2021-635_BL2020-316_e7fe762d-ba78-40a0-8558-b723053d7d98_MC-Legis20190722_93626_1.pdf
   - assets/legislation/2024DDU-001-001_plan.pdf
   - assets/legislation/2023DDU-001-001_plan.pdf
   - assets/legislation/2023DDU-002-001_plan.pdf
   - assets/legislation/2022DDU-001-001_plan.pdf
   - assets/legislation/2021DDU-001-001_plan.pdf
   - assets/legislation/2021UD-001-001_plan.pdf
   These MUST appear in the appropriate tabs (bill PDFs in Tab 1 cards, overlay PDFs in Tab 3 DADU Overlay accordion).

## DO NOT change
- The nav bar
- Any external URLs or links
- Any bill data or citation content — keep it ALL, just reorganize

## BONUS DELIVERABLE: Master Links Database

After building v4, generate a file called `data/legislation_links_database.json` containing every link from all four source files, organized by category. Structure:

```json
{
  "generated": "2026-02-12",
  "source_files": [
    "dadu_code_legislation_v3.html",
    "dadu_citations_complete.html", 
    "dadu_legal_citations.html",
    "dadu_legislation.html"
  ],
  "total_links": 0,
  "categories": {
    "legistar_bills": [
      {
        "bill": "BL2025-1007",
        "status": "Passed",
        "description": "Major DADU reform",
        "url": "https://nashville.legistar.com/...",
        "source_files": ["v3", "citations_complete", "legislation"]
      }
    ],
    "legistar_attachments": [
      {
        "bill": "BL2025-1007",
        "attachment": "Second Substitute Text",
        "url": "https://nashville.legistar.com/View.ashx?...",
        "source_files": ["v3"]
      }
    ],
    "bill_text_pdfs": [
      {
        "bill": "BL2024-559",
        "local_path": "assets/legislation/BL2024-559_ecba1856-82c4-4b1e-8443-b18670afba6a_MC-Legis20190722_105046_1.pdf",
        "source_files": ["legislation"]
      }
    ],
    "overlay_plan_pdfs": [
      {
        "plan": "2024 DDU-001-001",
        "type": "DADU Overlay",
        "local_path": "assets/legislation/2024DDU-001-001_plan.pdf",
        "source_files": ["legislation"]
      }
    ],
    "municode_sections": [
      {
        "section": "§ 17.16.030(G)",
        "title": "Detached Accessory Dwelling Unit",
        "url": "https://library.municode.com/...",
        "source_files": ["v3", "legal_citations"]
      }
    ],
    "mhzc_design_guidelines": [
      {
        "district": "Hillsboro-West End",
        "adopted": "Dec. 2005",
        "revised": "2017",
        "dadu_section": "Section II.h Outbuildings (p. 16)",
        "url": "https://www.nashville.gov/sites/default/files/...",
        "source_files": ["v3"]
      }
    ],
    "arcgis_endpoints": [
      {
        "name": "DADU Eligibility Enhanced",
        "url": "https://services3.arcgis.com/...",
        "source_files": ["v3"]
      }
    ],
    "nashville_gov_resources": [
      {
        "name": "Metro Codes Portal",
        "url": "https://www.nashville.gov/departments/law/metro-codes",
        "source_files": ["legislation", "legal_citations"]
      }
    ],
    "planning_commission_docs": [
      {
        "name": "...",
        "url": "...",
        "source_files": ["v3"]
      }
    ],
    "video_links": [
      {
        "bill": "BL2025-1007",
        "description": "Council vote video",
        "url": "https://nashville.granicus.com/...",
        "source_files": ["v3"]
      }
    ],
    "internal_page_links": [
      {
        "page": "dadu_eligibility_map.html",
        "context": "Related resource link",
        "source_files": ["legislation"]
      }
    ]
  }
}
```

Rules for building this:
1. Scrape every `href` from all four HTML files
2. Categorize each link by type (Legistar, Municode, PDF, ArcGIS, Nashville.gov, internal page, video, etc.)
3. Track which source file(s) each link appeared in
4. Deduplicate — if the same URL appears in multiple files, list all source files
5. Fill in metadata (bill number, section number, district name) from the surrounding HTML context
6. Count total unique links and put in `total_links`
7. Save to `data/legislation_links_database.json`

Also generate a human-readable version at `data/legislation_links_database.csv` with columns:
category, name, bill_or_section, url, local_path, source_files, notes

This database becomes the master reference so no link ever gets lost again during page redesigns.

## After finishing, VERIFY LINKS:
1. Run: `grep -ohP 'href="[^"]*"' dadu_code_legislation_v4.html | sort -u > /tmp/v4_links.txt`
2. Run: `diff /tmp/all_legislation_links.txt /tmp/v4_links.txt`
3. Any link in the original list that's NOT in v4 — add it back immediately
4. Each tab shows/hides correctly
5. All links still work
6. Tab 1 is active by default on page load
7. Accordions in Tab 3 open/close properly
8. All PDF download buttons point to correct assets/legislation/ paths
