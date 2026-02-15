# TASK: Page Deletions, Nav Simplification, New Legal Portal, Designer Merge, Contractor Report Fix

## Overview

Multiple changes across deletions, nav restructuring, new page creation, and content merges. Read CLAUDE.md first, then execute in order.

---

## PART 1: Delete Three Pages

Delete these files. They are confirmed for removal:

```bash
git rm area_analysis_report.html
git rm contractor_advertising.html
git rm dadu_zoning_standards.html
```

**Nav updates required after deletion:**

1. **`contractor_advertising.html`** is currently linked in WHO WE SERVE > Professional > "Advertise With Us". Remove that nav entry entirely. (The advertising content will eventually live at contractor_portal.html#advertise, but that task is separate.)

2. **`dadu_zoning_standards.html`** is currently linked in RESOURCES > Learn > "Zoning Standards". Remove that nav entry.

3. **`area_analysis_report.html`** is not in the nav (it was in the "Unlinked but Worth Keeping" list). No nav change needed.

Update `homebody_header.js` and `homebody_header.html` to remove these entries.

Update CLAUDE.md:
- Move all three from their current lists to "Previously Deleted"
- Remove "Zoning Standards" row from RESOURCES > Learn table
- Remove "Advertise With Us" row from WHO WE SERVE > Professional table

---

## PART 2: Simplify WHO WE SERVE Dropdown — Remove Columns

**Current structure (two columns):**
- Column 1: "User Portals" — Homeowners, Contractors, Designers & Architects
- Column 2: "Professional" — Municipal & Agencies, Legal Professionals, Advertise With Us

**New structure (single flat list, NO columns, NO column headers):**

| Label | Icon | File |
|-------|------|------|
| Homeowners | Property_Owners.svg | homeowner_portal.html |
| Contractors | Building_and_Construction.svg | contractor_portal.html |
| Designers & Architects | Surveyors_and_Engineers.svg | designer_portal.html |
| Municipal & Agencies | Municipal.svg | user-homeowners.html |
| Legal Professionals | Legal.svg | legal_professionals_portal.html |

Notes:
- **Removed:** "Advertise With Us" (file deleted in Part 1)
- **Changed:** Legal Professionals now points to `legal_professionals_portal.html` (new, created in Part 3) instead of `dadu_contractors_infographic.html`
- **No column headers.** No "User Portals" or "Professional" grouping. Just a single flat dropdown list with icons.
- Keep the dropdown icon style: each item shows its SVG icon at 32-40px in a #F0EBE1 (Linen) circle, label next to it.
- The dropdown should be narrower than a mega-menu since it's a single column. Style it as a standard dropdown list, not a wide mega-menu panel.

### Implementation in homebody_header.js

Change the WHO WE SERVE dropdown from `mega-menu-2` (two columns) to a single-column dropdown. Remove the column wrapper divs and column header elements. Each item is just an icon + label + link in a vertical list.

```css
/* Single-column dropdown styling */
.dropdown-single {
  min-width: 280px;
  padding: 12px 0;
}
.dropdown-single .dropdown-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 20px;
  color: var(--cream);
  text-decoration: none;
  font-family: Inter, sans-serif;
  font-size: 14px;
  font-weight: 500;
  transition: background 0.15s;
}
.dropdown-single .dropdown-item:hover {
  background: var(--slate-mid); /* #496778 */
}
.dropdown-single .dropdown-item img {
  width: 32px;
  height: 32px;
  background: var(--linen); /* #F0EBE1 */
  border-radius: 50%;
  padding: 4px;
}
```

---

## PART 3: Create Legal Professionals Portal

**File:** `legal_professionals_portal.html` (new)

Read `dadu_contractors_infographic.html` first to see what content was previously shown to "Legal Professionals" (it was a wrong link, but check if anything is reusable).

### Page Structure

**Hero:**
- Background: var(--slate) #3A5566
- Icon: Legal.svg (large, in linen circle)
- Headline: "Legal Professionals" — white, Inter, 800
- Subtitle: "Covenant research, zoning compliance, permit documentation, and regulatory tools for Nashville DADU projects." — var(--cream)

**Section 1: "Your Legal Toolkit"**
- Background: var(--background) #F2F0ED
- Heading: "Your Legal Toolkit" — var(--slate), Inter, 700
- Grid of tool cards (same card style as other portal pages):

| Tool | Icon | Description | Link |
|------|------|-------------|------|
| Form Wizard | Claims.png | Determine which Metro Nashville forms and applications your client needs for a DADU project. | form_wizard.html |
| PDF Database | Recorded_Docs.svg | Search permits, site plans, property cards, and recorded documents by APN, address, or permit number. | pdf_database_lookup.html |
| Restrictive Covenants | Restrictive_Covenants.svg | Search 43,000+ recorded covenant documents that may restrict DADU construction on a parcel. | restrictive_covenants_v2.html |
| Recorded Documents | Recorded_Docs.svg | Access the full document portal: permits, covenants, site plans, and surveys indexed by parcel. | dadu_documents_portal.html |
| Permit Explorer | Permit_Explorer.svg | Search all Nashville building permits with contractor, cost, timeline, and linked documents. | permit_explorer.html |
| Code & Legislation | Legislation.svg | 111 legal citations database covering all Nashville DADU legislation, Bluebook format. | dadu_code_legislation_v5.html |
| Property Report Card | Property_Detail_Report_.svg | Complete parcel analysis with eligibility, permits, covenants, building specs, and external links. | property-report-card.html |

Each card: var(--card-bg) background, var(--gray-light) border, icon in var(--linen) circle, heading var(--slate), body var(--gray-warm), "Open Tool" link.

**Section 2: "Regulatory Requirements to Know"**
- Background: white
- Heading: "Regulatory Requirements" — var(--slate), Inter, 700
- Subheading: "Key compliance areas for DADU projects" — var(--gray-warm)
- Reference cards (not tool links — these are informational summaries with "Learn More" links):

| Topic | Icon | Summary | Link |
|-------|------|---------|------|
| Owner Occupancy | Owner_Occupancy.svg | BL2025-1007 requires the property owner to occupy either the principal structure or the DADU. A restrictive covenant must be recorded before permit issuance. | owner_occupancy.html |
| Short-Term Rental Restrictions | STR_Permit.svg | New DADUs on single-family, RN, and RL lots are prohibited from obtaining short-term rental permits under the current code. | str_permit.html |
| Restrictive Covenants | Restrictive_Covenants.svg | Property owners must record a restrictive covenant with the Register of Deeds acknowledging owner occupancy and DADU conditions before receiving a building permit. | restrictive_covenants_v2.html |
| Overlay District Requirements | Zoning_Documents.svg | Parcels in DADU Overlays, UDO districts, or Specific Plans may have additional design standards and require Planning Department review. | overlay-districts.html |
| Design Standards | Overlay_Design_Standards.svg | DADUs must match the principal structure in style, materials, color, and roof form. Specific height, dormer, and setback rules apply. | dadu_design_standards.html |
| Trade Permits | Renewals.png | Separate electrical, plumbing, mechanical, and gas permits are required in addition to the building permit. | trade_permits.html |

Each card: lighter treatment than tool cards. White background, left-border accent in var(--slate), summary text, "Learn More >" link.

**Section 3: CTA**
- Background: var(--slate)
- Heading: "Search a Property" — var(--cream), Inter, 700
- Subtitle: "Run a complete eligibility and document analysis for any Nashville parcel." — var(--linen)
- Button: "Property Report Card" → property-report-card.html — var(--wheat) bg, var(--slate) text

**Footer:** Standard shared footer via homebody_header.js

### Style
- Load `homebody_shared.css`
- Inject shared header via `homebody_header.js`
- Match the layout pattern of `homeowner_portal.html` or `contractor_portal.html` (read those files first to match structure)
- No emoji, no #003039, no old colors, Inter font

---

## PART 4: Merge designer_resources.html into designer_portal.html

**Step 1:** Read both files:
```bash
cat designer_resources.html
cat designer_portal.html
```

**Step 2:** Extract all unique content from `designer_resources.html` that does not already exist in `designer_portal.html`. This likely includes building requirements details, precedent gallery references, setback information, and site analysis guidance.

**Step 3:** Add the extracted content as a NEW SECTION at the BOTTOM of `designer_portal.html`, below the existing content. Do not replace or reorganize what's already there. Suggested section heading: "Design Resources & Reference Materials" or similar.

**Step 4:** After confirming all content is merged, flag `designer_resources.html` as absorbed (add to deletion candidates in CLAUDE.md, but do NOT delete yet).

---

## PART 5: Simplify BUILD Dropdown — Remove Columns

**Current structure (three columns):**
- Column 1: "Project Planner" — Planning Hub, Interactive Checklist, Draw DADU on Parcel, Permit Process Timeline
- Column 2: "Calculators" — All Calculators, Size Calculator
- Column 3: "Form Wizard" — Form Wizard

**New structure (single flat list, NO columns, NO column headers):**

| Label | Icon | File |
|-------|------|------|
| Planning Hub | Project_Planner.svg | project_planner_hub.html |
| Interactive Checklist | Project_Checklist.svg | project_checklist.html |
| Draw DADU on Parcel | Draw_on_Parcel.svg | draw_dadu_on_parcel.html |
| Permit Process Timeline | Renewals.png | permit_process_timeline.html |
| All Calculators | Appraisers.svg | dadu_calculators.html |
| Size Calculator | ADU.png | size_calculator.html |
| Form Wizard | Claims.png | form_wizard.html |

Same single-column dropdown styling as WHO WE SERVE (from Part 2). No column headers, no mega-menu width.

---

## PART 6: Add Contractor Report to DATA > Report Generator

### Step 1: Fix contractor_report.html

Read the current file:
```bash
cat contractor_report.html
```

The current version is reportedly about contractors in an AREA (similar to a neighborhood report). That's wrong. The Contractor Report should be about a **specific contractor** — their full permit history, project locations, average costs, permit types, and years active.

**Rewrite the page so it generates a report for a single contractor.** It should:

1. **Search input:** "Enter contractor name or license number" search box at the top
2. **Load data from:** `data/contractor_stats.json` (370 contractors, 628 permits)
3. **Report output for one contractor:**
   - Contractor business name (heading)
   - License number (if available)
   - Total permits completed
   - Total DADU permits specifically
   - Years active (first permit year to last permit year)
   - Total construction value
   - Average cost per project
   - Permit types breakdown (building, DADU, accessory structure, etc.)
   - Zip codes served (list)
   - Individual permit table: permit number, address, date, type, value, status, with links to Nashville permit documents (`https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}`)
4. **Style:** Match the other report pages (eligibility_report.html, project_report.html). Use the standard dark hero, card layout, and brand palette.

### Step 2: Add to DATA > Report Generator Nav

Add "Contractor Report" to the Report Generator column in the DATA dropdown:

| Label | Icon | File |
|-------|------|------|
| Eligibility Report | Claims.png | eligibility_report.html |
| Project Report | Exports__Reports.svg | project_report.html |
| Neighbors Report | Neighbors.svg | neighbors_report.html |
| **Contractor Report** | **Building_and_Construction.svg** | **contractor_report.html** |
| Market Report | Market Statistics Report .svg | dadu_reports_store.html |
| Property Report Card | Property Detail Report .svg | property-report-card.html |

Insert it after Neighbors Report and before Market Report.

---

## CONSTRAINTS (Apply to All Parts)

1. **No emoji.** SVG/PNG icons only.
2. **No #003039.** Use #3A5566.
3. **No old colors** (#6b8fa3, #6b8e4e, #2c3e50, #c9a86c, #e8e4df, #C58B2A, #7A2A1D, #D4A017, #2E6F4E).
4. **Font: Inter** (body and subpage headings). Source Serif 4 for homepage headlines only.
5. **Brand: "Homebody Projects"** user-facing. "Castlehold" only in footer "Powered by".
6. **Logo: ADU.png** (nav), ADU_MultiColors.svg (light backgrounds), ADU_Light2.svg (dark sections).
7. **Nav source of truth:** `homebody_header.js`. Mirror: `homebody_header.html`. Both must match.
8. Provide **complete file contents** for every file touched.
9. Load `homebody_shared.css` and inject header via `homebody_header.js` on all new/modified pages.

---

## CLAUDE.md UPDATES

After all parts complete, update CLAUDE.md:

### Section 4 (Nav Structure):
- WHO WE SERVE: Replace two-column table with single flat list (5 items, no column headers)
- BUILD: Replace three-column table with single flat list (7 items, no column headers)
- DATA > Report Generator: Add Contractor Report row
- RESOURCES > Learn: Remove "Zoning Standards" row

### Section 5 (Current State):
- Move area_analysis_report.html, contractor_advertising.html, dadu_zoning_standards.html to "Previously Deleted"
- Add legal_professionals_portal.html to "Linked in Navigation" under WHO WE SERVE
- Add contractor_report.html to "Linked in Navigation" under DATA > Report Generator
- Move designer_resources.html from "Unlinked but Worth Keeping" to "Unlinked Duplicates (candidates for deletion)" with note: "content absorbed into designer_portal.html"
- Note: "WHO WE SERVE and BUILD dropdowns are now single-column flat lists, not mega-menus"

---

## VERIFICATION

```bash
# Deleted files gone
ls area_analysis_report.html contractor_advertising.html dadu_zoning_standards.html 2>&1 | grep -c "No such file"
# Should be 3

# New file exists
ls legal_professionals_portal.html
# Should exist

# Nav entries removed
grep -c 'contractor_advertising' homebody_header.js
grep -c 'dadu_zoning_standards' homebody_header.js
# Both should be 0

# Legal portal linked
grep -c 'legal_professionals_portal' homebody_header.js
# Should be 1+

# Contractor report in nav
grep -c 'contractor_report' homebody_header.js
# Should be 1+

# WHO WE SERVE has no column headers
grep -c 'User Portals\|Professional' homebody_header.js
# Should be 0 (column headers removed)

# BUILD has no column headers
grep -c 'Project Planner\|Calculators\|Form Wizard' homebody_header.js
# Check these are NOT used as column headers (they may still be labels)

# No banned colors in new files
grep -c '#003039' legal_professionals_portal.html contractor_report.html
# Should be 0

# No emoji in new files
python3 -c "
import re
for f in ['legal_professionals_portal.html', 'contractor_report.html']:
    with open(f) as fh:
        matches = re.findall('[\U0001F300-\U0001F9FF]', fh.read())
        print(f'{f}: {len(matches)} emoji')
"
# Should be 0 for both
```

Visually verify:
1. WHO WE SERVE dropdown is a single narrow column with 5 items, icons visible
2. BUILD dropdown is a single narrow column with 7 items, icons visible
3. Legal Professionals portal loads with tools grid and regulatory reference cards
4. designer_portal.html has the merged content from designer_resources.html at the bottom
5. contractor_report.html search works and generates a report for a single contractor
6. Contractor Report appears in DATA dropdown

```bash
git add -A
git commit -m "Delete 3 pages, simplify WHO WE SERVE + BUILD to flat dropdowns, create legal portal, merge designer resources, add contractor report"
git push origin main
```

---

## IF CONTEXT GETS LONG

Work through parts in order. Do not ask questions. Make reasonable decisions and keep going. Commit after each part.

**If context is getting long or you are losing track:**
1. Finish the current part completely
2. Run its verification checks
3. `git add -A && git commit -m "descriptive message" && git push origin main`
4. Print what you completed and what parts remain
5. STOP

I will start a new session and say "Continue from where you left off, check git log."

**Priority if you can only finish some parts:**
1. Part 1 (deletions) + Part 2 (WHO WE SERVE flatten) — fast, high impact
2. Part 5 (BUILD flatten) — quick, same pattern as Part 2
3. Part 3 (legal portal) — new page, high value
4. Part 6 (contractor report) — rewrite + nav add
5. Part 4 (designer merge) — can wait
