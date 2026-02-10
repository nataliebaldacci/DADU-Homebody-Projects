#!/usr/bin/env python3
"""Verify all navigation links exist"""
import os
from pathlib import Path

REPO_DIR = Path("/Users/nataliebaldacci/Desktop/Master_Data/DADU/DADU_Homebody/GitHub_Repo")

# All links from the navigation
NAV_LINKS = [
    # Logo
    "index.html",
    # Explore > Learn
    "what_is_dadu.html",
    "dadu_history.html",
    "dadu_building_requirements.html",
    "dadu_zoning_standards.html",
    "dadu_code_legislation_v3.html",
    "permit_process_timeline.html",
    # Explore > Discover
    "dadu_eligibility_map.html",
    "property_search.html",
    "dadu_near_me_v2.html",
    "dadu_opportunity_explorer_v2.html",
    # Explore > User Types
    "user-homeowners.html",
    "contractor_marketplace.html",
    "designer_resources.html",
    "municipal_dashboard.html",
    "legal_resources.html",
    # Build > Plan
    "project_planner.html",
    "project_checklist.html",
    "draw_dadu_on_parcel.html",
    # Build > Design
    "site_plan_downloads.html",
    # Build > Calculate
    "project_cost_estimator.html",
    "roi_calculator.html",
    "size_calculator.html",
    "property_tax_calculator.html",
    # Build > Hire
    "contractor_marketplace.html",
    # Build > File
    "determine_forms_required.html",
    "legal_form_filler.html",
    "owner_occupancy.html",
    "short_term_rental_permit.html",
    # Data > Activity
    "permit_activity_dashboard.html",
    "contractor_dashboard.html",
    "market_trends.html",
    # Data > Reports
    "eligibility_report.html",
    "project_report.html",
    "dadu_reports_store.html",
    "sample_reports/sample_property_report.html",
    "sample_reports/sample_contractor_report.html",
    "sample_reports/sample_market_stats_report.html",
    "sample_reports/sample_neighbors_report.html",
    # Data > Records
    "nashville_permit_explorer_v3.html",
    "site_plan_downloads.html",
    "dadu_documents_portal.html",
    "restrictive_covenants_v2.html",
    "overlay-districts.html",
    "pdf_database_lookup.html",
    # Pricing
    "homebody_pricing.html",
    # Header actions
    "property_search.html",
    "project_planner.html",
    "am_i_eligible.html",
]

os.chdir(REPO_DIR)

missing = []
existing = []

for link in sorted(set(NAV_LINKS)):
    filepath = REPO_DIR / link
    if filepath.exists() or (filepath.is_symlink() and filepath.resolve().exists()):
        existing.append(link)
    else:
        missing.append(link)

print("=" * 70)
print("NAVIGATION LINK VERIFICATION")
print("=" * 70)

if missing:
    print(f"\n✗ BROKEN LINKS ({len(missing)}):")
    for link in missing:
        print(f"  • {link}")
else:
    print("\n✓ ALL LINKS WORKING")

print(f"\n✓ Valid links: {len(existing)}/{len(set(NAV_LINKS))}")
print("=" * 70)
