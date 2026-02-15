# TASK: Create the About Page — Merge Platform Info + Features + Data Sources

## What This Is

Create `about_platform.html` — a single comprehensive "About the Platform" page that merges content from three source types:

1. **`about_platform_infographic.html`** (previously deleted, but content preserved below) — what the platform is, how the data works, key statistics
2. **`features.html`** (currently unlinked) — the full feature grid organized by category (Discovery Tools, Documents & Data, Planning Tools)
3. **Feature landing page style** from `feature-documents.html` and `feature-eligibility-map.html` — the "What It Does / How It Works / Data Sources / Related Tools" layout pattern that describes where data comes from

The result: one polished About page that answers "What is this platform, what can it do, and where does the data come from?" — then routes users into the actual tools.

## STEP 1: Read Source Files First

Before writing any code, read the full content of these files to extract all content worth preserving:

```bash
cat features.html
cat feature-documents.html
cat feature-eligibility-map.html
```

Also check if a local copy of `about_platform_infographic.html` exists anywhere:
```bash
find . -name "about_platform*" -type f 2>/dev/null
```

If `about_platform_infographic.html` does not exist in the repo, use the content described in Section "PLATFORM INFO CONTENT" below.

---

## STEP 2: Build about_platform.html

### Page Structure (7 sections)

---

**SECTION 1: HERO**
- Background: #3A5566
- Logo: ADU_Light2.svg (dark background, so light variant is correct here)
- Headline: "About Homebody Projects" — #E1D4BB, serif (Source Serif 4 or Georgia), italic, 700
- Subtitle: "Nashville's most comprehensive DADU eligibility, planning, and market intelligence platform. Built on authoritative public data from Metro Nashville-Davidson County." — #F0EBE1
- Stats row (same style as homepage):
  - 285,512 — PARCELS ANALYZED
  - 67,707 — ELIGIBLE PARCELS
  - 827+ — DADUS PERMITTED
  - 12,500+ — DOCUMENTS INDEXED
  - Numbers: #CBB279, font-weight 800. Labels: #E1D4BB, uppercase, letter-spacing 2px

---

**SECTION 2: WHAT IS HOMEBODY PROJECTS?**
- Background: #F2F0ED
- Heading: "What Is Homebody Projects?" — #3A5566, serif, italic
- Two-column layout (text left, visual right on desktop; stacked on mobile):

Left column (text):
"Homebody Projects aggregates public parcel data, building permits, restrictive covenants, and regulatory information into a single platform for Nashville-Davidson County. The platform addresses information gaps in residential construction by making DADU (Detached Accessory Dwelling Unit) eligibility, requirements, and market data accessible to homeowners, contractors, designers, investors, and municipal staff.

Nashville's BL2025-1007 legislation, effective December 12, 2025, expanded DADU eligibility to 67,707 parcels in the Urban Services District. Homebody Projects helps property owners determine whether they qualify, understand what they can build, find contractors who have completed similar projects, and access the permits and documents they need.

All data on this platform comes from authoritative Nashville-Davidson County sources. We do not generate or estimate data. We aggregate, normalize, and present public records."

Right column: a simple card or callout box with:
- "A Vanderbilt Law School Project"
- "Developed by Natalie Baldacci, J.D. 2026"
- "Supporting coursework in Networks, Law, and Entrepreneurial Strategy"
- "Powered by Castlehold" (small, muted — this is one of the allowed Castlehold placements)

---

**SECTION 3: PLATFORM FEATURES**
- Background: white
- Heading: "Platform Features" — #3A5566, serif, italic
- Subheading: "Comprehensive tools for every stage of your Nashville DADU journey" — #706F6C

Pull the feature grid directly from `features.html` and organize into three category groups. Use the same card style as features.html but ensure colors match the locked palette.

