# TASK: Fix BUILD Dropdown + Contrast Audit Across All Pages

## Task 1: Fix BUILD Dropdown

Fix the BUILD dropdown in `homebody_header.js` and `homebody_header.html`. Two problems.

### Problem 1: Transparent Background

The BUILD dropdown background is see-through. Hero content shows through it. Add to the dropdown CSS:

```css
.mega-menu, .mega-menu-content, .dropdown-menu, nav .dropdown-content {
  background: #FFFFFF !important;
  background-color: #FFFFFF !important;
  opacity: 1 !important;
}
```

Find wherever the BUILD dropdown container is styled and make sure it has `background: #FFFFFF` with no transparency, no opacity less than 1, and no `rgba()` with alpha < 1.

### Problem 2: Wrong Items

The BUILD dropdown should be a single column with exactly these 7 items in this order:

1. Planning Hub → project_planner_hub.html
2. Interactive Checklist → project_checklist.html
3. Draw DADU on Parcel → draw_dadu_on_parcel.html
4. Permit Process Timeline → permit_process_timeline.html
5. All Calculators → dadu_calculators.html
6. Size Calculator → size_calculator.html
7. Form Wizard → form_wizard.html

No column headers. No sub-sections. Just 7 links in a single narrow column. No "Find a Contractor" (that belongs in WHO WE SERVE).

Check BOTH `homebody_header.js` AND `homebody_header.html`. They must match. Do NOT change any other dropdown.

---

## Task 2: Contrast Audit Across All Pages

Scan every HTML file in the repo root. For each page, check text/icon visibility against backgrounds.

### Rules

**Dark background sections** (var(--slate) #3A5566, or any dark color):
- Text must be white (#FFFFFF), var(--cream) #E1D4BB, or var(--wheat) #CBB279
- NOT dark text on dark background
- Stats numbers should be var(--wheat) or white
- Icons must be white or light colored. Dark PNG/SVG icons are invisible on dark backgrounds.

**Light background sections** (var(--background) #F2F0ED, var(--card-bg) #F5F3F0, white):
- Text must be var(--slate) #3A5566, var(--graphite) #3E4A4F, or similar dark color
- NOT white or cream text on light background

**Hero sections specifically:**
- Headings: white or cream on dark bg
- Subtitles: var(--cream) or var(--linen)
- Stats numbers: var(--wheat) #CBB279 or white

**Icons on dark backgrounds:**
- If a dark-colored SVG/PNG icon sits on a dark background, add `filter: brightness(0) invert(1)` to make it white
- Or swap to a white version of the icon if one exists in assets/icons/

### How to Audit

```bash
# List all HTML files to check
ls *.html | wc -l
```

For each file:
1. Look for sections with dark backgrounds (background: var(--slate), #3A5566, #003039, or dark rgba values)
2. Check that all text inside those sections uses light colors
3. Look for sections with light backgrounds
4. Check that all text inside those sections uses dark colors
5. Check icon `<img>` tags inside dark sections for missing brightness filters

### Common Fixes

```css
/* White text on dark bg */
color: #FFFFFF;
color: var(--cream);

/* Dark text on light bg */
color: var(--slate);
color: var(--graphite);

/* Stats on dark bg */
color: var(--wheat);

/* Dark icon on dark bg - make white */
filter: brightness(0) invert(1);
```

### Known Problem Pages

- `about_platform.html` — hero stats and icon may have contrast issues
- Any page with a var(--slate) hero section

### Output

Print a summary listing every file you fixed and what you changed. Format:

```
CONTRAST FIXES:
- about_platform.html: fixed hero icon filter, stats number color
- homeowner_portal.html: fixed subtitle color on dark hero
- (etc.)
```

---

## Constraints

- Do NOT delete any files
- Do NOT change nav structure on any dropdown except BUILD
- Do NOT change page content or layout, only colors and icon filters for contrast
- Font stays Inter everywhere

```bash
git add -A && git commit -m "Fix BUILD dropdown + contrast audit across all pages" && git push origin main
```
