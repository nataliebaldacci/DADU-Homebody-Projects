# TASK: Move Documents Portal to Pricing Page + Add External Links to DATA Nav

Three nav/content changes in this task.

---

## CHANGE 1: Remove dadu_documents_portal.html from DATA > Document Database

### Current state (in homebody_header.js)

**DATA > Column 2: Document Database** currently contains:
- Site Plans & Permits → site_plan_downloads.html
- **Recorded Documents → dadu_documents_portal.html** ← REMOVE FROM HERE
- Restrictive Covenants → restrictive_covenants_v2.html
- PDF Database → pdf_database_lookup.html

### Target state

Remove the "Recorded Documents" entry pointing to `dadu_documents_portal.html`. The other three items stay. The vacated slot gets filled in Change 3 below.

---

## CHANGE 2: Add dadu_documents_portal.html as a section on the Pricing page

### What
The documents portal is a premium product, not a reference database. Add it to `homebody_dadu_pricing.html` as a distinct section alongside the existing report tiers.

### Before writing code
Read the full content of both files:
- `dadu_documents_portal.html` (to understand what it offers)
- `homebody_dadu_pricing.html` (to understand the current pricing layout)

### Implementation
Add a new section on `homebody_dadu_pricing.html` that presents the Document Portal as a product offering. Place it after the existing report pricing cards (Detail Report $4.99, Contractor Report $9.99, Area Analysis $14.99) but before any footer or bulk pricing section.

The section should include:
- A heading like "Document Portal" or "Recorded Documents Access"
- A short description explaining what the portal provides (search permits, site plans, property cards, restrictive covenants by APN, address, or permit number)
- A CTA button that links to `dadu_documents_portal.html` (label: "Browse Documents" or "Access Document Portal")
- Present it as a card or section that matches the visual style of the existing pricing cards on the page

Do NOT remove or restructure the existing pricing content. Add to it.

### Also add a PRICING nav anchor
Since PRICING is a direct link to `homebody_dadu_pricing.html` (no dropdown), the documents portal becomes accessible through the pricing page itself. No nav dropdown change needed for this — users get to it by visiting Pricing and scrolling.

---

## CHANGE 3: Add dadu_resources.html to DATA > Document Database as "External Links"

### What
`dadu_resources.html` contains external links to Nashville official resources, Metro portals, and reference materials. It currently sits in the unlinked duplicates list (CLAUDE.md lists it as a deletion candidate). Rescue it by placing it in the DATA > Document Database column in the slot vacated by the documents portal.

### Current state (after Change 1)

**DATA > Column 2: Document Database** will be:
- Site Plans & Permits → site_plan_downloads.html
- *(empty slot)*
- Restrictive Covenants → restrictive_covenants_v2.html
- PDF Database → pdf_database_lookup.html

### Target state

**DATA > Column 2: Document Database:**
- Site Plans & Permits → site_plan_downloads.html
- **External Links → dadu_resources.html** ← NEW ENTRY
- Restrictive Covenants → restrictive_covenants_v2.html
- PDF Database → pdf_database_lookup.html

Use icon `Recorded_Docs.svg` (same icon the documents portal was using) for the "External Links" entry. Label it exactly **"External Links"** in the nav.

---

## FILES TO MODIFY

1. `homebody_header.js` — Remove "Recorded Documents" from DATA > Document Database, add "External Links" pointing to `dadu_resources.html` in its place
2. `homebody_header.html` — Same changes (must stay in sync with homebody_header.js)
3. `homebody_dadu_pricing.html` — Add Document Portal section after existing report pricing cards

## FILES TO READ FIRST (before writing any code)
- `dadu_documents_portal.html`
- `dadu_resources.html`
- `homebody_dadu_pricing.html`
- `homebody_header.js`

---

## CLAUDE.md UPDATES

Update CLAUDE.md Section 4 (Navigation Structure):
- In the DATA > Document Database table: replace the "Recorded Documents → dadu_documents_portal.html" row with "External Links → dadu_resources.html"
- Note that dadu_documents_portal.html is now accessed through the Pricing page

Update CLAUDE.md Section 5 (Current State):
- Move `dadu_resources.html` from the "Unlinked Duplicates (candidates for deletion)" list to the "Linked in Navigation" list under DATA > Docs
- Move `dadu_documents_portal.html` from DATA > Docs to "Direct links" or add a note that it is accessed via the Pricing page

---

## CONSTRAINTS

1. **No emoji.** Use SVG/PNG icons from assets/icons/ only.
2. **Banned color #003039** — if you see it in any file you touch, replace with #3A5566.
3. **No old palette colors** in any file you touch (#6b8fa3, #6b8e4e, #2E6F4E, #D4A017, #C58B2A, #7A2A1D).
4. Logo = ADU.png. Brand = "Homebody Projects" on user-facing content.
5. The nav source of truth is `homebody_header.js`. The static mirror `homebody_header.html` must match it exactly.
6. Provide complete file contents for every file you modify.
7. Do not delete or rename any existing files.
8. Do not modify existing pricing cards or report tiers on the pricing page. Add the Document Portal section alongside them.

---

## VERIFICATION

1. Open nav on any page — confirm "Recorded Documents" no longer appears under DATA > Document Database
2. Confirm "External Links" appears under DATA > Document Database, linking to `dadu_resources.html`
3. Open `dadu_resources.html` — confirm it loads and contains external Nashville resource links
4. Open `homebody_dadu_pricing.html` — confirm the new Document Portal section appears after the report pricing cards
5. Confirm the Document Portal section links to `dadu_documents_portal.html`
6. Confirm existing pricing cards (Detail Report, Contractor Report, Area Analysis) are untouched
7. Verify `homebody_header.js` and `homebody_header.html` match each other
8. Verify no #003039, no emoji, no old colors in any modified file
9. Commit:
   ```bash
   git add -A
   git commit -m "Move documents portal to pricing page, add external links to DATA nav"
   git push origin main
   ```