**Category 1: Discovery Tools** (icon: Parcel Search.svg or .png)
| Feature | Description | Key Stats | Link |
|---------|-------------|-----------|------|
| DADU Eligibility Map | Interactive parcel-level visualization. Color-coded: Eligible, Not Eligible, Conditional. | 285,000+ parcels analyzed | dadu_eligibility_map.html |
| Property Report Card | Enter any Nashville address or APN for complete eligibility analysis with linked documents, covenants, and costs. | Instant eligibility determination | property-report-card.html |
| DADU Explorer | Find and analyze existing DADUs across Nashville. Filter by location, cost, size, year. | 827+ permitted DADUs | dadu_opportunity_explorer_v2.html |
| Near Me Locator | Find existing DADUs within a customizable radius of any address. | Radius search 0.25-2 miles | dadu_near_me_v2.html |

**Category 2: Documents & Data** (icon: Recorded Docs.svg or .png)
| Feature | Description | Key Stats | Link |
|---------|-------------|-----------|------|
| Recorded Documents | Access building permits, site plans, restrictive covenants, and surveys. Indexed by parcel, searchable by address. | 12,500+ documents indexed | dadu_documents_portal.html |
| Code & Legislation | 111 legal citations database covering all Nashville DADU legislation from 2011-2025. | 111 citations, 62+ bills | dadu_code_legislation_v5.html |
| Permit Explorer | Search all Nashville building permits with contractor, cost, and timeline data. | 4,700+ permits | permit_explorer.html |
| Restrictive Covenants | Search 43,000+ covenant records that may affect DADU construction. | 43,000+ covenants searched | restrictive_covenants_v2.html |

**Category 3: Planning Tools** (icon: Market Statistics Report.svg or .png)
| Feature | Description | Key Stats | Link |
|---------|-------------|-----------|------|
| Size Calculator | Calculate maximum DADU dimensions based on lot size and BL2025-1007 rules. | Lot-specific calculations | size_calculator.html |
| Cost Estimator | Construction cost estimates by size, finish level, and Nashville market data. | Category breakdown | dadu_calculators.html |
| Contractor Directory | Browse contractors who have completed DADU projects in Nashville. | 370+ contractors | contractor_marketplace.html |
| Project Planner | Step-by-step DADU project planning hub. | Checklist and timeline | project_planner_hub.html |

