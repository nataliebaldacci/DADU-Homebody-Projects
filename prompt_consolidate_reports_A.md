# TASK: Rebuild Report Generator Landing Page

Rebuild `dadu_reports_store.html` as a master Report Generator landing page showcasing all 6 report types.

## Page Structure

**Hero:** var(--slate) #3A5566 background, Exports__Reports.svg icon in linen circle, "Report Generator" heading (white, Inter, 800), subtitle "Property intelligence reports built from Nashville's public permit, parcel, and regulatory data." (var(--cream)), stats row: "6 Report Types | 285,512 Parcels | 4,700+ Permits | 12,500+ Documents"

**Section "Choose a Report":** var(--background) #F2F0ED, grid of 6 report cards. Each card has: icon in linen circle, report name, price badge (var(--wheat) bg pill), description (3-4 sentences), "What's Included" bullets (4-6 items), two buttons ("Generate Report" var(--wheat) bg + "View Sample" outline), "Popular with:" tags at bottom.

## The 6 Report Cards

**1. DADU Eligibility Report - $4.99** (Claims.png)
Instant eligibility determination under BL2025-1007. Zoning, service district, lot size, max dimensions, height, owner occupancy. Flags overlay districts, covenants, historic designations.
Included: zoning/service district verification, max living area + footprint calcs, height limit, covenant flag, overlay check, owner occupancy summary.
Generate → eligibility_report.html | Sample → sample_reports/sample_eligibility_report.html
Popular with: Homeowners, Agents, Attorneys

**2. Property Report Card - $4.99** (Property_Detail_Report_.svg)
Complete parcel intelligence. Assessor data, building characteristics, permit history, covenants, portal links, aerial, street view.
Included: parcel details, building characteristics, permit history, covenant records, aerial + street view, links to ParcelViewer/ePermits/Assessor/Property Card.
Generate → property-report-card.html | Sample → sample_reports/sample_property_report.html
Popular with: Homeowners, Appraisers, Investors

**3. Neighbors / Area Comparables - $14.99** (Neighbors.svg)
All DADU activity in neighborhood/zip. Costs, timelines, contractors, sizes. Most active builders and cost trends.
Included: all DADUs in radius, avg cost + cost/SF, most active contractors, timeline stats, cost trends, comparable details.
Generate → neighbors_report.html | Sample → sample_reports/sample_neighbors_report.html
Popular with: Homeowners, Investors, Contractors

**4. Contractor Report - $9.99** (Building_and_Construction.svg)
Search by contractor NAME or LICENSE. Full permit history, avg costs, zip codes, years active. Each permit links to Nashville docs.
Included: total permits + DADU permits, avg cost, zip codes served, years active, individual permits with doc links, permit type breakdown.
Generate → contractor_report.html | Sample → sample_reports/sample_contractor_report.html
Popular with: Homeowners, Contractors, Investors

**5. Project Report - $9.99** (Project_Planner.svg)
Planning-stage analysis. Eligibility + cost estimates + permits + timeline from comparable projects. Includes forms checklist and recommended contractors.
Included: eligibility summary, estimated cost range, required permits/forms, comparable costs, estimated timeline, recommended contractors.
Generate → project_report.html | Sample → "Coming Soon" (disabled/grayed button)
Popular with: Homeowners, Designers, Contractors

**6. Market Statistics - $14.99** (Market_Statistics_Report_.svg)
Nashville DADU market analysis. Permit trends, costs, contractor share, demand by zip. 2017-present with YoY comparisons.
Included: permit volume by year/month, cost trends, top contractors, activity by zip, permit type distribution, YoY growth.
Generate → nashville_permit_analytics.html | Sample → sample_reports/sample_market_stats_report.html
Popular with: Investors, Contractors, Municipal

**Additional Sample Reports** section below the 6 cards (var(--card-bg)):
- Covenant Analysis → sample_reports/sample_covenant_report.html
- Permit History → sample_reports/sample_permit_history_report.html
- Cost Estimate → sample_reports/sample_cost_estimate_report.html
- Zoning Verification → sample_reports/sample_zoning_report.html

**Bottom CTA:** var(--slate) bg, "Need Custom Analysis?", "Contact us for bulk reports, custom data exports, or enterprise pricing.", button mailto:hello@castlehold.com

## Branding
- Load homebody_shared.css, inject homebody_header.js
- No #003039, no emoji, Inter font
- "Homebody Projects" user-facing, "Castlehold" only in footer

## Do NOT delete any files. Do NOT change any other pages. Only rebuild dadu_reports_store.html.

```bash
git add -A && git commit -m "Rebuild Report Generator landing page with 6 report cards" && git push origin main
```
