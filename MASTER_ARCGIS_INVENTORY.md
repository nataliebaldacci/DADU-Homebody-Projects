# MASTER ARCGIS INVENTORY
# All Feature Services & Webmaps for Castlehold / Homebody Projects
# Organized by category with recommended site placement

## WEBMAPS (Ready to embed as iframes or "View in ArcGIS" links)

| ID | Name | Recommended Page | Action |
|----|------|-----------------|--------|
| 50bbdc9c... | DADU Permits (map 1) | permit_explorer.html | "View in ArcGIS" button |
| e07213bc... | DADU Permits (map 2, + covenants) | existing_dadus_map.html | "View in ArcGIS" button |
| d3f149a9... | DADU Footprints | parcel_footprint_map.html | "View in ArcGIS" button |
| 168e16cf... | Restrictive Covenants | restrictive_covenants_v2.html | Full iframe embed |
| d6c2c06d... | DADU Eligibility BL2025-1007 | dadu_eligibility_map.html | "View in ArcGIS" button |
| 9f40d0ca... | Existing DADUs | existing_dadus_map.html | Full iframe embed option |
| ea4b9925... | Unknown (Vandy private) | TBD | Need to identify |
| 07538ad8... | Unknown (Vandy private) | TBD | Need to identify |
| a02edb68... | Unknown (Vandy private) | TBD | Need to identify |

---

## FEATURE SERVICES - PERMITS (Point layers)

| Service | Records | URL | Used On Site? |
|---------|---------|-----|---------------|
| DADU_All_Permits_MERGED_v2_20260213 | 4,117 | services3.arcgis.com/.../DADU_All_Permits_MERGED_v2_20260213/FeatureServer | BEST - newest merged |
| NEW_ADU_Permits_20260114 | 4,117 | services3.arcgis.com/.../NEW_ADU_Permits_20260114/FeatureServer/0 | Used by permit_explorer |
| DADU_All_Permits_Final | ~4,100 | services3.arcgis.com/.../DADU_All_Permits_Final/FeatureServer/0 | Used by some pages |
| DADU_All_Permits | older | services3.arcgis.com/.../DADU_All_Permits/FeatureServer/0 | Older version |
| DADU_Permits_Combined | older | services3.arcgis.com/.../DADU_Permits_Combined/FeatureServer/0 | Older version |
| DADU_Permit_Type_1bUTSV | ? | services3.arcgis.com/.../DADU_Permit_Type_1bUTSV/FeatureServer | Unknown subset |

**RECOMMENDATION:** Standardize all pages to use DADU_All_Permits_MERGED_v2_20260213 as the single permit source.

---

## FEATURE SERVICES - ELIGIBILITY (161,703 parcels)

| Service | Records | Type | URL |
|---------|---------|------|-----|
| DADU_Eligibility_ENHANCED_20260119 | 161,703 | Points | services3.arcgis.com/.../DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer/0 |
| Eligibility_Enhanced_Polygons_20260213 | 161,703 | Polygons | services3.arcgis.com/.../Eligibility_Enhanced_Polygons_20260213_065606/FeatureServer |
| eligibility_parcels | ~161K | Polygons | services3.arcgis.com/.../eligibility_parcels/FeatureServer |
| DADU_BL2025_1007_Eligible_20251230 | eligible only | Points | services3.arcgis.com/.../DADU_BL2025_1007_Eligible_20251230_011045/FeatureServer/0 |

**Key fields:** Final_Eligibility, Eligibility_Path, Eligibility_Status, Lot_SqFt, Max_DADU_Living_SF, Zoning, Service_District, In_USD, In_GSD, all overlay fields

**RECOMMENDATION:** Use Eligibility_Enhanced_Polygons for the eligibility map (fills parcels with color). Use the points version for property search lookups (faster queries).

---

## FEATURE SERVICES - BUILDING SPECS (per-parcel DADU rules)

| Service | Records | URL |
|---------|---------|-----|
| DADU_Building_Specs_20260119 | 161,703 | services3.arcgis.com/.../DADU_Building_Specs_20260119_042856/FeatureServer/0 |
| Building_Specs_Polygons_20260213 | 209,000 | services3.arcgis.com/.../Building_Specs_Polygons_20260213_065606/FeatureServer |
| Parcels_Building_Info_20260213 | ? | services3.arcgis.com/.../Parcels_Building_Info_20260213_070754/FeatureServer |

**Key fields:** DADU_Max_Living_SF, DADU_Max_Footprint_SF, DADU_Max_Height_Ft, DADU_Front/Side/Rear_Setback_Ft, DADU_Parking_Required, Owner_Occupancy_Required, STR_Allowed, Design_Review_Required, Principal_Footprint_SF, Principal_Height_Ft, Approx_Buildable_Area_SF

**RECOMMENDATION:** Use Building_Specs for property_search.html, am_i_eligible.html, eligibility_report.html, and property-report-card.html. This has everything needed for the "What Can I Build" section.

---

## FEATURE SERVICES - BUILDING FOOTPRINTS

