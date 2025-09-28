from django.core.management.base import BaseCommand
from app.models import ThemeSettings, SiteSettings
from django.core.cache import cache
import json


class Command(BaseCommand):
    help = 'Force update theme settings and clear cache'

    def handle(self, *args, **options):
        self.stdout.write('Forcing theme update...')
        
        # Clear any cache
        cache.clear()
        self.stdout.write('Cache cleared.')
        
        # Get or create theme settings
        theme = ThemeSettings.objects.filter(is_active=True).first()
        if not theme:
            self.stdout.write('Creating new theme...')
            theme = ThemeSettings.objects.create(
                name="Default Theme",
                is_active=True,
                primary_color="#667eea",
                secondary_color="#764ba2",
                accent_color="#f093fb",
                background_color="#1a1a2e",
                text_color="#ffffff",
                card_color="#16213e"
            )
        else:
            # Force update the theme with correct values
            self.stdout.write(f'Updating theme: {theme.name}')
            theme.primary_color = "#667eea"
            theme.secondary_color = "#764ba2"
            theme.accent_color = "#f093fb"
            theme.background_color = "#1a1a2e"
            theme.text_color = "#ffffff"
            theme.card_color = "#16213e"
            theme.save()
        
        # Get or create site settings
        site_settings = SiteSettings.objects.first()
        if not site_settings:
            self.stdout.write('Creating site settings...')
            site_settings = SiteSettings.objects.create()
        
        self.stdout.write(self.style.SUCCESS('Theme updated successfully!'))
        self.stdout.write(f'Background: {theme.background_color}')
        self.stdout.write(f'Primary: {theme.primary_color}')
        self.stdout.write(f'Secondary: {theme.secondary_color}')
        
        # Test the API response
        from app.views import theme_api
        from django.test import RequestFactory
        
        factory = RequestFactory()
        request = factory.get('/api/theme/')
        response = theme_api(request)
        
        if response.status_code == 200:
            data = json.loads(response.content)
            self.stdout.write('API Response:')
            self.stdout.write(f'  Background: {data["colors"]["background"]}')
            self.stdout.write(f'  Primary: {data["colors"]["primary"]}')
            self.stdout.write(f'  Secondary: {data["colors"]["secondary"]}')
        else:
            self.stdout.write(self.style.ERROR(f'API Error: {response.status_code}'))
