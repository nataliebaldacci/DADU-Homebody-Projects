# TASK: Consolidate and Fix Eligibility Checklist + Flowchart

## The Problem

Two pages exist that overlap and are both broken:
- `dadu_eligibility_checklist.html` — eligibility checklist
- `dadu_eligibility_flowchart.html` — eligibility flowchart

Both are currently in the unlinked duplicates list. A previous session broke the flowchart by making it ask about "base zoning" as the first step, which is WRONG. It also broke the external links that were tied to each step (e.g., the USD step linked to the USD boundary map, the zoning step linked to Parcel Viewer, etc.).

## The Fix

Consolidate both pages into ONE fixed page: `dadu_eligibility_flowchart.html`. Delete `dadu_eligibility_checklist.html` after confirming its unique content has been absorbed.

The flowchart must follow the EXACT eligibility process from Nashville.gov's official DADU page:
https://www.nashville.gov/departments/codes/construction-and-permits/building-permits-central/detached-accessory-dwelling-unit

## STEP 1: Read Both Existing Pages First

Before writing any code, read the full content of:
- `dadu_eligibility_checklist.html`
- `dadu_eligibility_flowchart.html`

Also read `data/legislation_links_database.json` if it exists — it contains the URL database for all Nashville external links.

Identify any content and external links worth preserving. Then proceed with the rebuild.

## STEP 2: Rebuild the Flowchart Using the Official Nashville.gov Process

### THE CORRECT ELIGIBILITY FLOW (from Nashville.gov — do NOT deviate)

The flowchart must present these steps in this order. Do NOT start with "What is your base zoning?" That is wrong.

---

**STEP 1: Land Use Table Check**
"Does the Land Use Table show your parcel's zoning district permits DADUs with conditions (PC)?"
- YES → proceed to Step 2
- NO → NOT ELIGIBLE. Your zoning district does not permit DADUs.
- Note: R, RS, RN, and RL zones permit DADUs with conditions per BL2025-1007

