#!/usr/bin/env python3
import sys
import os

print("Testing Django setup...")

try:
    import django
    print(f"✅ Django imported successfully - version {django.get_version()}")
except ImportError as e:
    print(f"❌ Django import failed: {e}")
    sys.exit(1)

try:
    from django.conf import settings
    from django.http import HttpResponse
    
    # Configure Django
    settings.configure(
        DEBUG=True,
        SECRET_KEY='test-key',
        ALLOWED_HOSTS=['*'],
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        }
    )
    print("✅ Django settings configured")
    
    from django.urls import path
    from django.core.wsgi import get_wsgi_application
    
    def test_view(request):
        return HttpResponse("<h1>Django is working!</h1>")
    
    urlpatterns = [
        path('', test_view),
    ]
    
    application = get_wsgi_application()
    print("✅ Django app configured")
    
    if __name__ == "__main__":
        from django.core.management import execute_from_command_line
        print("🚀 Starting Django server...")
        execute_from_command_line(['test_django.py', 'runserver', '127.0.0.1:8001'])
        
except Exception as e:
    import traceback
    print(f"❌ Error: {e}")
    traceback.print_exc()