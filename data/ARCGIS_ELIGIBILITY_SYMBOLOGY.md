# ArcGIS Eligibility Layer Symbology Guide

This document defines the color palette and symbology for the DADU Eligibility parcel layer in ArcGIS. These colors must match the Homebody website palette for visual consistency.

---

## Color Palette (RGB & Hex)

| Status | Hex Code | RGB | Description |
|--------|----------|-----|-------------|
| **Eligible** | `#6b8e4e` | `107, 142, 78` | Property meets all DADU requirements |
| **Conditional** | `#f39c12` | `243, 156, 18` | May require variance or additional review |
| **Not Eligible** | `#c0392b` | `192, 57, 43` | Property does not meet DADU requirements |
| **Unknown/Null** | `#999999` | `153, 153, 153` | Eligibility not determined |

---

## ArcGIS Pro Symbology Settings

### Unique Values Renderer

**Field:** `[ELIGIBILITY_FIELD_NAME]` *(see below for field configuration)*

| Value | Symbol Color | Outline |
|-------|--------------|---------|
| `E` or `Eligible` | #6b8e4e (fill) | #5a7a42, 0.5pt |
| `C` or `Conditional` | #f39c12 (fill) | #d68910, 0.5pt |
| `N` or `Not Eligible` | #c0392b (fill) | #a93226, 0.5pt |
| `U` or `Unknown` / `<Null>` | #999999 (fill) | #777777, 0.5pt |

### Fill Opacity
- **Recommended:** 70% fill opacity for parcel polygons
- **Outline:** 100% opacity, 0.5pt width

---

## Layer Definition Query (Optional)

To show only residential parcels eligible for DADU analysis:

```sql
LAND_USE IN ('RS', 'RS-A', 'R', 'R-A', 'RM') OR ZONING LIKE 'RS%' OR ZONING LIKE 'R%'
```

---

## Legend Configuration

**Title:** DADU Eligibility Status

**Legend Items:**
1. Eligible - Meets all DADU requirements
2. Conditional - May require variance
3. Not Eligible - Does not qualify
4. Unknown - Not yet determined

---

## Field Configuration

### REQUIRED: Eligibility Field Name

**Please confirm the field name in your parcel layer that contains eligibility status.**

Common options:
- `DADU_ELIGIBLE`
- `ELIGIBILITY`
- `DADU_STATUS`
- `ADU_ELIGIBLE`

### Expected Coded Values

**Option A: Single Character Codes**
| Code | Meaning |
|------|---------|
| `E` | Eligible |
| `C` | Conditional |
| `N` | Not Eligible |
| `U` | Unknown |

**Option B: Full Text Values**
| Value | Meaning |
|-------|---------|
| `Eligible` | Eligible |
| `Conditional` | Conditional |
| `Not Eligible` | Not Eligible |
| `Unknown` | Unknown |

**Option C: Numeric Codes**
| Code | Meaning |
|------|---------|
| `1` | Eligible |
| `2` | Conditional |
| `0` | Not Eligible |
| `-1` or `NULL` | Unknown |

---

## CSS Variables for Web Map Integration

If using ArcGIS Online Web Map with custom popups:

```css
:root {
    --eligible: #6b8e4e;
    --eligible-dark: #5a7a42;
    --conditional: #f39c12;
    --conditional-dark: #d68910;
    --not-eligible: #c0392b;
    --not-eligible-dark: #a93226;
    --unknown: #999999;
}
```

---

## Popup Configuration

**Title:** `{ADDRESS}` or `{APN}`

**Content:**
```
Eligibility: {ELIGIBILITY_FIELD}
Zoning: {ZONING}
Lot Size: {LOT_SQFT} sq ft
APN: {APN}

[Link to Property Report Card]
```

---

## Action Required

To complete the ArcGIS layer configuration, please provide:

1. **Field name** containing eligibility status
2. **Coded values** used in that field (E/C/N or Eligible/Conditional/Not Eligible, etc.)
3. **Layer URL** if hosted on ArcGIS Online

Once confirmed, the web application will be updated to match these values exactly.
