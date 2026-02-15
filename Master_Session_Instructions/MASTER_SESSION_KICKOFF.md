# HOMEBODY PROJECTS — NEW SESSION KICKOFF
## Read This First Before Doing Anything

### What This Project Is
Homebody Projects is a DADU (Detached Accessory Dwelling Unit) platform for Nashville-Davidson County, hosted on GitHub Pages at https://nataliebaldacci.github.io/DADU-Homebody-Projects/. It has ~87 HTML pages, shared navigation, ArcGIS map integrations, and JSON data files.

### Source of Truth
**Read `CLAUDE.md` in the repo root FIRST.** It is version 5.0 and contains the locked palette, nav structure, page inventory, branding rules, and priority list. Everything below supplements CLAUDE.md — it does not override it.

### What Was Just Completed (Last Session, Feb 14-15, 2026)
1. **contractor_dashboard.html** — Fully redesigned, connected to live `data/contractor_stats.json` (370 contractors, 628 permits). Working search, filters, sort, detail modals. DONE.
2. **Logo visibility** — Audited. ADU_Light2.svg only appears on dark nav (correct). No invisible logos on light backgrounds. DONE.
3. **dadu_eligibility_flowchart.html** — Rebuilt with correct Nashville.gov eligibility order (Land Use Table → Lot Area → Service District → Single Structure → Conditions → Special Cases). Has 45+ external links. Added to RESOURCES > Learn nav. DONE but currently STATIC — needs to be made interactive (Task 1 below).
4. **dadu_eligibility_checklist.html** — Deleted (content absorbed into flowchart). DONE.
5. **Nav updated** — homebody_header.js and homebody_header.html both have the flowchart entry. DONE.

---

## TASK QUEUE — Execute In This Order

### TASK 1: Make Eligibility Flowchart Interactive
**File:** `dadu_eligibility_flowchart.html`
**Priority:** HIGH — user specifically requested this

The flowchart has all the correct content and 45+ links but displays everything at once. Make it a step-through wizard:

