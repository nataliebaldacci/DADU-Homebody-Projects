#!/usr/bin/env python3
"""Propagate 3 nav changes to all HTML files:
1. Replace SVG logo with PNG img tag
2. Remove Hire column from Build dropdown (mega-menu-4 -> mega-menu-3)
3. Add Records column to Data dropdown (mega-menu-3 -> mega-menu-4)
"""

import glob
import re

# ── 1. Logo: replace SVG with PNG img ──
SVG_PATTERN = re.compile(
    r'<svg[^>]*viewBox="0 0 60 50"[^>]*>\s*'
    r'<!-- Left castle \(DADU\)[^>]*-->'
    r'.*?</svg>',
    re.DOTALL
)

LOGO_IMG = '<img src="assets/castlehold-logo.png" alt="Castlehold" width="44" height="37" style="object-fit:contain;">'

def replace_svg_with_img(match):
    """Replace SVG block with img tag, preserving indentation."""
    matched = match.group(0)
    first_line = matched.split('\n')[0]
    indent = len(first_line) - len(first_line.lstrip())
    return ' ' * indent + LOGO_IMG

# ── 2. Build: remove Hire column, change mega-menu-4 to mega-menu-3 ──
BUILD_PATTERN = re.compile(
    r'(<div\s+class="dropdown-menu mega-menu )(mega-menu-4)(" id="build-dropdown"[^>]*>)'
    r'(.*?)'
    r'(</div>\s*</div>\s*</div>(?=\s*<!-- DATA))',
    re.DOTALL
)

# Match the Hire column
HIRE_COLUMN = re.compile(
    r'\s*<!-- Column \d+: Hire -->.*?</div>\s*(?=\s*<!-- Column)',
    re.DOTALL
)

# Also handle compact (single-line) nav variations
HIRE_COLUMN_ALT = re.compile(
    r'\s*<div class="mega-menu-column">\s*<div class="mega-menu-column-title">.*?Hire.*?</div>.*?Contractor Marketplace.*?</div>\s*(?=\s*<div class="mega-menu-column">)',
    re.DOTALL
)

# ── 3. Data: replace entire data dropdown with new 4-col version ──
DATA_PATTERN = re.compile(
    r'<div\s+class="dropdown-menu mega-menu mega-menu-\d+"\s+id="data-dropdown"[^>]*>'
    r'.*?'
    r'</div>\s*</div>\s*</div>(?=\s*(?:<!-- PRICING|<a href="homebody_pricing))',
    re.DOTALL
)

NEW_DATA_MENU_LINES = [
    '<div class="dropdown-menu mega-menu mega-menu-4" id="data-dropdown" role="menu">',
    '    <!-- Column 1: Activity -->',
    '    <div class="mega-menu-column">',
    '        <div class="mega-menu-column-title">',
    '            <img src="assets/icons/Enhanced Transaction History Report .png" alt=""> Activity',
    '        </div>',
    '        <a href="permit_activity_dashboard.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Enhanced Transaction History Report .png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Permit Activity</div>',
    '            </div>',
    '        </a>',
    '        <a href="contractor_dashboard.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Contractor Dashboard</div>',
    '            </div>',
    '        </a>',
    '        <a href="market_trends.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Investments.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Market Trends</div>',
    '            </div>',
    '        </a>',
    '    </div>',
    '',
    '    <!-- Column 2: Reports -->',
    '    <div class="mega-menu-column">',
    '        <div class="mega-menu-column-title">',
    '            <img src="assets/icons/Exports & Reports.png" alt=""> Reports',
    '        </div>',
    '        <a href="eligibility_report.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Claims.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Eligibility Report</div>',
    '            </div>',
    '        </a>',
    '        <a href="project_report.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Exports & Reports.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Project Report</div>',
    '            </div>',
    '        </a>',
    '        <a href="dadu_reports_store.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Building and Construction.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Contractor Report</div>',
    '            </div>',
    '        </a>',
    '        <a href="dadu_reports_store.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Market Statistics Report .png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Market Analysis</div>',
    '            </div>',
    '        </a>',
    '        <a href="dadu_reports_store.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Area Maps and Visual layers.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Area Analysis</div>',
    '            </div>',
    '        </a>',
    '        <a href="property-report-card.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Property Detail Report .png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Property Report</div>',
    '            </div>',
    '        </a>',
    '    </div>',
    '',
    '    <!-- Column 3: Records -->',
    '    <div class="mega-menu-column">',
    '        <div class="mega-menu-column-title">',
    '            <img src="assets/icons/Recorded Docs.png" alt=""> Records',
    '        </div>',
    '        <a href="dadu_documents_portal.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Recorded Docs.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Recorded Documents</div>',
    '            </div>',
    '        </a>',
    '        <a href="restrictive_covenants_v2.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Legal.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Restrictive Covenants</div>',
    '            </div>',
    '        </a>',
    '        <a href="overlay-districts.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Zoning.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Zoning Documents</div>',
    '            </div>',
    '        </a>',
    '        <a href="property-report-card.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Property Detail Report .png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Property Cards</div>',
    '            </div>',
    '        </a>',
    '    </div>',
    '',
    '    <!-- Column 4: Documents -->',
    '    <div class="mega-menu-column">',
    '        <div class="mega-menu-column-title">',
    '            <img src="assets/icons/Enhanced Transaction History Report .png" alt=""> Documents',
    '        </div>',
    '        <a href="nashville_permit_explorer_v3.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Enhanced Transaction History Report .png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Permit Explorer</div>',
    '            </div>',
    '        </a>',
    '        <a href="dadu_code_legislation_v3.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Legal.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Code &amp; Legislation</div>',
    '            </div>',
    '        </a>',
    '        <a href="dadu_design_standards.html" class="dropdown-item" role="menuitem">',
    '            <div class="dropdown-item-icon"><img src="assets/icons/Surveyers adn Engineers.png" alt=""></div>',
    '            <div class="dropdown-item-content">',
    '                <div class="dropdown-item-title">Design Standards</div>',
    '            </div>',
    '        </a>',
    '    </div>',
    '</div>',
]


