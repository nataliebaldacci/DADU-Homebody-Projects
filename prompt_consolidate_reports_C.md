# TASK: Fix Contractor Report + Preserve Aerial Embed

Two small tasks.

## Task 1: Fix contractor_report.html

Read the current file. If it searches by AREA (showing contractors in a neighborhood), rewrite it to search by CONTRACTOR instead.

- Search input: "Enter contractor name or license number"
- Load data from: data/contractor_stats.json
- Output for ONE contractor:
  - Business name
  - License number
  - Total permits and DADU permits
  - Years active
  - Total project value
  - Average cost per project
  - Zip codes served
  - Permit type breakdown
  - Individual permit table with columns: permit #, address, date, cost, sqft, status
  - Each permit row links to Nashville docs: https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={PERMIT_NUMBER}

Branding: homebody_shared.css, homebody_header.js, Inter font, no #003039, no emoji.

If this was already done correctly (searches by contractor not area), skip it.

## Task 2: Preserve Aerial Embed

Check if `property-report-card.html` already has an aerial image section (Patriot Properties iframe or Google aerial link) and a Google Street View section.

If NOT, check `dadu_report_full.html` for these sections and copy them into property-report-card.html.

Aerial URL pattern:
```
https://portal.patriotproperties.com/?APIKEY=5D050659143EB96630FB38B91DE12E40&SECRETKEY=...&LAT={lat}&LONG={lon}
```

Street View URL pattern:
```
https://www.google.com/maps?q&layer=c&cbll={LATITUDE},{LONGITUDE}
```

Add these as sections in property-report-card.html if they're missing. They should use the same lat/lon that the page already has for the parcel.

Do NOT delete any files.

```bash
git add -A && git commit -m "Fix contractor report search + preserve aerial embed" && git push origin main
```
