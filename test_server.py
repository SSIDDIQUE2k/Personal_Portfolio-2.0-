#!/usr/bin/env python
import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    print("Starting Django server test...")
    
    # Set Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    
    try:
        # Setup Django
        django.setup()
        print("Django setup successful")
        
        # Test database connection
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"Database tables: {[table[0] for table in tables]}")
        
        # Test models
        from app.models import ThemeSettings, SiteSettings
        print("Models imported successfully")
        
        # Test theme API
        from app.views import theme_api
        from django.test import RequestFactory
        factory = RequestFactory()
        request = factory.get('/api/theme/')
        response = theme_api(request)
        print(f"Theme API response status: {response.status_code}")
        if response.status_code == 200:
            print("Theme API working correctly!")
        else:
            print(f"Theme API error: {response.content}")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
