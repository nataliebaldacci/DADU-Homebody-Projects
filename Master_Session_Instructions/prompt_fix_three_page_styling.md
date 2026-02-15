# TASK: Fix Styling on Three Resource/Dashboard Pages

## The Problem

Three nav-linked pages have incorrect or outdated styling. They likely have some combination of:
- Title says "Castlehold" instead of "Homebody Projects"
- Old or missing shared header (not using homebody_header.js)
- Old colors (hardcoded hex instead of CSS variables, or wrong palette entirely)
- Missing `homebody_shared.css` import
- Old or missing footer
- Emoji icons instead of SVG/PNG icons
- Inconsistent typography (not Inter)

The three pages:
1. **`trade_permits.html`** — RESOURCES page, guide to trade permits for DADU projects
2. **`contractor_dashboard.html`** — EXPLORE > Dashboards page, contractor performance analytics
3. **`overlay-districts.html`** — RESOURCES page, UDO/DADU/SP overlay district reference

## STEP 1: Audit All Three Pages

Before changing anything, read each file and log every issue:

```bash
for page in trade_permits.html contractor_dashboard.html overlay-districts.html; do
  echo "=== $page ==="
  echo "Title:"
  grep -i '<title>' "$page"
  echo "Shared CSS loaded?"
  grep -c 'homebody_shared.css' "$page"
  echo "Shared header JS loaded?"
  grep -c 'homebody_header.js' "$page"
  echo "CASTLEHOLD in title/h1:"
  grep -ci 'castlehold' "$page"
  echo "BANNED #003039:"
  grep -c '#003039' "$page"
  echo "Old colors:"
  grep -c '#2c3e50\|#6b8fa3\|#6b8e4e\|#c9a86c\|#e8e4df\|#C58B2A\|#7A2A1D\|#D4A017\|#2E6F4E\|#B55A3C\|#34495e\|#1a252f' "$page"
  echo "Emoji:"
  grep -Pc '[\x{1F300}-\x{1F9FF}]|[\x{2600}-\x{26FF}]|[\x{2700}-\x{27BF}]' "$page" 2>/dev/null || echo "0 (grep failed, check manually)"
  echo "Inline styles (potential hardcoded colors):"
  grep -c 'style="' "$page"
  echo "---"
done
```

Print the full results. Then proceed with fixes.

## STEP 2: Fix Each Page

For EACH of the three pages, apply ALL of the following fixes. Do not skip any step.

### 2A: Shared Header and CSS

Every page must have this in `<head>`:
```html
<link rel="stylesheet" href="homebody_shared.css">
```

And this just inside `<body>` (before page content):
```html
<div id="homebody-header"></div>
<script src="homebody_header.js"></script>
```

If the page already has a hardcoded `<header>` or `<nav>`, REMOVE it entirely and replace with the shared header injection above. The shared header is the single source of truth for navigation.

### 2B: Page Title

Change `<title>` from any "Castlehold" reference to the correct format:
```
Trade Permits | Homebody Projects
Contractor Dashboard | Homebody Projects
Overlay Districts | Homebody Projects
```

Also fix any `<h1>` that says "Castlehold" in the body content.

### 2C: Remove All Emoji

Find and remove every emoji character. Replace with appropriate SVG/PNG icons from `assets/icons/` or just remove if decorative. Common replacements:
- Any tool/wrench emoji → `<img src="assets/icons/Building_and_Construction.svg" ...>`
- Any document emoji → `<img src="assets/icons/Recorded_Docs.svg" ...>`
- Any map/location emoji → `<img src="assets/icons/Zoning.svg" ...>`
- Any chart emoji → `<img src="assets/icons/Market_Statistics_Report_.svg" ...>`
- Any numbered step emoji (1️⃣, 2️⃣, etc.) → plain styled number in a circle div

If removing emoji from card headers or section titles, just use text. Do not replace with nothing and leave an empty space.

### 2D: Color Fixes

Replace ALL hardcoded hex colors with CSS variables. Use this mapping:

**If the page has a `<style>` block with hardcoded colors:**

