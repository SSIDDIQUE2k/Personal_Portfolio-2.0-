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
    full_name = models.CharField(max_length=100, default="Shazib", help_text="Your full name")
    job_title = models.CharField(max_length=100, default="Frontend Developer", help_text="Your job title")
    bio = models.TextField(default="I have high level experience in web design, development knowledge and producing quality work", help_text="Short bio/description")
    profile_image = models.ImageField(upload_to='profile/', blank=True, help_text="Your profile image")
    
    # Contact Info
    email = models.EmailField(default="mariam@example.com", help_text="Contact email")
    phone = models.CharField(max_length=20, default="+1 234 567 8900", help_text="Contact phone")
    location = models.CharField(max_length=100, default="New York, NY", help_text="Location")
    
    # Social Media
    facebook_url = models.URLField(blank=True, help_text="Facebook profile URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter profile URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")
    
    # About Section
    about_title = models.CharField(max_length=200, default="About Me", help_text="About section title")
    about_description = models.TextField(default="I am a passionate frontend developer with expertise in creating beautiful and functional web applications.", help_text="About section description")
    
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
