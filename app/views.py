from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.utils import timezone
from django.conf import settings
from .models import ThemeSettings, SiteSettings, Skill, Project, Experience, Education, LandingPageSection, Service, Testimonial


def healthcheck(request):
    """Simple healthcheck endpoint for Railway"""
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        # Return more detailed health info
        return JsonResponse({
            "status": "healthy", 
            "database": "connected",
            "timestamp": str(timezone.now()),
            "debug": settings.DEBUG,
            "static_files": "configured"
        })
    except Exception as e:
        return JsonResponse({
            "status": "unhealthy", 
            "error": str(e),
            "timestamp": str(timezone.now())
        }, status=500)


def static_test(request):
    """Test endpoint to check static file configuration"""
    import os
    
    static_info = {
        'STATIC_URL': settings.STATIC_URL,
        'STATIC_ROOT': str(settings.STATIC_ROOT) if hasattr(settings, 'STATIC_ROOT') else None,
        'STATICFILES_DIRS': [str(d) for d in settings.STATICFILES_DIRS] if hasattr(settings, 'STATICFILES_DIRS') else [],
        'RAILWAY_ENVIRONMENT': bool(os.environ.get('RAILWAY_ENVIRONMENT')),
        'static_root_exists': os.path.exists(settings.STATIC_ROOT) if hasattr(settings, 'STATIC_ROOT') else False,
        'static_files_count': 0,
        'sample_files': []
    }
    
    # Check STATIC_ROOT if it exists
    if hasattr(settings, 'STATIC_ROOT') and os.path.exists(settings.STATIC_ROOT):
        try:
            # Count files recursively
            count = 0
            sample_files = []
            for root, dirs, files in os.walk(settings.STATIC_ROOT):
                count += len(files)
                if len(sample_files) < 5:  # Show first 5 files as samples
                    sample_files.extend([os.path.join(root, f) for f in files[:5-len(sample_files)]])
            
            static_info['static_files_count'] = count
            static_info['sample_files'] = [os.path.relpath(f, settings.STATIC_ROOT) for f in sample_files]
        except Exception as e:
            static_info['error'] = str(e)
    
    return JsonResponse(static_info)


def static_test(request):
    """Test endpoint to check if static files are accessible"""
    from django.conf import settings
    import os
    
    static_info = {
        'STATIC_URL': settings.STATIC_URL,
        'STATIC_ROOT': str(settings.STATIC_ROOT),
        'STATICFILES_DIRS': [str(d) for d in settings.STATICFILES_DIRS],
        'DEBUG': settings.DEBUG,
        'static_root_exists': os.path.exists(settings.STATIC_ROOT),
        'static_files_count': len(os.listdir(settings.STATIC_ROOT)) if os.path.exists(settings.STATIC_ROOT) else 0,
    }
    
    return JsonResponse(static_info)


def media_test(request):
    """Test endpoint to check media file configuration"""
    import os
    
    media_info = {
        'MEDIA_URL': settings.MEDIA_URL,
        'MEDIA_ROOT': str(settings.MEDIA_ROOT),
        'RAILWAY_ENVIRONMENT': bool(os.environ.get('RAILWAY_ENVIRONMENT')),
        'media_root_exists': os.path.exists(settings.MEDIA_ROOT),
        'media_files_count': 0,
        'sample_files': []
    }
    
    if os.path.exists(settings.MEDIA_ROOT):
        try:
            # Count files recursively
            count = 0
            sample_files = []
            for root, dirs, files in os.walk(settings.MEDIA_ROOT):
                count += len(files)
                if len(sample_files) < 5:  # Show first 5 files as samples
                    sample_files.extend([os.path.join(root, f) for f in files[:5-len(sample_files)]])
            
            media_info['media_files_count'] = count
            media_info['sample_files'] = [os.path.relpath(f, settings.MEDIA_ROOT) for f in sample_files]
        except Exception as e:
            media_info['error'] = str(e)
    
    return JsonResponse(media_info)


