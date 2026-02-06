/**
 * Nashville DADU - ArcGIS Feature Service Utilities
 * Connect to live GIS data from ArcGIS REST services
 */

const ARCGIS_SERVICES = {
    // Vanderbilt hosted services
    eligibility: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Eligibility_ENHANCED_20260119_042533/FeatureServer/0',
    newPermits: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/NEW_ADU_Permits_20260114/FeatureServer/0',
    allPermits: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/DADU_All_Permits_Final/FeatureServer/0',
    buildingSpecs: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/DADU_Building_Specs_20260119_042856/FeatureServer/0',
    existingDADUs: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Secondary_SFH_Merged_SHP_20251231_0015/FeatureServer/0',
    sfhParcels: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/SFH_parcels/FeatureServer/0',
    parcelsWithCovenants: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/Parcels_with_Restrictive_Covenants_ohoMJQ/FeatureServer/0',
    covenantLinks: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/arcgis/rest/services/_Restrictive_Covenant_Links__A1_R2978_QuLdfD/FeatureServer/0',
    secondaryStructures: 'https://services3.arcgis.com/58WV6GqBWodG9Kll/ArcGIS/rest/services/Secondary_On_SF_Parcels_SHP_20251230_2352/FeatureServer/0',

    // Nashville official services
    zoningOverlays: 'https://maps.nashville.gov/arcgis/rest/services/Zoning_Landuse/Zoning_Overlay_Districts/MapServer/0',
    zoningOverlaysView: 'https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Zoning_Overlay_Districts_Vw/FeatureServer/0',
    addressPoints: 'https://maps.nashville.gov/arcgis/rest/services/Addressing/AddressPoints/MapServer/0',
    parcelHistory: 'https://maps.nashville.gov/arcgis2/rest/services/Parcels/ParcelHistory/MapServer/5',
    cadastral: 'https://maps.nashville.gov/arcgis/rest/services/Cadastral/Cadastral_Layers/MapServer/4'
};

/**
 * Query an ArcGIS Feature Service
 * @param {string} serviceUrl - The feature service URL
 * @param {Object} options - Query options
 * @returns {Promise<Object>} - GeoJSON FeatureCollection
 */
async function queryArcGISService(serviceUrl, options = {}) {
    const defaults = {
        where: '1=1',
        outFields: '*',
        returnGeometry: true,
        outSR: 4326,
        f: 'geojson',
        resultRecordCount: 1000
    };

    const params = { ...defaults, ...options };
    const queryString = new URLSearchParams(params).toString();
    const url = `${serviceUrl}/query?${queryString}`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error('ArcGIS query failed:', error);
        throw error;
    }
}

/**
 * Query features by bounding box (for map viewport)
 * @param {string} serviceUrl - The feature service URL
 * @param {Object} bounds - {minX, minY, maxX, maxY} in WGS84
 * @param {Object} options - Additional query options
 */
async function queryByBounds(serviceUrl, bounds, options = {}) {
    const geometry = JSON.stringify({
        xmin: bounds.minX,
        ymin: bounds.minY,
        xmax: bounds.maxX,
        ymax: bounds.maxY,
        spatialReference: { wkid: 4326 }
    });

    return queryArcGISService(serviceUrl, {
        ...options,
        geometry: geometry,
        geometryType: 'esriGeometryEnvelope',
        spatialRel: 'esriSpatialRelIntersects'
    });
}

/**
 * Query features by point (for click events)
 * @param {string} serviceUrl - The feature service URL
 * @param {number} lat - Latitude
 * @param {number} lng - Longitude
 * @param {number} tolerance - Search tolerance in meters
 */
async function queryByPoint(serviceUrl, lat, lng, tolerance = 50, options = {}) {
    const geometry = JSON.stringify({
        x: lng,
        y: lat,
        spatialReference: { wkid: 4326 }
    });

    return queryArcGISService(serviceUrl, {
        ...options,
        geometry: geometry,
        geometryType: 'esriGeometryPoint',
        spatialRel: 'esriSpatialRelIntersects',
        distance: tolerance,
        units: 'esriSRUnit_Meter'
    });
}

/**
 * Query parcels by address
 * @param {string} address - Address to search
 */
async function queryByAddress(address, options = {}) {
    return queryArcGISService(ARCGIS_SERVICES.eligibility, {
        ...options,
        where: `Address LIKE '%${address.toUpperCase().replace(/'/g, "''")}%'`,
        resultRecordCount: 10
    });
}

