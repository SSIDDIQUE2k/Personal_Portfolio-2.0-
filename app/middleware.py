from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import views as auth_views


# Custom middleware to restrict admin access to admin users only
class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for admin URLs
        if request.path.startswith('/admin/'):
            # Allow access to admin login page
            if request.path == '/admin/login/' or request.path == '/admin/logout/':
                return self.get_response(request)
            
            # Check if user is authenticated and has admin privileges
            if not request.user.is_authenticated:
                # Redirect to admin login page
                return redirect('/admin/login/?next=' + request.path)
            
            # Check if user is admin/staff
            if not (request.user.is_staff or request.user.is_superuser):
                return HttpResponseForbidden(
                    "<h1>Access Denied</h1>"
                    "<p>You don't have permission to access the admin panel. "
                    "Only admin users can access this area.</p>"
                    "<p><a href='/'>Return to Home</a></p>"
                )
        
        return self.get_response(request)


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
