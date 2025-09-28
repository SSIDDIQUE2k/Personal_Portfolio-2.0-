from django.core.management.base import BaseCommand
from app.models import ThemeSettings


class Command(BaseCommand):
    help = 'Fix corrupted theme data on Railway deployment'

    def handle(self, *args, **options):
        self.stdout.write('Fixing corrupted theme data...')
        
        # Get all theme settings
        themes = ThemeSettings.objects.all()
        
        if not themes.exists():
            self.stdout.write('No theme settings found. Creating default theme...')
            ThemeSettings.objects.create(
                name="Default Theme",
                is_active=True,
                primary_color="#667eea",
                secondary_color="#764ba2",
                accent_color="#f093fb",
                background_color="#1a1a2e",
                text_color="#ffffff",
                card_color="#16213e"
            )
            self.stdout.write(self.style.SUCCESS('Default theme created successfully!'))
            return
        
        # Fix corrupted themes
        fixed_count = 0
        for theme in themes:
            needs_fix = False
            
            # Fix invalid color values
            if theme.background_color.startswith('@'):
                theme.background_color = theme.background_color.replace('@', '#')
                needs_fix = True
            
            if theme.primary_color == "#000000":
                theme.primary_color = "#667eea"
                needs_fix = True
                
            if theme.secondary_color == "#000000":
                theme.secondary_color = "#764ba2"
                needs_fix = True
            
            if needs_fix:
                theme.save()
                fixed_count += 1
                self.stdout.write(f'Fixed theme: {theme.name}')
        
        if fixed_count > 0:
            self.stdout.write(self.style.SUCCESS(f'Successfully fixed {fixed_count} theme(s)!'))
        else:
            self.stdout.write('No themes needed fixing.')
        
        # Display current theme data
        active_theme = ThemeSettings.objects.filter(is_active=True).first()
        if active_theme:
            self.stdout.write(f'\nActive theme: {active_theme.name}')
            self.stdout.write(f'Background: {active_theme.background_color}')
            self.stdout.write(f'Primary: {active_theme.primary_color}')
            self.stdout.write(f'Secondary: {active_theme.secondary_color}')