/**
 * Query DADU permits by various criteria
 */
async function queryPermits(options = {}) {
    return queryArcGISService(ARCGIS_SERVICES.allPermits, options);
}

/**
 * Check if a parcel has restrictive covenants
 * @param {string} parcelId - The parcel ID (STANPAR format)
 */
async function checkRestrictiveCovenants(parcelId) {
    const result = await queryArcGISService(ARCGIS_SERVICES.parcelsWithCovenants, {
        where: `STANPAR = '${parcelId}'`,
        returnGeometry: false
    });
    return result.features && result.features.length > 0;
}

/**
 * Get covenant PDF links for a parcel
 * @param {string} parcelId - The parcel ID
 */
async function getCovenantLinks(parcelId) {
    return queryArcGISService(ARCGIS_SERVICES.covenantLinks, {
        where: `STANPAR = '${parcelId}'`,
        returnGeometry: false
    });
}

/**
 * Get DADU overlay districts
 */
async function getDADUOverlays() {
    return queryArcGISService(ARCGIS_SERVICES.zoningOverlays, {
        where: "ZONE_DESC = 'Detached Accessory Dwelling Unit Overlay District'",
        outFields: 'ZONE_DESC,CASE_NO,ORDINANCE,ORD_DATE,ACRES'
    });
}

/**
 * Get Urban Design Overlays
 */
async function getUrbanDesignOverlays() {
    return queryArcGISService(ARCGIS_SERVICES.zoningOverlaysView, {
        where: "zone_desc like '%Urban Design Overlay%'",
        outFields: 'OBJECTID,ZONE_DESC,CASE_NO,ORDINANCE,ORD_DATE,NAME,IMPACT_ZONE,SUBDISTRICT'
    });
}

/**
 * Query Nashville address points for DADU-related addresses
 */
async function queryDADUAddresses() {
    return queryArcGISService(ARCGIS_SERVICES.addressPoints, {
        where: "Description like '%DADU%' OR DESCRIPTION LIKE '%ACCESSORY DWELL%' OR DESCRIPTION LIKE '%Carriage%' OR Description like '%guest%'",
        outFields: '*'
    });
}

/**
 * Get service metadata (record count, fields, etc.)
 * @param {string} serviceUrl - The feature service URL
 */
async function getServiceInfo(serviceUrl) {
    try {
        const response = await fetch(`${serviceUrl}?f=json`);
        return await response.json();
    } catch (error) {
        console.error('Failed to get service info:', error);
        throw error;
    }
}

/**
 * Get total record count for a service
 * @param {string} serviceUrl - The feature service URL
 * @param {string} where - Optional where clause
 */
async function getRecordCount(serviceUrl, where = '1=1') {
    const result = await queryArcGISService(serviceUrl, {
        where: where,
        returnCountOnly: true,
        returnGeometry: false,
        f: 'json'
    });
    return result.count;
}

/**
 * Query with pagination for large datasets
 * @param {string} serviceUrl - The feature service URL
 * @param {Object} options - Query options
 * @param {Function} onProgress - Callback for progress updates
 */
async function queryAllFeatures(serviceUrl, options = {}, onProgress = null) {
    const allFeatures = [];
    const pageSize = options.resultRecordCount || 1000;
    let offset = 0;
    let hasMore = true;

    while (hasMore) {
        const result = await queryArcGISService(serviceUrl, {
            ...options,
            resultOffset: offset,
            resultRecordCount: pageSize
        });

        if (result.features && result.features.length > 0) {
            allFeatures.push(...result.features);
            offset += result.features.length;

            if (onProgress) {
                onProgress(allFeatures.length);
            }

            hasMore = result.features.length === pageSize;
        } else {
            hasMore = false;
        }
    }

    return {
        type: 'FeatureCollection',
        features: allFeatures
    };
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        ARCGIS_SERVICES,
        queryArcGISService,
        queryByBounds,
        queryByPoint,
        queryByAddress,
        queryPermits,
        checkRestrictiveCovenants,
        getCovenantLinks,
        getDADUOverlays,
        getUrbanDesignOverlays,
        queryDADUAddresses,
        getServiceInfo,
        getRecordCount,
        queryAllFeatures
    };
}