| Find | Replace With | CSS Variable |
|------|-------------|--------------|
| #003039 | #3A5566 | var(--slate) |
| #2c3e50 | #3A5566 | var(--slate) |
| #34495e | #4A6B7D | var(--slate-light) |
| #1a252f | #2F3A45 | var(--dark-anchor) |
| #6b8fa3 | #7B746D | var(--stone) |
| #6b8e4e | #3A5566 | var(--slate) |
| #c9a86c | #CBB279 | var(--wheat) |
| #e8e4df | #F2F0ED | var(--background) |
| #C58B2A | #CBB279 | var(--wheat) |
| #D4A017 | #918A83 | var(--stone-light) |
| #7A2A1D | #B58676 | var(--not-eligible) |
| #2E6F4E | #406A64 | var(--eligible) |
| #B55A3C | #CBB279 | var(--wheat) |

**Preferred approach:** Convert the page's `<style>` block to use CSS variables instead of hex values. This way, if the palette changes again, only `homebody_shared.css` needs updating.

Key mappings for common patterns:
```css
/* Dark section backgrounds (hero, footer, dark cards) */
background: var(--slate);           /* was #2c3e50, #003039, etc. */

/* Page background */
background: var(--background);      /* was #e8e4df, #f5f5f0, etc. */

/* Card backgrounds */
background: var(--card-bg);         /* #F5F5F0 */

/* Card borders */
border: 1px solid var(--gray-light); /* #E2E2E0 */

/* Headings */
color: var(--slate);                /* #3A5566 */

/* Body text */
color: var(--gray-warm);            /* #706F6C */

/* Secondary/muted text */
color: var(--stone);                /* #7B746D */

/* CTA buttons */
background: var(--wheat);           /* #CBB279 */
color: var(--slate);                /* #3A5566 */

/* Light text on dark backgrounds */
color: var(--cream);                /* #E1D4BB */

/* Icon circle backgrounds */
background: var(--linen);           /* #F0EBE1 */

/* Hover states on dark backgrounds */
background: var(--slate-mid);       /* #496778 */
```

### 2E: Typography

Ensure font-family is Inter throughout:
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

Remove any Montserrat, Arial, or other font references. If Google Fonts is loaded in `<head>`, ensure it loads Inter:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

### 2F: Footer

If the page has an old hardcoded footer or no footer, remove it. The shared header injection via `homebody_header.js` handles the footer. If `homebody_header.js` does NOT inject a footer, add a simple one:

```html
<footer style="background: var(--slate); color: var(--cream); text-align: center; padding: 24px; font-size: 13px; font-family: Inter, sans-serif;">
  Homebody Projects | A Vanderbilt Law School Project | Powered by Castlehold
</footer>
```

### 2G: Page Hero Section

Each page should have a consistent hero/header section. The pattern for reference/resource pages:

```html
<section class="page-hero" style="background: var(--slate); padding: 48px 24px 40px; text-align: center;">
  <h1 style="color: white; font-family: Inter, sans-serif; font-weight: 800; font-size: 2rem; margin-bottom: 8px;">
    Page Title Here
  </h1>
  <p style="color: var(--cream); font-size: 1rem; max-width: 600px; margin: 0 auto;">
    Subtitle description here
  </p>
</section>
```

If the page already has a hero with the right structure but wrong colors, just fix the colors. Do not restructure content that already works.

---

## PAGE-SPECIFIC NOTES

### trade_permits.html
- **Location in nav:** RESOURCES > Learn column
- **Content:** Trade permit types (electrical, plumbing, mechanical, gas, fire, general), fee tables, required documentation, inspection requirements, 5-step process flow
- **Known issues from fetch:** Title says "Castlehold". No visible shared header. Has a clean content structure with permit cards, fee tables, requirements, and step flow. Keep all this content. Just fix the branding wrapper.
- **Keep all fee data and permit type cards intact.** Do not modify the actual permit information, fee amounts, or descriptions.

### contractor_dashboard.html
- **Location in nav:** EXPLORE > Dashboards
- **Content:** Contractor performance analytics, likely has contractor leaderboard, permit counts, cost data
- **Likely issues:** Same branding/color problems as trade_permits. May have old variable names (--navy, --gold-light, etc.) that need mapping to current variables.
- **If it loads data from `contractor_stats.json` or `data/contractor_stats.json`, do NOT change the data loading logic.** Only fix styling.

