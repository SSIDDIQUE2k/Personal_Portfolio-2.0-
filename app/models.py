from django.db import models


class ThemeSettings(models.Model):
    """Model to store website theme customization settings"""
    
    # Basic Info
    name = models.CharField(max_length=100, default="Default Theme", help_text="Theme name")
    is_active = models.BooleanField(default=True, help_text="Is this theme currently active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Color Scheme
    primary_color = models.CharField(max_length=7, default="#667eea", help_text="Primary color (hex)")
    secondary_color = models.CharField(max_length=7, default="#764ba2", help_text="Secondary color (hex)")
    accent_color = models.CharField(max_length=7, default="#f093fb", help_text="Accent color (hex)")
    background_color = models.CharField(max_length=7, default="#1a1a2e", help_text="Background color (hex)")
    text_color = models.CharField(max_length=7, default="#ffffff", help_text="Text color (hex)")
    card_color = models.CharField(max_length=7, default="#16213e", help_text="Card/box color (hex)")
    
    # Typography
    font_family = models.CharField(max_length=100, default="Poppins", help_text="Main font family")
    heading_font = models.CharField(max_length=100, default="Turret Road", help_text="Heading font family")
    font_size_base = models.IntegerField(default=16, help_text="Base font size (px)")
    
    # Layout
    sidebar_width = models.IntegerField(default=100, help_text="Sidebar width (px)")
    border_radius = models.IntegerField(default=8, help_text="Border radius (px)")
    spacing_unit = models.IntegerField(default=16, help_text="Spacing unit (px)")
    
    # Animations
    enable_animations = models.BooleanField(default=True, help_text="Enable animations")
    animation_speed = models.FloatField(default=1.0, help_text="Animation speed multiplier")
    enable_stars = models.BooleanField(default=True, help_text="Enable star background")
    
    # Custom CSS
    custom_css = models.TextField(blank=True, help_text="Custom CSS code")
    
    class Meta:
        verbose_name = "Theme Settings"
        verbose_name_plural = "Theme Settings"
        ordering = ['-is_active', '-created_at']
    
    def __str__(self):
        return f"{self.name} {'(Active)' if self.is_active else ''}"
    
    def save(self, *args, **kwargs):
        # Ensure only one theme is active at a time
        if self.is_active:
            ThemeSettings.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class SiteSettings(models.Model):
    """Model to store general site settings"""
    
    # Site Info
    site_title = models.CharField(max_length=200, default="Mariam's Portfolio", help_text="Site title")
    site_description = models.TextField(default="Frontend Developer Portfolio", help_text="Site description")
    site_keywords = models.CharField(max_length=500, default="portfolio, frontend, developer, web design", help_text="SEO keywords")
    
    # Personal Information
    full_name = models.CharField(max_length=100, default="Shazib S", help_text="Your full name")
    job_title = models.CharField(max_length=100, default="Frontend Developer", help_text="Your job title")
    bio = models.TextField(default="I have high level experience in web design, development knowledge and producing quality work", help_text="Short bio/description")
    profile_image = models.ImageField(upload_to='profile/', blank=True, help_text="Your profile image")
    about_image = models.ImageField(upload_to='profile/', blank=True, help_text="Image for the about section")
    
    # Home Section
    welcome_message = models.CharField(max_length=200, default="Hello, I am", help_text="Welcome message prefix ONLY (e.g., 'Hello, I am', 'Hi, I'm', 'Welcome, I'm'). Do NOT include your name - it will be added automatically from the Full Name field.")
    home_background_image = models.ImageField(upload_to='backgrounds/', blank=True, help_text="Background image for the home section")
    home_image_url = models.URLField(blank=True, default="https://i.postimg.cc/3NgvPcZD/home-img.png", help_text="URL for the home section profile image")
    social_follow_text = models.CharField(max_length=50, default="Follow Me", help_text="Text for social media section")
    cta_button_text = models.CharField(max_length=100, default="More About me!", help_text="Call-to-action button text")
    
    # About Stats
    years_experience = models.CharField(max_length=20, default="5+", help_text="Years of experience display")
    completed_projects = models.CharField(max_length=20, default="30+", help_text="Number of completed projects")
    support_availability = models.CharField(max_length=50, default="Online 24/7", help_text="Support availability text")
    
    # Contact Info
    email = models.EmailField(default="mariam@example.com", help_text="Contact email")
    phone = models.CharField(max_length=20, default="+1 234 567 8900", help_text="Contact phone")
    location = models.CharField(max_length=100, default="New York, NY", help_text="Location")
    
    # Contact Info Display
    messenger_display = models.CharField(max_length=100, blank=True, help_text="What to show for Messenger contact (leave blank for full name)")
    whatsapp_display = models.CharField(max_length=100, blank=True, help_text="What to show for WhatsApp contact (leave blank for phone)")
    email_display = models.CharField(max_length=100, blank=True, help_text="What to show for email contact (leave blank for email)")
    
    # Social Media
    facebook_url = models.URLField(blank=True, help_text="Facebook profile URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")
    
    # About Section
    about_title = models.CharField(max_length=200, default="About Me", help_text="About section title")
    about_description = models.TextField(default="I am a passionate frontend developer with expertise in creating beautiful and functional web applications.", help_text="About section description")
    
    # Section Titles
    qualifications_title = models.CharField(max_length=200, default="My Journey", help_text="Qualifications section title")
    qualifications_subtitle = models.CharField(max_length=200, default="Qualifications", help_text="Qualifications section subtitle")
    experience_title = models.CharField(max_length=200, default="My Abilities", help_text="Experience section title")
    experience_subtitle = models.CharField(max_length=200, default="My Experience", help_text="Experience section subtitle")
    portfolio_title = models.CharField(max_length=200, default="My Portfolio", help_text="Portfolio section title")
    portfolio_subtitle = models.CharField(max_length=200, default="Recent Works", help_text="Portfolio section subtitle")
    services_title = models.CharField(max_length=200, default="Services", help_text="Services section title")
    services_subtitle = models.CharField(max_length=200, default="What I Offer", help_text="Services section subtitle")
    testimonials_title = models.CharField(max_length=200, default="My clients say", help_text="Testimonials section title")
    testimonials_subtitle = models.CharField(max_length=200, default="Testimonials", help_text="Testimonials section subtitle")
    contact_title = models.CharField(max_length=200, default="Get in Touch", help_text="Contact section title")
    contact_subtitle = models.CharField(max_length=200, default="Contact me", help_text="Contact section subtitle")
    
    # Default Images
    default_project_image = models.URLField(blank=True, default="https://i.postimg.cc/43Th5VXJ/work-1.png", help_text="Default image for projects")
    default_testimonial_image = models.URLField(blank=True, default="https://i.postimg.cc/MTr9j4Yn/client1.jpg", help_text="Default image for testimonials")
    default_about_image = models.URLField(blank=True, default="https://i.postimg.cc/2SXX3YbS/Screenshot-from-2025-08-28-19-27-55.png", help_text="Default image for about section")
    
    # Footer
    footer_copyright_text = models.CharField(max_length=200, default="All rights reserved", help_text="Footer copyright text")
    footer_copyright_link = models.URLField(blank=True, help_text="Footer copyright link URL")
    footer_copyright_link_text = models.CharField(max_length=100, blank=True, help_text="Footer copyright link text")
    
    # SEO
    google_analytics_id = models.CharField(max_length=50, blank=True, help_text="Google Analytics ID")
    meta_image = models.ImageField(upload_to='meta/', blank=True, help_text="Meta image for social sharing")
    
    # Features
    enable_blog = models.BooleanField(default=False, help_text="Enable blog section")
    enable_contact_form = models.BooleanField(default=True, help_text="Enable contact form")
    enable_dark_mode = models.BooleanField(default=True, help_text="Enable dark mode toggle")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return f"Site Settings - {self.site_title}"
    
    def save(self, *args, **kwargs):
        # Ensure only one site settings instance exists
        if not self.pk and SiteSettings.objects.exists():
            return SiteSettings.objects.first()
        
        # Validate welcome_message doesn't contain the full name
        if self.full_name and self.full_name.lower() in self.welcome_message.lower():
            # Extract just the greeting part
            greeting_options = ['hello, i am', 'hi, i\'m', 'welcome, i\'m', 'hey, i\'m']
            for greeting in greeting_options:
                if greeting in self.welcome_message.lower():
                    self.welcome_message = greeting.title()
                    break
            else:
                self.welcome_message = "Hello, I am"
        
        super().save(*args, **kwargs)


class Skill(models.Model):
    """Model to store skills"""
    
    name = models.CharField(max_length=100, help_text="Skill name")
    category = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
        ('other', 'Other')
    ], default='frontend', help_text="Skill category")
    proficiency = models.IntegerField(default=80, help_text="Proficiency percentage (0-100)")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show this skill")
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    """Model to store portfolio projects"""
    
    title = models.CharField(max_length=200, help_text="Project title")
    description = models.TextField(help_text="Project description")
    image = models.ImageField(upload_to='projects/', blank=True, help_text="Project image")
    technologies = models.CharField(max_length=500, help_text="Technologies used (comma separated)")
    demo_url = models.URLField(blank=True, help_text="Demo URL")
    github_url = models.URLField(blank=True, help_text="GitHub URL")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show this project")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title


