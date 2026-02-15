# TASK: Consolidate Reports into Single Report Generator Landing Page

## Overview

The DATA dropdown currently lists 5 individual report pages. That's too granular for a nav dropdown. Instead, "Report Generator" should be a single link to one landing page that showcases all report types with descriptions, buttons to the live report tools, and links to sample reports.

---

## PART 1: Restructure DATA Dropdown

### Current DATA dropdown (two columns):

**Column 1: Report Generator**
- Eligibility Report → eligibility_report.html
- Project Report → project_report.html
- Neighbors Report → neighbors_report.html
- Market Report → dadu_reports_store.html
- Property Report Card → property-report-card.html

**Column 2: Document Database**
- Site Plans & Permits → site_plan_downloads.html
- Recorded Documents → dadu_documents_portal.html
- Restrictive Covenants → restrictive_covenants_v2.html
- PDF Database → pdf_database_lookup.html

### New DATA dropdown (two columns):

**Column 1: Reports** (Icon: Exports__Reports.svg)

| Label | Icon | File |
|-------|------|------|
| Report Generator | Exports__Reports.svg | dadu_reports_store.html |

That's it. ONE link. The landing page handles everything else.

**Column 2: Document Database** (Icon: Recorded_Docs.svg)

| Label | Icon | File |
|-------|------|------|
| Site Plans & Permits | Permit_Site_Plans.svg | site_plan_downloads.html |
| Recorded Documents | Recorded_Docs.svg | dadu_documents_portal.html |
| Restrictive Covenants | Restrictive_Covenants.svg | restrictive_covenants_v2.html |
| PDF Database | Recorded_Docs.svg | pdf_database_lookup.html |

Document Database stays exactly as-is. No changes.

Update `homebody_header.js` and `homebody_header.html` with this new structure.

---

## PART 2: Rebuild dadu_reports_store.html as the Master Report Generator

### Page Structure

**Hero:**
- Background: var(--slate) #3A5566
- Icon: Exports__Reports.svg (large, in linen circle)
- Headline: "Report Generator" — white, Inter, 800
- Subtitle: "Property intelligence reports built from Nashville's public permit, parcel, and regulatory data." — var(--cream)
- Stats row: "6 Report Types" | "285,512 Parcels" | "4,700+ Permits" | "12,500+ Documents"

**Section: "Choose a Report"**
- Background: var(--background) #F2F0ED
- Grid of report cards, one per report type
- Each card has:
  - Icon in var(--linen) circle (48px)
  - Report name (var(--slate), Inter, 700, 18px)
  - Price badge (e.g., "$4.99" in small pill, var(--wheat) bg)
  - Description paragraph (var(--gray-warm), 14px, 3-4 sentences)
  - "What's Included" bullet list (short, 4-6 items)
  - Two buttons side by side:
    - "Generate Report" (var(--wheat) bg, var(--slate) text, bold) → links to the live report tool page
    - "View Sample" (outline button, var(--slate) border, var(--slate) text) → links to the sample report page
  - "Popular with:" tag line at bottom (small, var(--stone) text) showing user types

### The 6 Report Types (in this order on the page):

**1. DADU Eligibility Report**
- Icon: Claims.png
- Price: $4.99
- Description: Instant eligibility determination for any Nashville parcel under BL2025-1007. Covers zoning classification, service district (USD/GSD), lot size analysis, maximum DADU dimensions, height restrictions, and owner occupancy requirements. Identifies potential issues including overlay districts, restrictive covenants, and historic designations.
- What's Included:
  - Zoning and service district verification
  - Maximum living area and footprint calculations
  - Height limit based on principal structure
  - Restrictive covenant flag
  - Overlay district check
  - Owner occupancy requirement summary
- Generate Report → eligibility_report.html
- View Sample → sample_reports/sample_eligibility_report.html
- Popular with: Homeowners, Real Estate Agents, Attorneys

**2. Property Report Card**
- Icon: Property_Detail_Report_.svg
- Price: $4.99
- Description: Complete parcel intelligence for any Nashville property. Combines assessor data, building characteristics, permit history, covenant records, and external portal links into one consolidated view. Includes aerial imagery, street view, and direct links to Metro Nashville verification portals.
- What's Included:
  - Parcel details (lot size, zoning, assessed value)
  - Building characteristics (year built, sqft, stories)
  - Permit history with document links
  - Restrictive covenant records
  - Aerial view and street view
  - Links to ParcelViewer, ePermits, Assessor, Property Card
- Generate Report → property-report-card.html
- View Sample → sample_reports/sample_property_report.html
- Popular with: Homeowners, Appraisers, Investors

