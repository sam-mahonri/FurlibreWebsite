document.addEventListener('DOMContentLoaded', () => {
    const HTML_TAG = document.documentElement;
    const THEME_BTN = document.getElementById('themeBtn');
    const ICON_ELEMENT = document.getElementById('themeIcon');
    const STORED_THEME = localStorage.getItem('theme') || 'auto';

    function setTheme(theme) {
        HTML_TAG.setAttribute('class', theme);
        updateIcon(theme);
    }

    function toggleTheme() {
        const currentTheme = HTML_TAG.getAttribute('class');
        const THEMES = ['auto', 'light-theme', 'dark-theme'];
        const nextTheme = THEMES[(THEMES.indexOf(currentTheme) + 1) % THEMES.length];
        setTheme(nextTheme);
        localStorage.setItem('theme', nextTheme);
    }

    function updateIcon(theme) {
        if (ICON_ELEMENT) {
            let iconClass;

            if (theme === 'auto') {
                iconClass = 'fas fa-circle-half-stroke';
            } else {
                iconClass = theme === 'dark-theme' ? 'fas fa-moon' : 'fas fa-sun';
            }

            ICON_ELEMENT.className = iconClass;
        }
    }

    if (THEME_BTN) {
        THEME_BTN.addEventListener('click', toggleTheme);
    }

    if (ICON_ELEMENT) {
        updateIcon(STORED_THEME);
    }

    if (STORED_THEME === 'auto') {
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');

        function updateThemeFromSystem() {
            setTheme(mediaQuery.matches ? 'dark-theme' : 'light-theme');
        }

        mediaQuery.addEventListener('change', updateThemeFromSystem);
        updateThemeFromSystem();
    } else {
        setTheme(STORED_THEME);
    }
});