- On load, only Step 1 visible. Progress bar shows "Step 1 of 6"
- Each step has YES / NO buttons. YES collapses the step into a summary bar and reveals the next step with smooth scroll. NO shows a "Not Eligible" result card.
- Step 3 (Service District) is special — show 5 option buttons: "I'm in the USD", "I have a DADU Overlay (GSD)", "I'm in a UDO with DADU standards", "I'm in an SP with DADU standards", "None of the above"
- Step 5 (Conditions) is informational, not a gate. Show checklist then "Continue" button.
- Step 6 (Special Cases) is informational. Then show final "Eligible" result.
- Result cards: Eligible (#406A64 bg), Not Eligible (#B58676 bg), Conditional (#918A83 bg)
- "Show All Steps" toggle for people who want to read the static version
- "Start Over" resets to Step 1
- Completed steps collapse to summary with "Change Answer" link
- **Do NOT remove any external links.** All 45+ must remain. Verify with grep after.
- **Do NOT change step order, content, or branding.**
- Provide complete file contents.

### TASK 2: Fix Styling on Three Pages
**Files:** `trade_permits.html`, `contractor_dashboard.html`, `overlay-districts.html`

NOTE: contractor_dashboard.html was just redesigned — it may already be correct. Audit it first; only fix if needed.

For each page, fix:
- Title says "Castlehold" → change to "Page Name | Homebody Projects"
- Missing shared header → add `homebody_header.js` + `homebody_shared.css`, remove hardcoded nav
- Old hardcoded colors → replace with CSS variables (see CLAUDE.md Section 3 replacement table)
- Emoji icons → replace with SVG/PNG from assets/icons/ or remove
- Wrong font (Montserrat/Arial) → Inter
- Old/missing footer → shared footer

**Keep all content, data, links, and functionality intact.** Styling-only pass.

Audit first:
```bash
for page in trade_permits.html contractor_dashboard.html overlay-districts.html; do
  echo "=== $page ==="
  grep -i '<title>' "$page"
  grep -c 'homebody_shared.css' "$page"
  grep -c 'homebody_header.js' "$page"
  grep -c '#003039' "$page"
  grep -c '#2c3e50\|#6b8fa3\|#6b8e4e' "$page"
  echo "---"
done
```

### TASK 3: Create About Page
**File:** `about_platform.html` (new)

Merge content from these sources into one comprehensive About page:
- `features.html` (unlinked orphan — full feature grid + data sources)
- `feature-documents.html` and `feature-eligibility-map.html` (unlinked orphans — "What It Does / How It Works / Data Sources" pattern)
- Platform info previously in deleted `about_platform_infographic.html`

**Page structure (7 sections):**
1. **Hero** — dark (#3A5566), stats row (285K parcels, 67K eligible, 827 permits, 12.5K docs), ADU_Light2.svg logo
2. **"What Is Homebody Projects?"** — two columns: platform description left, Vanderbilt project callout right (one of the allowed Castlehold placements)
3. **"Platform Features"** — 3 category groups: Discovery Tools (4 cards), Documents & Data (4 cards), Planning Tools (4 cards). Each links to real tool page.
4. **"How It Works"** — 4 numbered steps: Search → Check Eligibility → Review Documents → Plan
5. **"Data Sources"** — dark section, 6 source cards: Metro Codes, Assessor, Planning, Register of Deeds, Nashville GIS, Third-Party Validation
6. **"Built For Every User"** — user type cards linking to portals
7. **CTA** — "Check Eligibility Now" → am_i_eligible.html

**Nav change:** ABOUT → `about_platform.html` (currently routes to `homebody_dadu_pricing.html#about`). Update in homebody_header.js AND homebody_header.html.

After building, flag these as absorbed (do NOT delete yet): features.html, feature-documents.html, feature-eligibility-map.html, user-types.html

### TASK 4: Merge Contractor Advertising
**Files:** `contractor_portal.html`, `homebody_dadu_pricing.html`, `homebody_header.js`, `homebody_header.html`

1. Add "Promote Your Business" section to `contractor_portal.html` with `id="advertise"` anchor. Three tiers: Featured Listing, Sponsored Results, Lead Generation. "Contact Us" buttons (mailto:hello@castlehold.com). No Stripe yet.
2. Add contractor pricing track to `homebody_dadu_pricing.html`: tab switcher "For Homeowners" | "For Contractors". Placeholder pricing $29/$79/$149 mo.
3. Update nav: WHO WE SERVE > Professional > "Advertise With Us" href from `contractor_advertising.html` to `contractor_portal.html#advertise`
4. Do NOT delete contractor_advertising.html (just delink from nav)

### TASK 5: ADU Infographic + Contractor Nav Move
**Files:** `what_is_dadu.html`, `homebody_shared.css`, `homebody_header.js`, `homebody_header.html`

1. Copy `New_Icons/ADU_Types_Recolored.png` to `assets/images/adu_types_homebody.png`. Insert as `<figure class="edu-figure">` with caption after intro section of what_is_dadu.html. Add CSS classes to homebody_shared.css.
2. Move `contractor_dashboard.html` from EXPLORE > Dashboards to BUILD dropdown. Label: "Find a Contractor", icon: Building_and_Construction.svg. Keep "Contractor Marketplace" in EXPLORE unchanged.

### TASK 6: Documents Portal + External Links Nav
**Files:** `homebody_dadu_pricing.html`, `homebody_header.js`, `homebody_header.html`

1. Remove `dadu_documents_portal.html` from DATA > Document Database nav
2. Add "Document Portal" section to `homebody_dadu_pricing.html` below pricing cards. CTA button links to dadu_documents_portal.html.
3. Add `dadu_resources.html` to DATA > Document Database as "External Links" (icon: Recorded_Docs.svg) in the slot vacated by documents portal.

### TASK 7: Delete 24 Duplicate Pages
**Confirmed for deletion** (dadu_eligibility_checklist.html already deleted in last session):

```bash
git rm am_i_eligible_compact.html castlehold_homepage_flat.html dadu_build_explorer.html dadu_build_explorer_v2.html dadu_build_tool.html dadu_build_tool_backup.html dadu_explorer_attom.html dadu_explorer_attom_v2.html dadu_explorer_v2.html dadu_near_me_locator.html dadu_near_me_v3.html dadu_platform.html dadu_property_report.html dadu_property_viewer_v3.html dadu_report_connected.html dadu_report_full.html dadu_resources.html dadu_symbium_map.html footprints_proof_of_concept.html homebody_index.html homebody_index_v3.html homebody_index_v4.html homebody_main.html index_pq.html nashville_permit_explorer_v3.html
```

**WAIT — before deleting `dadu_report_full.html`:** Check if `property-report-card.html` (the active report card) has an aerial image embed. If NOT, extract the aerial section from `dadu_report_full.html` and add it to `property-report-card.html` BEFORE deleting. The aerial URL pattern is:
```
https://portal.patriotproperties.com/?APIKEY=5D050659143EB96630FB38B91DE12E40&SECRETKEY=A92169630C9BC3C00A1C0F9F140E6DAEC21C8E62DCFF9FC443FB1BE70DDF6AA4268527B9DDE2ECC2C7EE9BB5BF728C06F0DF4019BBECDEBD2A6DD0BBE28A419D8F929E1F3E8DF478E56619995BEFCA8E369276689D791197DC1284F14B3252DBFB2A19A2E451EEA832D6D96488DDC673EBA4B37BD741223B656A793D93209C0F&LAT={lat}&LONG={lon}
```
Also check for Google Street View embed:
```
https://www.google.com/maps?q&layer=c&cbll={LATITUDE},{LONGITUDE}
```
Both should be on the active property report card as iframe or link.

### TASK 8: Branding Sweep (All Pages)
Run across ALL ~60 remaining HTML files:
1. Replace old colors using CLAUDE.md Section 3 replacement table
2. Replace "CASTLEHOLD" with "Homebody Projects" in titles and body (keep ONLY in footer "Powered by" lines and reports/data attribution)
3. Ensure every page loads `homebody_shared.css`
4. Ensure every page injects shared header via `homebody_header.js`
5. Remove all emoji characters — replace with SVG/PNG icons or plain text
6. Replace Montserrat font references with Inter

Verification:
```bash
grep -rl "#003039" --include="*.html" --include="*.css" --include="*.js" . | wc -l  # should be 0
grep -rl "#2c3e50\|#6b8e4e\|#e8e4df\|#6b8fa3\|#c9a86c" *.html | wc -l  # should be 0
grep -l "CASTLEHOLD" *.html  # only footer/report pages
```

### TASK 9: Verify Maps Render
Check these 8 map pages actually render (not blank):
- dadu_eligibility_map.html (MOST IMPORTANT)
- property_search.html
- dadu_near_me_v2.html
- dadu_opportunity_explorer_v2.html
- permit_explorer.html
- parcel_footprint_map.html
- adu_permit_map.html
- homebody_index_map.html

Common problems: map container has no height, CDN libraries missing, basemap changed without permission. Fix height/CDN issues. Do NOT change basemaps.

### TASK 10: Homepage Refresh
Rebuild `index.html` to match the spec in CLAUDE.md Section 6B. It has 8 detailed sections with exact colors, links, and card content specified.

---

## CRITICAL CONSTRAINTS (Apply to ALL Tasks)

### Branding
- User-facing brand = **"Homebody Projects"**
- "Castlehold" appears ONLY in: footer "Powered by" line, reports, data attribution, legal pages
- Logo: **ADU.png** (nav), **ADU_MultiColors.svg** (light backgrounds), **ADU_Light2.svg** (dark sections only)
- **No castle logo anywhere**

### Palette (Locked — from CLAUDE.md Section 3)
```
Core:       #3A5566 (Deep Slate), #2F3A45 (True Dark), #496778 (Slate Mid)
Stone:      #7B746D (Warm Stone), #918A83 (Lighter Stone), #706F6C (Gray Warm)
Accent:     #CBB279 (Wheat)
Neutrals:   #E1D4BB (Cream), #E2E2E0 (Light Gray), #F0EBE1 (Linen), #F2F0ED (Background), #F5F5F0 (Card)
Functional: #406A64 (Eligible), #B58676 (Not Eligible), #918A83 (Conditional)
```

### BANNED
- **#003039** — replace with #3A5566 everywhere
- **Old colors:** #6b8fa3, #6b8e4e, #2E6F4E, #D4A017, #C58B2A, #7A2A1D, #c9a86c, #e8e4df, #2c3e50, #B55A3C
- **Emoji** — zero emoji anywhere, use SVG/PNG icons
- **Castle logo** — only ADU.png / ADU variants
- **Montserrat font** — use Inter

### Typography
- Body: Inter
- Homepage headlines ONLY: Source Serif 4 (serif, italic)
- Subpage headings: Inter (not serif)

### Navigation
- Source of truth: `homebody_header.js`
- Static mirror: `homebody_header.html` — must always match
- Structure: WHO WE SERVE | EXPLORE | BUILD | DATA | RESOURCES | PRICING | ABOUT

### Files
- Never overwrite — create new versions
- Never delete /samples/ folder contents
- Provide complete file contents for every file touched
- Git commit with descriptive message after each task group

---

## EXECUTION APPROACH

1. Read `CLAUDE.md` first
2. For each task, audit the current state before changing anything
3. Run verification commands after each task
4. Commit after each completed task (not all at once)
5. If a task is too large for one pass, break it into sub-commits
6. If context is running long, prioritize Tasks 1-3 (flowchart interactivity, three page styling, about page) — these are the most impactful

---

## DETAILED PROMPT FILES

If you need more specific instructions for any task, these detailed prompt files exist in the repo or can be provided:

| Task | Detailed Prompt File |
|------|---------------------|
| Task 1: Interactive Flowchart | prompt_interactive_eligibility_flowchart.md |
| Task 2: Three Page Styling | prompt_fix_three_page_styling.md |
| Task 3: About Page | prompt_create_about_page.md |
| Task 4: Contractor Advertising | prompt_merge_contractor_advertising.md |
| Task 5: Infographic + Nav | prompt_infographic_and_contractor_nav.md |
| Task 6: Docs Portal + Links | prompt_documents_portal_and_external_links.md |

Ask the user to paste any of these if you need the full details.
