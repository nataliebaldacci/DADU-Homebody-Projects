#!/usr/bin/env python3
"""Replace old castle SVG with new mockup-matching SVG in all HTML files."""

import glob
import re

# Regex to match old castle SVG regardless of indentation
OLD_PATTERN = re.compile(
    r'<svg[^>]*viewBox="0 0 64 64"[^>]*>\s*'
    r'<!-- Secondary castle \(DADU\)[^>]*-->'
    r'.*?'
    r'<!-- Shared ground line -->'
    r'.*?</svg>',
    re.DOTALL
)

# New SVG content (without leading indent — will be re-indented per match)
NEW_SVG_LINES = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 50" width="44" height="37" aria-hidden="true">',
    '    <!-- Left castle (DADU) — Tan -->',
    '    <rect x="6" y="12" width="5" height="5" fill="#D4C5A9"/>',
    '    <rect x="15" y="12" width="5" height="5" fill="#D4C5A9"/>',
    '    <rect x="6" y="17" width="14" height="3" fill="#D4C5A9"/>',
    '    <rect x="8" y="20" width="10" height="23" fill="#D4C5A9"/>',
    '    <rect x="11" y="34" width="4" height="9" rx="2" fill="#F2F0ED"/>',
    '    <!-- Right castle (main) — Deep Slate -->',
    '    <rect x="26" y="4" width="6" height="6" fill="#3A5566"/>',
    '    <rect x="38" y="4" width="6" height="6" fill="#3A5566"/>',
    '    <rect x="26" y="10" width="18" height="4" fill="#3A5566"/>',
    '    <rect x="28" y="14" width="14" height="29" fill="#3A5566"/>',
    '    <rect x="32" y="32" width="6" height="11" rx="3" fill="#F2F0ED"/>',
    '    <!-- Ground arc — Warm Stone -->',
    '    <path d="M1,46 Q30,40 59,46" stroke="#7B746D" stroke-width="2.5" fill="none" stroke-linecap="round"/>',
    '</svg>',
]

def replace_svg(match):
    """Replace old SVG, preserving the indentation of the <svg> tag."""
    matched = match.group(0)
    # Detect indentation: find leading whitespace before <svg
    lines = matched.split('\n')
    svg_line = lines[0]
    indent = len(svg_line) - len(svg_line.lstrip())
    base = ' ' * indent
    inner = base + '    '
    result_lines = []
    for i, line in enumerate(NEW_SVG_LINES):
        if i == 0:
            result_lines.append(base + line)
        elif line == '</svg>':
            result_lines.append(base + line)
        else:
            result_lines.append(inner + line)
    return '\n'.join(result_lines)


def main():
    files = glob.glob("/Users/nataliebaldacci/DADU-Homebody-Projects/**/*.html", recursive=True)
    updated = 0

    for filepath in sorted(files):
        if filepath.endswith("homebody_header.html"):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if OLD_PATTERN.search(content):
            new_content = OLD_PATTERN.sub(replace_svg, content)
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                updated += 1
                print(f"  Updated: {filepath.split('/')[-1]}")

    print(f"\nDone! Updated {updated} files.")

if __name__ == "__main__":
    main()