class Experience(models.Model):
    """Model to store work experience"""
    
    title = models.CharField(max_length=200, help_text="Job title")
    company = models.CharField(max_length=200, help_text="Company name")
    description = models.TextField(help_text="Job description")
    start_date = models.DateField(help_text="Start date")
    end_date = models.DateField(null=True, blank=True, help_text="End date (leave blank if current)")
    is_current = models.BooleanField(default=False, help_text="Current job")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show this experience")
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    """Model to store education"""
    
    degree = models.CharField(max_length=200, help_text="Degree name")
    institution = models.CharField(max_length=200, help_text="Institution name")
    description = models.TextField(blank=True, help_text="Additional details")
    start_date = models.DateField(help_text="Start date")
    end_date = models.DateField(null=True, blank=True, help_text="End date")
    is_current = models.BooleanField(default=False, help_text="Currently studying")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show this education")
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education"
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"


class LandingPageSection(models.Model):
    """Model to store custom landing page sections"""
    
    SECTION_TYPES = [
        ('services', 'Services'),
        ('testimonials', 'Testimonials'),
        ('stats', 'Statistics'),
        ('custom', 'Custom Content'),
    ]
    
    title = models.CharField(max_length=200, help_text="Section title")
    subtitle = models.CharField(max_length=300, blank=True, help_text="Section subtitle")
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, default='custom', help_text="Type of section")
    content = models.TextField(help_text="Section content (supports HTML)")
    icon_class = models.CharField(max_length=100, blank=True, help_text="CSS class for icon (e.g., 'uil uil-palette')")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show this section")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Landing Page Section"
        verbose_name_plural = "Landing Page Sections"
        ordering = ['order', 'title']
    
    def __str__(self):
        return f"{self.title} ({self.get_section_type_display()})"


class Service(models.Model):
    """Model to store services offered"""
    
    title = models.CharField(max_length=200, help_text="Service title")
    description = models.TextField(help_text="Service description")
    icon_class = models.CharField(max_length=100, help_text="CSS class for icon (e.g., 'uil uil-web-grid')")
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True, help_text="Show this service")
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100, help_text="Client's name")
    position = models.CharField(max_length=100, help_text="Client's job title or position")
    company = models.CharField(max_length=100, blank=True, help_text="Client's company (optional)")
    testimonial_text = models.TextField(help_text="The testimonial content")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True, help_text="Client's photo (optional)")
    date = models.DateField(help_text="Date when the testimonial was given")
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        default=5,
        help_text="Rating from 1 to 5 stars"
    )
    is_active = models.BooleanField(default=True, help_text="Show this testimonial on the website")
    order = models.PositiveIntegerField(default=0, help_text="Order of display (lower numbers appear first)")
    
    class Meta:
        ordering = ['order', 'date']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.name} - {self.company or self.position}"
