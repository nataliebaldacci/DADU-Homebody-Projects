#!/usr/bin/env python3
"""Remove remaining inline nav blocks from files that have both
site-header div AND a leftover inline nav."""

import re

FILES = [
    'feature-documents.html',
    'features.html',
    'index_pq.html',
    'property-report-card.html',
    'user-homeowners.html',
    'user-types.html',
]

BASE = '/Users/nataliebaldacci/DADU-Homebody-Projects/'

# Match old-style nav: from <!-- Top Bar --> or <div class="top-bar"> through </nav>
OLD_NAV = re.compile(
    r'\s*<!-- Top Bar -->.*?</nav>\s*\n?',
    re.DOTALL
)

OLD_NAV_ALT = re.compile(
    r'\s*<div class="top-bar">.*?</nav>\s*\n?',
    re.DOTALL
)

# Also match <!-- Navigation --> blocks
NAV_COMMENT = re.compile(
    r'\s*<!-- Navigation -->.*?</nav>\s*\n?',
    re.DOTALL
)

for fname in FILES:
    path = BASE + fname
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only process if site-header is already present
    if 'id="site-header"' not in content:
        print(f"  SKIP {fname}: no site-header div")
        continue

    original = content

    # Remove any remaining inline nav blocks (after the site-header div)
    # Find position of site-header
    sh_pos = content.find('id="site-header"')

    # Search for old nav blocks after site-header
    after = content[sh_pos:]

    m = OLD_NAV.search(after)
    if not m:
        m = OLD_NAV_ALT.search(after)
    if not m:
        m = NAV_COMMENT.search(after)

    if m:
        # Remove the matched block from the full content
        abs_start = sh_pos + m.start()
        abs_end = sh_pos + m.end()
        content = content[:abs_start] + '\n' + content[abs_end:]

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  FIXED {fname}")
    else:
        print(f"  NO CHANGE {fname}")

print("\nDone!")
