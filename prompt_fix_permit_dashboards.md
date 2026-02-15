# TASK: Fix Two Permit Dashboard Pages — Real Data + DADU Filtering

## Overview

Two permit dashboard pages need fixes. Both have "Castlehold" branding (fix to "Homebody Projects"), and both have data problems.

---

## PAGE 1: permit_activity_dashboard.html → "DADU Activity Dashboard"

### The Problem

This page has a great layout (stats bar, recent activity feed, monthly chart, top zip codes) but ALL the data is **fabricated**. Fake permit numbers ("2026-DADU-0156"), invented addresses, made-up statistics. None of it connects to real data.

### What to Keep
- The overall layout and section structure: stats bar at top, recent activity feed with status tabs, monthly chart, top zip codes table
- The visual design pattern (cards, progress bars on zip codes, status badges)
- The filter tabs (All, New, Approved, Issued, Completed)

### What to Change

**1. Rename to "DADU Activity Dashboard"**
- Title: "DADU Activity Dashboard | Homebody Projects"
- H1: "DADU Activity Dashboard"
- Subtitle: "DADU permit tracking for Nashville-Davidson County"
- Footer: "Homebody Projects" / "Powered by Castlehold"

**2. Connect to real data**

Load data from `data/contractor_stats.json` which has 628 permits (304 DADU-specific). Read the file first to understand its structure:
```bash
cat data/contractor_stats.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(type(d)); print(list(d.keys()) if isinstance(d,dict) else len(d))" 
```

Also check if any of these exist and could provide better data:
```bash
ls data/*.json
```

**3. Stats bar — use REAL numbers from the loaded data**

Calculate from the actual permit records:
- Total DADU Permits: count of DADU-type permits in the dataset
- Permits by year: count for current year vs. previous year (calculate YoY change)
- Average project cost: mean of permit values where value > 0
- Active contractors: count of unique contractors with DADU permits

If a stat cannot be calculated from available data, show "N/A" — never fabricate a number.

**4. Recent Activity feed — use REAL permits**

Pull the most recent permits from the dataset, sorted by date descending. For each permit card show:
- Address (from the data)
- Permit number (real)
- Date (real)
- Square footage (if available, otherwise omit)
- Cost (if available, otherwise omit)
- Status badge (use the real permit status field)
- Link to Nashville permit documents: `https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}`

The status tabs (All, New, Approved, Issued, Completed) should filter the feed by the actual status values in the data. Map whatever status values exist in the data to these display categories. If the data uses different status labels, map them:
- "ISSUED" / "ACTIVE" → Issued
- "COMPLETED" / "CLOSED" / "FINALED" → Completed
- Everything else → show as-is

Show 10-20 most recent permits. Add a "Load More" button if there are more.

**5. Monthly chart — use REAL monthly counts**

Group permits by month/year and show actual counts. Use a simple bar chart or CSS bars (no external charting library required, but Chart.js is fine if already loaded). Show the last 12-24 months.

**6. Top Zip Codes — use REAL zip code counts**

Group DADU permits by zip code, count them, sort descending, show top 5-8. The progress bar width should be proportional to the count (max count = 100% width). Include the neighborhood name if you can map it:
- 37206 = East Nashville
- 37212 = Belmont/12 South  
- 37209 = Sylvan Park/The Nations
- 37208 = Germantown
- 37204 = Berry Hill/Woodbine
- 37211 = South Nashville
- 37207 = North Nashville/Inglewood
- 37210 = Wedgewood-Houston
- 37216 = Inglewood/Madison

If zip codes aren't in the dataset, extract them from addresses or note "Zip data not available" and hide the section.

