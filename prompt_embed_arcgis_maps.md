# TASK: Add "View in ArcGIS" Buttons and Embeds to Map Pages

Add ArcGIS webmap links to 5 pages. Each gets either a full iframe embed or a "View in ArcGIS" button depending on the page.

## Shared Button Style

```html
<a href="{URL}" target="_blank" rel="noopener"
   style="display:inline-flex; align-items:center; gap:6px; padding:8px 16px; 
          background:var(--linen,#F0EBE1); color:var(--slate,#3A5566); 
          border:1px solid rgba(62,74,79,.15); border-radius:6px; 
          font-size:13px; font-family:Inter,sans-serif; font-weight:600; text-decoration:none;">
  View in ArcGIS ↗
</a>
```

Place buttons near the top of each page, next to any existing filter controls or toolbar.

---

## Page 1: restrictive_covenants_v2.html — FULL EMBED

Add after the hero, before any table/list content:

```html
<section style="padding:32px 24px; background:var(--background,#F2F0ED);">
  <h2 style="color:var(--slate,#3A5566); font-family:Inter,sans-serif; font-weight:700; margin-bottom:8px;">
    Restrictive Covenants Map
  </h2>
  <p style="color:var(--graphite,#3E4A4F); font-size:14px; margin-bottom:16px;">
    Explore parcels with recorded restrictive covenants across Nashville-Davidson County. Click any parcel for covenant details and document links.
  </p>
  <iframe src="https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=168e16cf3b08411296759cf39f22dc6d"
    width="100%" height="600" frameborder="0"
    style="border-radius:8px; border:1px solid rgba(62,74,79,.12);"
    title="Nashville Restrictive Covenants Map" loading="lazy">
  </iframe>
</section>
```

## Page 2: existing_dadus_map.html — TWO BUTTONS

Add near the filter/toolbar area, side by side:

Button 1:
- Text: "View Permits + Covenants in ArcGIS ↗"
- URL: `https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=e07213bcf33748679b195c72ee421e42`

Button 2:
- Text: "View Existing DADUs in ArcGIS ↗"
- URL: `https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=9f40d0ca10b1453198617aa9cd2f6b9f`

## Page 3: dadu_eligibility_map.html — BUTTON

- Text: "View Eligibility Map in ArcGIS ↗"
- URL: `https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=d6c2c06db5744bb0836cfb0227548275`

## Page 4: permit_explorer.html — BUTTON

- Text: "View All Permits in ArcGIS ↗"
- URL: `https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=50bbdc9cb0c24ab4aaaadc3951cc1555`

## Page 5: parcel_footprint_map.html — BUTTON

- Text: "View Footprints in ArcGIS ↗"
- URL: `https://vanderbilt.maps.arcgis.com/apps/mapviewer/index.html?webmap=d3f149a92f1c4131b3fc711bc4809b5b`

---

## Constraints

- Do NOT change any map functionality, filters, data queries, or layout
- Only ADD the buttons/embeds
- Do NOT delete any files
- Inter font, Castlehold palette, no emoji

```bash
git add -A && git commit -m "Add ArcGIS webmap links and covenant map embed to 5 pages" && git push origin main
```