External links for this step:
- [Land Use Tables § 17.08.030 (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.08LAUSDEST_17.08.030DILAUSTA)
- [Check Your Zoning on Parcel Viewer](https://maps.nashville.gov/ParcelViewer/)
- [Base Zoning Map (ArcGIS)](https://maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/BaseZoning/MapServer/0)
- [BL2025-1007 on Legistar](https://nashville.legistar.com/LegislationDetail.aspx?ID=7639644&GUID=45E2F5DA-7D4A-4979-98DE-40BD2B8833CE)

---

**STEP 2: Minimum Lot Area**
"Does your lot meet the minimum lot area required for your zoning district?"
- YES → proceed to Step 3
- NO → NOT ELIGIBLE. Lot does not meet minimum area.

External links for this step:
- [Bulk Regulation Tables § 17.12 (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.12BUDINGS)
- [Setback Requirements § 17.12.030 (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.12BUDINGS_17.12.030SE)
- [Check Your Lot Size on Parcel Viewer](https://maps.nashville.gov/ParcelViewer/)

---

**STEP 3: Service District / Overlay Check**
"Does your parcel meet ONE of the following?"
- a. In the Urban Services District (USD) → ELIGIBLE by-right. Proceed to conditions.
- b. In a DADU Overlay within the General Services District (GSD) → ELIGIBLE with overlay. Proceed to conditions.
- c. In an Urban Design Overlay (UDO) with DADU development standards → ELIGIBLE with UDO standards. Contact Planning.
- d. In a Specific Plan (SP) with DADU development standards → ELIGIBLE with SP standards. Contact Planning.
- NONE of the above → NOT ELIGIBLE.

External links for this step (CRITICAL — these were the links that got broken):
- **USD Map PDF:** [Urban Services District Map (Nashville.gov PDF)](https://maps.nashville.gov/webimages/MapGallery/PDFMaps/Urban%20Services%20District.pdf)
- **USD/GSD Boundary (ArcGIS):** [USD/GSD Boundary MapServer](https://maps.nashville.gov/arcgis/rest/services/Boundaries/USD_GSD/MapServer/0)
- **USD Charter Definition (Municode):** [Charter Appendix 1 — USD Boundary](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=THCH_APCH_APXONEDEBOURSEDI)
- **DADU Overlay Districts:** link to `overlay-districts.html` (internal page)
- **DADU Overlay Ordinance § 17.36.730 (Municode):** [Detached Accessory Dwelling Unit Overlay District](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.36OVDI_ARTXVIIDEACDWUNDAOVDI_17.36.730DEACDWUNOVDI)
- **UDO (Municode):** [§ 17.40.130 Urban Design Overlay](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.40ADPR)
- **Specific Plan (Municode):** [§ 17.40.105 Specific Plan](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.40ADPR_ARTIIIAMZOCOOFZOMA_17.40.105SPPLURIN)
- **Zoning Overlay Districts (ArcGIS):** [Zoning Overlay Districts MapServer](https://maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/Zoning_Overlay_Districts/MapServer)
- **Check Overlays on Parcel Viewer:** [Parcel Viewer](https://maps.nashville.gov/ParcelViewer/)

---

**STEP 4: Single Principal Structure**
"Is there exactly ONE single-family principal structure on the parcel?"
- YES → proceed to conditions
- NO (two or more principal structures) → NOT ELIGIBLE. DADUs not permitted when 2+ principal structures exist.

External links for this step:
- [DADU Definition § 17.04.060 (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.04DERU_17.04.060DEF)
- [Check Building Count on Parcel Viewer](https://maps.nashville.gov/ParcelViewer/)

---

**STEP 5: IF ELIGIBLE — Zoning Conditions Apply (§ 17.16.030G)**
Present these as a checklist/summary, not as pass/fail gates:

- **Owner Occupancy:** Owner must occupy principal structure or DADU
- **Size Limits:**
  - Lot < 10,000 SF → max 700 SF living space
  - Lot ≥ 10,000 SF → max 850 SF living space
  - Living space cannot exceed size of principal structure
- **Footprint:** DADU footprint cannot exceed footprint of primary structure. No other accessory structure over 200 SF when DADU exists.
- **Height:** DADU cannot be taller than principal structure. Max eave height: 10 ft (1-story) or 17 ft (2-story). Ridge line must be less than primary and cannot exceed 27 ft.
- **Setbacks:** Footprint ≤ 850 SF and to rear → half required side setback (min 3 ft), rear min 3 ft (10 ft if garage doors face alley). Footprint > 850 SF → full district setbacks.
- **Design:** Similar style, materials, color, roof form/pitch as principal. Dormers ≤ 50% of roof, set back min 2 ft from exterior wall.
- **STR Prohibition:** No short-term rental permits for new DADUs on SF, RN, or RL lots.

External links for this step:
- [§ 17.16.030G Full DADU Conditions (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.16SPDINGS_17.16.030DINGS)
- [§ 17.12.040(E) Accessory Buildings (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO_CH17.12BUDINGS_17.12.040ACST)
- [§ 6.28.030 Short Term Rental Restrictions (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT6BULIRE_DIVIGERE_CH6.28HORO_6.28.030SHTEREPRPE)
- [Restrictive Covenants (Nashville.gov)](https://www.nashville.gov/departments/codes/construction-and-permits/land-use-and-zoning-information/zoning-examinations/restrictive-covenants)
- [Full Zoning Code Title 17 (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT17ZO)

---

**STEP 6: Special Cases**
- **Historic Overlay:** Additional MHZC review. Setbacks/size/design enforced by Historic Commission. Use/living space enforced by Zoning. Historic permit required in addition to building permit.
- **SP or UDO:** Planning Department determines requirements. Building permit requires Planning approval.

External links for this step:
- [Historic Commission — Districts & Design Guidelines](https://www.nashville.gov/departments/historic-preservation/programs/districts-and-design-guidelines)
- [Accessory Dwelling Units in Historic Overlays (Nashville.gov)](https://www.nashville.gov/departments/historic-preservation/programs/districts-and-design-guidelines/detached-accessory-dwelling-units)
- [BL2011-900 Historic DADUs (Legistar)](https://nashville.legistar.com/LegislationDetail.aspx?ID=1025702)
- [Planning Department Contact List](https://www.nashville.gov/departments/codes/construction-and-permits/contact-list)
- [Register of Deeds (for Restrictive Covenant recording)](https://www.nashville.gov/departments/county-clerk/register-of-deeds)
- [Metro Stormwater (for footprint increases)](https://www.nashville.gov/departments/water/stormwater)
- [Tennessee 811 (call before digging)](https://www.tn811.com/)
- [Residential Building Code Ch. 16 (Municode)](https://library.municode.com/tn/metro_government_of_nashville_and_davidson_county/codes/code_of_ordinances?nodeId=CD_TIT16BUCO)
- [Nashville.gov Official DADU Page](https://www.nashville.gov/departments/codes/construction-and-permits/building-permits-central/detached-accessory-dwelling-unit)

---

### ADDITIONAL RESOURCE LINKS (include in a "Resources" section at the bottom of the page)
- [Parcel Viewer](https://maps.nashville.gov/ParcelViewer/)
- [ePermits Portal](https://epermits.nashville.gov/)
- [Codes Permits Search](https://documents.nashville.gov/Request/Form/PermitCodes)
- [Legistar — Metro Council Legislation](https://nashville.legistar.com/Legislation.aspx)
- [Zoning Help Desk Email: zoninghelpdesk@nashville.gov](mailto:zoninghelpdesk@nashville.gov)
- [Codes Help Desk: 615-862-6550](tel:6158626550)
- [Metro Codes Address: 800 President Ronald Reagan Way, Nashville, TN 37210](https://www.google.com/maps/place/800+President+Ronald+Reagan+Way,+Nashville,+TN+37210)

---

### Visual format
Build the flowchart as a visual stepped flow — connected cards/boxes with YES/NO paths, color-coded outcomes:
- Eligible: var(--eligible) which is #406A64
- Not Eligible: var(--not-eligible) which is #B58676
- Conditional/Special Case: var(--conditional) which is #918A83
- Step boxes: var(--card-bg) #F5F5F0 with var(--gray-light) #E2E2E0 border

Each step box must have:
- The question in bold
- The YES/NO outcomes clearly labeled
- External link pills styled as small buttons below each step (e.g., "View USD Map PDF →", "Read § 17.16.030G →", "Check on Parcel Viewer →")
- Every external link listed above for that step must appear — do NOT drop any

### Also include a quick checklist summary
Below the flowchart, add a condensed "Quick Eligibility Checklist":
- [ ] Zoning district permits DADUs (Land Use Table)
- [ ] Lot meets minimum area for district
- [ ] Property in USD, DADU Overlay (GSD), UDO, or SP
- [ ] Only one principal structure on parcel
- [ ] Owner will occupy principal or DADU
This absorbs the useful content from `dadu_eligibility_checklist.html`.

## STEP 3: Link the Page in Navigation

Add `dadu_eligibility_flowchart.html` to the nav:

**RESOURCES > Column 1: Learn** — add as a new entry after "General Requirements" and before "DADU History":
| Label | Icon | File |
|-------|------|------|
| Eligibility Flowchart | Zoning.svg | dadu_eligibility_flowchart.html |

Update `homebody_header.js` and `homebody_header.html` accordingly.

## STEP 4: Delete dadu_eligibility_checklist.html

After confirming its content is absorbed:
```bash
git rm dadu_eligibility_checklist.html
```

---

## CONSTRAINTS

1. **Follow the Nashville.gov eligibility order exactly.** Do NOT start with base zoning. Start with Land Use Table.
2. **Every external link listed above MUST appear on the final page.** Run a grep after building to verify. Zero links lost.
3. **No emoji.** Use SVG/PNG icons from assets/icons/ only.
4. **Banned color #003039** — replace with #3A5566 if found.
5. **No old palette colors** (#6b8fa3, #6b8e4e, #2E6F4E, #D4A017, #C58B2A, #7A2A1D).
6. Use correct functional colors: Eligible #406A64, Not Eligible #B58676, Conditional #918A83.
7. Logo = ADU.png (or ADU_MultiColors.svg on light backgrounds). No castle logo.
8. Page must load `homebody_shared.css` and inject the shared header via `homebody_header.js`.
9. Provide complete file contents for every file you modify.
10. Nav source of truth = `homebody_header.js`. Mirror = `homebody_header.html`. Must match.

## LINK VERIFICATION (CRITICAL)

After building the page, run:
```bash
grep -oP 'href="[^"]*"' dadu_eligibility_flowchart.html | sort -u > /tmp/flowchart_links.txt
cat /tmp/flowchart_links.txt
wc -l /tmp/flowchart_links.txt
```

The page should have AT MINIMUM 25+ unique external links. If fewer, links were dropped. Check against the list above and add back any that are missing.

Specifically verify these critical links are present:
```bash
grep -c "Urban%20Services%20District.pdf" dadu_eligibility_flowchart.html    # USD map PDF
grep -c "USD_GSD/MapServer" dadu_eligibility_flowchart.html                   # USD/GSD ArcGIS layer
grep -c "ParcelViewer" dadu_eligibility_flowchart.html                        # Parcel Viewer
grep -c "17.16.030" dadu_eligibility_flowchart.html                           # DADU conditions code
grep -c "17.08.030" dadu_eligibility_flowchart.html                           # Land Use Tables
grep -c "17.36.730" dadu_eligibility_flowchart.html                           # DADU Overlay code
grep -c "epermits.nashville.gov" dadu_eligibility_flowchart.html              # ePermits
grep -c "legistar.com" dadu_eligibility_flowchart.html                        # Legistar bills
```

All should return 1 or more. If any return 0, the link was dropped — add it back.

## CLAUDE.md UPDATES

- Remove `dadu_eligibility_checklist.html` and `dadu_eligibility_flowchart.html` from "Unlinked Duplicates"
- Add `dadu_eligibility_checklist.html` to "Previously Deleted"
- Add `dadu_eligibility_flowchart.html` to "Linked in Navigation" under RESOURCES
- Update RESOURCES dropdown table in Section 4

## VERIFICATION

1. Flowchart follows Nashville.gov order (Land Use Table → Lot Area → USD/GSD/UDO/SP → Single Structure → Conditions → Special Cases)
2. The USD Map PDF link works: https://maps.nashville.gov/webimages/MapGallery/PDFMaps/Urban%20Services%20District.pdf
3. Every step has its external links visible as pill buttons
4. Link count verification passes (25+ unique links)
5. Quick checklist appears below the flowchart
6. Page appears in RESOURCES > Learn nav
7. `dadu_eligibility_checklist.html` deleted
8. Colors are muted palette (#406A64, #B58676, #918A83) not traffic-light
9. No #003039, no emoji, no old colors
10. Commit:
    ```bash
    git add -A
    git commit -m "Fix eligibility flowchart: correct Nashville.gov order, restore all external links, consolidate checklist"
    git push origin main
    ```
