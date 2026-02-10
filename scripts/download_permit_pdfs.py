#!/usr/bin/env python3
"""
Download ADU permit PDFs from Nashville Documents Portal
Uses Playwright for browser automation.

Setup:
    pip install playwright
    playwright install chromium

Usage:
    python scripts/download_permit_pdfs.py
    python scripts/download_permit_pdfs.py --start 0 --count 50  # process 50 permits starting at index 0
"""

import json
import os
import sys
import time
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Download ADU permit PDFs')
    parser.add_argument('--start', type=int, default=0, help='Start index')
    parser.add_argument('--count', type=int, default=50, help='Number of permits to process')
    parser.add_argument('--output', type=str, default='permit_pdfs', help='Output directory')
    parser.add_argument('--timeout', type=int, default=30000, help='Page timeout in ms')
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright not installed. Run:")
        print("  pip install playwright")
        print("  playwright install chromium")
        sys.exit(1)

    # Load ADU permits
    script_dir = Path(__file__).parent
    permits_file = script_dir / '..' / 'data' / 'adu_permit_numbers.json'

    with open(permits_file) as f:
        permits = json.load(f)

    print(f"Total ADU permits: {len(permits)}")
    subset = permits[args.start:args.start + args.count]
    print(f"Processing permits {args.start} to {args.start + len(subset)}")

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)

    # Track results
    results = {
        'downloaded': [],
        'no_docs': [],
        'errors': []
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False so you can see what's happening
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        page.set_default_timeout(args.timeout)

        for i, permit in enumerate(subset):
            permit_num = permit['permit_number']
            apn = permit.get('apn', 'unknown')
            idx = args.start + i

            print(f"\n[{idx+1}/{args.start + len(subset)}] Permit: {permit_num} (APN: {apn})")

            try:
                # Navigate to the permit documents page
                url = f"https://documents.nashville.gov/Request/Form/PermitCodes?permitnumber={permit_num}"
                page.goto(url)

                # Wait for the page to load
                time.sleep(3)

                # Click the Search button if present
                search_btn = page.query_selector('input[type="submit"], button[type="submit"]')
                if search_btn:
                    search_btn.click()
                    print("  Clicked search button, waiting for results...")
                    time.sleep(5)

                # Wait for results to appear
                # Look for document links in the results
                page.wait_for_selector('.results-table a, .document-link, table a[href*="Request/Open"], a[href*="Request/Open"]', timeout=15000)

                # Find all document links
                doc_links = page.query_selector_all('a[href*="Request/Open"]')

                if not doc_links:
                    print(f"  No documents found for permit {permit_num}")
                    results['no_docs'].append(permit_num)
                    continue

                print(f"  Found {len(doc_links)} document(s)")

                # Click the first document link
                first_link = doc_links[0]
                href = first_link.get_attribute('href')
                print(f"  Opening: {href}")

                # Try to download
                with page.expect_download(timeout=30000) as download_info:
                    first_link.click()

                download = download_info.value
                filename = f"{apn}_{permit_num}_{download.suggested_filename}"
                save_path = output_dir / filename
                download.save_as(str(save_path))

                print(f"  Saved: {filename}")
                results['downloaded'].append({
                    'permit': permit_num,
                    'apn': apn,
                    'filename': filename
                })

            except Exception as e:
                error_msg = str(e)[:100]
                print(f"  Error: {error_msg}")
                results['errors'].append({
                    'permit': permit_num,
                    'apn': apn,
                    'error': error_msg
                })

            # Brief pause between requests
            time.sleep(2)

        browser.close()

    # Save results
    results_file = output_dir / 'download_results.json'
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*50}")
    print(f"RESULTS")
    print(f"{'='*50}")
    print(f"Downloaded: {len(results['downloaded'])}")
    print(f"No docs:    {len(results['no_docs'])}")
    print(f"Errors:     {len(results['errors'])}")
    print(f"\nResults saved to: {results_file}")

if __name__ == '__main__':
    main()
