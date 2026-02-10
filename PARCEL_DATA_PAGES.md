# Live Parcel Data Pages

These pages are **fully functional** with your Nashville parcel data and are ready to use:

## 🏠 Main Interactive Pages (4 Live Pages)

### 1. **index.html** - Homepage with Eligibility Checker
- **Status:** ✅ LIVE with parcel data
- **Features:**
  - Interactive map showing eligible parcels
  - Quick eligibility lookup by address
  - Visual parcel eligibility indicators
- **Data:** `parcels_eligibility_lite.json` (21MB, all Nashville parcels with eligibility scores)
- **Use Case:** Landing page that answers "Can I build a DADU on my property?"

### 2. **property_search.html** - Advanced Property Search
- **Status:** ✅ LIVE with parcel data + permit data
- **Features:**
  - Full map search interface
  - Parcel boundary overlays
  - Eligibility filtering
  - Permit history overlay
  - Search by address, parcel ID, or map click
- **Data:** 
  - Parcel eligibility: `parcels_eligibility_lite.json`
  - Permit history: `permit_history_20260118_093536.geojson`
- **Use Case:** Power users searching for properties with detailed filters

### 3. **dadu_opportunity_explorer_v2.html** - Opportunity Scoring Dashboard
- **Status:** ✅ LIVE with scored parcel data
- **Features:**
  - Scored parcels (opportunity rankings)
  - Investment potential indicators
  - Comparative parcel analysis
  - Interactive map with scoring visualization
- **Data:** `parcels_scored_v2.json` (20MB, parcels with opportunity scores)
- **Use Case:** Investors/homeowners looking for highest-potential DADU sites

### 4. **nashville_permit_explorer_v3.html** - Permit Activity Explorer
- **Status:** ✅ LIVE with permit data
- **Features:**
  - Historical permit data visualization
  - Permit type filtering
  - Contractor lookup
  - Timeline view of permit activity
- **Data:** `permits_with_apn.json` (13MB, permits linked to parcels)
- **Use Case:** Research permit trends, contractor activity, and DADU adoption rates

---

## 📊 Supporting Data Pages

### **contractor_dashboard.html** - Contractor Analytics
- **Status:** ✅ LIVE with contractor/permit data
- **Features:**
  - Contractor performance metrics
  - Permit history by contractor
  - Project completion analytics
- **Data:** `contractor_data_enhanced.json`, permit datasets

---

## 🔧 Pages That Reference Parcel Data (But May Be Incomplete)

These pages load parcel data but may have incomplete features:

- `dadu_eligibility_map.html` - Similar to index but dedicated eligibility map
- `dadu_near_me_v2.html` - Find nearby DADUs (may need geolocation setup)
- `am_i_eligible.html` - Eligibility wizard (may be form-focused vs map)
- `dadu_property_viewer_v3.html` - Individual property detail viewer

---

## 📦 Your Parcel Data Files (Ready to Use)

| File | Size | Description |
|------|------|-------------|
| `parcels_eligibility_lite.json` | 21MB | All Nashville parcels with eligibility flags |
| `parcels_eligibility_light.json` | 973KB | Lightweight version for fast loading |
| `parcels_scored_v2.json` | 20MB | Parcels with opportunity scores |
| `permits_with_apn.json` | 13MB | Permit history linked to parcel IDs |
| `permit_history_20260118_093536.geojson` | 19MB | Geocoded permit locations |
| `contractor_data_enhanced.json` | 1MB | Contractor performance data |

---

## 🎯 Which Page Should You Use?

**For general visitors:**
→ Start with **index.html** (homepage) - simple eligibility check

**For property research:**
→ Use **property_search.html** - full search + filters

**For investment analysis:**
→ Use **dadu_opportunity_explorer_v2.html** - scored opportunities

**For market research:**
→ Use **nashville_permit_explorer_v3.html** - permit trends

**For contractor vetting:**
→ Use **contractor_dashboard.html** - contractor analytics

---

## ✅ All 4 Main Pages Now Have:
- ✅ New Castlehold navigation header
- ✅ Castlehold color palette
- ✅ Working parcel data integration
- ✅ No broken links

Ready to deploy! 🚀
