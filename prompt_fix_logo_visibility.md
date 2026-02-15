# TASK: Fix Logo Visibility on Light-Background Pages

## The Problem

A previous task replaced the logo across the site, but it used `ADU_Light2.svg` on EVERY page. That logo variant is white/light-colored, designed for dark backgrounds. On pages with light backgrounds (like `what_is_dadu.html`), the logo is now invisible.

**This was a mistake.** The logo swap was only supposed to apply to the homepage. It should not have been applied to every page's body content.

## The Fix

### Rule: Match logo variant to background color

| Background | Logo File | Where |
|------------|-----------|-------|
| Dark (#3A5566 nav bar) | `assets/icons/ADU.png` | Nav bar logo (handled by shared header, leave alone) |
| Dark hero/section | `assets/icons/ADU_Light2.svg` or `ADU_Light.svg` | Only on dark-background hero sections |
| Light page body (#F2F0ED, #F5F5F0, white, #F0EBE1) | `assets/icons/ADU_MultiColors.svg` | Any logo reference in page body content on light backgrounds |

### Step 1: Find every page using ADU_Light2.svg outside the nav

Run this audit first:
```bash
cd /Users/nataliebaldacci/Documents/GitHub/DADU-Homebody-Projects

# Find all references to ADU_Light2.svg
echo "=== ADU_Light2.svg references ==="
grep -rn "ADU_Light2.svg" --include="*.html" . | grep -v "samples/"

# Also check for ADU_Light.svg
echo "=== ADU_Light.svg references ==="
grep -rn "ADU_Light.svg" --include="*.html" . | grep -v "samples/"
```

### Step 2: For each match, determine if it's in the nav or in page body content

- **If it's inside the shared header / nav bar** (dark #3A5566 background): LEAVE IT ALONE. The light logo is correct on the dark nav.
- **If it's in page body content on a light background**: Replace `ADU_Light2.svg` with `ADU_MultiColors.svg`.

### Step 3: Replace on light-background pages

For every page where `ADU_Light2.svg` appears in the page body (not the nav), replace it with `ADU_MultiColors.svg`:

```
assets/icons/ADU_Light2.svg  →  assets/icons/ADU_MultiColors.svg
```

Do this for ALL affected pages, not just `what_is_dadu.html`. Check every HTML file the audit finds.

### Step 4: Verify ADU_MultiColors.svg exists and is tracked

```bash
ls -la assets/icons/ADU_MultiColors.svg
git ls-files --error-unmatch assets/icons/ADU_MultiColors.svg 2>/dev/null && echo "TRACKED" || echo "NOT TRACKED"
```

If not tracked, `git add assets/icons/ADU_MultiColors.svg`.

## DO NOT

- Do not change the nav bar logo. The shared header (`homebody_header.js`) controls the nav logo and it should remain `ADU.png` on the dark nav background.
- Do not change logos on pages with dark hero sections where the light variant is actually correct.
- Do not touch `homebody_header.js` or `homebody_header.html` for this task.
- Do not swap every logo sitewide to one variant. The whole point is using the RIGHT variant for the RIGHT background.

## CONSTRAINTS

1. **No emoji.** Use SVG/PNG icons from assets/icons/ only.
2. **Banned color #003039** — if you see it in any file you touch, replace with #3A5566.
3. Provide complete file contents for every file you modify.
4. Do not delete or rename any existing files.

## CLAUDE.md UPDATE

Update CLAUDE.md Section 3 (Logo) to clarify the variant rules:
```
### Logo
- **Nav bar:** `assets/icons/ADU.png` at ~42px height (on dark #3A5566 nav background)
- **Dark hero/sections:** `assets/icons/ADU_Light2.svg` or `ADU_Light.svg` (white variant for dark backgrounds)
- **Light page body:** `assets/icons/ADU_MultiColors.svg` (colored variant, visible on light backgrounds)
- **DO NOT USE** the old castle logo (castlehold-logo.png) or castle SVG
- **DO NOT** use ADU_Light2.svg on light backgrounds — it is invisible
```

## VERIFICATION

1. Open `what_is_dadu.html` — confirm the logo is now `ADU_MultiColors.svg` and clearly visible
2. Check 2-3 other affected pages from the audit — confirm logos are visible on light backgrounds
3. Open any page and check the nav bar — confirm the nav logo is still `ADU.png` (unchanged)
4. Open the homepage — confirm any dark-section logos still use the appropriate light variant
5. No #003039, no emoji, no old colors in any modified file
6. Commit:
   ```bash
   git add -A
   git commit -m "Fix logo visibility: use ADU_MultiColors.svg on light backgrounds, keep light variant on dark backgrounds only"
   git push origin main
   ```