**7. Fix branding and styling**
- Load homebody_shared.css
- Inject shared header via homebody_header.js
- Remove any hardcoded header/nav
- Fix all colors to current palette (no #003039, no old colors)
- "Castlehold" only in footer "Powered by"
- No emoji

---

## PAGE 2: nashville_permit_analytics.html — Add DADU Filter Toggle

### The Problem

This page loads all Nashville permits dynamically and shows charts + contractor search. It works but has no way to filter to DADU-only permits. The user wants a toggle.

### What to Keep
- ALL existing functionality: charts, contractor search, detail modal, data loading
- The existing layout and chart types

### What to Change

**1. Add a prominent filter toggle at the top of the page, below the stats bar:**

```html
<div class="filter-toggle" style="display: flex; justify-content: center; gap: 0; margin: 20px auto; max-width: 400px;">
  <button class="toggle-btn active" data-filter="all">All Permits</button>
  <button class="toggle-btn" data-filter="dadu">DADU Only</button>
</div>
```

Style:
```css
.toggle-btn {
  padding: 10px 24px;
  font-family: Inter, sans-serif;
  font-size: 14px;
  font-weight: 600;
  border: 2px solid var(--slate);
  background: transparent;
  color: var(--slate);
  cursor: pointer;
  transition: all 0.15s;
}
.toggle-btn:first-child { border-radius: 8px 0 0 8px; }
.toggle-btn:last-child { border-radius: 0 8px 8px 0; }
.toggle-btn.active {
  background: var(--slate);
  color: white;
}
```

**2. Filter logic:**

Read the current JavaScript to understand how data is loaded and what fields are available. Then:

- When "All Permits" is active: show all data (current behavior)
- When "DADU Only" is active: filter the dataset to only permits where the permit type/description/scope contains DADU-related terms. Check what field names exist in the data and filter on terms like:
  - "DADU"
  - "DETACHED ACCESSORY"
  - "ACCESSORY DWELLING"
  - "ADU"
  
  The filter should be case-insensitive and check description/type/scope fields.

- When toggled, ALL charts and stats should re-render with the filtered data:
  - Stats bar recalculates
  - Year chart re-renders
  - Permit type chart re-renders
  - Value distribution chart re-renders
  - Top contractors re-rank based on filtered set
  
- The contractor detail modal should also respect the active filter (show only DADU permits for that contractor when DADU filter is on)

**3. Fix branding**
- Title: "Nashville Permit Analytics | Homebody Projects" (keep "Nashville" since this one covers all permits)
- Footer: "Homebody Projects" / "Powered by Castlehold"
- Load homebody_shared.css, inject shared header
- Fix old colors, remove emoji, Inter font

**4. Do NOT break existing data loading**

The page currently loads data from somewhere (likely a JSON file or inline). Read the source to find the data source. Do not change the data source or format. Only add the filtering layer on top.

---

## CONSTRAINTS

1. **Never fabricate data.** If a stat can't be calculated, show "N/A" or hide the element. Every number on these pages must come from real loaded data.
2. **No emoji.** SVG/PNG icons only.
3. **No #003039.** Replace with #3A5566.
4. **No old colors.**
5. **Font: Inter.** No Montserrat.
6. **Brand: "Homebody Projects"** user-facing. "Castlehold" only in footer.
7. **Load homebody_shared.css** and inject header via `homebody_header.js` on both pages.
8. **Provide complete file contents** for both files.
9. Do not change existing data files. Only read from them.

---

## VERIFICATION

### permit_activity_dashboard.html
```bash
# No fabricated permit numbers
grep -c "2026-DADU-0156\|2026-DADU-0148\|2026-DADU-0132" permit_activity_dashboard.html
# Should be 0

# No hardcoded fake stats
grep -c '"827"\|"156"\|"34"\|"\$153K"' permit_activity_dashboard.html
# Should be 0 (stats should be calculated dynamically)

# Loads real data
grep -c 'contractor_stats\|\.json' permit_activity_dashboard.html
# Should be 1+

# Correct title
grep '<title>' permit_activity_dashboard.html
# Should say "DADU Activity Dashboard | Homebody Projects"

# No banned colors
grep -c '#003039' permit_activity_dashboard.html
# Should be 0
```

### nashville_permit_analytics.html
```bash
# Has filter toggle
grep -c 'data-filter.*dadu\|DADU Only\|toggle-btn' nashville_permit_analytics.html
# Should be 2+

# Correct title
grep '<title>' nashville_permit_analytics.html
# Should say "Nashville Permit Analytics | Homebody Projects"

# No banned colors
grep -c '#003039' nashville_permit_analytics.html
# Should be 0
```

Visual verification:
1. permit_activity_dashboard.html loads with real stats (numbers may differ from old fake ones)
2. Recent activity shows real permit numbers and addresses
3. Monthly chart shows real monthly distribution
4. Top zip codes shows real counts
5. nashville_permit_analytics.html loads with "All Permits" active by default
6. Clicking "DADU Only" re-renders all charts with filtered data
7. Stats bar numbers change when toggling
8. Contractor search still works in both modes

```bash
git add -A
git commit -m "Fix permit dashboards: connect to real data, rename to DADU Activity Dashboard, add DADU filter toggle to analytics"
git push origin main
```

---

## IF CONTEXT GETS LONG

Do permit_activity_dashboard.html first (it's the bigger fix). If context runs out, commit that and stop. The nashville_permit_analytics.html filter toggle can be done in a follow-up session.
