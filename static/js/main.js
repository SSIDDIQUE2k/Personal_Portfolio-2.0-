// Simple Typewriter Effect for Name Only
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        } else {
            // Add blinking cursor after typing is complete
            element.innerHTML += '<span class="cursor">|</span>';
        }
    }
    
    type();
}

// Initialize typewriter effect when page loads
document.addEventListener('DOMContentLoaded', function() {
    const typewriterElement = document.querySelector('.typeJsText');
    if (typewriterElement) {
        const originalText = typewriterElement.textContent.trim();
        typeWriter(typewriterElement, originalText, 80);
    }
});

// Toggling Skill Tabs

const tabs = document.querySelectorAll('[data-target]');
const tabContent = document.querySelectorAll('[data-content]');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target);

        tabContent.forEach(tabContents => {
            tabContents.classList.remove('skills-active');
        })

        if (target) {
            target.classList.add('skills-active');
        }

        tabs.forEach(tab => {
            tab.classList.remove('skills-active');
        })

        tab.classList.add('skills-active');
    })
})

//Mix it up Sorting

let mixerPortfolio = mixitup('.work-container', {
    selectors: {
        target: '.work-card'
    },
    animation: {
        duration: 300
    }
});

// Active link changing

const linkWork = document.querySelectorAll('.work-item');

function activeWork() {
    linkWork.forEach(l => l.classList.remove('active-work'))
    this.classList.add('active-work')
}
linkWork.forEach(l => l.addEventListener('click', activeWork));

//Portfolio Popup

document.addEventListener('click', (e) => {
    if(e.target.classList.contains('work-button')){
        togglePortfolioPopup();
        portfolioItemDetails(e.target.parentElement);
    }
})

function togglePortfolioPopup() {
    document.querySelector('.portfolio-popup').classList.toggle('open');
}

document.querySelector('.portfolio-popup-close').addEventListener('click', togglePortfolioPopup);

function portfolioItemDetails(portfolioItem) {
    document.querySelector('.pp-thumbnail img').src = portfolioItem.querySelector('.work-img').src;
    document.querySelector('.portfolio-popup-subtitle span').innerHTML = portfolioItem.querySelector('.work-title').innerHTML;
    document.querySelector('.portfolio-popup-body').innerHTML = portfolioItem.querySelector('.portfolio-item-details').innerHTML;
}

//Services Popup
const modalViews = document.querySelectorAll('.services-modal');
const modelBtns = document.querySelectorAll('.services-button');
const modalCloses = document.querySelectorAll('.services-modal-close');

let modal = function(modalClick) {
    modalViews[modalClick].classList.add('active-modal');
}

modelBtns.forEach((modelBtn, i) => {
    modelBtn.addEventListener('click', () => {
        modal(i);
    })
})

modalCloses.forEach((modalClose) => {
    modalClose.addEventListener('click', () => {
        modalViews.forEach((modalView) => {
            modalView.classList.remove('active-modal');
        })
    })
})

//Swiper Testimonial
document.addEventListener('DOMContentLoaded', function() {
    // Check if Swiper container exists
    const swiperContainer = document.querySelector(".testimonials-container");
    if (!swiperContainer) {
        console.error("Swiper container not found!");
        return;
    }
    
    // Count the number of slides
    const slides = swiperContainer.querySelectorAll('.swiper-slide');
    const slideCount = slides.length;
    
    // Determine if we should enable loop mode
    // Loop mode requires at least 2 slides, but for better UX, we'll use 3+
    const enableLoop = slideCount >= 3;
    
    if (!enableLoop && slideCount < 2) {
        console.warn('Not enough testimonial slides for carousel. Consider adding more testimonials.');
        return;
    }
    
    // Initialize Swiper after DOM is loaded
    let swiper = new Swiper(".testimonials-container", {
        spaceBetween: 24,
        loop: enableLoop, // Only enable loop if we have enough slides
        grabCursor: true,
        autoplay: enableLoop ? { // Only enable autoplay if loop is enabled
            delay: 5000,
            disableOnInteraction: false,
        } : false,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        navigation: {
            nextEl: ".swiper-button-next",
            prevEl: ".swiper-button-prev",
        },
        breakpoints: {
            576: {
                slidesPerView: Math.min(1, slideCount),
            },
            768: {
                slidesPerView: Math.min(2, slideCount),
                spaceBetween: 48,
            },
            1024: {
                slidesPerView: Math.min(3, slideCount),
                spaceBetween: 48,
            },
        },
    });
    
    console.log(`Swiper initialized with ${slideCount} slides, loop: ${enableLoop}`);
    
});

// Input Animation

const inputs = document.querySelectorAll('.input');

function focusFunc() {
    let parent = this.parentNode;
    parent.classList.add('focus');
}

function blurFunc() {
    let parent = this.parentNode;
    if(this.value == "") {
        parent.classList.remove('focus');
    }
}

inputs.forEach((input) => {
    input.addEventListener('focus', focusFunc);
    input.addEventListener('blur', blurFunc);
})

// Scroll Section Active Link

const sections = document.querySelectorAll('section[id]');

window.addEventListener('scroll', navHighlighter);

function navHighlighter() {
    let scrollY = window.pageYOffset;
    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        const sectionId = current.getAttribute('id');

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.add('active-link');
        }else {
            document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.remove('active-link');
        }
    })
}

// Activating Sidebar

// Mobile Navigation
const navMenu = document.getElementById('sidebar');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');

// Mobile navigation toggle
if(navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    })
}

// Close mobile navigation
if(navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show');
        document.body.style.overflow = 'auto'; // Restore scrolling
    })
}

// Close mobile navigation when clicking on nav links
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('show');
        document.body.style.overflow = 'auto';
    })
})

// Close mobile navigation when clicking outside
document.addEventListener('click', (e) => {
    if (window.innerWidth <= 576) {
        if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
            navMenu.classList.remove('show');
            document.body.style.overflow = 'auto';
        }
    }
})

// Handle window resize
window.addEventListener('resize', () => {
    if (window.innerWidth > 576) {
        navMenu.classList.remove('show');
        document.body.style.overflow = 'auto';
    }
})