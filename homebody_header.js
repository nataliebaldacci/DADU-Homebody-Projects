/**
 * Homebody Projects - Shared Header JavaScript
 * Handles dropdown menus with keyboard accessibility
 */

(function() {
    'use strict';

    // Initialize when DOM is ready
    document.addEventListener('DOMContentLoaded', initHeader);

    function initHeader() {
        const navItems = document.querySelectorAll('.nav-item');
        const dropdownButtons = document.querySelectorAll('.nav-link[data-dropdown]');

        // Setup dropdown toggles
        dropdownButtons.forEach(button => {
            const dropdownId = button.getAttribute('data-dropdown');
            const dropdown = document.getElementById(`${dropdownId}-dropdown`);

            if (!dropdown) return;

            // Click handler
            button.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                toggleDropdown(button, dropdown);
            });

            // Keyboard handler
            button.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleDropdown(button, dropdown);
                } else if (e.key === 'Escape') {
                    closeDropdown(button, dropdown);
                    button.focus();
                } else if (e.key === 'ArrowDown' && button.getAttribute('aria-expanded') === 'true') {
                    e.preventDefault();
                    const firstItem = dropdown.querySelector('.dropdown-item');
                    if (firstItem) firstItem.focus();
                }
            });

            // Dropdown item keyboard navigation
            const items = dropdown.querySelectorAll('.dropdown-item');
            items.forEach((item, index) => {
                item.addEventListener('keydown', (e) => {
                    if (e.key === 'Escape') {
                        closeDropdown(button, dropdown);
                        button.focus();
                    } else if (e.key === 'ArrowDown') {
                        e.preventDefault();
                        const nextItem = items[index + 1] || items[0];
                        nextItem.focus();
                    } else if (e.key === 'ArrowUp') {
                        e.preventDefault();
                        const prevItem = items[index - 1] || items[items.length - 1];
                        prevItem.focus();
                    }
                });
            });
        });

        // Close dropdowns when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.nav-item')) {
                closeAllDropdowns();
            }
        });

        // Close dropdowns on Escape key anywhere
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeAllDropdowns();
            }
        });

        // Handle hover for desktop (optional enhancement)
        if (window.matchMedia('(hover: hover)').matches) {
            navItems.forEach(item => {
                let hoverTimeout;

                item.addEventListener('mouseenter', () => {
                    clearTimeout(hoverTimeout);
                    const button = item.querySelector('.nav-link[data-dropdown]');
                    const dropdown = item.querySelector('.dropdown-menu');
                    if (button && dropdown) {
                        closeAllDropdowns();
                        openDropdown(button, dropdown);
                    }
                });

                item.addEventListener('mouseleave', () => {
                    hoverTimeout = setTimeout(() => {
                        const button = item.querySelector('.nav-link[data-dropdown]');
                        const dropdown = item.querySelector('.dropdown-menu');
                        if (button && dropdown) {
                            closeDropdown(button, dropdown);
                        }
                    }, 150);
                });
            });
        }
    }

    function toggleDropdown(button, dropdown) {
        const isOpen = button.getAttribute('aria-expanded') === 'true';

        if (isOpen) {
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
        document.querySelectorAll('.nav-link[data-dropdown]').forEach(btn => {
            const dropdownId = btn.getAttribute('data-dropdown');
            const dropdown = document.getElementById(`${dropdownId}-dropdown`);
            if (dropdown) {
                closeDropdown(btn, dropdown);
            }
        });
    }
})();
