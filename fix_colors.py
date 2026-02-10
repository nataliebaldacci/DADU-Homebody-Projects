#!/usr/bin/env python3
"""Replace all legacy colors with Castlehold palette across all HTML and CSS files."""

import glob
import re

# Color mappings: old → new (case-insensitive matching)
COLOR_MAP = {
    '#2c3e50': '#3A5566',   # old navy → Deep Slate
    '#34495e': '#4A6B7D',   # old dark → Lighter Slate
    '#1a252f': '#2E4553',   # old darker → Darker Slate
    '#6b8fa3': '#7B746D',   # old blue-gray → Warm Stone
    '#6b8e4e': '#3A5566',   # old green → Deep Slate (no green in palette)
    '#c9a86c': '#7B746D',   # old gold → Warm Stone
    '#e8e4df': '#F2F0ED',   # old warm bg → Background
    '#b55a3c': '#C58B2A',   # old terracotta → Ochre
}

def main():
    files = glob.glob("/Users/nataliebaldacci/DADU-Homebody-Projects/**/*.html", recursive=True)
    files += glob.glob("/Users/nataliebaldacci/DADU-Homebody-Projects/**/*.css", recursive=True)
    files += glob.glob("/Users/nataliebaldacci/DADU-Homebody-Projects/**/*.js", recursive=True)

    total_replacements = 0
    files_changed = 0

    for filepath in sorted(files):
        # Skip our own script files
        if filepath.endswith(('.py',)):
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content
        file_count = 0

        for old_color, new_color in COLOR_MAP.items():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(old_color), re.IGNORECASE)
            matches = len(pattern.findall(content))
            if matches > 0:
                content = pattern.sub(new_color, content)
                file_count += matches

        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            fname = filepath.split('DADU-Homebody-Projects/')[-1]
            print(f"  {fname}: {file_count} replacements")
            total_replacements += file_count
            files_changed += 1

    print(f"\nDone! {total_replacements} color replacements across {files_changed} files.")


if __name__ == "__main__":
    main()
