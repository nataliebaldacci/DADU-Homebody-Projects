/**
 * Homebody Projects - Shared Header Component
 * Single source of truth for site navigation.
 * Usage: Add <div id="site-header"></div> to any page, then include this script.
 *
 * NAV STRUCTURE (Feb 18, 2026):
 * WHO WE SERVE | EXPLORE | BUILD | RESOURCES | PRICING | ABOUT | [Am I Eligible?]
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
    '      <img src="' + basePath + 'assets/icons/ADU_MultiColors.svg" alt="Homebody Projects" class="nav-logo-img" style="height:42px;width:auto;">' +
    '      <span class="nav-logo-brand">Homebody Projects</span>' +
    '    </a>' +
    '    <div class="nav-links">' +

    // ═══ WHO WE SERVE (single-column flat list) ═══
    '      <div class="nav-item">' +
    '        <a href="' + basePath + 'user-types.html" class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="who-we-serve">' +
    '          WHO WE SERVE <span class="chevron">&#9660;</span>' +
    '        </a>' +
    '        <div class="dropdown-menu dropdown-single" id="who-we-serve-dropdown" role="menu">' +
                 item('homeowner_portal.html', 'Property_Owners.svg', 'Homeowners') +
                 item('contractor_portal.html', 'Building_and_Construction.svg', 'Contractors') +
                 item('designer_portal.html', 'Surveyors_and_Engineers.svg', 'Designers &amp; Architects') +
                 item('user-homeowners.html', 'Municipal.svg', 'Municipal &amp; Agencies') +
                 item('legal_professionals_portal.html', 'Legal.svg', 'Legal Professionals') +
    '        </div>' +
    '      </div>' +

    // ═══ EXPLORE ═══
    '      <div class="nav-item">' +
    '        <a href="' + basePath + 'features.html" class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="explore">' +
    '          EXPLORE <span class="chevron">&#9660;</span>' +
    '        </a>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="explore-dropdown" role="menu">' +
             col('Area_Maps_and_Visual_layers.svg', 'Interactive Maps',
                 item('dadu_eligibility_map.html', 'Zoning.svg', 'Eligibility Map') +
                 item('property_search.html', 'Parcel Search.svg', 'Property Search') +
                 item('existing_dadus_map.html', 'ADU.png', 'Existing DADUs') +
                 item('permit_explorer.html', 'Permit_Explorer.svg', 'Permit Explorer Map') +
                item('dadu_near_me_v3.html', 'Neighbors.svg', 'DADUs Near Me')
             ) +
             col('Dashboard.svg', 'Dashboards',
                 item('permit_activity_dashboard.html', 'Permit_Activity.svg', 'Permit Activity') +
                 item('contractor_marketplace.html', 'Contractor_Marketplace.svg', 'Contractor Marketplace') +
                 item('market_trends.html', 'Cost_Market.png', 'Market Trends') +
                 item('nashville_permit_analytics.html', 'Permit_Analytics.svg', 'Permit Analytics')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ BUILD (mega-menu-2: Plan My Project + Research) ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="build">' +
    '          BUILD <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="build-dropdown" role="menu">' +
             col('Project_Planner.svg', 'Plan My Project',
                 item('dadu_build_tool_v2.html', 'Build_DADU.svg', 'Build My DADU') +
                 item('project_planner_hub.html', 'Checklist_.svg', 'Planning Hub') +
                 item('draw_dadu_on_parcel.html', 'Draw_DADU.svg', 'Draw DADU on Parcel') +
                 item('permit_process_timeline.html', 'Permit_Timeline.svg', 'Permit Process Timeline') +
                 item('dadu_calculators.html', 'Appraisers.svg', 'All Calculators') +
                 item('form_wizard.html', 'Form_Wizard.svg', 'Form Wizard')
             ) +
             col('Exports__Reports.svg', 'Research',
                 item('dadu_reports_store.html', 'Exports__Reports.svg', 'Report Generator') +
                 item('find_site_plans.html', 'Permit_Site_Plans.svg', 'Find Site Plans &amp; Permit Docs') +
                 item('dadu_resources.html', 'External_Links.svg', 'External Links') +
                 item('pdf_database_lookup.html', 'Document_Database.svg', 'PDF Database') +
                 item('contractor_dashboard.html', 'Find_Contractor.svg', 'Find a Contractor')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ RESOURCES ═══
    '      <div class="nav-item">' +
    '        <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="resources">' +
    '          RESOURCES <span class="chevron">&#9660;</span>' +
    '        </button>' +
    '        <div class="dropdown-menu mega-menu mega-menu-2" id="resources-dropdown" role="menu">' +
             col('Recorded_Docs.svg', 'Learn',
                 item('what_is_dadu.html', 'What_is_DADU.svg', 'What is a DADU?') +
                 item('dadu_requirements_overview.html', 'General_Requirements.svg', 'General Requirements') +
                 item('dadu_eligibility_flowchart.html', 'Eligibility_Check.svg', 'Eligibility Flowchart') +
                 item('dadu_history.html', 'DADU_History.svg', 'DADU History') +
                 item('dadu_code_legislation_v5.html', 'Legislation.svg', 'Code &amp; Legislation') +
                item('arcgis_maps.html', 'GIS.svg', 'ArcGIS Maps')
             ) +
             col('Permit_Approval.svg', 'Permits &amp; Forms',
                 item('owner_occupancy.html', 'Owner_Occupancy.svg', 'Owner Occupancy') +
                 item('str_permit.html', 'STR_Permit.svg', 'Short Term Rental Permit') +
                 item('trade_permits.html', 'Renewals.svg', 'Required Trade Permits') +
                 item('overlay-districts.html', 'Zoning_Documents.svg', 'Overlay Districts') +
                 item('restrictive_covenants_v2.html', 'Restrictive_Covenants.svg', 'Restrictive Covenants') +
                 item('dadu_design_standards.html', 'Overlay_Design_Standards.svg', 'Design Standards')
             ) +
    '        </div>' +
    '      </div>' +

    // ═══ PRICING (direct link) ═══
    '      <a href="' + basePath + 'homebody_dadu_pricing.html" class="nav-link">PRICING</a>' +

    // ═══ ABOUT (direct link) ═══
    '      <a href="' + basePath + 'about_platform.html" class="nav-link">ABOUT</a>' +

    '    </div>' +

    // Right side: hamburger + CTA
    '    <div style="display:flex;align-items:center;gap:12px;">' +
    '      <a href="' + basePath + 'am_i_eligible.html" class="nav-search-btn">' +
    '        <span>Am I Eligible?</span>' +
    '        <span>&rarr;</span>' +
    '      </a>' +
    '      <button class="mobile-menu-btn" aria-label="Open menu" aria-expanded="false">' +
    '        <span class="hamburger-line"></span>' +
    '        <span class="hamburger-line"></span>' +
    '        <span class="hamburger-line"></span>' +
    '      </button>' +
    '    </div>' +
    '  </div>' +
    '</nav>' +
    '<div class="mobile-overlay" aria-hidden="true"></div>';


    // ══════════════════════════════════════
    //  INJECTION + BEHAVIOR
    // ══════════════════════════════════════

    document.addEventListener('DOMContentLoaded', function() {
        var target = document.getElementById('site-header');
        if (target) {
            target.innerHTML = HEADER_HTML;
        }
        initDropdowns();
        initMobileMenu();
        highlightCurrentPage();
    });


    function initDropdowns() {
        var navItems = document.querySelectorAll('.nav-item');
        var dropdownButtons = document.querySelectorAll('.nav-link[data-dropdown]');

        dropdownButtons.forEach(function(button) {
            var dropdownId = button.getAttribute('data-dropdown');
            var dropdown = document.getElementById(dropdownId + '-dropdown');
            if (!dropdown) return;

            // Click: if it's an <a> with href, navigate; if <button>, toggle dropdown
            button.addEventListener('click', function(e) {
                if (button.tagName === 'A' && button.getAttribute('href')) {
                    // Allow default navigation for clickable links
                    return;
                }
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

    // ══════════════════════════════════════
    //  MOBILE MENU
    // ══════════════════════════════════════
    function initMobileMenu() {
        var btn = document.querySelector('.mobile-menu-btn');
        var navLinks = document.querySelector('.nav-links');
        var overlay = document.querySelector('.mobile-overlay');
        if (!btn || !navLinks) return;

        function openMobile() {
            btn.classList.add('active');
            btn.setAttribute('aria-expanded', 'true');
            navLinks.classList.add('mobile-open');
            if (overlay) { overlay.classList.add('visible'); overlay.setAttribute('aria-hidden', 'false'); }
            document.body.style.overflow = 'hidden';
        }

        function closeMobile() {
            btn.classList.remove('active');
            btn.setAttribute('aria-expanded', 'false');
            navLinks.classList.remove('mobile-open');
            if (overlay) { overlay.classList.remove('visible'); overlay.setAttribute('aria-hidden', 'true'); }
            document.body.style.overflow = '';
            closeAllDropdowns();
        }

        btn.addEventListener('click', function(e) {
            e.stopPropagation();
            if (navLinks.classList.contains('mobile-open')) { closeMobile(); } else { openMobile(); }
        });

        if (overlay) {
            overlay.addEventListener('click', closeMobile);
        }

        // On mobile, make nav-link buttons toggle their dropdown accordion-style
        navLinks.addEventListener('click', function(e) {
            if (window.innerWidth > 1024) return;
            var navLink = e.target.closest('.nav-link[data-dropdown]');
            if (!navLink) return;
            e.preventDefault();
            e.stopPropagation();
            var ddId = navLink.getAttribute('data-dropdown');
            var dd = document.getElementById(ddId + '-dropdown');
            if (!dd) return;
            var isOpen = navLink.getAttribute('aria-expanded') === 'true';
            // Close all other dropdowns first
            document.querySelectorAll('.nav-links .nav-link[data-dropdown]').forEach(function(other) {
                if (other !== navLink) {
                    other.setAttribute('aria-expanded', 'false');
                    var otherDd = document.getElementById(other.getAttribute('data-dropdown') + '-dropdown');
                    if (otherDd) otherDd.classList.remove('open');
                }
            });
            if (isOpen) {
                navLink.setAttribute('aria-expanded', 'false');
                dd.classList.remove('open');
            } else {
                navLink.setAttribute('aria-expanded', 'true');
                dd.classList.add('open');
            }
        });

        // Close mobile menu when a dropdown-item link is clicked
        navLinks.addEventListener('click', function(e) {
            if (window.innerWidth > 1024) return;
            if (e.target.closest('.dropdown-item')) {
                closeMobile();
            }
        });

        // Close on resize to desktop
        window.addEventListener('resize', function() {
            if (window.innerWidth > 1024 && navLinks.classList.contains('mobile-open')) {
                closeMobile();
            }
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
