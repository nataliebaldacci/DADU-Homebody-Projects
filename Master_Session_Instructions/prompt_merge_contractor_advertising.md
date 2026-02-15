# TASK: Merge Contractor Advertising into Contractor Portal + Add to Pricing

## Context

The WHO WE SERVE dropdown currently has "Advertise With Us" as a standalone link pointing to `contractor_advertising.html`. That page's content needs to be folded into `contractor_portal.html` (the Contractors landing page in WHO WE SERVE > User Portals). The advertising tiers also need to appear on `homebody_dadu_pricing.html` as a contractor pricing track.

After this work, "Advertise With Us" in the nav should point to `contractor_portal.html#advertise` (an anchor on the merged page) instead of the standalone `contractor_advertising.html`. Do not delete `contractor_advertising.html`.

## FILES TO TOUCH

1. `contractor_portal.html` — Add advertising section below existing dashboard/tools content
2. `homebody_dadu_pricing.html` — Add a "For Contractors" pricing track alongside existing homeowner report pricing
3. `homebody_header.js` — Update the "Advertise With Us" link from `contractor_advertising.html` to `contractor_portal.html#advertise`
4. `homebody_header.html` — Same link update (must stay in sync with homebody_header.js)

## STEP 1: Read Source Files First

Before writing any code, read the full content of:
- `contractor_advertising.html` (content being merged)
- `contractor_portal.html` (destination page)
- `homebody_dadu_pricing.html` (pricing page getting a new track)
- `homebody_header.js` (nav source of truth)

## STEP 2: Add Advertising Section to contractor_portal.html

Below whatever dashboard options, market intelligence tools, and permit explorer links already exist on the contractor portal, add a new section with `id="advertise"` so the nav can anchor-link to it.

### Section heading
"Promote Your Business" or similar heading that fits the existing page tone.

### Content to include
- Short pitch: Homebody Projects connects homeowners to contractors through permit data. Contractors can promote their business to homeowners actively researching DADU projects in their area.
- Three advertising tiers pulled from `contractor_advertising.html`:
  - **Featured Listing** — Highlighted placement in contractor directory, badge on profile, priority in search results
  - **Sponsored Results** — Appear at top of "Find a Contractor" searches for selected ZIP codes
  - **Lead Generation** — Direct inquiry form, homeowner contact routing, project match notifications
- Each tier: card with "Coming Soon" or "Contact Us" button (mailto:hello@castlehold.com). No Stripe yet.
- If `contractor_advertising.html` has additional content worth preserving (testimonials, FAQ, how-it-works steps), fold those into this section too.

### Style rules (CRITICAL — follow exactly)
- Use the CSS variables from homebody_shared.css. The correct variables are:
  ```
  --dark-anchor: #2F3A45    (hero/footer backgrounds)
  --slate: #3A5566          (headings, nav, brand color)
  --slate-mid: #496778      (hover states)
  --stone: #7B746D          (secondary text)
  --wheat: #CBB279          (CTA buttons, highlights)
  --cream: #E1D4BB          (light text on dark bg)
  --linen: #F0EBE1          (section backgrounds, icon circles)
  --background: #F2F0ED     (page background)
  --card-bg: #F5F5F0        (card surfaces)
  --gray-light: #E2E2E0     (borders)
  ```
- CTA buttons: background var(--wheat), text var(--slate), font-weight 700, border-radius 8px
- Headings: color var(--slate), Inter font (NOT serif for subpage headings, serif is homepage hero only)
- Body text: color var(--gray-warm) which is #706F6C
- Cards: background var(--card-bg), border 1px solid var(--gray-light)
- **NO EMOJI.** Use SVG icons from assets/icons/ (e.g., Building_and_Construction.svg) or plain text. No emoji anywhere.
- **BANNED COLORS:** Do not use #003039, #6b8fa3, #6b8e4e, #2E6F4E, #D4A017, #C58B2A, #7A2A1D, or any teal/sage/terracotta/ochre.
- Font: Inter (body), Source Serif 4 (headlines on homepage only). This page uses Inter throughout.
- Logo: ADU.png. Do not use castle logo.

## STEP 3: Add Contractor Pricing Track to homebody_dadu_pricing.html

The current pricing page shows homeowner report tiers (Detail Report $4.99, Contractor Report $9.99, Area Analysis $14.99). Add a second pricing track for contractors.

### Implementation
- Add a tab switcher or section divider: **"For Homeowners"** | **"For Contractors"**
- Homeowner section stays exactly as-is. Do not modify existing content.
- Contractor section shows advertising tiers with placeholder pricing:
  - Featured Listing: $29/mo (placeholder)
  - Sponsored Results: $79/mo (placeholder)
  - Lead Generation: $149/mo (placeholder)
  - Mark all prices clearly as "Starting at" or similar placeholder language
- Each contractor tier card must match the visual style of the existing homeowner pricing cards
- "Contact Us" CTA on each card (mailto:hello@castlehold.com)
- Bottom note: "All contractor advertising packages include a verified permit history badge and listing in the Homebody Projects contractor directory."
- Same style rules as Step 2. No emoji. No banned colors.

## STEP 4: Update Nav Links

In `homebody_header.js` (source of truth for navigation), find the WHO WE SERVE dropdown, Column 2 (Professional), the "Advertise With Us" entry. Change its href from `contractor_advertising.html` to `contractor_portal.html#advertise`.

Make the same change in `homebody_header.html` (static mirror, must match homebody_header.js).

The PRICING nav link already points to `homebody_dadu_pricing.html`. Verify this is correct and do not change it.

## CONSTRAINTS

1. **Brand = "Homebody Projects"** on all user-facing content. "Castlehold" appears ONLY in footer "Powered by" lines and on reports/data attribution.
2. **No emoji anywhere.** Use SVG/PNG icons from assets/icons/ or plain text only.
3. **Logo = ADU.png.** Never castle logo.
4. **Banned color #003039** — if you see it in any file you touch, replace with #3A5566.
5. Do not delete `contractor_advertising.html`. Just stop linking to it in nav.
6. Do not break existing content on either destination page. Add sections, do not replace.
7. No fake contractor data. The advertising section describes the platform's offering to contractors, not sample contractor profiles.
8. Provide complete file contents for every file you modify.
9. The nav source of truth is `homebody_header.js`. The static mirror is `homebody_header.html`. Both must stay in sync.

## VERIFICATION

After completing the work:
1. Open `contractor_portal.html` — confirm "Promote Your Business" section appears below existing tools, with `id="advertise"` anchor
2. Open `contractor_portal.html#advertise` — confirm it scrolls to the advertising section
3. Open `homebody_dadu_pricing.html` — confirm both Homeowner and Contractor pricing tracks display
4. Check `homebody_header.js` — confirm "Advertise With Us" href is `contractor_portal.html#advertise`
5. Check `homebody_header.html` — confirm same link update
6. Verify: no #003039, no emoji, no castle logo, no old palette colors in any modified file
7. Commit:
   ```bash
   git add -A
   git commit -m "Merge contractor advertising into portal, add contractor pricing track, update nav link"
   git push origin main
   ```
