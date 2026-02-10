#!/usr/bin/env python3
"""Refactor all HTML files to use injected header via <div id="site-header"></div>.

For each file:
1. Remove inline nav block (from <!-- Top Bar --> through </nav>)
2. Insert <div id="site-header"></div> in its place
3. Ensure <link rel="stylesheet" href="homebody_shared.css"> is in <head>
4. Ensure <script src="homebody_header.js"></script> is before </body>
"""

import glob
import re

SITE_HEADER_DIV = '<div id="site-header"></div>'

# Pattern to match the full inline nav block:
# Starts with <!-- Top Bar --> or <div class="top-bar">
# Ends with </nav> (possibly followed by whitespace/newline)
NAV_BLOCK = re.compile(
    r'\n*\s*<!-- Top Bar -->.*?</nav>\s*\n?',
    re.DOTALL
)

# Alternate pattern: starts directly with <div class="top-bar">
NAV_BLOCK_ALT = re.compile(
    r'\n*\s*<div class="top-bar">.*?</nav>\s*\n?',
    re.DOTALL
)

CSS_LINK = '<link rel="stylesheet" href="homebody_shared.css">'
JS_TAG = '<script src="homebody_header.js"></script>'


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = []

    # Step 1: Replace inline nav with site-header div
    m = NAV_BLOCK.search(content)
    if not m:
        m = NAV_BLOCK_ALT.search(content)

    if m:
        # Preserve the newline before main content
        replacement = '\n' + SITE_HEADER_DIV + '\n\n'
        content = content[:m.start()] + replacement + content[m.end():]
        changes.append('nav→injected')
    else:
        return None  # No inline nav found, skip

    # Step 2: Ensure CSS link is in <head>
    if 'homebody_shared.css' not in content:
        # Insert before </head>
        content = content.replace('</head>', '    ' + CSS_LINK + '\n</head>')
        changes.append('+css')

    # Step 3: Ensure JS tag is present (before </body>)
    if 'homebody_header.js' not in content:
        content = content.replace('</body>', JS_TAG + '\n</body>')
        changes.append('+js')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return None


def main():
    files = glob.glob("/Users/nataliebaldacci/DADU-Homebody-Projects/*.html")
    updated = 0
    skipped = 0

    for filepath in sorted(files):
        fname = filepath.split('/')[-1]

        # Skip the header template file itself
        if fname == 'homebody_header.html':
            continue

        result = process_file(filepath)
        if result:
            print(f"  {fname}: {', '.join(result)}")
            updated += 1
        else:
            skipped += 1

    print(f"\nDone! {updated} files refactored, {skipped} skipped (no inline nav).")


if __name__ == "__main__":
    main()
