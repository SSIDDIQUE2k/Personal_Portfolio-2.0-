from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import ThemeSettings, SiteSettings, Skill, Project, Experience, Education


def home_view(request, *args, **kwargs):
    return render(request, 'index.html')


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