| Service | Records | URL |
|---------|---------|-----|
| Footprints_With_ParcelData_20260118 | 327K+ | services3.arcgis.com/.../Footprints_With_ParcelData_20260118_011423/FeatureServer/0 |
| Building_Footprints_SingleFamily | subset | services3.arcgis.com/.../Building_Footprints_SingleFamily/FeatureServer/0 |
| SF_Footprints_Flattened_20251118_2 | subset | services3.arcgis.com/.../SF_Footprints_Flattened_20251118_2/FeatureServer |
| TN_Structure_Footprints | statewide | services3.arcgis.com/.../TN_Structure_Footprints/FeatureServer/0 |
| Nashville Building_Footprints_view | 327K+ | services2.arcgis.com/HdTo6HJqh92wn4D8/.../Building_Footprints_view/FeatureServer |

**Key fields:** APN, AssessorCardNumber, Nash_Height, Nash_Area, StructureType, FinishedArea, YearBuilt, Height_Combined, Footprint_Rank

**RECOMMENDATION:** Use Footprints_With_ParcelData as the primary footprint layer. It has APN linkage, assessor card numbers, and height data. Load on zoom 16+ only.

---

## FEATURE SERVICES - EXISTING DADUS / SECONDARY STRUCTURES

| Service | Description | URL |
|---------|-------------|-----|
| Secondary_SFH_Merged_20251231 | Merged existing DADUs | services3.arcgis.com/.../Secondary_SFH_Merged_SHP_20251231_0015/FeatureServer/0 |
| Secondary_On_SF_Parcels_20251230 | Secondary structures on SF lots | services3.arcgis.com/.../Secondary_On_SF_Parcels_SHP_20251230_2352/FeatureServer/0 |
| Secondary_Addresses_NotP_20251230 | Non-primary address points | services3.arcgis.com/.../Secondary_Addresses_NotP_SHP_20251230_2312/FeatureServer |
| DADU_Complete_20251230 | 178K all SF homes | services3.arcgis.com/.../DADU_Complete_SHP_20251230_1348/FeatureServer/0 |
| SFH_parcels | All SF homes with URLs | services3.arcgis.com/.../SFH_parcels/FeatureServer/0 |

**RECOMMENDATION:** Use Secondary_SFH_Merged as the "Existing DADUs" layer on existing_dadus_map.html and secondary_structures_map.html.

---

## FEATURE SERVICES - RESTRICTIVE COVENANTS

| Service | Description | URL |
|---------|-------------|-----|
| Restrictive_Covenant_Links | Covenants WITH PDF links | services3.arcgis.com/.../\_Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer/0 |
| Parcels_with_CR | Parcels flagged with covenants | services3.arcgis.com/.../\_Parcels_with_CR__A1_AP43711_wk1ztG/FeatureServer/0 |
| Parcels_with_Restrictive_Covenants | Another covenant parcel layer | services3.arcgis.com/.../Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer/0 |

**RECOMMENDATION:** Use Restrictive_Covenant_Links on restrictive_covenants_v2.html and property-report-card.html (it has the actual PDF URLs). Use Parcels_with_CR for the eligibility map covenant toggle.

---

## METRO NASHVILLE SERVICES (may have CORS issues from GitHub Pages)

| Service | URL |
|---------|-----|
| Address Points | maps.nashville.gov/arcgis/rest/services/Addressing/AddressPoints/MapServer/0 |
| Zoning Overlay Districts | services2.arcgis.com/HdTo6HJqh92wn4D8/.../Zoning_Overlay_Districts_Vw/FeatureServer/0 |
| Parcel History / Zoning | maps.nashville.gov/arcgis2/rest/services/Parcels/ParcelHistory/MapServer/5 |

**NOTE:** maps.nashville.gov has CORS issues. Use services2 and services3 URLs from GitHub Pages.

---

## RECOMMENDED LAYER ASSIGNMENTS PER PAGE

### dadu_eligibility_map.html
- PRIMARY: Eligibility_Enhanced_Polygons (fill parcels green/red/yellow)
- TOGGLE: Parcels_with_CR (covenant overlay)
- TOGGLE: Footprints_With_ParcelData (at zoom 16+)
- LINK: Webmap d6c2c06d (View in ArcGIS)

### existing_dadus_map.html
- PRIMARY: DADU_All_Permits_MERGED_v2 (permit markers)
- TOGGLE: Secondary_SFH_Merged (existing secondary structures)
- TOGGLE: Footprints_With_ParcelData (at zoom 16+)
- TOGGLE: Restrictive_Covenant_Links (covenants with PDF links)
- LINK: Webmap e07213bc (View in ArcGIS with Covenants)
- EMBED: Webmap 9f40d0ca (Existing DADUs ArcGIS view)

### property_search.html
- PRIMARY: DADU_Building_Specs (query per parcel)
- OVERLAY: Footprints_With_ParcelData (show building shapes)
- DATA: DADU_Eligibility_ENHANCED (eligibility status per parcel)

### permit_explorer.html
- PRIMARY: DADU_All_Permits_MERGED_v2 (all permits with filters)
- LINK: Webmap 50bbdc9c (View in ArcGIS)

### restrictive_covenants_v2.html
- EMBED: Webmap 168e16cf (full ArcGIS covenant map)
- DATA: Restrictive_Covenant_Links (searchable table with PDF links)

### parcel_footprint_map.html
- PRIMARY: Footprints_With_ParcelData
- LINK: Webmap d3f149a9 (View in ArcGIS)

### property-report-card.html
- QUERY: DADU_Building_Specs (per-parcel specs)
- QUERY: Footprints_With_ParcelData (building shapes for that APN)
- QUERY: Restrictive_Covenant_Links (covenant check for that APN)
- QUERY: DADU_All_Permits_MERGED_v2 (permit history for that APN)
