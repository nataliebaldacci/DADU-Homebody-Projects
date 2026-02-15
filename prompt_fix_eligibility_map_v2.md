# TASK: Fix DADU Eligibility Map Page — Stats, Layer Controls, Layout

**File:** `dadu_eligibility_map.html`

## Problems to Fix

### Problem 1: Eligibility Statistics Are Wrong

The stats displayed on the page do not match verified data. The correct numbers are:

| Stat | Correct Value | Source |
|------|--------------|--------|
| Total Nashville Parcels | 285,512 | ArcGIS Parcels_with_Building_Characteristics view |
| Eligible (USD, by-right) | 67,707 | BL2025-1007 analysis |
| Eligible (USD + GSD with overlay) | ~161,702 | DADU_Eligibility_ENHANCED layer (161,703 records) |
| Not Eligible | ~123,810 | 285,512 minus 161,702 |

**How to display these stats:**

The stats bar should show 4 values:
- **285,512** — "Total Parcels Analyzed"
- **67,707** — "Eligible (USD By-Right)" — use var(--eligible) #406A64 for the number
- **~94,000** — "Conditional (GSD + Overlay Required)" — use var(--conditional) #918A83 for the number. Calculate as: 161,702 minus 67,707 = ~94,000
- **~123,810** — "Not Eligible" — use var(--not-eligible) #B58676 for the number

**Do NOT dynamically query ArcGIS to calculate these.** Hardcode the verified numbers. Dynamic queries are too slow for page load and the numbers don't change (they're based on a fixed legislative analysis). If you want, add a small note below the stats: "Based on BL2025-1007 eligibility analysis of all Nashville-Davidson County parcels."

### Problem 2: Layer Toggle Controls Are Confusing

The left sidebar currently has dropdowns/toggles labeled:
- Zoning District
- All Zoning
- Overlay Layers
- DADU Permits
- Restrictive Covenants
- Building Footprints
- Existing DADUs

These are **map layer visibility toggles** — turning them on/off shows or hides data layers on the map. But they're presented as dropdowns, which makes users think they need to select something. The user found them confusing and didn't understand what they do.

**Fix: Redesign the layer panel as clear ON/OFF toggles with explanations.**

Replace the current sidebar with a "Map Layers" panel that uses toggle switches (not dropdowns):

```html
<div class="layer-panel">
  <h3 style="color: var(--slate); font-weight: 700; font-size: 14px; margin-bottom: 12px;">
    Map Layers
  </h3>
  <p style="color: var(--stone); font-size: 12px; margin-bottom: 16px;">
    Toggle data layers on the map
  </p>
  
  <!-- Each layer toggle -->
  <div class="layer-toggle">
    <label class="toggle-switch">
      <input type="checkbox" checked data-layer="eligibility">
      <span class="toggle-slider"></span>
    </label>
    <div class="layer-info">
      <span class="layer-name">DADU Eligibility</span>
      <span class="layer-desc">Parcel eligibility under BL2025-1007</span>
    </div>
  </div>
  
  <div class="layer-toggle">
    <label class="toggle-switch">
      <input type="checkbox" data-layer="permits">
      <span class="toggle-slider"></span>
    </label>
    <div class="layer-info">
      <span class="layer-name">DADU Permits</span>
      <span class="layer-desc">827 historic DADU building permits</span>
    </div>
  </div>
  
  <div class="layer-toggle">
    <label class="toggle-switch">
      <input type="checkbox" data-layer="covenants">
      <span class="toggle-slider"></span>
    </label>
    <div class="layer-info">
      <span class="layer-name">Restrictive Covenants</span>
      <span class="layer-desc">43,000+ parcels with recorded covenants</span>
    </div>
  </div>
  
  <div class="layer-toggle">
    <label class="toggle-switch">
      <input type="checkbox" data-layer="footprints">
      <span class="toggle-slider"></span>
    </label>
    <div class="layer-info">
      <span class="layer-name">Building Footprints</span>
      <span class="layer-desc">327,000+ structures with height data</span>
    </div>
  </div>
  
  <div class="layer-toggle">
    <label class="toggle-switch">
      <input type="checkbox" data-layer="existing">
      <span class="toggle-slider"></span>
    </label>
    <div class="layer-info">
      <span class="layer-name">Existing DADUs</span>
      <span class="layer-desc">Properties with confirmed secondary structures</span>
    </div>
  </div>
  
  <hr style="border: none; border-top: 1px solid var(--gray-light); margin: 16px 0;">
  
  <!-- Zoning filter is the ONE dropdown that makes sense -->
  <div class="layer-filter">
    <label class="filter-label">Filter by Zoning</label>
    <select class="zoning-select" data-filter="zoning">
      <option value="all">All Eligible Zones</option>
      <option value="R">R (Residential)</option>
      <option value="RS">RS (Single Family)</option>
    </select>
  </div>
  
  <div class="layer-filter">
    <label class="filter-label">Service District</label>
    <select class="district-select" data-filter="district">
      <option value="all">All</option>
      <option value="USD">USD (By-Right)</option>
      <option value="GSD">GSD (Overlay Required)</option>
    </select>
  </div>
</div>
```

