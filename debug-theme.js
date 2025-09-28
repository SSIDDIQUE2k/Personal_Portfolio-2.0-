// Debug script to check theme application
console.log('=== THEME DEBUG INFO ===');

// Check if CSS variables are set
const root = document.documentElement;
const computedStyle = getComputedStyle(root);

console.log('CSS Variables:');
console.log('--body-color:', computedStyle.getPropertyValue('--body-color'));
console.log('--background-color:', computedStyle.getPropertyValue('--background-color'));
console.log('--primary-color:', computedStyle.getPropertyValue('--primary-color'));
console.log('--secondary-color:', computedStyle.getPropertyValue('--secondary-color'));

// Check if theme manager exists
console.log('Theme Manager:', window.themeManager ? 'Found' : 'Not found');

// Check theme data
if (window.themeManager && window.themeManager.themeData) {
    console.log('Theme Data:', window.themeManager.themeData.colors);
} else {
    console.log('Theme Data: Not loaded');
}

// Check home section background
const homeSection = document.querySelector('.home');
if (homeSection) {
    const homeStyle = getComputedStyle(homeSection);
    console.log('Home section background-color:', homeStyle.backgroundColor);
    console.log('Home section background-image:', homeStyle.backgroundImage);
} else {
    console.log('Home section: Not found');
}

// Check body background
const bodyStyle = getComputedStyle(document.body);
console.log('Body background-color:', bodyStyle.backgroundColor);

console.log('=== END DEBUG INFO ===');