def home_view(request, *args, **kwargs):
    # Get or create site settings
    site_settings = SiteSettings.objects.first()
    if not site_settings:
        site_settings = SiteSettings.objects.create()
    
    # Get active theme
    theme = ThemeSettings.objects.filter(is_active=True).first()
    if not theme:
        theme = ThemeSettings.objects.create(name="Default Theme", is_active=True)
    
    # Get all content data
    skills = Skill.objects.filter(is_active=True).order_by('order', 'name')
    projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')
    experiences = Experience.objects.filter(is_active=True).order_by('order', '-start_date')
    education = Education.objects.filter(is_active=True).order_by('order', '-start_date')
    services = Service.objects.filter(is_active=True).order_by('order', 'title')
    testimonials = Testimonial.objects.filter(is_active=True).order_by('order', 'date')
    landing_sections = LandingPageSection.objects.filter(is_active=True).order_by('order', 'title')
    
    # Group skills by category
    skills_by_category = {
        'frontend': skills.filter(category='frontend'),
        'backend': skills.filter(category='backend'),
        'databases': skills.filter(category='databases'),
        'apis': skills.filter(category='apis'),
        'cloud': skills.filter(category='cloud'),
        'infrastructure': skills.filter(category='infrastructure'),
        'cicd': skills.filter(category='cicd'),
        'containers': skills.filter(category='containers'),
        'monitoring': skills.filter(category='monitoring'),
        'security': skills.filter(category='security'),
        'tools': skills.filter(category='tools'),
        'other': skills.filter(category='other'),
    }
    
    context = {
        'site_settings': site_settings,
        'theme': theme,
        'skills': skills,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'services': services,
        'testimonials': testimonials,
        'landing_sections': landing_sections,
    }
    
    return render(request, 'index.html', context)


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About World</h1>")


def theme_api(request):
    """API endpoint to serve theme data"""
    try:
        # Get active theme or default
        theme = ThemeSettings.objects.filter(is_active=True).first()
        if not theme:
            # Create default theme if none exists
            theme = ThemeSettings.objects.create(
                name="Default Theme",
                is_active=True
            )
        
        # Get site settings
        site_settings = SiteSettings.objects.first()
        if not site_settings:
            site_settings = SiteSettings.objects.create()
        
        # Get all content data
        skills = Skill.objects.filter(is_active=True).order_by('order', 'name')
        projects = Project.objects.filter(is_active=True).order_by('order', '-created_at')
        experiences = Experience.objects.filter(is_active=True).order_by('order', '-start_date')
        education = Education.objects.filter(is_active=True).order_by('order', '-start_date')
        
        theme_data = {
            'colors': {
                'primary': theme.primary_color,
                'secondary': theme.secondary_color,
                'accent': theme.accent_color,
                'background': theme.background_color,
                'text': theme.text_color,
                'card': theme.card_color,
            },
            'typography': {
                'font_family': theme.font_family,
                'heading_font': theme.heading_font,
                'font_size_base': theme.font_size_base,
            },
            'layout': {
                'sidebar_width': theme.sidebar_width,
                'border_radius': theme.border_radius,
                'spacing_unit': theme.spacing_unit,
            },
            'animations': {
                'enabled': theme.enable_animations,
                'speed': theme.animation_speed,
                'stars': theme.enable_stars,
            },
            'custom_css': theme.custom_css,
            'site': {
                'title': site_settings.site_title,
                'description': site_settings.site_description,
                'email': site_settings.email,
                'phone': site_settings.phone,
                'location': site_settings.location,
                'social': {
                    'facebook': site_settings.facebook_url,
                    'instagram': site_settings.instagram_url,
                    'twitter': site_settings.twitter_url,
                    'linkedin': site_settings.linkedin_url,
                    'github': site_settings.github_url,
                }
            },
            'personal': {
                'full_name': site_settings.full_name,
                'job_title': site_settings.job_title,
                'bio': site_settings.bio,
                'profile_image': site_settings.profile_image.url if site_settings.profile_image else None,
                'about_title': site_settings.about_title,
                'about_description': site_settings.about_description,
            },
            'skills': [
                {
                    'name': skill.name,
                    'category': skill.category,
                    'proficiency': skill.proficiency,
                } for skill in skills
            ],
            'projects': [
                {
                    'title': project.title,
                    'description': project.description,
                    'image': project.image.url if project.image else None,
                    'technologies': project.technologies,
                    'demo_url': project.demo_url,
                    'github_url': project.github_url,
                } for project in projects
            ],
            'experience': [
                {
                    'title': exp.title,
                    'company': exp.company,
                    'description': exp.description,
                    'start_date': exp.start_date.strftime('%Y-%m-%d'),
                    'end_date': exp.end_date.strftime('%Y-%m-%d') if exp.end_date else None,
                    'is_current': exp.is_current,
                } for exp in experiences
            ],
            'education': [
                {
                    'degree': edu.degree,
                    'institution': edu.institution,
                    'description': edu.description,
                    'start_date': edu.start_date.strftime('%Y-%m-%d'),
                    'end_date': edu.end_date.strftime('%Y-%m-%d') if edu.end_date else None,
                    'is_current': edu.is_current,
                } for edu in education
            ]
        }
        
        return JsonResponse(theme_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