**Toggle switch CSS:**
```css
.layer-panel {
  padding: 16px;
  background: var(--card-bg);
  border-right: 1px solid var(--gray-light);
  width: 280px;
  overflow-y: auto;
}
.layer-toggle {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 8px 0;
  border-bottom: 1px solid var(--gray-light);
}
.toggle-switch {
  position: relative;
  width: 40px;
  height: 22px;
  flex-shrink: 0;
  margin-top: 2px;
}
.toggle-switch input { opacity: 0; width: 0; height: 0; }
.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: var(--gray-light);
  border-radius: 22px;
  transition: 0.2s;
}
.toggle-slider:before {
  content: "";
  position: absolute;
  height: 16px;
  width: 16px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  border-radius: 50%;
  transition: 0.2s;
}
.toggle-switch input:checked + .toggle-slider {
  background-color: var(--slate);
}
.toggle-switch input:checked + .toggle-slider:before {
  transform: translateX(18px);
}
.layer-name {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: var(--slate);
}
.layer-desc {
  display: block;
  font-size: 11px;
  color: var(--stone);
  margin-top: 2px;
}
.filter-label {
  display: block;
  font-size: 12px;
  font-weight: 600;
  color: var(--slate);
  margin-bottom: 4px;
}
.zoning-select, .district-select {
  width: 100%;
  padding: 6px 8px;
  border: 1px solid var(--gray-light);
  border-radius: 6px;
  font-family: Inter, sans-serif;
  font-size: 13px;
  color: var(--gray-warm);
  background: white;
}
.layer-filter {
  margin-bottom: 12px;
}
```

**Keep the zoning and district as dropdowns** (they filter data, which is a dropdown use case). But change the layer visibility controls from dropdowns to toggle switches. This makes the difference clear: toggles show/hide layers, dropdowns filter within a layer.

### Problem 3: Layout (Stats Above Map)

There's an old layout prompt (`eligibility_map_layout_prompt.md`) in the repo but it used banned colors and was never executed. The correct layout is:

```
[Shared Header Nav]
[Page Title: "DADU Eligibility Map" + subtitle]
[Stats Bar: 4 stat cards in a row]
[Legend: inline color dots with labels]
[Layer Panel (left sidebar) | Map (full remaining space)]
```

**Stats bar:** Horizontal row between the title and the map. Background var(--card-bg). Each stat card has a large number (24px, bold) with a small label below (12px). Use the functional colors for eligible/conditional/not-eligible numbers.

