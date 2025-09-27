// Toggling Skill Tabs

const tabs = document.querySelectorAll('[data-target]');
const tabContent = document.querySelectorAll('[data-content]');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.target);

        tabContent.forEach(tabContents => {
            tabContents.classList.remove('skills-active');
        })

        target.classList.add('skills-active');

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

let swiper = new Swiper(".testimonials-container", {
    spaceBetween: 24,
    loop: true,
    grabCursor: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
        576: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 48,
        },
    },
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

const navMenu = document.getElementById('sidebar');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');

if(navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-sidebar');
    })
}

if(navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-sidebar');
    })
}

// Animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            // Trigger animations for elements with animation classes
            if (entry.target.classList.contains('animate-fadeInUp')) {
                entry.target.style.animationPlayState = 'running';
            }
            if (entry.target.classList.contains('animate-fadeInLeft')) {
                entry.target.style.animationPlayState = 'running';
            }
            if (entry.target.classList.contains('animate-fadeInRight')) {
                entry.target.style.animationPlayState = 'running';
            }
        }
    });
}, observerOptions);

// Observe elements for animation
document.querySelectorAll('.home-data, .home-img, .section-title, .animate-fadeInUp, .animate-fadeInLeft, .animate-fadeInRight').forEach(el => {
    observer.observe(el);
});

// Add floating animation to home image
document.addEventListener('DOMContentLoaded', function() {
    const homeImg = document.querySelector('.home-img');
    if (homeImg) {
        homeImg.style.animation = 'float 6s ease-in-out infinite';
    }
    
    // Add staggered animation delays to home data elements
    const homeDataElements = document.querySelectorAll('.home-data > *');
    homeDataElements.forEach((el, index) => {
        if (el.classList.contains('animate-fadeInUp')) {
            el.style.animationDelay = `${index * 0.2}s`;
        }
    });

    // Add click animations to interactive elements
    const navLogo = document.querySelector('.nav-logo-text');
    if (navLogo) {
        navLogo.addEventListener('click', function(e) {
            e.preventDefault();
            this.classList.add('animate-shake');
            setTimeout(() => {
                this.classList.remove('animate-shake');
            }, 500);
        });
    }

    // Add hover effects to social links
    const socialLinks = document.querySelectorAll('.home-social-link');
    socialLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            this.style.animation = 'bounce 0.6s ease-in-out';
        });
        link.addEventListener('mouseleave', function() {
            this.style.animation = 'bounce 2s infinite';
        });
    });

    // Add rainbow effect to title on hover
    const title = document.querySelector('.home-title');
    if (title) {
        title.addEventListener('mouseenter', function() {
            this.classList.add('animate-rainbow');
        });
        title.addEventListener('mouseleave', function() {
            this.classList.remove('animate-rainbow');
        });
    }

    // Add wiggle effect to button on click
    const button = document.querySelector('.button');
    if (button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            this.classList.add('animate-wiggle');
            setTimeout(() => {
                this.classList.remove('animate-wiggle');
                // Scroll to about section
                const aboutSection = document.querySelector('#about');
                if (aboutSection) {
                    aboutSection.scrollIntoView({ behavior: 'smooth' });
                }
            }, 1000);
        });
    }
});

// Add sparkle effect to stars
function createSparkle() {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.style.position = 'absolute';
    sparkle.style.width = '4px';
    sparkle.style.height = '4px';
    sparkle.style.background = 'white';
    sparkle.style.borderRadius = '50%';
    sparkle.style.left = Math.random() * 100 + '%';
    sparkle.style.top = Math.random() * 100 + '%';
    sparkle.style.animation = 'sparkle 2s ease-out forwards';
    sparkle.style.pointerEvents = 'none';
    
    document.querySelector('.stars').appendChild(sparkle);
    
    setTimeout(() => {
        sparkle.remove();
    }, 2000);
}

// Create sparkles periodically
setInterval(createSparkle, 3000);

// Animate skill bars when they come into view
function animateSkillBars() {
    const skillBars = document.querySelectorAll('.skills-percentage');
    
    skillBars.forEach((bar, index) => {
        const targetWidth = bar.style.width;
        
        // Store the target width for later use
        bar.setAttribute('data-width', targetWidth);
        
        // Reset width to 0
        bar.style.width = '0%';
        
        // Animate to target width
        setTimeout(() => {
            bar.style.width = targetWidth;
        }, index * 200); // Staggered animation
    });
}


// Skill bars intersection observer
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateSkillBars();
            skillObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.5
});

// Observe skills section
const skillsSection = document.querySelector('#skills');
if (skillsSection) {
    skillObserver.observe(skillsSection);
}

// Add click animation to skill tabs
document.addEventListener('DOMContentLoaded', function() {
    const skillHeaders = document.querySelectorAll('.skills-header');
    skillHeaders.forEach(header => {
        header.addEventListener('click', function() {
            // Add shake animation
            this.classList.add('animate-shake');
            setTimeout(() => {
                this.classList.remove('animate-shake');
            }, 500);
            
            // Don't re-animate skill bars when switching tabs
            // Just show the bars at their target width immediately
            setTimeout(() => {
                const skillBars = document.querySelectorAll('.skills-percentage');
                skillBars.forEach(bar => {
                    const targetWidth = bar.getAttribute('data-width') || bar.style.width;
                    bar.style.width = targetWidth;
                });
            }, 300);
        });
    });
});

// Social Share Functionality
document.addEventListener('DOMContentLoaded', function() {
    const socialShareBtn = document.querySelector('.social-share');
    
    if (socialShareBtn) {
        socialShareBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Get current page URL
            const currentUrl = window.location.href;
            const portfolioTitle = "Mariam's Portfolio - Frontend Developer";
            const portfolioDescription = "Check out Mariam's amazing portfolio showcasing frontend development skills!";
            
            // Check if Web Share API is supported
            if (navigator.share) {
                navigator.share({
                    title: portfolioTitle,
                    text: portfolioDescription,
                    url: currentUrl
                }).then(() => {
                    console.log('Portfolio shared successfully!');
                }).catch((error) => {
                    console.log('Error sharing:', error);
                    fallbackShare(currentUrl, portfolioTitle);
                });
            } else {
                // Fallback for browsers that don't support Web Share API
                fallbackShare(currentUrl, portfolioTitle);
            }
        });
    }
});

// Fallback share function
function fallbackShare(url, title) {
    // Create a temporary textarea to copy URL
    const textarea = document.createElement('textarea');
    textarea.value = url;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    
    // Show notification
    showNotification('Portfolio URL copied to clipboard!');
}

// Show notification function
function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'share-notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        z-index: 10000;
        font-weight: 500;
        animation: slideInRight 0.5s ease-out;
    `;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.5s ease-out forwards';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 500);
    }, 3000);
}

console.log('Portfolio JavaScript loaded successfully!');