def replace_data_menu(match):
    """Replace data dropdown, detecting indent from the match."""
    matched = match.group(0)
    first_line = matched.split('\n')[0]
    indent = len(first_line) - len(first_line.lstrip())
    base = ' ' * indent

    # Build the closing </div></div></div> that was part of the match
    # The match ends with </div>\s*</div>\s*</div>
    # We need the new menu content + the closing tags for the nav-item wrapper
    lines = []
    for line in NEW_DATA_MENU_LINES:
        if line == '':
            lines.append('')
        elif line.startswith('<div class="dropdown-menu'):
            lines.append(base + line)
        elif line == '</div>':
            lines.append(base + line)
        else:
            lines.append(base + line)

    result = '\n'.join(lines)
    # Add the closing </div> tags for the nav-item and button wrapper
    result += '\n' + base[:-4] + '</div>\n' + base[:-8] + '</div>'
    return result


def main():
    files = glob.glob("/Users/nataliebaldacci/DADU-Homebody-Projects/**/*.html", recursive=True)
    stats = {'logo': 0, 'build': 0, 'data': 0}

    for filepath in sorted(files):
        if filepath.endswith(('homebody_header.html', 'fix_nav_v3.py', 'fix_nav_svg.py', 'fix_nav_v2.py')):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content
        changes = []

        # 1. Logo SVG -> PNG
        if SVG_PATTERN.search(content):
            content = SVG_PATTERN.sub(replace_svg_with_img, content)
            changes.append('logo')
            stats['logo'] += 1

        # 2. Build: remove Hire column + change mega-menu-4 to mega-menu-3
        if 'id="build-dropdown"' in content and 'mega-menu-4' in content.split('id="build-dropdown"')[0].split('data-dropdown="build"')[-1] if 'data-dropdown="build"' in content else False:
            # Change mega-menu-4 to mega-menu-3 for build
            content = re.sub(
                r'(class="dropdown-menu mega-menu )mega-menu-4(" id="build-dropdown")',
                r'\1mega-menu-3\2',
                content
            )
        # Remove Hire column from build section
        if '> Hire' in content and 'Contractor Marketplace' in content:
            # Try structured comment-based match first
            hire_match = HIRE_COLUMN.search(content)
            if hire_match:
                content = content[:hire_match.start()] + content[hire_match.end():]
                changes.append('build')
                stats['build'] += 1
            else:
                hire_match = HIRE_COLUMN_ALT.search(content)
                if hire_match:
                    content = content[:hire_match.start()] + content[hire_match.end():]
                    changes.append('build')
                    stats['build'] += 1
            # Also fix the mega-menu class
            content = re.sub(
                r'(class="dropdown-menu mega-menu )mega-menu-4(" id="build-dropdown")',
                r'\1mega-menu-3\2',
                content
            )

        # 3. Data: replace entire dropdown if it doesn't already have Records
        if 'id="data-dropdown"' in content and '> Records' not in content:
            # Find and replace the data dropdown content
            # Match from data-dropdown opening div to the closing tags before PRICING
            data_re = re.compile(
                r'(<div\s+class="dropdown-menu mega-menu mega-menu-\d+"\s+id="data-dropdown"[^>]*>)'
                r'(.*?)'
                r'(</div>\s*</div>\s*</div>)(?=\s*(?:<!-- PRICING|<a href="homebody_pricing|<a\s+href="homebody_pricing))',
                re.DOTALL
            )
            m = data_re.search(content)
            if m:
                # Detect indentation
                start_line = content[:m.start()].split('\n')[-1] if '\n' in content[:m.start()] else ''
                indent = len(start_line)
                base = ' ' * indent

                new_lines = []
                for line in NEW_DATA_MENU_LINES:
                    if line == '':
                        new_lines.append('')
                    else:
                        new_lines.append(base + line)
                new_menu = '\n'.join(new_lines)
                # Close the dropdown div, then the nav-item div
                closing = '\n' + ' ' * max(0, indent - 4) + '</div>\n' + ' ' * max(0, indent - 8) + '</div>'

                content = content[:m.start()] + new_menu + closing + content[m.end():]
                changes.append('data')
                stats['data'] += 1

        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            fname = filepath.split('/')[-1]
            print(f"  {fname}: {', '.join(changes)}")

    print(f"\nDone! Logo: {stats['logo']}, Build: {stats['build']}, Data: {stats['data']} files updated.")


if __name__ == "__main__":
    main()
