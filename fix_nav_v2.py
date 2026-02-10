#!/usr/bin/env python3
"""
Fix nav structure v2 — updated EXPLORE/BUILD/DATA per spec.
EXPLORE: Learn | Discover | User Types (6 items incl Developer/Investor)
BUILD: Plan | Design | Calculate | Hire | File (5 columns)
DATA: Activity | Reports | Records (renamed from Documents, expanded)
"""

import glob
import re
import os

# The OLD nav-links block (what we just deployed)
# We'll match from '<div class="nav-links">' through the right-side controls closing '</div>'
# and replace with the new version.

NEW_NAV_LINKS = '''        <div class="nav-links">
            <!-- EXPLORE: "How does this work?" -->
            <div class="nav-item">
                <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="explore">
                    Explore <span class="chevron">&#9660;</span>
                </button>
                <div class="dropdown-menu mega-menu mega-menu-3" id="explore-dropdown" role="menu">
                    <!-- Column 1: Learn -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/ADU.png" alt=""> Learn
                        </div>
                        <a href="what_is_dadu.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/ADU.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">What is a DADU?</div>
                            </div>
                        </a>
                        <a href="dadu_history.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Recorded Docs.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">History &amp; Timeline</div>
                            </div>
                        </a>
                        <a href="dadu_building_requirements.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Requirements</div>
                            </div>
                        </a>
                        <a href="dadu_zoning_standards.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Zoning.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Zoning Standards</div>
                            </div>
                        </a>
                        <a href="dadu_code_legislation_v3.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Legal.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Code &amp; Legislation</div>
                            </div>
                        </a>
                        <a href="permit_process_timeline.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Renewals.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Permit Process</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 2: Discover -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Zoning.png" alt=""> Discover
                        </div>
                        <a href="dadu_eligibility_map.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Zoning.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Eligibility Map</div>
                            </div>
                        </a>
                        <a href="property_search.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Parcel Search.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Property Search</div>
                            </div>
                        </a>
                        <a href="dadu_near_me_v2.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Neighbors.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">DADUs Near Me</div>
                            </div>
                        </a>
                        <a href="dadu_opportunity_explorer_v2.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Area Maps and Visual layers.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Opportunity Explorer</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 3: User Types -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Property Owners.png" alt=""> User Types
                        </div>
                        <a href="user-homeowners.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Property Owners.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Homeowner</div>
                            </div>
                        </a>
                        <a href="contractor_marketplace.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Contractor</div>
                            </div>
                        </a>
                        <a href="designer_resources.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Surveyers adn Engineers.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Designer / Architect</div>
                            </div>
                        </a>
                        <a href="market_trends.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Investors.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Developer / Investor</div>
                            </div>
                        </a>
                        <a href="municipal_dashboard.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Municipal.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Municipal / Agency</div>
                            </div>
                        </a>
                        <a href="legal_resources.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Legal.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Legal / Appraiser</div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>

            <!-- BUILD: "What do I do next?" -->
            <div class="nav-item">
                <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="build">
                    Build <span class="chevron">&#9660;</span>
                </button>
                <div class="dropdown-menu mega-menu mega-menu-5" id="build-dropdown" role="menu">
                    <!-- Column 1: Plan -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Exports & Reports.png" alt=""> Plan
                        </div>
                        <a href="project_planner.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Exports & Reports.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Project Planner</div>
                            </div>
                        </a>
                        <a href="project_checklist.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Renewals.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Interactive Checklist</div>
                            </div>
                        </a>
                        <a href="draw_dadu_on_parcel.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/APN Maps.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Draw DADU on Parcel</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 2: Design -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Surveyers adn Engineers.png" alt=""> Design
                        </div>
                        <a href="site_plan_downloads.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Surveyers adn Engineers.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Site Plan Finder &amp; Downloads</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 3: Calculate -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Valuations.png" alt=""> Calculate
                        </div>
                        <a href="project_cost_estimator.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Valuations.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Cost Estimator</div>
                            </div>
                        </a>
                        <a href="roi_calculator.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Appraisers.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">ROI Calculator</div>
                            </div>
                        </a>
                        <a href="size_calculator.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/ADU.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Size Calculator</div>
                            </div>
                        </a>
                        <a href="property_tax_calculator.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Investments.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Tax Calculator</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 4: Hire -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Building and Construction.png" alt=""> Hire
                        </div>
                        <a href="contractor_dashboard.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Parcel Search.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Contractor Finder</div>
                            </div>
                        </a>
                        <a href="contractor_marketplace.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Contractor Marketplace</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 5: File -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Claims.png" alt=""> File
                        </div>
                        <a href="determine_forms_required.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Claims.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Forms Wizard</div>
                            </div>
                        </a>
                        <a href="legal_form_filler.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Recordable Legal Report.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Form Filler</div>
                            </div>
                        </a>
                        <a href="owner_occupancy.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Property Owners.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Owner Occupancy</div>
                            </div>
                        </a>
                        <a href="short_term_rental_permit.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Renewals.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Short Term Rental Permit</div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>

            <!-- DATA: "Show me the proof." -->
            <div class="nav-item">
                <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="data">
                    Data <span class="chevron">&#9660;</span>
                </button>
                <div class="dropdown-menu mega-menu mega-menu-3" id="data-dropdown" role="menu">
                    <!-- Column 1: Activity -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Enhanced Transaction History Report .png" alt=""> Activity
                        </div>
                        <a href="permit_activity_dashboard.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Enhanced Transaction History Report .png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Permit Activity</div>
                            </div>
                        </a>
                        <a href="contractor_dashboard.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Contractor Activity</div>
                            </div>
                        </a>
                        <a href="market_trends.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Investments.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Market Trends</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 2: Reports -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Exports & Reports.png" alt=""> Reports
                        </div>
                        <a href="eligibility_report.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Claims.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Eligibility Report</div>
                            </div>
                        </a>
                        <a href="property-report-card.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Property Detail Report .png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Property Intelligence Report</div>
                            </div>
                        </a>
                        <a href="project_report.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Exports & Reports.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Project Report</div>
                            </div>
                        </a>
                        <a href="dadu_reports_store.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Contractor Report</div>
                            </div>
                        </a>
                        <a href="dadu_reports_store.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Market Statistics Report .png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Market Analysis</div>
                            </div>
                        </a>
                        <a href="dadu_reports_store.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Area Maps and Visual layers.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Area Analysis</div>
                            </div>
                        </a>
                    </div>

                    <!-- Column 3: Records -->
                    <div class="mega-menu-column">
                        <div class="mega-menu-column-title">
                            <img src="assets/icons/Recorded Docs.png" alt=""> Records
                        </div>
                        <a href="nashville_permit_explorer_v3.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Enhanced Transaction History Report .png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Permit Explorer</div>
                            </div>
                        </a>
                        <a href="dadu_documents_portal.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Surveyers adn Engineers.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Permit Site Plans</div>
                            </div>
                        </a>
                        <a href="property-report-card.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Property Detail Report .png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Assessor Property Card</div>
                            </div>
                        </a>
                        <a href="dadu_documents_portal.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Recorded Docs.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Recorded Documents</div>
                            </div>
                        </a>
                        <a href="restrictive_covenants_v2.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Legal.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Restrictive Covenants</div>
                            </div>
                        </a>
                        <a href="overlay-districts.html" class="dropdown-item" role="menuitem">
                            <div class="dropdown-item-icon"><img src="assets/icons/Zoning.png" alt=""></div>
                            <div class="dropdown-item-content">
                                <div class="dropdown-item-title">Zoning Documents</div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>

            <!-- PRICING: direct link -->
            <a href="homebody_pricing.html" class="nav-link">Pricing</a>
        </div>

        <!-- Right-side: Search + CTA -->
        <div style="display:flex;align-items:center;gap:12px;">
            <a href="property_search.html" class="nav-link" title="Search" style="padding:12px;">
                &#128269;
            </a>
            <a href="am_i_eligible.html" class="nav-search-btn">
                <span>Get Started</span>
                <span>&rarr;</span>
            </a>
        </div>'''


