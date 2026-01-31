# Document Matching Rules for Python Processing

## Overview

This document defines the rules for matching PDF documents to parcels and permits. The Python processing pipeline will use these rules to populate `docs_index.json` and `parcels_docs_summary.json`.

## APN Extraction and Normalization

### Step 1: Extract APN Candidates from Filenames

```python
import re

def extract_apn_candidates(filename):
    """
    Extract potential APN patterns from filename.
    Nashville APNs are typically 11 digits: XXX-XX-X-XXX-XX or XXXXXXXXXXX
    """
    patterns = [
        r'\b(\d{3}[-\s]?\d{2}[-\s]?\d{1}[-\s]?\d{3}[-\s]?\d{2})\b',  # XXX-XX-X-XXX-XX
        r'\b(\d{11})\b',  # 11 consecutive digits
        r'\b(\d{3}\d{2}\d{1}\d{3}\d{2})\b',  # No separators
        r'[Aa][Pp][Nn][-_\s]*(\d{10,11})',  # APN prefix
        r'[Pp]arcel[-_\s]*(\d{10,11})',  # Parcel prefix
    ]

    candidates = []
    for pattern in patterns:
        matches = re.findall(pattern, filename)
        candidates.extend(matches)

    return candidates
```

### Step 2: Normalize APNs to Standard Format

```python
def normalize_apn(apn_string):
    """
    Normalize APN to 11-digit format without separators.
    Nashville standard: XXXXXXXXXXX (11 digits)
    """
    # Remove all non-digit characters
    digits_only = re.sub(r'\D', '', apn_string)

    # Pad or truncate to 11 digits
    if len(digits_only) == 10:
        digits_only = '0' + digits_only  # Pad with leading zero
    elif len(digits_only) == 11:
        pass  # Correct length
    elif len(digits_only) > 11:
        digits_only = digits_only[:11]  # Truncate (log warning)
    else:
        return None  # Invalid APN

    return digits_only

def format_apn_display(normalized_apn):
    """
    Format normalized APN for display: XXX-XX-X-XXX-XX
    """
    if len(normalized_apn) != 11:
        return normalized_apn
    return f"{normalized_apn[:3]}-{normalized_apn[3:5]}-{normalized_apn[5]}-{normalized_apn[6:9]}-{normalized_apn[9:]}"
```

## Permit Number Extraction

### Step 3: Extract Permit Number Candidates

```python
def extract_permit_candidates(filename):
    """
    Extract potential permit numbers from filename.
    Nashville permit formats:
    - 2024BL12345 (Building)
    - 2024EL12345 (Electrical)
    - 2024PL12345 (Plumbing)
    - 2024ME12345 (Mechanical)
    - T2024-12345 (Trade)
    """
    patterns = [
        r'\b(20\d{2}[A-Z]{2}\d{4,6})\b',  # 2024BL12345
        r'\b([TBEMPC]20\d{2}[-]?\d{4,6})\b',  # T2024-12345
        r'[Pp]ermit[-_\s#]*(\d{4}[-]?\d{4,6})',  # Permit#2024-12345
        r'\b(BL[-]?\d{4}[-]?\d{4,6})\b',  # BL-2024-12345
    ]

    candidates = []
    for pattern in patterns:
        matches = re.findall(pattern, filename, re.IGNORECASE)
        candidates.extend([m.upper() for m in matches])

    return candidates
```

## Document Type Classification

### Step 4: Classify Document Type from Filename

