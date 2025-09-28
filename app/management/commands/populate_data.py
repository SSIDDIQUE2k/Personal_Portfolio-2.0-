from django.core.management.base import BaseCommand
from app.models import SiteSettings, ThemeSettings, Skill, Service


class Command(BaseCommand):
    help = 'Populate database with default data for portfolio'

    def handle(self, *args, **options):
        # Create or update SiteSettings
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_title': "Shazib's Portfolio",
                'site_description': "Frontend Developer Portfolio",
                'full_name': "Shazib Siddique",
                'job_title': "Frontend Developer",
                'bio': "I have high level experience in web design, development knowledge and producing quality work",
                'welcome_message': "Hello, I am",
                'social_follow_text': "Follow Me",
                'cta_button_text': "More About me!",
                'email': "shazib@example.com",
                'phone': "+1-234-567-8900",
                'location': "New York, NY",
                'facebook_url': "https://facebook.com/shazib",
                'instagram_url': "https://instagram.com/shazib",
                'twitter_url': "https://twitter.com/shazib",
                'linkedin_url': "https://linkedin.com/in/shazib",
                'github_url': "https://github.com/shazib",
                'years_experience': "3+",
                'completed_projects': "50+",
                'support_availability': "24/7",
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created SiteSettings'))
        else:
            self.stdout.write(self.style.SUCCESS('SiteSettings already exists'))

        # Create or update ThemeSettings
        theme, created = ThemeSettings.objects.get_or_create(
            is_active=True,
            defaults={
                'name': "Default Theme",
                'primary_color': '#667eea',
                'secondary_color': '#764ba2',
                'accent_color': '#f093fb',
                'background_color': '#1a1a2e',
                'text_color': '#ffffff',
                'card_color': '#16213e',
                'font_family': 'Poppins',
                'heading_font': 'Turret Road',
                'font_size_base': '16px',
                'sidebar_width': '60px',
                'border_radius': '8px',
                'spacing_unit': '1rem',
                'enable_animations': True,
                'animation_speed': '0.3s',
                'enable_stars': True,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created ThemeSettings'))
        else:
            self.stdout.write(self.style.SUCCESS('ThemeSettings already exists'))

        # Create default skills
        default_skills = [
            {'name': 'HTML', 'category': 'frontend', 'proficiency': 90, 'order': 1},
            {'name': 'CSS', 'category': 'frontend', 'proficiency': 85, 'order': 2},
            {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 80, 'order': 3},
            {'name': 'React', 'category': 'frontend', 'proficiency': 75, 'order': 4},
            {'name': 'Python', 'category': 'backend', 'proficiency': 70, 'order': 5},
            {'name': 'Django', 'category': 'backend', 'proficiency': 65, 'order': 6},
            {'name': 'Git', 'category': 'tools', 'proficiency': 80, 'order': 7},
            {'name': 'VS Code', 'category': 'tools', 'proficiency': 85, 'order': 8},
        ]

        for skill_data in default_skills:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill: {skill.name}'))

        # Create default services
        default_services = [
            {'title': 'Web Design', 'description': 'Creating beautiful and responsive web designs', 'icon_class': 'uil uil-web-grid', 'order': 1},
            {'title': 'Frontend Development', 'description': 'Building interactive user interfaces', 'icon_class': 'uil uil-brackets-curly', 'order': 2},
            {'title': 'UI/UX Design', 'description': 'Designing user-friendly interfaces', 'icon_class': 'uil uil-swatchbook', 'order': 3},
        ]

        for service_data in default_services:
            service, created = Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created service: {service.title}'))

        self.stdout.write(self.style.SUCCESS('Database populated with default data!'))
