// Theme Manager - Dynamic theme application
class ThemeManager {
    constructor() {
        this.themeData = null;
        this.init();
    }

    async init() {
        try {
            await this.loadTheme();
            this.applyTheme();
            this.setupThemeWatcher();
        } catch (error) {
            console.error('Failed to load theme:', error);
        }
    }

    async loadTheme() {
        try {
            const response = await fetch('/api/theme/');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            this.themeData = await response.json();
        } catch (error) {
            console.error('Error loading theme:', error);
            // Fallback to default theme
            this.themeData = this.getDefaultTheme();
        }
    }

    getDefaultTheme() {
        return {
            colors: {
                primary: '#667eea',
                secondary: '#764ba2',
                accent: '#f093fb',
                background: '#1a1a2e',
                text: '#ffffff',
                card: '#16213e'
            },
            typography: {
                font_family: 'Poppins',
                heading_font: 'Turret Road',
                font_size_base: 16
            },
            layout: {
                sidebar_width: 100,
                border_radius: 8,
                spacing_unit: 16
            },
            animations: {
                enabled: true,
                speed: 1.0,
                stars: true
            },
            custom_css: '',
            site: {
                title: "Mariam's Portfolio",
                description: "Frontend Developer Portfolio",
                email: "mariam@example.com",
                phone: "+1 234 567 8900",
                location: "New York, NY",
                social: {
                    facebook: "https://www.facebook.com",
                    instagram: "https://www.instagram.com",
                    twitter: "https://www.x.com",
                    linkedin: "",
                    github: ""
                }
            }
        };
    }

    applyTheme() {
        if (!this.themeData) return;

        const root = document.documentElement;
        const theme = this.themeData;

        // Apply CSS custom properties
        root.style.setProperty('--primary-color', theme.colors.primary);
        root.style.setProperty('--secondary-color', theme.colors.secondary);
        root.style.setProperty('--accent-color', theme.colors.accent);
        root.style.setProperty('--background-color', theme.colors.background);
        root.style.setProperty('--body-color', theme.colors.background);
        root.style.setProperty('--text-color', theme.colors.text);
        root.style.setProperty('--card-color', theme.colors.card);
        
        // Debug: Log the applied colors
        console.log('Theme applied:', {
            primary: theme.colors.primary,
            secondary: theme.colors.secondary,
            accent: theme.colors.accent
        });

        // Apply typography
        root.style.setProperty('--font-family', theme.typography.font_family);
        root.style.setProperty('--heading-font', theme.typography.heading_font);
        root.style.setProperty('--font-size-base', `${theme.typography.font_size_base}px`);

        // Apply layout
        root.style.setProperty('--sidebar-width', `${theme.layout.sidebar_width}px`);
        root.style.setProperty('--border-radius', `${theme.layout.border_radius}px`);
        root.style.setProperty('--spacing-unit', `${theme.layout.spacing_unit}px`);

        // Apply animations
        if (!theme.animations.enabled) {
            document.body.classList.add('no-animations');
        } else {
            document.body.classList.remove('no-animations');
        }

        // Apply animation speed
        root.style.setProperty('--animation-speed', theme.animations.speed);

        // Apply stars
        const starsContainer = document.querySelector('.stars');
        if (starsContainer) {
            starsContainer.style.display = theme.animations.stars ? 'block' : 'none';
        }

        // Apply custom CSS
        this.applyCustomCSS(theme.custom_css);

        // Update site content
        this.updateSiteContent(theme.site);

        // Update social links
        this.updateSocialLinks(theme.site.social);
    }

    applyCustomCSS(customCSS) {
        // Remove existing custom CSS
        const existingStyle = document.getElementById('custom-theme-css');
        if (existingStyle) {
            existingStyle.remove();
        }

        // Add new custom CSS
        if (customCSS && customCSS.trim()) {
            const style = document.createElement('style');
            style.id = 'custom-theme-css';
            style.textContent = customCSS;
            document.head.appendChild(style);
        }
    }

    updateSiteContent(siteData) {
        // Update page title
        document.title = siteData.title;

        // Update meta description
        let metaDescription = document.querySelector('meta[name="description"]');
        if (!metaDescription) {
            metaDescription = document.createElement('meta');
            metaDescription.name = 'description';
            document.head.appendChild(metaDescription);
        }
        metaDescription.content = siteData.description;

        // Update contact info
        const emailElements = document.querySelectorAll('[data-field="email"]');
        emailElements.forEach(el => el.textContent = siteData.email);

        const phoneElements = document.querySelectorAll('[data-field="phone"]');
        phoneElements.forEach(el => el.textContent = siteData.phone);

        const locationElements = document.querySelectorAll('[data-field="location"]');
        locationElements.forEach(el => el.textContent = siteData.location);
    }

    updateSocialLinks(socialData) {
        // Update social media links
        const socialMappings = {
            'facebook': 'facebook',
            'instagram': 'instagram', 
            'twitter': 'twitter',
            'linkedin': 'linkedin',
            'github': 'github'
        };

        Object.entries(socialMappings).forEach(([platform, selector]) => {
            const links = document.querySelectorAll(`a[href*="${selector}"], .${selector}-link`);
            links.forEach(link => {
                if (socialData[platform]) {
                    link.href = socialData[platform];
                    link.style.display = 'block';
                } else {
                    // Show icon with default URL if no custom URL is set
                    const defaultUrls = {
                        'facebook': 'https://www.facebook.com',
                        'instagram': 'https://www.instagram.com',
                        'twitter': 'https://www.twitter.com',
                        'linkedin': 'https://www.linkedin.com',
                        'github': 'https://www.github.com'
                    };
                    link.href = defaultUrls[platform] || '#';
                    link.style.display = 'block';
                }
            });
        });
    }

    setupThemeWatcher() {
        // Poll for theme changes every 5 seconds
        setInterval(async () => {
            try {
                const response = await fetch('/api/theme/');
                if (response.ok) {
                    const newThemeData = await response.json();
                    if (JSON.stringify(newThemeData) !== JSON.stringify(this.themeData)) {
                        this.themeData = newThemeData;
                        this.applyTheme();
                        console.log('Theme updated!');
                    }
                }
            } catch (error) {
                console.error('Error checking for theme updates:', error);
            }
        }, 5000);
    }

    // Method to manually refresh theme
    async refreshTheme() {
        await this.loadTheme();
        this.applyTheme();
    }
}

// Initialize theme manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.themeManager = new ThemeManager();
});

// Add CSS for no-animations class
const noAnimationsCSS = `
.no-animations * {
    animation-duration: 0s !important;
    animation-delay: 0s !important;
    transition-duration: 0s !important;
    transition-delay: 0s !important;
}
`;

const style = document.createElement('style');
style.textContent = noAnimationsCSS;
document.head.appendChild(style);
