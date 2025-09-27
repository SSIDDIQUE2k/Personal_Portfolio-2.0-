import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Define AppConfig before Django setup
import django.apps

class AppConfig(django.apps.AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    verbose_name = 'Portfolio App'

# Check if Django is already configured
if not hasattr(sys, '_django_configured'):
    from django.conf import settings
    from django.core.wsgi import get_wsgi_application
    from django.http import HttpResponse
    from django.urls import path, include
    from django.shortcuts import render

    # https://docs.djangoproject.com/en/dev/topics/settings/#using-settings-without-setting-django-settings-module
    settings.configure(
        DEBUG=True,
        SECRET_KEY = 'w^h13cf0p8fl^98raarj#-u$c6e!)l@1rl!+9j^a%rrb*8xpe3',
        ALLOWED_HOSTS=['localhost', '127.0.0.1', '*'],
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app',  # Use string instead of __name__
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            __name__ + '.LocalhostCOOPMiddleware',
        ],
        SECURE_CROSS_ORIGIN_OPENER_POLICY = None,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': ['templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ],
        STATIC_URL='/static/',
        STATICFILES_DIRS=[
            'static',
        ],
    )

    # Initialize Django
    import django
    import django.apps
    django.setup()
    
    # Mark Django as configured
    sys._django_configured = True

# Now we can safely import Django components
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.urls import path, include
from django.shortcuts import render
from django.utils.html import format_html

# Import models from the app module
from app.models import ThemeSettings, SiteSettings, Skill, Project, Experience, Education

def admin_required(user):
    """Check if user is staff/admin"""
    return user.is_authenticated and user.is_staff

def restricted_admin(request):
    """Redirect non-admin users trying to access admin"""
    if not admin_required(request.user):
        return HttpResponse("<h1>Access Denied</h1><p>You must be an admin user to access this page.</p>", status=403)
    return redirect('/admin/')

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

# Custom middleware to handle COOP headers for localhost
class LocalhostCOOPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Only set COOP header for localhost/127.0.0.1
        if request.get_host() in ['localhost:8000', '127.0.0.1:8000', 'localhost', '127.0.0.1']:
            response['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
        
        return response

# Admin classes are now defined in app/admin.py

# Customize admin site
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"

# Use default admin site for simplicity
urlpatterns = [
    path("", home_view),
    path("about/", about_view),
    path("api/theme/", theme_api, name="theme_api"),
    path('admin/', admin.site.urls),
]


# Django app configuration
default_app_config = 'app.AppConfig'

application = get_wsgi_application()

if __name__ == "__main__":
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)