**3. Neighbors Report / Area Comparables**
- Icon: Neighbors.svg
- Price: $14.99
- Description: Analysis of all DADU activity within a neighborhood or zip code. Shows permitted and completed DADUs near any address, with construction costs, timelines, contractors used, and building sizes. Identifies the most active builders and cost trends in the area.
- What's Included:
  - All DADUs within selected radius
  - Average construction cost and cost per SF
  - Most active contractors in area
  - Permit timeline statistics
  - Cost trends over time
  - Comparable project details
- Generate Report → neighbors_report.html
- View Sample → sample_reports/sample_neighbors_report.html
- Popular with: Homeowners, Investors, Contractors

**4. Contractor Report**
- Icon: Building_and_Construction.svg
- Price: $9.99
- Description: Complete permit history for any Nashville DADU contractor. Search by contractor name or license number to see every project they have completed, average costs, zip codes served, permit types, and years active. Each permit links directly to Nashville's official permit documents.
- What's Included:
  - Total permits and DADU permits
  - Average cost per project
  - Zip codes served
  - Years active
  - All individual permits with document links
  - Permit type breakdown
- Generate Report → contractor_report.html
- View Sample → sample_reports/sample_contractor_report.html
- Popular with: Homeowners, Contractors, Investors
- NOTE: This report searches by CONTRACTOR, not by area. It shows one contractor's full history.

**5. Project Report**
- Icon: Project_Planner.svg
- Price: $9.99
- Description: Planning-stage analysis for a specific DADU project. Combines eligibility data with cost estimates, permit requirements, and timeline projections based on comparable projects in the same area. Includes required forms checklist and recommended contractors.
- What's Included:
  - Eligibility summary
  - Estimated construction cost range
  - Required permits and forms list
  - Comparable project costs in area
  - Estimated timeline based on similar permits
  - Recommended contractors (by area activity)
- Generate Report → project_report.html
- View Sample → (no sample exists — use "Coming Soon" button styled as disabled/grayed out)
- Popular with: Homeowners, Designers, Contractors

**6. Market Statistics Report**
- Icon: Market_Statistics_Report_.svg
- Price: $14.99
- Description: Nashville DADU market analysis covering permit activity trends, construction costs, contractor market share, and demand by zip code. Covers historical data from 2017 through present with year-over-year comparisons.
- What's Included:
  - Permit volume by year and month
  - Average construction cost trends
  - Top contractors by permit count and value
  - Activity by zip code
  - Permit type distribution
  - Year-over-year growth rates
- Generate Report → nashville_permit_analytics.html (this is the analytics dashboard, which serves as the market report)
- View Sample → sample_reports/sample_market_stats_report.html
- Popular with: Investors, Contractors, Municipal Staff

### Additional Sample Reports (link at bottom)

Below the 6 main report cards, add a section:

**"Additional Sample Reports"**
- Background: var(--card-bg)
- Small cards or a simple list showing the remaining sample reports that don't map 1:1 to the main 6:
  - Covenant Analysis Report → sample_reports/sample_covenant_report.html
  - Permit History Report → sample_reports/sample_permit_history_report.html
  - Cost Estimate Report → sample_reports/sample_cost_estimate_report.html
  - Zoning Verification Report → sample_reports/sample_zoning_report.html
- Label: "These sample reports demonstrate additional analysis available within the platform."

### Bottom CTA

- Background: var(--slate)
- Heading: "Need a Custom Analysis?" — var(--cream)
- Subtitle: "Contact us for bulk reports, custom data exports, or enterprise pricing." — var(--linen)
- Button: "Contact Us" (mailto:hello@castlehold.com) — var(--wheat) bg, var(--slate) text

---

## PART 3: Fix contractor_report.html

Read the current file. If it searches by AREA (showing contractors in a neighborhood), rewrite it to search by CONTRACTOR instead. This was specified in the earlier nav prompt (prompt_nav_simplify_legal_portal_deletions.md, Part 6) but repeating here for completeness:

- Search input: "Enter contractor name or license number"
- Load from: data/contractor_stats.json
- Report output for ONE contractor: name, license, total permits, DADU permits, years active, total value, average cost, zip codes, permit types, individual permit table with Nashville document links
- If this was already done in a previous task, skip it.

---

## PART 4: Delete Duplicate/Obsolete Report Pages

**Before deleting `dadu_report_full.html`:** Check if `property-report-card.html` has an aerial image embed (Patriot Properties iframe/link) and a Google Street View embed. If NOT, extract those sections from dadu_report_full.html and add them to property-report-card.html BEFORE deleting.