Each feature card format:
- Icon in #F0EBE1 circle (48px)
- Feature name as heading (#3A5566, Inter, 600)
- 2-line description (#706F6C)
- Key stat in small muted text
- "Open Tool" or "Explore" link button

---

**SECTION 4: HOW IT WORKS**
- Background: #F2F0ED
- Heading: "How It Works" — #3A5566, serif, italic

Use the numbered steps pattern from the feature landing pages:

| Step | Title | Description |
|------|-------|-------------|
| 1 | Search Your Property | Enter any Nashville address or APN. The platform queries parcel data, zoning, building footprints, and permit history. |
| 2 | Check Eligibility | Instant determination based on BL2025-1007 criteria: zoning district, lot size, service district, and existing structures. |
| 3 | Review Documents | Access linked permits, site plans, restrictive covenants, and property cards for your parcel and nearby DADUs. |
| 4 | Plan Your Project | Use calculators for size limits, cost estimates, and ROI projections. Find contractors with experience on similar lots. |

Style: numbered circles (#3A5566 background, white number), title as bold heading, description as body text. Horizontal on desktop, vertical on mobile.

---

**SECTION 5: DATA SOURCES**
- Background: #3A5566 (dark section)
- Heading: "Data Sources" — #E1D4BB, serif, italic
- Subheading: "Built on authoritative Nashville-Davidson County public records" — #F0EBE1

This is the section that describes WHERE the data comes from — pull from features.html and the feature landing pages. Use the same 4-card grid pattern from features.html Data Sources section, but expand with more detail.

| Source | Icon | Description | Update Frequency |
|--------|------|-------------|-----------------|
| Metro Nashville Codes | Building_and_Construction.png | Building permits, inspections, certificates of occupancy, and DADU-specific permit records from the Metro Codes Department. | Updated via ePermits API |
| Davidson County Assessor | Appraisers.png | Parcel boundaries, lot dimensions, property characteristics, ownership records, and assessed values for all 285,512 parcels. | Assessor data refreshed periodically |
| Metro Planning Department | Zoning.png | Zoning classifications, overlay districts, service district boundaries (USD/GSD), and DADU overlay approvals. | Zoning layers via ArcGIS |
| Register of Deeds | Legal.png | Recorded restrictive covenants, deed restrictions, and property transfers that may restrict DADU construction. | 43,000+ covenant records |
| Nashville GIS | GIS.png | Parcel geometry, building footprints (327,000+ with height data), and spatial layers powering all maps. | ArcGIS Feature Services |
| Third-Party Validation | Exports__Reports.png | PropertyShark, RE Data, and RealtyTrac records cross-referenced for 98.9% ADU detection accuracy. | Validated against 6,800+ confirmed properties |

Cards on dark background: #f5f5f0 card background, icon in circle at top, source name as heading, description as body, update note as small muted badge.

---

**SECTION 6: BUILT FOR EVERY USER**
- Background: #F2F0ED
- Heading: "Built For Every User" — #3A5566, serif, italic
- Subheading: "Specialized tools for homeowners, contractors, designers, investors, and municipal staff" — #706F6C

User type cards (pull from features.html Section 4 / WHO WE SERVE nav):

| User Type | Icon | Description | Link |
|-----------|------|-------------|------|
| Homeowners | Property_Owners.png | Check eligibility, understand requirements, estimate costs, find contractors. | homeowner_portal.html |
| Contractors & Builders | Building_and_Construction.png | Market intelligence, permit data, leads, pricing benchmarks. | contractor_portal.html |
| Designers & Architects | Surveyors_and_Engineers.png | Building requirements, site analysis, precedent projects. | designer_portal.html |
| Municipal & Government | Municipal.png | Permit tracking, policy impact analysis, compliance monitoring. | permit_activity_dashboard.html |

Each card: larger format with PNG icon prominently displayed, heading, 1-2 line description, "Get Started" button (#CBB279 bg, #3A5566 text).

---

**SECTION 7: CTA**
- Background: #3A5566
- Heading: "Ready to Check Your Property?" — #E1D4BB, serif, italic
- Subtitle: "Get instant eligibility results and a complete DADU analysis." — #F0EBE1
- Button: "Check Eligibility Now" — #CBB279 bg, #3A5566 text, large, centered
- Links to: am_i_eligible.html

---

**FOOTER:** Standard shared footer via homebody_header.js

---

## STEP 3: Update Navigation

Change the ABOUT routing:
- **Current:** ABOUT → `homebody_dadu_pricing.html#about`
- **New:** ABOUT → `about_platform.html`

Update in `homebody_header.js` and `homebody_header.html`.

ABOUT remains a direct link (no dropdown), same as PRICING.

---

## STEP 4: Handle Orphan Pages

After `about_platform.html` is built:

1. **`features.html`** — Its content is now absorbed into about_platform.html Section 3 (Platform Features) and Section 5 (Data Sources). Move to deletion candidates.

2. **`feature-documents.html`** — Its unique content (document categories, how it works) lives in `dadu_documents_portal.html`. The "about" content (data sources, what it does) is now in about_platform.html. Move to deletion candidates.

3. **`feature-eligibility-map.html`** — Its unique content (what the map does, how it works) lives in `dadu_eligibility_map.html` itself. The "about" content is now in about_platform.html. Move to deletion candidates.

4. **`user-types.html`** — Its content is absorbed into about_platform.html Section 6. Move to deletion candidates.

Do NOT delete these files yet. Just note them as absorbed. I will confirm deletion separately.

---

## STEP 5: CLAUDE.md Updates

1. Change ABOUT routing in Section 4:
   ```
   ABOUT → about_platform.html (no dropdown)
   ```

2. Add `about_platform.html` to "Linked in Navigation" under "Direct links":
   ```
   | Direct links | homebody_dadu_pricing.html, am_i_eligible.html, about_platform.html |
   ```

3. Move these from "Unlinked but Worth Keeping" to "Unlinked Duplicates (candidates for deletion)":
   - features.html (absorbed into about_platform.html)
   - feature-documents.html (absorbed into about_platform.html)
   - feature-eligibility-map.html (absorbed into about_platform.html)
   - user-types.html (absorbed into about_platform.html)

4. Add note: "about_platform.html consolidates content from: features.html, feature-documents.html, feature-eligibility-map.html, user-types.html, and the deleted about_platform_infographic.html"

---

## PLATFORM INFO CONTENT (from deleted about_platform_infographic.html)

If the original file cannot be found, use this content which was preserved from it:

**What the platform does:**
Homebody Projects is a comprehensive DADU eligibility and development platform for Nashville-Davidson County. It aggregates public data, permit records, restrictive covenant signals, and regulatory information into an accessible web application.

**Key statistics:**
- 285,512 total Nashville parcels analyzed
- 67,707 parcels eligible under BL2025-1007 (USD)
- ~161,702 total eligible parcels (USD + GSD with overlay)
- 827 historic DADU permits (Metro, 2017-2025)
- 4,700+ total permits in database
- 2,072 unique contractors
- 43,000+ parcels with covenant records
- 327,000+ building footprints with height data
- 111 legal citations in legislation database
- 12,500+ documents indexed (permits, site plans, property cards, covenants)
- 98.9% ADU detection accuracy using 5-indicator methodology

**ADU detection methodology:**
Five combined indicators: building count (67K parcels with 2+ buildings), county permits (827), third-party permits (1,800), address fractions (10K secondary addresses), restrictive covenant filings (1,100). Properties with 2+ indicators = strong ADU signal (5,647 parcels). Validated against PropertyShark's 6,800+ confirmed 2-unit properties.

**Data architecture:**
- Static website on GitHub Pages
- ArcGIS Feature Services for map layers (Vanderbilt portal)
- JSON data files for client-side search and filtering
- Google Drive for PDF document storage (permits, property cards, covenants)
- Python data processing pipeline for ETL

---

## CONSTRAINTS

1. **No emoji.** Use SVG/PNG icons from assets/icons/ only.
2. **Banned color #003039** — use #3A5566 instead.
3. **No old palette colors** (#6b8fa3, #6b8e4e, #2E6F4E, #D4A017, #C58B2A, #7A2A1D, #2c3e50, #c9a86c, #e8e4df).
4. Use the locked palette: #3A5566 (Deep Slate), #2F3A45 (True Dark), #CBB279 (Wheat), #F2F0ED (background), #F5F5F0 (card), #E2E2E0 (border), #706F6C (body text), #E1D4BB (cream), #F0EBE1 (linen), #918A83 (muted).
5. Functional colors: Eligible #406A64, Not Eligible #B58676, Conditional #918A83.
6. Logo: ADU_Light2.svg in hero (dark bg), ADU_MultiColors.svg if used on light sections. ADU.png in nav (handled by shared header).
7. Font: Inter for body. Source Serif 4 or Georgia for section headings (serif, italic).
8. Page must load `homebody_shared.css` and inject shared header via `homebody_header.js`.
9. No "CASTLEHOLD" in page title, nav, or headings. "Castlehold" appears ONLY in the Vanderbilt project callout box and footer "Powered by" line.
10. Provide complete file contents for every file you modify.

---

## VERIFICATION

1. Page loads with shared header and correct nav highlighting on ABOUT
2. ABOUT link in nav goes to `about_platform.html` (not pricing#about)
3. All feature card links route to real, existing pages
4. No emoji anywhere on the page
5. No #003039 or old palette colors
6. Stats row numbers match the key statistics listed above
7. Data Sources section has 6 source cards
8. Mobile responsive: cards stack on small screens, hero text readable
9. `homebody_header.js` and `homebody_header.html` both updated and matching
10. CLAUDE.md updated with new routing and absorbed pages list
11. Commit:
    ```bash
    git add -A
    git commit -m "Create about_platform.html: merge features, data sources, platform info into comprehensive About page"
    git push origin main
    ```
