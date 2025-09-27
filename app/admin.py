from django.contrib import admin
from django.utils.html import format_html
from .models import ThemeSettings, SiteSettings, Skill, Project, Experience, Education


@admin.register(ThemeSettings)
class ThemeSettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_preview', 'is_active', 'created_at']
    list_filter = ['is_active', 'enable_animations', 'enable_stars']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'is_active')
        }),
        ('Color Scheme', {
            'fields': ('primary_color', 'secondary_color', 'accent_color', 'background_color', 'text_color', 'card_color'),
            'description': 'Customize the color scheme of your portfolio'
        }),
        ('Typography', {
            'fields': ('font_family', 'heading_font', 'font_size_base'),
            'description': 'Configure fonts and text styling'
        }),
        ('Layout', {
            'fields': ('sidebar_width', 'border_radius', 'spacing_unit'),
            'description': 'Adjust layout dimensions and spacing'
        }),
        ('Animations', {
            'fields': ('enable_animations', 'animation_speed', 'enable_stars'),
            'description': 'Control animation effects and performance'
        }),
        ('Custom CSS', {
            'fields': ('custom_css',),
            'description': 'Add custom CSS for advanced styling'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def color_preview(self, obj):
        """Display color previews in admin list"""
        colors = [
            ('Primary', obj.primary_color),
            ('Secondary', obj.secondary_color),
            ('Accent', obj.accent_color)
        ]
        
        preview_html = ''
        for name, color in colors:
            preview_html += f'''
                <div style="display: inline-block; margin-right: 10px;">
                    <div style="width: 20px; height: 20px; background-color: {color}; border: 1px solid #ccc; display: inline-block; vertical-align: middle;"></div>
                    <span style="margin-left: 5px; font-size: 12px;">{name}</span>
                </div>
            '''
        return format_html(preview_html)
    
    color_preview.short_description = 'Color Preview'


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title', 'email', 'location', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Site Information', {
            'fields': ('site_title', 'site_description', 'site_keywords')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'instagram_url', 'twitter_url', 'linkedin_url', 'github_url'),
            'description': 'Add your social media profile URLs'
        }),
        ('SEO & Analytics', {
            'fields': ('google_analytics_id', 'meta_image'),
            'description': 'Configure SEO and analytics'
        }),
        ('Features', {
            'fields': ('enable_blog', 'enable_contact_form', 'enable_dark_mode'),
            'description': 'Enable or disable site features'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def has_add_permission(self, request):
        # Only allow one site settings instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of site settings
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    list_editable = ['proficiency', 'order', 'is_active']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category', 'proficiency')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'demo_url', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Links & Technologies', {
            'fields': ('technologies', 'demo_url', 'github_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'is_current', 'order', 'is_active']
    list_filter = ['is_current', 'is_active', 'start_date']
    search_fields = ['title', 'company', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-start_date']
    
    fieldsets = (
        ('Job Information', {
            'fields': ('title', 'company', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'order', 'is_active']
    list_filter = ['is_current', 'is_active', 'start_date']
    search_fields = ['degree', 'institution', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-start_date']
    
    fieldsets = (
        ('Education Information', {
            'fields': ('degree', 'institution', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        })
    )

# Customize admin site
admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
