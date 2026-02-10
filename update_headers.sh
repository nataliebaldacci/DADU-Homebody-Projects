#!/bin/bash
# Script to update headers in all HTML files

REPO_DIR="/Users/nataliebaldacci/Desktop/Master_Data/DADU/DADU_Homebody/GitHub_Repo"
cd "$REPO_DIR"

# List of key pages to update
KEY_PAGES=(
    "index.html"
    "what_is_dadu.html"
    "dadu_history.html"
    "dadu_building_requirements.html"
    "dadu_zoning_standards.html"
    "dadu_code_legislation_v3.html"
    "permit_process_timeline.html"
    "dadu_eligibility_map.html"
    "property_search.html"
    "dadu_near_me_v2.html"
    "dadu_opportunity_explorer_v2.html"
    "user-homeowners.html"
    "project_planner.html"
    "project_checklist.html"
    "draw_dadu_on_parcel.html"
    "site_plan_downloads.html"
    "project_cost_estimator.html"
    "roi_calculator.html"
    "size_calculator.html"
    "property_tax_calculator.html"
    "determine_forms_required.html"
    "legal_form_filler.html"
    "owner_occupancy.html"
    "contractor_dashboard.html"
    "eligibility_report.html"
    "project_report.html"
    "nashville_permit_explorer_v3.html"
    "dadu_documents_portal.html"
    "restrictive_covenants_v2.html"
    "overlay-districts.html"
    "pdf_database_lookup.html"
    "property-report-card.html"
    "am_i_eligible.html"
    "homebody_dadu_pricing.html"
)

echo "Pages to be updated:"
for page in "${KEY_PAGES[@]}"; do
    if [ -f "$page" ]; then
        echo "  ✓ $page"
    else
        echo "  ✗ MISSING: $page"
    fi
done
