/**
 * Castlehold - Shared Header Component
 * Single source of truth for site navigation.
 * Usage: Add <div id="site-header"></div> to any page, then include this script.
 */

(function() {
    'use strict';

    // ── Detect base path for subdirectory pages ──
    var scriptTag = document.querySelector('script[src*="homebody_header.js"]');
    var basePath = '';
    if (scriptTag) {
        var src = scriptTag.getAttribute('src');
        basePath = src.replace('homebody_header.js', '');
    }

    // ── Helper: build a dropdown menu item ──
    function item(href, icon, title) {
        return `<a href="${basePath}${href}" class="dropdown-item" role="menuitem">
            <div class="dropdown-item-icon"><img src="${basePath}assets/icons/${icon}" alt=""></div>
            <div class="dropdown-item-content"><div class="dropdown-item-title">${title}</div></div>
        </a>`;
    }

    // ── Helper: build a mega-menu column ──
    function col(icon, label, items) {
        return `<div class="mega-menu-column">
            <div class="mega-menu-column-title"><img src="${basePath}assets/icons/${icon}" alt=""> ${label}</div>
            ${items}
        </div>`;
    }

    // ══════════════════════════════════════
    //  HEADER HTML — Edit nav structure here
    // ══════════════════════════════════════

    const HEADER_HTML = `
<!-- Main Navigation -->
<nav class="main-nav" role="navigation" aria-label="Main navigation">
    <div class="nav-container">
        <!-- Logo -->
        <a href="${basePath}index.html" class="nav-logo">
            <img src="${basePath}assets/icons/ADU.png" alt="Homebody Projects" class="nav-logo-img" style="height: 42px; width: auto;">
            <span class="nav-logo-brand" style="color: #3A5566; font-weight: 700; font-family: Inter, sans-serif; font-size: 20px; margin-left: 10px;">Homebody Projects</span>
        </a>

        <!-- Navigation Links -->
        <div class="nav-links">

            <!-- ═══ EXPLORE ═══ -->
            <div class="nav-item">
                <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="explore">
                    EXPLORE <span class="chevron">&#9660;</span>
                </button>
                <div class="dropdown-menu mega-menu mega-menu-3" id="explore-dropdown" role="menu">
                    ${col('ADU.png', 'Learn',
                        item('what_is_dadu.html', 'ADU.png', 'What is a DADU?') +
                        item('dadu_history.html', 'Recorded Docs.png', 'History &amp; Timeline') +
                        item('dadu_building_requirements.html', 'Building and Construction.png', 'Requirements') +
                        item('dadu_zoning_standards.html', 'Zoning.png', 'Zoning Standards') +
                        item('dadu_code_legislation_v3.html', 'Legal.png', 'Code &amp; Legislation') +
                        item('permit_process_timeline.html', 'Renewals.png', 'Permit Process')
                    )}
                    ${col('Zoning.png', 'Discover',
                        item('dadu_eligibility_map.html', 'Zoning.png', 'Eligibility Map') +
                        item('property_search.html', 'Parcel Search.png', 'Property Search') +
                        item('dadu_near_me_v2.html', 'Neighbors.png', 'DADUs Near Me') +
                        item('dadu_opportunity_explorer_v2.html', 'Area Maps and Visual layers.png', 'Opportunity Explorer')
                    )}
                    ${col('Property Owners.png', 'By Role',
                        item('homeowner_portal.html', 'Property Owners.png', 'Homeowner') +
                        item('contractor_marketplace.html', 'Building and Construction.png', 'Contractor') +
                        item('designer_portal.html', 'Surveyers adn Engineers.png', 'Designer / Architect') +
                        item('municipal_dashboard.html', 'Municipal.png', 'Municipal / Agency') +
                        item('legal_resources.html', 'Legal.png', 'Legal / Appraiser')
                    )}
                </div>
            </div>

            <!-- ═══ BUILD ═══ -->
            <div class="nav-item">
                <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="build">
                    BUILD <span class="chevron">&#9660;</span>
                </button>
                <div class="dropdown-menu mega-menu mega-menu-3" id="build-dropdown" role="menu">
                    ${col('Exports & Reports.png', 'Plan',
                        item('project_planner.html', 'Exports & Reports.png', 'Project Planner') +
                        item('project_checklist.html', 'Renewals.png', 'Interactive Checklist') +
                        item('site_plan_downloads.html', 'Surveyers adn Engineers.png', 'Site Plans') +
                        item('draw_dadu_on_parcel.html', 'APN Maps.png', 'Draw DADU on Parcel')
                    )}
                    ${col('Valuations.png', 'Calculate',
                        item('project_cost_estimator.html', 'Valuations.png', 'Cost Estimator') +
                        item('roi_calculator.html', 'Appraisers.png', 'ROI Calculator') +
                        item('size_calculator.html', 'ADU.png', 'Size Calculator') +
                        item('property_tax_calculator.html', 'Investments.png', 'Tax Calculator')
                    )}
                    ${col('Claims.png', 'File',
                        item('determine_forms_required.html', 'Claims.png', 'Determine Forms') +
                        item('legal_form_filler.html', 'Recordable Legal Report.png', 'Form Filler') +
                        item('owner_occupancy.html', 'Property Owners.png', 'Owner Occupancy') +
                        item('short_term_rental_permit.html', 'Renewals.png', 'Short Term Permit')
                    )}
                </div>
            </div>

            <!-- ═══ DATA ═══ -->
            <div class="nav-item">
                <button class="nav-link" aria-expanded="false" aria-haspopup="true" data-dropdown="data">
                    DATA <span class="chevron">&#9660;</span>
                </button>
                <div class="dropdown-menu mega-menu mega-menu-4" id="data-dropdown" role="menu">
                    ${col('Enhanced Transaction History Report .png', 'Activity',
                        item('permit_activity_dashboard.html', 'Enhanced Transaction History Report .png', 'Permit Activity') +
                        item('contractor_dashboard.html', 'Building and Construction.png', 'Contractor Dashboard') +
                        item('market_trends.html', 'Investments.png', 'Market Trends')
                    )}
                    ${col('Exports & Reports.png', 'Reports',
                        item('eligibility_report.html', 'Claims.png', 'Eligibility Report') +
                        item('project_report.html', 'Exports & Reports.png', 'Project Report') +
                        item('dadu_reports_store.html', 'Building and Construction.png', 'Contractor Report') +
                        item('dadu_reports_store.html', 'Market Statistics Report .png', 'Market Analysis') +
                        item('dadu_reports_store.html', 'Area Maps and Visual layers.png', 'Area Analysis') +
                        item('property-report-card.html', 'Property Detail Report .png', 'Property Report')
                    )}
                    ${col('Recorded Docs.png', 'Records',
                        item('dadu_documents_portal.html', 'Recorded Docs.png', 'Recorded Documents') +
                        item('restrictive_covenants_v2.html', 'Legal.png', 'Restrictive Covenants') +
                        item('overlay-districts.html', 'Zoning.png', 'Zoning Documents') +
                        item('property-report-card.html', 'Property Detail Report .png', 'Property Cards')
                    )}
                    ${col('Enhanced Transaction History Report .png', 'Documents',
                        item('nashville_permit_explorer_v3.html', 'Enhanced Transaction History Report .png', 'Permit Explorer') +
                        item('dadu_code_legislation_v3.html', 'Legal.png', 'Code &amp; Legislation') +
                        item('dadu_design_standards.html', 'Surveyers adn Engineers.png', 'Design Standards')
                    )}
                </div>
            </div>

            <!-- ═══ PRICING ═══ -->
            <a href="${basePath}homebody_dadu_pricing.html" class="nav-link">PRICING</a>
        </div>

        <!-- Right-side: Search + CTA -->
        <div style="display:flex;align-items:center;gap:12px;">
            <a href="${basePath}property_search.html" class="nav-link" title="Search" style="padding:12px;">
                &#128269;
            </a>
            <a href="${basePath}am_i_eligible.html" class="nav-search-btn">
                <span>Get Started</span>
                <span>&rarr;</span>
            </a>
        </div>
    </div>
</nav>`;


    // ══════════════════════════════════════
    //  INJECTION + BEHAVIOR
    // ══════════════════════════════════════

    document.addEventListener('DOMContentLoaded', function() {
        // Inject header HTML
        var target = document.getElementById('site-header');
        if (target) {
            target.innerHTML = HEADER_HTML;
        }

        // Initialize dropdown behavior
        initDropdowns();

        // Highlight current page in nav
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
            items.forEach(function(item, index) {
                item.addEventListener('keydown', function(e) {
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
            navItems.forEach(function(item) {
                var hoverTimeout;
                item.addEventListener('mouseenter', function() {
                    clearTimeout(hoverTimeout);
                    var btn = item.querySelector('.nav-link[data-dropdown]');
                    var dd = item.querySelector('.dropdown-menu');
                    if (btn && dd) { closeAllDropdowns(); openDropdown(btn, dd); }
                });
                item.addEventListener('mouseleave', function() {
                    hoverTimeout = setTimeout(function() {
                        var btn = item.querySelector('.nav-link[data-dropdown]');
                        var dd = item.querySelector('.dropdown-menu');
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
            if (link.getAttribute('href') === currentPage) {
                link.style.background = 'var(--card-bg)';
                link.querySelector('.dropdown-item-title').style.color = 'var(--terracotta)';
            }
        });
        // Also highlight direct nav links (Pricing)
        document.querySelectorAll('.nav-links > a.nav-link').forEach(function(link) {
            if (link.getAttribute('href') === currentPage) {
                link.style.color = 'var(--terracotta)';
                link.style.fontWeight = '700';
            }
        });
    }

})();
