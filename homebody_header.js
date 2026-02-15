/**
 * Homebody Projects - Shared Header Component
 * Single source of truth for site navigation.
 * Usage: Add <div id="site-header"></div> to any page, then include this script.
 *
 * NAV STRUCTURE (Feb 14, 2026):
 * WHO WE SERVE | EXPLORE | BUILD | DATA | RESOURCES | PRICING | ABOUT | [Am I Eligible?]
 */

(function() {
    'use strict';

    // Detect base path for subdirectory pages
    var scriptTag = document.querySelector('script[src*="homebody_header.js"]');
    var basePath = '';
    if (scriptTag) {
        var src = scriptTag.getAttribute('src');
        basePath = src.replace('homebody_header.js', '');
    }

    // Helper: build a dropdown menu item
    function item(href, icon, title) {
        return '<a href="' + basePath + href + '" class="dropdown-item" role="menuitem">' +
            '<div class="dropdown-item-icon"><img src="' + basePath + 'assets/icons/' + icon + '" alt=""></div>' +
            '<div class="dropdown-item-content"><div class="dropdown-item-title">' + title + '</div></div>' +
        '</a>';
    }

    // Helper: build a mega-menu column
    function col(icon, label, items) {
        return '<div class="mega-menu-column">' +
            '<div class="mega-menu-column-title"><img src="' + basePath + 'assets/icons/' + icon + '" alt=""> ' + label + '</div>' +
            items +
        '</div>';
    }

    // ══════════════════════════════════════
    //  HEADER HTML
    // ══════════════════════════════════════

    var HEADER_HTML = '' +
    '<nav class="main-nav" role="navigation" aria-label="Main navigation">' +
    '  <div class="nav-container">' +
    '    <a href="' + basePath + 'index.html" class="nav-logo">' +
    '      <img src="' + basePath + 'assets/icons/ADU_Light2.svg" alt="Homebody Projects" class="nav-logo-img" style="height:42px;width:auto;">' +
    '      <span class="nav-logo-brand">Homebody Projects</span>' +
    '    </a>' +
    '    <div class="nav-links">' +

    // ═══ WHO WE SERVE ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="who-we-serve">' +
    '          WHO WE SERVE <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="who-we-serve-dropdown" role="menu">' +
             col('Property_Owners.svg', 'User Portals',
                 item('homeowner_portal.html', 'Property_Owners.svg', 'Homeowners') +
                 item('contractor_portal.html', 'Building_and_Construction.svg', 'Contractors') +
                 item('designer_portal.html', 'Surveyors_and_Engineers.svg', 'Designers &amp; Architects')
             ) +
             col('Municipal.svg', 'Professional',
                 item('user-homeowners.html', 'Municipal.svg', 'Municipal &amp; Agencies') +
                 item('dadu_contractors_infographic.html', 'Legal.svg', 'Legal Professionals') +
                 item('contractor_portal.html#advertise', 'Building_and_Construction.svg', 'Advertise With Us')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ EXPLORE ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="explore">' +
    '          EXPLORE <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="explore-dropdown" role="menu">' +
             col('Area_Maps_and_Visual_layers.svg', 'Interactive Maps',
                 item('dadu_eligibility_map.html', 'Zoning.svg', 'Eligibility Map') +
                 item('property_search.html', 'Parcel Search.svg', 'Property Search') +
                 item('dadu_near_me_v2.html', 'Neighbors.svg', 'DADUs Near Me') +
                 item('dadu_opportunity_explorer_v2.html', 'Area_Maps_and_Visual_layers.svg', 'Opportunity Explorer') +
                 item('permit_explorer.html', 'Permit_Explorer.svg', 'Permit Explorer Map') +
                 item('parcel_footprint_map.html', 'APN Maps.svg', 'Parcel Footprint Map') +
                 item('adu_permit_map.html', 'Permit_Activity.svg', 'ADU Permit Map') +
                 item('homebody_index_map.html', 'GIS.svg', 'Overview Map')
             ) +
             col('Permit_Activity.svg', 'Dashboards',
                 item('permit_activity_dashboard.html', 'Permit_Activity.svg', 'Permit Activity') +
                 item('contractor_marketplace.html', 'Building_and_Construction.svg', 'Contractor Marketplace') +
                 item('market_trends.html', 'Investments.png', 'Market Trends') +
                 item('nashville_permit_analytics.html', 'Enhanced Transaction History Report .svg', 'Permit Analytics')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ BUILD ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="build">' +
    '          BUILD <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-4" id="build-dropdown" role="menu">' +
             col('Project_Planner.svg', 'Project Planner',
                 item('project_planner_hub.html', 'Project_Planner.svg', 'Project Planner')
             ) +
             col('Appraisers.svg', 'Calculators',
                 item('dadu_calculators.html', 'Appraisers.svg', 'All Calculators')
             ) +
             col('Claims.png', 'Form Wizard',
                 item('form_wizard.html', 'Claims.png', 'Form Wizard')
             ) +
             col('Building_and_Construction.svg', 'Hire',
                 item('contractor_dashboard.html', 'Building_and_Construction.svg', 'Find a Contractor')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ DATA ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="data">' +
    '          DATA <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="data-dropdown" role="menu">' +
             col('Exports__Reports.svg', 'Report Generator',
                 item('eligibility_report.html', 'Claims.png', 'Eligibility Report') +
                 item('project_report.html', 'Exports__Reports.svg', 'Project Report') +
                 item('neighbors_report.html', 'Neighbors.svg', 'Neighbors Report') +
                 item('dadu_reports_store.html', 'Market Statistics Report .svg', 'Market Report') +
                 item('property-report-card.html', 'Property Detail Report .svg', 'Property Report Card')
             ) +
             col('Recorded_Docs.svg', 'Document Database',
                 item('site_plan_downloads.html', 'Permit_Site_Plans.svg', 'Site Plans &amp; Permits') +
                 item('dadu_documents_portal.html', 'Recorded_Docs.svg', 'Recorded Documents') +
                 item('restrictive_covenants_v2.html', 'Restrictive_Covenants.svg', 'Restrictive Covenants') +
                 item('pdf_database_lookup.html', 'Recorded_Docs.svg', 'PDF Database')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ RESOURCES ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="resources">' +
    '          RESOURCES <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="resources-dropdown" role="menu">' +
             col('ADU.png', 'Learn',
                 item('what_is_dadu.html', 'ADU.png', 'What is a DADU?') +
                 item('dadu_requirements_overview.html', 'Building_and_Construction.svg', 'General Requirements') +
                 item('dadu_history.html', 'Recorded_Docs.svg', 'DADU History') +
                 item('dadu_code_legislation_v5.html', 'Legislation.svg', 'Code &amp; Legislation')
             ) +
             col('Legal.svg', 'Permits &amp; Forms',
                 item('owner_occupancy.html', 'Owner_Occupancy.svg', 'Owner Occupancy') +
                 item('str_permit.html', 'STR_Permit.svg', 'STR Permit') +
                 item('trade_permits.html', 'Renewals.png', 'Required Trade Permits') +
                 item('overlay-districts.html', 'Zoning_Documents.svg', 'Overlay Districts') +
                 item('dadu_design_standards.html', 'Overlay_Design_Standards.svg', 'Design Standards')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ PRICING (direct link) ═══
    '      <a href="' + basePath + 'homebody_dadu_pricing.html" class="nav-link">PRICING</a>' +

    // ═══ ABOUT (direct link) ═══
    '      <a href="' + basePath + 'homebody_dadu_pricing.html#about" class="nav-link">ABOUT</a>' +

    '    </div>' +

    // Right side: CTA button
    '    <div style="display:flex;align-items:center;gap:12px;">' +
    '      <a href="' + basePath + 'am_i_eligible.html" class="nav-search-btn">' +
    '        <span>Am I Eligible?</span>' +
    '        <span>&rarr;</span>' +
    '      </a>' +
    '    </div>' +
    '  </div>' +
    '</nav>';


    // ══════════════════════════════════════
    //  INJECTION + BEHAVIOR
    // ══════════════════════════════════════

    document.addEventListener('DOMContentLoaded', function() {
        var target = document.getElementById('site-header');
        if (target) {
            target.innerHTML = HEADER_HTML;
        }
        initDropdowns();
        highlightCurrentPage();
    });


    function initDropdowns() {
        var navItems = document.querySelectorAll('.nav-item');
        var dropdownButtons = document.querySelectorAll('.nav-link[data-dropdown]');

        dropdownButtons.forEach(function(button) {
            var dropdownId = button.getAttribute('data-dropdown');
            var dropdown = document.getElementById(dropdownId + '-dropdown');
            if (!dropdown) return;

            // Click toggle
            button.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                toggleDropdown(button, dropdown);
            });

            // Keyboard
            button.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleDropdown(button, dropdown);
                } else if (e.key === 'Escape') {
                    closeDropdown(button, dropdown);
                    button.focus();
                } else if (e.key === 'ArrowDown' && button.getAttribute('aria-expanded') === 'true') {
                    e.preventDefault();
                    var firstItem = dropdown.querySelector('.dropdown-item');
                    if (firstItem) firstItem.focus();
                }
            });

            // Arrow key nav within dropdown
            var items = dropdown.querySelectorAll('.dropdown-item');
            items.forEach(function(menuItem, index) {
                menuItem.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape') {
                        closeDropdown(button, dropdown);
                        button.focus();
                    } else if (e.key === 'ArrowDown') {
                        e.preventDefault();
                        (items[index + 1] || items[0]).focus();
                    } else if (e.key === 'ArrowUp') {
                        e.preventDefault();
                        (items[index - 1] || items[items.length - 1]).focus();
                    }
                });
            });
        });

        // Close on outside click
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.nav-item')) {
                closeAllDropdowns();
            }
        });

        // Close on Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') closeAllDropdowns();
        });

        // Hover for desktop
        if (window.matchMedia('(hover: hover)').matches) {
            navItems.forEach(function(navItem) {
                var hoverTimeout;
                navItem.addEventListener('mouseenter', function() {
                    clearTimeout(hoverTimeout);
                    var btn = navItem.querySelector('.nav-link[data-dropdown]');
                    var dd = navItem.querySelector('.dropdown-menu');
                    if (btn && dd) { closeAllDropdowns(); openDropdown(btn, dd); }
                });
                navItem.addEventListener('mouseleave', function() {
                    hoverTimeout = setTimeout(function() {
                        var btn = navItem.querySelector('.nav-link[data-dropdown]');
                        var dd = navItem.querySelector('.dropdown-menu');
                        if (btn && dd) closeDropdown(btn, dd);
                    }, 150);
                });
            });
        }
    }

    function toggleDropdown(button, dropdown) {
        if (button.getAttribute('aria-expanded') === 'true') {
            closeDropdown(button, dropdown);
        } else {
            closeAllDropdowns();
            openDropdown(button, dropdown);
        }
    }

    function openDropdown(button, dropdown) {
        button.setAttribute('aria-expanded', 'true');
        dropdown.classList.add('open');
    }

    function closeDropdown(button, dropdown) {
        button.setAttribute('aria-expanded', 'false');
        dropdown.classList.remove('open');
    }

    function closeAllDropdowns() {
        document.querySelectorAll('.nav-link[data-dropdown]').forEach(function(btn) {
            var dd = document.getElementById(btn.getAttribute('data-dropdown') + '-dropdown');
            if (dd) closeDropdown(btn, dd);
        });
    }

    function highlightCurrentPage() {
        var currentPage = window.location.pathname.split('/').pop() || 'index.html';
        document.querySelectorAll('.dropdown-item').forEach(function(link) {
            var href = link.getAttribute('href');
            if (href && href.split('/').pop() === currentPage) {
                link.style.background = '#F0EBE1';
                var titleEl = link.querySelector('.dropdown-item-title');
                if (titleEl) titleEl.style.color = '#CBB279';
            }
        });
        // Highlight direct nav links (Pricing, About)
        document.querySelectorAll('.nav-links > a.nav-link').forEach(function(link) {
            var href = link.getAttribute('href');
            if (href && href.split('/').pop() === currentPage) {
                link.style.color = '#CBB279';
                link.style.fontWeight = '700';
            }
        });
    }

})();