```python
DOC_TYPE_PATTERNS = {
    'site_plan': [
        r'site[-_\s]?plan',
        r'plot[-_\s]?plan',
        r'survey[-_\s]?plan',
    ],
    'building_permit': [
        r'building[-_\s]?permit',
        r'permit[-_\s]?application',
        r'\bBL\d',
    ],
    'restrictive_covenant': [
        r'covenant',
        r'restriction',
        r'deed[-_\s]?restriction',
        r'ccr',
    ],
    'property_report': [
        r'property[-_\s]?report',
        r'assessment',
        r'appraisal',
    ],
    'survey': [
        r'\bsurvey\b',
        r'\bplat\b',
        r'boundary',
    ],
    'inspection_report': [
        r'inspection',
        r'certificate[-_\s]?of[-_\s]?occupancy',
        r'\bCO\b',
    ],
    'zoning_letter': [
        r'zoning[-_\s]?letter',
        r'zoning[-_\s]?verification',
        r'use[-_\s]?determination',
    ],
}

def classify_doc_type(filename):
    """
    Classify document type based on filename patterns.
    Returns (doc_type, confidence)
    """
    filename_lower = filename.lower()

    for doc_type, patterns in DOC_TYPE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, filename_lower):
                return (doc_type, 'high')

    # Check file path for hints
    if '/permits/' in filename_lower or '/permit/' in filename_lower:
        return ('building_permit', 'medium')
    if '/covenant' in filename_lower:
        return ('restrictive_covenant', 'medium')
    if '/survey' in filename_lower:
        return ('survey', 'medium')

    return ('unknown', 'low')
```

## Matching Pipeline

### Step 5: Match Documents to Permits

```python
def match_doc_to_permit(doc, permits_lookup):
    """
    Match document to permit by permit number.
    permits_lookup: dict keyed by normalized permit number
    """
    permit_candidates = extract_permit_candidates(doc['filename'])

    for candidate in permit_candidates:
        normalized = normalize_permit_number(candidate)
        if normalized in permits_lookup:
            return {
                'permit_id': normalized,
                'confidence': 'high',
                'method': 'permit_number_match'
            }

    return None
```

### Step 6: Match Documents to Parcels

```python
def match_doc_to_parcel(doc, parcels_lookup, address_index):
    """
    Match document to parcel. Priority order:
    1. Direct APN match
    2. Permit -> Parcel lookup
    3. Address match
    4. Manual review flag
    """
    # Try APN match first
    apn_candidates = extract_apn_candidates(doc['filename'])
    for candidate in apn_candidates:
        normalized = normalize_apn(candidate)
        if normalized and normalized in parcels_lookup:
            return {
                'apn': normalized,
                'confidence': 'high',
                'method': 'apn_match'
            }

    # Try permit -> parcel lookup
    if doc.get('linked_permit_id'):
        permit = permits_lookup.get(doc['linked_permit_id'])
        if permit and permit.get('parcel_apn'):
            return {
                'apn': permit['parcel_apn'],
                'confidence': 'high',
                'method': 'permit_to_parcel'
            }

    # Try address extraction and match
    address = extract_address_from_filename(doc['filename'])
    if address:
        normalized_addr = normalize_address(address)
        if normalized_addr in address_index:
            apns = address_index[normalized_addr]
            if len(apns) == 1:
                return {
                    'apn': apns[0],
                    'confidence': 'medium',
                    'method': 'address_match'
                }
            else:
                # Multiple parcels at address - flag for review
                return {
                    'apn': None,
                    'confidence': 'low',
                    'method': 'address_ambiguous',
                    'candidates': apns
                }

    # No match found - flag for manual review
    return {
        'apn': None,
        'confidence': 'none',
        'method': 'manual_review_needed'
    }
```

### Step 7: Address Extraction and Normalization

