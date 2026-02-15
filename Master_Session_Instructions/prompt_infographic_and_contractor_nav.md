# TASK: Add ADU Types Infographic + Move Contractor Dashboard to BUILD Nav

Two changes in this task.

---

## CHANGE 1: Add ADU_Types_Recolored.png to what_is_dadu.html

### Step 1A: Place the image in the repo

The source file is at `New_Icons/ADU_Types_Recolored.png` in the repo root. Copy it to a stable, tracked location:

```bash
mkdir -p assets/images
cp New_Icons/ADU_Types_Recolored.png assets/images/adu_types_homebody.png
```

If `assets/images/` is blocked by `.gitignore`, add an exception:
```bash
echo '!assets/images/*.png' >> .gitignore
```

Verify it will be tracked:
```bash
git add assets/images/adu_types_homebody.png
git status assets/images/adu_types_homebody.png
```

### Step 1B: Read what_is_dadu.html first

Read the full file to understand the page structure. Find the section after the introductory explanation of what a DADU is. That is where the image goes — not at the very top above all content, not buried at the bottom.

### Step 1C: Insert the figure element

Add this markup at the appropriate location in `what_is_dadu.html`:

```html
<figure class="edu-figure">
  <img
    src="assets/images/adu_types_homebody.png"
    alt="Accessory dwelling unit types: detached, attached, interior upper level, interior lower level, above garage, and garage conversion"
    class="edu-img"
    loading="lazy"
  >
  <figcaption class="edu-caption">Accessory dwelling units can be detached, attached, internal, above a garage, or a garage conversion.</figcaption>
</figure>
```

Important: because `what_is_dadu.html` is in the repo root, the path must be exactly `assets/images/...` with no leading slash and no `../`.

### Step 1D: Add CSS to homebody_shared.css

Add these classes near the bottom of `homebody_shared.css` (before any closing comments or media queries). These use the existing palette variables:

```css
/* Educational figure (infographic images) */
.edu-figure {
  margin: 24px auto;
  max-width: 980px;
}

.edu-img {
  display: block;
  width: 100%;
  height: auto;
  border-radius: 12px;
  border: 1px solid var(--gray-light, #E2E2E0);
  background: var(--card-bg, #F5F5F0);
}

.edu-caption {
  margin-top: 10px;
  color: var(--gray-warm, #706F6C);
  font-size: 0.95rem;
}
```

This keeps the image consistent with the Slate/Stone palette and makes the class reusable on other educational pages.

---

## CHANGE 2: Move "Contractor Dashboard" from EXPLORE to BUILD Nav, Rename to "Find a Contractor"

### What
Move `contractor_dashboard.html` out of the EXPLORE > Dashboards column and into the BUILD dropdown. Rename its nav label from "Contractor Dashboard" to **"Find a Contractor"**. The filename stays `contractor_dashboard.html` — only the display label in the nav changes.

### Current state (in homebody_header.js)

**EXPLORE > Column 2: Dashboards** currently contains:
- Permit Activity → permit_activity_dashboard.html
- Contractor Marketplace → contractor_marketplace.html
- Market Trends → market_trends.html
- **Contractor Dashboard → contractor_dashboard.html** ← REMOVE FROM HERE
- Permit Analytics → nashville_permit_analytics.html

**BUILD** currently has three columns:
- Column 1 (Project Planner): Planning Hub, Interactive Checklist, Draw DADU on Parcel, Permit Process Timeline
- Column 2 (Calculators): All Calculators, Size Calculator
- Column 3 (Form Wizard): Form Wizard

### Target state

**EXPLORE > Column 2: Dashboards** — remove Contractor Dashboard from this list. The other four items stay (including Contractor Marketplace, which remains here unchanged).

**BUILD** — add "Find a Contractor" to the BUILD dropdown. Place it as a new item in Column 1 (Project Planner) at the bottom, OR create a new Column 4 called "Hire" with just this one item. Pick whichever approach fits the existing mega-menu layout better. Use icon `Building_and_Construction.svg` and link to `contractor_dashboard.html`.

### Files to modify
- `homebody_header.js` (source of truth for navigation)
- `homebody_header.html` (static mirror — must stay in sync with homebody_header.js)

### Do NOT rename the file
The HTML file stays `contractor_dashboard.html`. Only the nav label changes to "Find a Contractor."

---

## CONSTRAINTS

1. **No emoji.** Use SVG/PNG icons from assets/icons/ only.
2. **Banned color #003039** — if you see it in any file you touch, replace with #3A5566.
3. **No old palette colors** in any file you touch (#6b8fa3, #6b8e4e, #2E6F4E, #D4A017, #C58B2A, #7A2A1D).
4. Logo = ADU.png. Brand = "Homebody Projects" on user-facing content.
5. The nav source of truth is `homebody_header.js`. The static mirror `homebody_header.html` must match it exactly.
6. Provide complete file contents for every file you modify.
7. Do not delete or rename any existing files.

## SCOPE RULE UPDATE

The CLAUDE.md Section 15 currently says: `Do not use "Contractor Finder" (use "Contractor Marketplace" only)`. This rule is now updated. The nav label "Find a Contractor" is approved for `contractor_dashboard.html` in the BUILD dropdown. The label "Contractor Marketplace" remains correct for `contractor_marketplace.html` in EXPLORE. Update CLAUDE.md Section 15 to replace that line with:
```
- Nav label for contractor_dashboard.html is "Find a Contractor" in the BUILD dropdown. "Contractor Marketplace" stays as the label for contractor_marketplace.html in EXPLORE.
```

Also update the BUILD dropdown table in CLAUDE.md Section 4 to reflect the new item, and remove "Contractor Dashboard" from the EXPLORE > Dashboards table.

## VERIFICATION

1. Open `what_is_dadu.html` — confirm the ADU Types infographic displays with border, caption, and correct sizing
2. Confirm `assets/images/adu_types_homebody.png` exists and is git-tracked
3. Confirm `homebody_shared.css` has the `.edu-figure`, `.edu-img`, `.edu-caption` classes
4. Open the nav on any page — confirm "Find a Contractor" appears under BUILD
5. Confirm "Contractor Dashboard" no longer appears under EXPLORE > Dashboards
6. Confirm "Contractor Marketplace" still appears under EXPLORE > Dashboards (unchanged)
7. Confirm clicking "Find a Contractor" navigates to `contractor_dashboard.html`
8. Verify no #003039, no emoji, no old colors in any modified file
9. Commit:
   ```bash
   git add -A
   git commit -m "Add branded ADU types graphic to what_is_dadu, move contractor dashboard to BUILD as Find a Contractor"
   git push origin main
   ```
10. Hard-refresh the live page (Cmd+Shift+R) — GitHub Pages caches images.
