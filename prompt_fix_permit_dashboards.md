# TASK: Fix Three Dashboard Pages — Real Data, DADU Filtering, Market Trends

## Overview

Three dashboard pages need fixes. All have "Castlehold" branding (fix to "Homebody Projects"), and all have data problems.

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

**2. Connect to real data — AUDIT LOCAL DATA FIRST**

Before using `data/contractor_stats.json` (which only has 628 permits, 304 DADU), check for richer datasets. Run this audit:

```bash
# Step 1: Check the FINAL_FINAL folder for latest processed data
ls -lhS ~/Documents/GitHub/DADU-Homebody-Projects/DADU/FINAL_FINAL/*.csv 2>/dev/null | head -20
ls -lhS ~/Documents/GitHub/DADU-Homebody-Projects/DADU/FINAL_FINAL/*.json 2>/dev/null | head -10

# Step 2: Check the repo data/ folder
ls -lhS data/*.json | head -15

# Step 3: Check the repo root for CSV files
ls -lhS *.csv 2>/dev/null | head -10

# Step 4: Preview the most promising files
# Look for files with permit data (dates, costs, sqft, contractors, addresses, zip codes)
head -1 ~/Documents/GitHub/DADU-Homebody-Projects/DADU/FINAL_FINAL/*.csv 2>/dev/null | head -40
```

**Choose the BEST available dataset** based on these criteria (in priority order):
1. Has the most DADU permits (not all permits — filtered to DADU/ADU type)
2. Has cost, sqft, date, address, zip code, contractor, status fields
3. Has real permit numbers (not fabricated)
4. Is the most recent version (check dates in filenames)

Known candidates to look for:
- `DADU_All_Permits_Cleaned.csv` (4,700+ permits in repo root) — likely the richest
- `MASTER_ALL_DADU_Permits_Combined.csv` or `MASTER_ALL_DADU_Permits_Deduplicated.csv` in MASTER_ADU_DATA/
- Any file in FINAL_FINAL/ with "permit" or "DADU" in the name
- `data/permits_with_apn.json` (13MB, may have more records)
- `data/contractor_stats.json` (628 permits — use as FALLBACK only)

**Once you identify the best file:**
1. If it's a CSV not already in `data/`, convert it to a lightweight JSON and save to `data/` with a descriptive name (e.g., `data/dadu_permits_dashboard.json`)
2. Only include the fields needed for the dashboard: permit_number, address, date, status, cost, sqft, contractor_name, zip_code, APN, latitude, longitude
3. If the full dataset exceeds 5MB as JSON, filter to DADU-only permits before saving
4. `git add` the new JSON file and commit it with the dashboard changes so the page has real data on GitHub Pages

**Do NOT skip this step.** The old contractor_stats.json was a summary file with limited fields. The FINAL_FINAL folder and repo root likely have thousands more permits with richer data.

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