### overlay-districts.html
- **Location in nav:** RESOURCES > Learn column
- **Content:** UDO, DADU overlay, and SP overlay district information with ordinance links
- **Critical:** This page likely contains Municode URLs, Legistar links, and overlay ordinance references. Do NOT change or remove any external links. Only fix styling.
- **If it has accordion sections for different overlay types, keep the accordion JS functional.**

---

## CONSTRAINTS

1. **Keep all content, data, links, and functionality intact.** This is a styling-only pass. Do not rewrite page content, remove sections, change link targets, or modify JavaScript data-loading logic.
2. **No emoji.** Replace any found with SVG/PNG icons or plain text.
3. **Banned color #003039.** Replace with #3A5566 (var(--slate)).
4. **No old palette colors.** See replacement table in Step 2D.
5. **Logo = ADU.png** in nav (handled by shared header). Do not add castle logo.
6. **Font = Inter.** No Montserrat.
7. **"Homebody Projects"** in titles and headers. "Castlehold" only in footer "Powered by" line.
8. **Provide complete file contents** for every file you modify.
9. **Do not touch homebody_header.js or homebody_header.html** — those are the shared nav source of truth. Only add the script/link tags to load them.

---

## VERIFICATION

After fixing all three pages, run:

```bash
echo "=== POST-FIX AUDIT ==="
for page in trade_permits.html contractor_dashboard.html overlay-districts.html; do
  echo "--- $page ---"
  
  # Title check
  echo "Title:"
  grep '<title>' "$page"
  
  # Shared CSS
  echo "homebody_shared.css loaded:"
  grep -c 'homebody_shared.css' "$page"
  
  # Shared header JS
  echo "homebody_header.js loaded:"
  grep -c 'homebody_header.js' "$page"
  
  # CASTLEHOLD in wrong places
  echo "CASTLEHOLD in title/h1 (should be 0):"
  grep -i '<title>.*castlehold\|<h1>.*castlehold' "$page" | wc -l
  
  # BANNED color
  echo "#003039 count (should be 0):"
  grep -c '#003039' "$page"
  
  # Old colors
  echo "Old palette colors (should be 0):"
  grep -c '#2c3e50\|#6b8fa3\|#6b8e4e\|#c9a86c\|#e8e4df\|#C58B2A\|#7A2A1D\|#D4A017\|#2E6F4E' "$page"
  
  # Font check
  echo "Montserrat references (should be 0):"
  grep -ci 'montserrat' "$page"
  
  # Emoji check
  echo "Emoji characters:"
  python3 -c "
import re
with open('$page','r') as f:
    content = f.read()
emoji_pattern = re.compile('[\U0001F300-\U0001F9FF\U00002600-\U000026FF\U00002700-\U000027BF\U0000FE00-\U0000FE0F\U0001F000-\U0001F02F]')
matches = emoji_pattern.findall(content)
print(len(matches))
" 2>/dev/null || echo "check manually"
  
  echo ""
done
```

All counts marked "should be 0" must actually be 0. If any are not, fix before committing.

Also visually verify:
1. Each page loads with the shared Homebody Projects nav bar at the top
2. Nav highlights the correct section (RESOURCES for trade_permits and overlay-districts, EXPLORE for contractor_dashboard)
3. Page hero background is var(--slate) (#3A5566) with white/cream text
4. Card backgrounds are var(--card-bg) (#F5F5F0) with var(--gray-light) borders
5. CTA buttons are var(--wheat) (#CBB279) background with var(--slate) text
6. Body text is var(--gray-warm) (#706F6C)
7. No bright/saturated colors anywhere
8. Footer says "Powered by Castlehold" (only place Castlehold appears)
9. All external links still work (especially Municode and Legistar links on overlay-districts.html)
10. Any data-loading JavaScript still functions (especially contractor_dashboard.html)

```bash
git add -A
git commit -m "Fix styling: trade_permits, contractor_dashboard, overlay-districts — shared header, correct palette, remove emoji"
git push origin main
```
