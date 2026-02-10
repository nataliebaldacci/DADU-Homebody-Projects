#!/usr/bin/env python3
"""
Script to update all HTML files to use the shared header
"""
import os
import re
from pathlib import Path

REPO_DIR = Path("/Users/nataliebaldacci/Desktop/Master_Data/DADU/DADU_Homebody/GitHub_Repo")

KEY_PAGES = [
    "index.html",
    "what_is_dadu.html",
    "dadu_history.html",
    "dadu_building_requirements.html",
    "dadu_zoning_standards.html",
    "dadu_code_legislation_v3.html",
    "permit_process_timeline.html",
    "dadu_eligibility_map.html",
    "property_search.html",
    "dadu_near_me_v2.html",
    "dadu_opportunity_explorer_v2.html",
    "user-homeowners.html",
    "project_planner.html",
    "project_checklist.html",
    "draw_dadu_on_parcel.html",
    "site_plan_downloads.html",
    "project_cost_estimator.html",
    "roi_calculator.html",
    "size_calculator.html",
    "property_tax_calculator.html",
    "determine_forms_required.html",
    "legal_form_filler.html",
    "owner_occupancy.html",
    "contractor_dashboard.html",
    "eligibility_report.html",
    "project_report.html",
    "nashville_permit_explorer_v3.html",
    "dadu_documents_portal.html",
    "restrictive_covenants_v2.html",
    "overlay-districts.html",
    "pdf_database_lookup.html",
    "property-report-card.html",
    "am_i_eligible.html",
    "homebody_dadu_pricing.html",
]

HEADER_INCLUDE = '''<div id="homebody-header-container"></div>
<script>
    fetch('homebody_header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('homebody-header-container').innerHTML = data;
        });
</script>
'''

def extract_body_content(html_content):
    """Extract everything after <body> tag"""
    body_match = re.search(r'<body[^>]*>(.*)</body>', html_content, re.DOTALL | re.IGNORECASE)
    if body_match:
        return body_match.group(1)
    return None

def remove_existing_header(body_content):
    """Remove existing header/nav elements"""
    # Remove common header patterns
    patterns = [
        r'<header[^>]*>.*?</header>',
        r'<div[^>]*class="[^"]*header[^"]*"[^>]*>.*?</div>(?:\s*</div>)*',
        r'<nav[^>]*class="[^"]*homebody-nav[^"]*"[^>]*>.*?</nav>',
        r'<!--.*?Homebody.*?Navigation.*?-->.*?(?=<div|<main|<section)',
    ]

    for pattern in patterns:
        body_content = re.sub(pattern, '', body_content, flags=re.DOTALL | re.IGNORECASE)

    return body_content.strip()

def update_html_file(filepath):
    """Update a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already using shared header
        if 'homebody-header-container' in content or 'homebody_header.html' in content:
            return 'already_updated'

        # Extract body content
        body_content = extract_body_content(content)
        if not body_content:
            return 'no_body_found'

        # Remove existing header
        cleaned_body = remove_existing_header(body_content)

        # Get head content
        head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL | re.IGNORECASE)
        head_content = head_match.group(1) if head_match else ''

        # Build new HTML
        new_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{head_content}
</head>
<body>
{HEADER_INCLUDE}

{cleaned_body}
</body>
</html>'''

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)

        return 'updated'

    except Exception as e:
        return f'error: {str(e)}'

def main():
    os.chdir(REPO_DIR)

    results = {
        'updated': [],
        'already_updated': [],
        'no_body_found': [],
        'missing': [],
        'error': []
    }

    for page in KEY_PAGES:
        filepath = REPO_DIR / page
        if not filepath.exists():
            results['missing'].append(page)
            continue

        result = update_html_file(filepath)

        if result == 'updated':
            results['updated'].append(page)
        elif result == 'already_updated':
            results['already_updated'].append(page)
        elif result == 'no_body_found':
            results['no_body_found'].append(page)
        else:
            results['error'].append(f"{page}: {result}")

    # Print results
    print("=" * 60)
    print("HEADER UPDATE RESULTS")
    print("=" * 60)

    if results['updated']:
        print(f"\n✓ Updated ({len(results['updated'])} files):")
        for page in results['updated']:
            print(f"  • {page}")

    if results['already_updated']:
        print(f"\n→ Already using shared header ({len(results['already_updated'])} files):")
        for page in results['already_updated']:
            print(f"  • {page}")

    if results['missing']:
        print(f"\n✗ Missing files ({len(results['missing'])}):")
        for page in results['missing']:
            print(f"  • {page}")

    if results['no_body_found']:
        print(f"\n⚠ Could not parse ({len(results['no_body_found'])}):")
        for page in results['no_body_found']:
            print(f"  • {page}")

    if results['error']:
        print(f"\n✗ Errors ({len(results['error'])}):")
        for error in results['error']:
            print(f"  • {error}")

    print("\n" + "=" * 60)
    print(f"Total: {len(results['updated']) + len(results['already_updated'])} pages ready")
    print("=" * 60)

if __name__ == '__main__':
    main()
