# TASK: Simplify DATA Dropdown to Single Report Generator Link

The DATA dropdown currently lists 5 individual report pages in Column 1. Replace them with a SINGLE link.

## Current Column 1 (Report Generator):
- Eligibility Report → eligibility_report.html
- Project Report → project_report.html
- Neighbors Report → neighbors_report.html
- Market Report → dadu_reports_store.html
- Property Report Card → property-report-card.html

## New Column 1 (Reports):
ONE link only:
- Report Generator (icon: Exports__Reports.svg) → dadu_reports_store.html

That's it. All report types are on the landing page now.

## Column 2 (Document Database): NO CHANGES
Keep exactly as-is:
- Site Plans & Permits → site_plan_downloads.html
- Recorded Documents → dadu_documents_portal.html
- Restrictive Covenants → restrictive_covenants_v2.html
- PDF Database → pdf_database_lookup.html

Update BOTH `homebody_header.js` AND `homebody_header.html`. They must stay in sync.

Do NOT change any other dropdown. Only change DATA Column 1.

```bash
git add -A && git commit -m "Simplify DATA dropdown: single Report Generator link" && git push origin main
```
