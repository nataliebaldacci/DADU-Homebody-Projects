# Document Matching Rules for Homebody Platform

This document defines the rules for matching documents to parcels and permits.
Implement these rules in Python for the document indexing pipeline.

## Overview

The document matching system has three primary goals:
1. Extract APN (Assessor Parcel Number) from document filenames
2. Extract permit numbers from document filenames
3. Link documents to parcels using APN, permit number, or address matching

---

## 1. APN Extraction Rules

### Pattern 1: Standard 11-digit APN
```python
import re

# Nashville/Davidson County standard format
PATTERN_11_DIGIT = r'^(\d{11})$'
# Example: 11801012200

# With separators
PATTERN_SEPARATED = r'^(\d{3})[-_](\d{2})[-_](\d{3})[-_](\d{2})[-_](\d{3})$'
# Example: 118-01-012-20-0

# Condo/multi-unit format (alphanumeric)
PATTERN_CONDO = r'^([A-Z0-9]{13,15})$'
# Example: 182120A00700CO
```

### Normalization Rules
```python
def normalize_apn(raw_apn: str) -> str:
    """
    Normalize APN to standard 11-digit format.
    
    Rules:
    1. Remove all non-alphanumeric characters
    2. Convert to uppercase
    3. If numeric-only and not 11 digits, pad with leading zeros
    4. Preserve alphanumeric condo APNs as-is
    """
    cleaned = re.sub(r'[^A-Z0-9]', '', raw_apn.upper())
    
    # If all numeric and less than 11 digits, pad
    if cleaned.isdigit() and len(cleaned) < 11:
        cleaned = cleaned.zfill(11)
    
    return cleaned
```

### Extraction from Filename
```python
def extract_apn_from_filename(filename: str) -> tuple[str, str]:
    """
    Extract APN candidates from filename.
    
    Returns: (normalized_apn, confidence)
    Confidence levels: 'high', 'medium', 'low', 'none'
    """
    # Remove extension
    name = os.path.splitext(filename)[0]
    
    # Try direct 11-digit match
    match = re.search(r'(\d{11})', name)
    if match:
        return normalize_apn(match.group(1)), 'high'
    
    # Try condo format (letters + numbers ending in CO)
    match = re.search(r'([A-Z0-9]{10,15}CO)', name.upper())
    if match:
        return match.group(1), 'high'
    
    # Try separated format
    match = re.search(r'(\d{3})[-_](\d{2})[-_](\d{3})[-_](\d{2})[-_](\d{3})', name)
    if match:
        apn = ''.join(match.groups())
        return normalize_apn(apn), 'medium'
    
    return None, 'none'
```

---

## 2. Permit Number Extraction Rules

### Pattern Definitions
```python
# Nashville permit format: YYYY + Type Code + Sequence
PATTERN_PERMIT_STANDARD = r'(\d{4})(BL|EL|PL|ME|DM)(\d{5,6})'
# Examples: 2024BL12345, 2023EL067890

# T-permit format
PATTERN_PERMIT_T = r'(T)(\d{4})[-_]?(\d{5})'
# Example: T2024-12345

PERMIT_TYPE_CODES = {
    'BL': 'building',
    'EL': 'electrical', 
    'PL': 'plumbing',
    'ME': 'mechanical',
    'DM': 'demolition',
    'T': 'trade'
}
```

### Extraction Function
```python
def extract_permit_number(filename: str) -> tuple[str, str, str]:
    """
    Extract permit number from filename.
    
    Returns: (permit_number, permit_type, confidence)
    """
    name = os.path.splitext(filename)[0].upper()
    
    # Try standard format
    match = re.search(r'(\d{4})(BL|EL|PL|ME|DM)(\d{5,6})', name)
    if match:
        year, type_code, seq = match.groups()
        permit_number = f"{year}{type_code}{seq}"
        permit_type = PERMIT_TYPE_CODES.get(type_code, 'unknown')
        return permit_number, permit_type, 'high'
    
    # Try T-permit
    match = re.search(r'T(\d{4})[-_]?(\d{5})', name)
    if match:
        year, seq = match.groups()
        permit_number = f"T{year}-{seq}"
        return permit_number, 'trade', 'medium'
    
    return None, None, 'none'
```

---

## 3. Document-to-Parcel Linking Strategy

### Priority Order for Linking

1. **APN Exact Match** (highest confidence)
   - Document APN matches parcel APN exactly
   - Link confidence: HIGH

2. **Permit Number Join** (high confidence)
   - Document has permit number
   - Permit is already linked to a parcel in permits database
   - Link confidence: HIGH