However, if the page currently loads from a source that lacks DADU-type identifiers (making the DADU filter useless), consider also loading the richer dataset created in Page 1 (`data/dadu_permits_dashboard.json`) alongside the existing data, and using it to cross-reference which permits are DADU-type by permit number.

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
git commit -m "Fix dashboards: real data for activity + market trends, DADU filter toggle for analytics"
git push origin main
```

---

## IF CONTEXT GETS LONG

Do permit_activity_dashboard.html first (it's the bigger fix). Then market_trends.html (Page 3). If context runs out, commit and stop. The nashville_permit_analytics.html filter toggle (Page 2) can be done in a follow-up session since it's the smallest change.

---

## PAGE 3: market_trends.html — Connect Charts to Real Data

### The Problem

This page has a GREAT layout with charts, neighborhood cost tables, yearly permit volume, and a cost breakdown. The user likes the visual structure. But every single number is fabricated: "$185 Avg Cost per SF," "156 Permits YTD 2026," "287 permits in 2025," specific neighborhood $/SF values, fake trend percentages, and an invented cost breakdown.

### What to Keep (the layout and visual patterns)
- Stats bar at top (4 stat cards with trend arrows)
- "Cost Trends" section with chart area
- "Key Insights" cards (3 insight boxes)
- "Cost by Neighborhood" table (zip code, avg $/SF, trend)
- "Yearly Permit Volume" table (year, count, change %)
- "Cost Breakdown" section (itemized construction costs)
- Overall card styling, progress bars, section headers

### What to Change

**1. Title and branding**
- Title: "DADU Market Trends | Homebody Projects"
- H1: "Nashville DADU Market Trends"
- Load homebody_shared.css, inject shared header via homebody_header.js
- Remove hardcoded nav/header
- Fix all colors to current palette (no #003039, no old colors)
- "Castlehold" only in footer
- No emoji, Inter font

**2. Load real data**

Use the same dataset identified in the Page 1 audit above. If you already created `data/dadu_permits_dashboard.json` for the activity dashboard, load it here too. Also check:
```bash
ls data/permits_with_apn.json data/zipcode_pricing_data.json data/permit_analytics.json 2>/dev/null
```

The market trends page needs cost, sqft, date, zip code, and contractor fields. Use whichever JSON files have the richest data for these fields. The dataset from FINAL_FINAL/ or the repo root CSV will almost certainly have more records than the old summary JSONs.

**3. Stats bar — calculate from REAL data**

From the loaded permit data, calculate:
- **Avg Cost per SF**: mean of (cost / sqft) where both values > 0. If cannot calculate, show "N/A"
- **Total DADU Permits**: count from the data
- **Avg DADU Size**: mean of sqft values where sqft > 0. If cannot calculate, show "N/A"
- **Avg Permit Time**: If the data has both issued and completed dates, calculate the average difference in days. If not available, show "N/A"

For the trend arrows/percentages: only show a trend if you can actually calculate year-over-year from the data. If you can compare current year to previous year counts, show the real percentage. Otherwise remove the trend badges entirely rather than faking them.

**4. Cost by Neighborhood table — use REAL zip code data**

Group DADU permits by zip code. For each zip that has permits with cost and sqft data:
- Calculate actual avg $/SF for that zip
- Only show zips that have 3+ permits with cost data (small samples are unreliable)
- Sort by avg $/SF descending
- Show the real count of permits per zip in a column

Neighborhood name mapping (include these):
- 37205 = Belle Meade
- 37215 = Green Hills
- 37212 = 12 South / Belmont
- 37206 = East Nashville
- 37209 = Sylvan Park / The Nations
- 37208 = Germantown
- 37204 = Berry Hill / Woodbine
- 37211 = South Nashville
- 37216 = Inglewood / Madison
- 37210 = Wedgewood-Houston

For the "trend" column: Only show a real YoY trend if you can calculate it from the data (compare avg $/SF this year vs last year for that zip). Otherwise remove the trend column and replace with a "Permits" count column.

**5. Yearly Permit Volume table — use REAL yearly counts**

Group permits by year, count them. Show actual counts and actual YoY percentage change. Do NOT invent years that have zero permits. Only show years present in the data.

**6. Cost Breakdown section — use REAL data or mark as estimates**

The current cost breakdown shows specific dollar amounts for Foundation, MEP, Interior, Permits, etc. We do NOT have itemized cost breakdowns in our data (permits only show total construction value).

Two options (pick whichever is more honest):

**Option A (preferred):** Replace the fake itemized breakdown with a REAL cost distribution chart based on actual permit data:
- Show a histogram or bar chart of total DADU construction costs (e.g., how many permits at $50-100K, $100-150K, $150-200K, $200-250K, $250K+)
- Label it "DADU Construction Cost Distribution"
- This uses real data and is genuinely useful

**Option B:** Keep the itemized layout but clearly label it "Industry Estimates (not Nashville-specific)" and cite a source like "Based on typical ADU construction cost ratios, HomeAdvisor 2025" — but do NOT present it as Nashville permit data.

**7. Key Insights cards — rewrite with real data**

The three insight boxes currently say specific things about BL2025-1007 impact (fine to keep, that's legislation not data), "hot markets" with fake percentages, and modular vs custom costs (we don't have this data).

Rewrite each insight card to reference real findings:
- **Card 1 - BL2025-1007 Impact**: Keep. The 67,707 parcels and 340% increase are verified. Fine as-is.
- **Card 2 - Most Active Areas**: Replace fake "17% of all permits" with real top zip code from the data. "East Nashville (37206) leads with [X] DADU permits, followed by [zip] and [zip]."
- **Card 3 - Cost Ranges**: Replace fake modular/custom comparison with actual cost range from the data. "Nashville DADU construction costs range from $[min] to $[max], with a median of $[median] based on [N] permits with reported values."

**8. Cost Trends chart**

If you can calculate avg $/SF by quarter or by year, render a real line chart or bar chart showing the trend. Use Chart.js (likely already available) or simple CSS bars. If there isn't enough data for a meaningful trend chart, show a simpler visualization (e.g., avg cost by year as a bar chart).

### CRITICAL: If data is insufficient

Some stats may not be calculable from the available JSON files (especially $/SF if many permits lack both cost AND sqft). For any stat that cannot be reliably calculated:
- Show "N/A" or "Insufficient data"
- Do NOT show a fake number
- Add a small note: "Cost data available for [X] of [Y] permits"

This is an analytics page. Showing honest "N/A" values is far better than showing fake numbers that undermine credibility.

---

### market_trends.html Verification

```bash
# Correct title
grep '<title>' market_trends.html
# "DADU Market Trends | Homebody Projects"

# No fabricated stats
grep -c '"156"\|"287"\|"214"\|"\$185"\|"\$245"\|"\$225"' market_trends.html
# Should be 0 (all stats calculated from data)

# Loads real data
grep -c 'contractor_stats\|permits_with_apn\|\.json' market_trends.html
# Should be 1+

# No banned colors
grep -c '#003039\|#2c3e50' market_trends.html
# Should be 0

# Shared CSS and header
grep -c 'homebody_shared.css' market_trends.html
grep -c 'homebody_header.js' market_trends.html
# Both 1+
```

Visual verification:
1. Stats bar shows real numbers (or N/A where data is missing)
2. Neighborhood table shows only zips with real data, sorted by actual avg $/SF
3. Yearly volume shows real year-by-year counts with real percentages
4. Cost breakdown uses Option A (real distribution) or Option B (clearly labeled estimates)
5. Key insights reference real data, not fake percentages
6. Charts render with real data points