**Legend:** Small horizontal row below the stats bar, above the map. Three items:
- Green dot (#406A64) + "Eligible"
- Gray dot (#918A83) + "Conditional"  
- Clay dot (#B58676) + "Not Eligible"

Keep it compact. The legend should not take more than one line.

**Map:** Full remaining viewport height below the stats bar/legend. The left sidebar layer panel overlaps or sits beside the map (whichever the current layout does — don't change the map positioning logic, just the sidebar content).

**Remove** any floating panel on the right side of the map if one exists. The stats are now in the top bar.

### Problem 5: Remove Hardcoded Example Addresses from Search

The search bar currently shows suggested/autocomplete addresses that include real people's home addresses (e.g., a Salem Dr address). This is inappropriate. 

**Fix:**
- Remove ALL hardcoded example addresses from the search suggestions/autocomplete dropdown
- Remove any static address list used to populate suggestions
- The ONLY acceptable placeholder text in the search input is: `placeholder="Enter a Nashville address (e.g., 100 Broadway)"`
- 100 Broadway is a commercial address (Bridgestone Arena area) and safe to use as an example
- If there is a JavaScript array or object containing sample addresses, delete it entirely
- If autocomplete is wired to a geocoder API (ArcGIS, etc.), that is fine and should stay. The issue is only with HARDCODED addresses of real homes.

Search for arrays, objects, or HTML that contain street addresses and remove them:
```bash
# Find hardcoded address lists
grep -n 'Salem\|suggested.*address\|sampleAddress\|exampleAddress\|autocomplete.*data' dadu_eligibility_map.html
```

### Problem 6: Branding

- Title: "DADU Eligibility Map | Homebody Projects"
- Load homebody_shared.css, inject homebody_header.js
- Remove hardcoded header/nav
- Fix all colors to current palette
- "Castlehold" only in footer "Powered by"
- No emoji
- Font: Inter

## CRITICAL: Do NOT Break the Map

The map itself works. It loads ArcGIS layers and renders parcels. **Do NOT change:**
- The ArcGIS layer URLs or query logic
- The map initialization code (tile layers, zoom, center)
- How parcels are rendered/colored on the map
- Click/hover behavior on parcels
- Any popup or tooltip logic

**ONLY change:**
- The HTML structure around the map (stats bar, legend, sidebar panel)
- The sidebar toggle/filter controls
- The CSS styling
- The branding

Read the existing JavaScript carefully. The layer toggles in the sidebar need to call the same show/hide functions the current dropdowns call. Map the `data-layer` attribute values to the existing layer variable names in the JS. If the current code uses something like `map.addLayer(permitsLayer)` / `map.removeLayer(permitsLayer)`, wire the new toggle switches to call the same functions.

## CONSTRAINTS

1. **Never fabricate stats.** Use the verified numbers listed above.
2. **No emoji.**
3. **No #003039.** Replace with #3A5566.
4. **No old colors** (#6b8fa3, #6b8e4e, #2c3e50, #c9a86c, #e8e4df, #C58B2A, #D4A017, #2E6F4E, #7A2A1D, #B55A3C).
5. **Font: Inter.**
6. **Map must still work after changes.** Test that layer toggles show/hide the correct layers.
7. Provide complete file contents.

## VERIFICATION

```bash
# No hardcoded home addresses
grep -ic 'salem\|sample.*address.*\[' dadu_eligibility_map.html
# Should be 0

# Placeholder uses 100 Broadway
grep -c '100 Broadway' dadu_eligibility_map.html
# Should be 1

# Correct title
grep '<title>' dadu_eligibility_map.html
# Should say "DADU Eligibility Map | Homebody Projects"

# Correct stats present
grep -c '285,512\|67,707\|123,810' dadu_eligibility_map.html
# Should be 3+ (all three stats present)

# No banned colors
grep -c '#003039\|#2c3e50\|#6b8fa3\|#6b8e4e' dadu_eligibility_map.html
# Should be 0

# Has toggle switches
grep -c 'toggle-switch\|toggle-slider' dadu_eligibility_map.html
# Should be 5+ (one per layer)

# Shared CSS and header
grep -c 'homebody_shared.css' dadu_eligibility_map.html
grep -c 'homebody_header.js' dadu_eligibility_map.html
# Both should be 1+

# ArcGIS layer URLs still present (not accidentally deleted)
grep -c 'arcgis\|FeatureServer\|MapServer' dadu_eligibility_map.html
# Should be 1+ (map code intact)
```

Visual verification:
1. Stats bar shows 4 correct numbers above the map
2. Legend shows 3 colored dots with labels
3. Layer panel has 5 toggle switches (not dropdowns) + 2 filter dropdowns
4. Toggling "DADU Permits" on/off shows/hides permit markers on the map
5. Toggling "Building Footprints" on/off shows/hides footprints
6. Zoning and District dropdowns filter visible parcels
7. Map still renders, zooms, and shows parcel popups on click
8. No floating panel on the right side of the map
9. Search bar placeholder says "Enter a Nashville address (e.g., 100 Broadway)" with NO dropdown of hardcoded addresses
10. Typing in the search bar does NOT show a list of real home addresses

```bash
git add -A
git commit -m "Fix eligibility map: correct stats, toggle switches for layers, stats bar above map"
git push origin main
```

---

## IF CONTEXT GETS LONG

The stats bar + branding fix is most important. If you can't finish the toggle switch conversion, at minimum:
1. Fix the stats numbers
2. Fix the branding (title, shared header, colors)
3. Move stats to horizontal bar above map
4. Commit and stop

The toggle switch conversion for the layer panel can be a follow-up.