```python
def extract_address_from_filename(filename):
    """
    Extract street address from filename.
    """
    patterns = [
        r'(\d+[-\s]?\w+[-\s]?\w*[-\s]?(?:st|street|ave|avenue|blvd|boulevard|dr|drive|rd|road|ln|lane|ct|court|pl|place|way|cir|circle))',
    ]

    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            return match.group(1)

    return None

def normalize_address(address):
    """
    Normalize address for matching.
    """
    if not address:
        return None

    addr = address.lower().strip()

    # Standardize street suffixes
    replacements = {
        r'\bstreet\b': 'st',
        r'\bavenue\b': 'ave',
        r'\bboulevard\b': 'blvd',
        r'\bdrive\b': 'dr',
        r'\broad\b': 'rd',
        r'\blane\b': 'ln',
        r'\bcourt\b': 'ct',
        r'\bplace\b': 'pl',
        r'\bcircle\b': 'cir',
    }

    for pattern, replacement in replacements.items():
        addr = re.sub(pattern, replacement, addr)

    # Remove extra spaces and punctuation
    addr = re.sub(r'[^\w\s]', '', addr)
    addr = re.sub(r'\s+', ' ', addr)

    return addr.strip()
```

## Output Generation

### Step 8: Generate parcels_docs_summary.json

```python
def generate_parcels_summary(docs_index):
    """
    Generate parcels_docs_summary.json from docs_index.json
    """
    parcels = {}
    address_index = {}

    for doc in docs_index['documents']:
        apn = doc.get('linked_parcel_apn')
        if not apn:
            continue

        if apn not in parcels:
            parcels[apn] = {
                'apn': apn,
                'apn_formatted': format_apn_display(apn),
                'address': doc.get('extracted_address'),
                'total_docs': 0,
                'docs_by_category': {},
                'permits': [],
                'flags': {}
            }

        # Update counts
        parcels[apn]['total_docs'] += 1

        # Group by category
        category = docs_index['doc_types'].get(doc['doc_type'], {}).get('category', 'other')
        if category not in parcels[apn]['docs_by_category']:
            parcels[apn]['docs_by_category'][category] = {
                'count': 0,
                'doc_ids': []
            }

        parcels[apn]['docs_by_category'][category]['count'] += 1
        parcels[apn]['docs_by_category'][category]['doc_ids'].append(doc['doc_id'])

        # Update address index
        if doc.get('extracted_address'):
            norm_addr = normalize_address(doc['extracted_address'])
            if norm_addr:
                if norm_addr not in address_index:
                    address_index[norm_addr] = []
                if apn not in address_index[norm_addr]:
                    address_index[norm_addr].append(apn)

    return {
        '_schema_version': '1.0.0',
        '_generated_from': 'docs_index.json',
        '_last_updated': datetime.now().isoformat(),
        'parcels': parcels,
        'index_by_address': address_index,
        'statistics': {
            'total_parcels_with_docs': len(parcels),
            'parcels_with_permits': sum(1 for p in parcels.values() if p.get('permits')),
            'parcels_with_covenants': sum(1 for p in parcels.values()
                if 'covenants' in p.get('docs_by_category', {}))
        }
    }
```

## Processing Pipeline Summary

```
1. Scan PDF directory for all files
2. For each PDF:
   a. Extract APN candidates from filename
   b. Extract permit number candidates from filename
   c. Classify document type
   d. Extract address if present
3. Load permits lookup table (from ArcGIS or existing data)
4. Load parcels lookup table (from ArcGIS or existing data)
5. For each document:
   a. Try permit number match
   b. Try APN match
   c. Try address match
   d. Flag for manual review if no match
6. Generate docs_index.json
7. Generate parcels_docs_summary.json
8. Output manual review list
```

## Confidence Levels

| Level | Description | Action Required |
|-------|-------------|-----------------|
| `high` | Direct match on APN or permit number | None |
| `medium` | Address match or permit-to-parcel lookup | Verify in UI |
| `low` | Multiple candidates or ambiguous | Review before publishing |
| `none` | No match found | Manual assignment required |

## File Naming Conventions for Best Results

To maximize automatic matching, recommend these filename patterns:

```
[APN]_[PermitNumber]_[DocType]_[Date].pdf
Example: 12345678900_2024BL12345_site_plan_20240315.pdf

[Address]_[DocType]_[Date].pdf
Example: 123_Main_St_covenant_20230601.pdf
```