def replace_nav(content):
    """Replace the nav-links div and right-side controls."""
    # Find start of nav-links
    start = content.find('<div class="nav-links">')
    if start == -1:
        return content, False

    # Find the closing </div> of nav-container (just before </nav>)
    nav_close = content.find('</nav>', start)
    if nav_close == -1:
        return content, False

    # The </div> right before </nav> closes nav-container
    pre_nav = content[:nav_close].rstrip()
    last_div = pre_nav.rfind('</div>')
    if last_div == -1:
        return content, False

    end = last_div + 6
    new_content = content[:start] + NEW_NAV_LINKS + '\n    ' + content[end:]
    return new_content, True


def main():
    base_dir = '/Users/nataliebaldacci/DADU-Homebody-Projects'
    html_files = sorted(glob.glob(os.path.join(base_dir, '*.html')))

    print(f"Found {len(html_files)} HTML files")
    modified = 0
    errors = []

    for filepath in html_files:
        filename = os.path.basename(filepath)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content, changed = replace_nav(content)

            if changed:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified += 1
                print(f"  [OK] {filename}")
            else:
                print(f"  [--] {filename}: no nav-links found")
        except Exception as e:
            errors.append((filename, str(e)))
            print(f"  [ERR] {filename}: {e}")

    print(f"\nModified: {modified}/{len(html_files)}")
    if errors:
        print(f"Errors: {len(errors)}")
        for fn, err in errors:
            print(f"  {fn}: {err}")


if __name__ == '__main__':
    main()