3. **Address Match** (medium confidence)
   - Document contains address text
   - Address normalizes to match parcel address
   - Link confidence: MEDIUM

4. **Manual Review Flag** (requires human)
   - None of the above methods succeeded
   - Flag for manual review
   - Link confidence: NONE

### Linking Implementation
```python
def link_document_to_parcel(doc: dict, parcels_db: dict, permits_db: dict) -> dict:
    """
    Attempt to link a document to a parcel.
    
    Returns updated doc with linking information.
    """
    # Method 1: APN exact match
    if doc.get('normalized_apn'):
        apn = doc['normalized_apn']
        if apn in parcels_db:
            return {
                **doc,
                'linked_parcel_id': apn,
                'link_method': 'apn_exact_match',
                'link_confidence': 'high',
                'requires_manual_review': False
            }
    
    # Method 2: Permit number join
    if doc.get('extracted_permit_number'):
        permit_num = doc['extracted_permit_number']
        if permit_num in permits_db:
            parcel_id = permits_db[permit_num].get('parcel_id')
            if parcel_id:
                return {
                    **doc,
                    'linked_parcel_id': parcel_id,
                    'link_method': 'permit_join',
                    'link_confidence': 'high',
                    'requires_manual_review': False
                }
    
    # Method 3: Address match
    if doc.get('normalized_address'):
        addr = doc['normalized_address']
        for parcel_id, parcel in parcels_db.items():
            if parcel.get('normalized_address') == addr:
                return {
                    **doc,
                    'linked_parcel_id': parcel_id,
                    'link_method': 'address_match',
                    'link_confidence': 'medium',
                    'requires_manual_review': False
                }
    
    # Method 4: Manual review required
    return {
        **doc,
        'linked_parcel_id': None,
        'link_method': None,
        'link_confidence': 'none',
        'requires_manual_review': True,
        'review_reason': 'No matching parcel found'
    }
```

---

## 4. Address Normalization

```python
ADDRESS_REPLACEMENTS = {
    'STREET': 'ST',
    'AVENUE': 'AVE',
    'BOULEVARD': 'BLVD',
    'DRIVE': 'DR',
    'ROAD': 'RD',
    'LANE': 'LN',
    'COURT': 'CT',
    'CIRCLE': 'CIR',
    'PLACE': 'PL',
    'NORTH': 'N',
    'SOUTH': 'S',
    'EAST': 'E',
    'WEST': 'W',
    'NORTHEAST': 'NE',
    'NORTHWEST': 'NW',
    'SOUTHEAST': 'SE',
    'SOUTHWEST': 'SW'
}

REMOVE_TOKENS = ['APT', 'UNIT', 'STE', 'SUITE', '#', '.', ',']

def normalize_address(address: str) -> str:
    """Normalize address for matching."""
    addr = address.upper()
    
    # Remove unwanted tokens
    for token in REMOVE_TOKENS:
        addr = addr.replace(token, ' ')
    
    # Standardize street types
    words = addr.split()
    normalized_words = [ADDRESS_REPLACEMENTS.get(w, w) for w in words]
    
    # Remove extra whitespace and return
    return ' '.join(normalized_words).strip()
```

---

## 5. Document Type Classification

```python
DOC_TYPE_KEYWORDS = {
    'permit': ['permit', 'BL', 'EL', 'PL', 'ME', 'inspection'],
    'property_card': ['property card', 'assessor', 'appraisal'],
    'deed': ['deed', 'warranty', 'quitclaim', 'trust deed'],
    'covenant': ['covenant', 'restriction', 'HOA', 'CC&R'],
    'survey': ['survey', 'plat', 'boundary', 'topographic'],
    'inspection': ['inspection', 'violation', 'citation']
}

def classify_document(filename: str, content_text: str = None) -> str:
    """Classify document type based on filename and optional content."""
    name_lower = filename.lower()
    
    for doc_type, keywords in DOC_TYPE_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in name_lower:
                return doc_type
    
    # If content provided, check that too
    if content_text:
        content_lower = content_text.lower()
        for doc_type, keywords in DOC_TYPE_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in content_lower:
                    return doc_type
    
    return 'unknown'
```

---

## 6. Output Schema

All matched documents should conform to the schema in `docs_index.json`.
Parcel summaries should conform to `parcels_docs_summary.json`.

---

## Implementation Checklist

- [ ] Implement APN extraction with all patterns
- [ ] Implement APN normalization
- [ ] Implement permit number extraction
- [ ] Implement address normalization
- [ ] Implement document classification
- [ ] Implement parcel linking with priority order
- [ ] Generate docs_index.json
- [ ] Generate parcels_docs_summary.json
- [ ] Create manual review queue for unlinked documents