Aerial URL pattern:
```
https://portal.patriotproperties.com/?APIKEY=5D050659143EB96630FB38B91DE12E40&SECRETKEY=A92169630C9BC3C00A1C0F9F140E6DAEC21C8E62DCFF9FC443FB1BE70DDF6AA4268527B9DDE2ECC2C7EE9BB5BF728C06F0DF4019BBECDEBD2A6DD0BBE28A419D8F929E1F3E8DF478E56619995BEFCA8E369276689D791197DC1284F14B3252DBFB2A19A2E451EEA832D6D96488DDC673EBA4B37BD741223B656A793D93209C0F&LAT={lat}&LONG={lon}
```

Street View URL pattern:
```
https://www.google.com/maps?q&layer=c&cbll={LATITUDE},{LONGITUDE}
```

**Then delete:**
```bash
git rm dadu_report_full.html
git rm dadu_report_connected.html
git rm dadu_property_report.html
git rm property_report.html
git rm property_intelligence_report.html
```

These are all older/duplicate report pages whose content is covered by the 6 report types above.

**Also delete (if not already deleted by a previous task):**
```bash
git rm area_analysis_report.html 2>/dev/null
git rm dadu_zoning_standards.html 2>/dev/null
```

---

## PART 5: Update CLAUDE.md

### Section 4 (Nav Structure) — DATA dropdown:
Replace the Report Generator column with:

**Column 1: Reports** (Icon: Exports__Reports.svg)
| Label | Icon | File |
|-------|------|------|
| Report Generator | Exports__Reports.svg | dadu_reports_store.html |

(Single link. All report types live on the landing page.)

### Section 5 (Current State):
- Move to "Previously Deleted": dadu_report_full.html, dadu_report_connected.html, dadu_property_report.html, property_report.html, property_intelligence_report.html
- Note: "dadu_reports_store.html is the master Report Generator landing page. Individual report tools (eligibility_report.html, property-report-card.html, neighbors_report.html, contractor_report.html, project_report.html) are linked FROM dadu_reports_store.html but not directly in the nav dropdown."
- Note: "Sample reports in sample_reports/ folder are linked from dadu_reports_store.html as preview/demo content."

---

## CONSTRAINTS

1. **No emoji.** SVG/PNG icons only.
2. **No #003039.** Use #3A5566.
3. **No old colors.**
4. **Font: Inter.**
5. **Brand: "Homebody Projects"** user-facing. "Castlehold" only in footer and contact email.
6. Load `homebody_shared.css` and inject header via `homebody_header.js`.
7. Provide **complete file contents** for dadu_reports_store.html and any modified files.
8. Do NOT delete the sample_reports/ folder or any sample report files.
9. Do NOT delete the individual report tool pages (eligibility_report.html, property-report-card.html, etc.) — they stay as the actual report generators. Only the nav links to them are consolidated.

---

## VERIFICATION

```bash
# DATA dropdown has single Report Generator link
grep -A5 'Report Generator' homebody_header.js | head -10
# Should show ONE entry pointing to dadu_reports_store.html

# Individual report pages NOT in nav dropdown
grep -c 'eligibility_report\|project_report\|neighbors_report' homebody_header.js
# Should be 0 (they're on the landing page, not in nav)

# Landing page links to all 6 report tools
grep -c 'eligibility_report\|property-report-card\|neighbors_report\|contractor_report\|project_report\|nashville_permit_analytics' dadu_reports_store.html
# Should be 6

# Landing page links to sample reports
grep -c 'sample_reports/' dadu_reports_store.html
# Should be 8+ (6 main samples + 4 additional)

# Deleted files gone
ls dadu_report_full.html dadu_report_connected.html dadu_property_report.html property_report.html property_intelligence_report.html 2>&1 | grep -c "No such file"
# Should be 5

# Property report card has aerial embed
grep -c 'patriotproperties\|aerial\|street.*view' property-report-card.html
# Should be 1+ (aerial section preserved from dadu_report_full.html)

# No banned colors in new landing page
grep -c '#003039' dadu_reports_store.html
# Should be 0
```

Visual verification:
1. DATA dropdown shows "Report Generator" as single link, Document Database column unchanged
2. dadu_reports_store.html loads with hero, 6 report cards, additional samples section, CTA
3. Each "Generate Report" button goes to the correct live tool page
4. Each "View Sample" button goes to the correct sample_reports/ page
5. Contractor Report card says "search by contractor" not "search by area"
6. property-report-card.html has aerial view section (preserved from deleted page)
7. All sample report links work

```bash
git add -A
git commit -m "Consolidate reports: single Report Generator landing page, simplify DATA nav, delete 5 duplicate report pages"
git push origin main
```

---

## IF CONTEXT GETS LONG

Priority order:
1. Rebuild dadu_reports_store.html (the landing page) — most important
2. Update DATA dropdown in homebody_header.js
3. Preserve aerial embed from dadu_report_full.html → property-report-card.html
4. Delete duplicate pages
5. Fix contractor_report.html (if not already done)
