# Castlehold Implementation Quick Reference

## Files You Care About

### 🎯 The One Header File
**`homebody_header.html`** - DO NOT MODIFY without careful consideration. This is the canonical header for the entire site.

### 📄 Documentation
- `IMPLEMENTATION_REPORT.md` - Full detailed report
- `IMPLEMENTATION_SUMMARY.txt` - Quick status overview
- `QUICK_REFERENCE.md` - This file

---

## How It Works

Every HTML page loads the shared header via JavaScript:

```html
<div id="homebody-header-container"></div>
<script>
    fetch('homebody_header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('homebody-header-container').innerHTML = data;
        });
</script>
```

---

## To Update the Navigation

1. Edit **`homebody_header.html`** only
2. Changes automatically appear on all 34 pages
3. Test by opening any HTML file in browser

---

## Castlehold Color Palette

```css
--navy: #3A5566         /* Primary blue */
--terracotta: #C58B2A   /* Accent orange/buttons */
--tan: #7B746D          /* Warm neutral */
--background: #F2F0ED   /* Page background */
--status-eligible: #2E6F4E  /* Green for eligible status */
```

### Castle Logo Colors
- Left (smaller DADU): `#D4C5A9` (tan)
- Right (main house): `#3A5566` (slate blue)
- Ground line: `#7B746D` (warm stone)
- Windows/doors: `#F2F0ED` (background)

---

## Navigation Structure (Locked)

```
LOGO → index.html

EXPLORE
  Learn (6 items)
  Discover (4 items)
  User Types (5 items)

BUILD
  Plan (3 items)
  Design (1 item)
  Calculate (4 items)
  Hire (1 item)
  File (4 items)

DATA
  Activity (3 items)
  Reports (7 items)
  Records (6 items)

PRICING → homebody_pricing.html

🔍 Search → property_search.html
My Projects → project_planner.html
Get Started → am_i_eligible.html
```

---

## Placeholder Pages (Under Development)

These exist but show "under development" messages:
- designer_resources.html
- municipal_dashboard.html
- legal_resources.html
- contractor_marketplace.html
- short_term_rental_permit.html
- permit_activity_dashboard.html
- market_trends.html
- dadu_reports_store.html
- pdf_database_lookup.html
- sample_reports/* (4 files)

**Replace these with real functionality as you build features.**

---

## Link Status

✅ **Zero broken links** - All 45 navigation targets exist and work

---

## Adding a New Page

1. Create your HTML file
2. Add this code at the start of `<body>`:
   ```html
   <div id="homebody-header-container"></div>
   <script>
       fetch('homebody_header.html')
           .then(response => response.text())
           .then(data => {
               document.getElementById('homebody-header-container').innerHTML = data;
           });
   </script>
   ```
3. Add your page content below
4. If it should be in nav, edit `homebody_header.html`

---

## Testing

Open any `.html` file in browser:
- Check header appears
- Check dropdowns work
- Check colors match Castlehold palette
- Check all links navigate correctly

---

## Git Commit

When ready to commit:

```bash
git add .
git commit -m "Implement Castlehold palette and locked navigation structure

- Created shared header (homebody_header.html)
- Updated 34 pages to use shared header
- Implemented Castlehold color palette
- Added castle SVG logo with correct colors
- Created 13 placeholder pages
- Zero broken links"
```

---

## Support

All navigation targets verified working. If you encounter issues:
1. Check browser console for fetch errors
2. Verify file paths are correct
3. Ensure homebody_header.html is in root directory
4. Test with a simple HTTP server (not file://)
