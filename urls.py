"""
URL configuration for the portfolio app.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.conf import settings
from django.conf.urls.static import static

# Import the views from app.views
from app.views import theme_api, home_view, about_view, healthcheck, static_test, media_test

urlpatterns = [
    path("", home_view),
    path("about/", about_view),
    path("api/theme/", theme_api, name="theme_api"),
    path("health/", healthcheck, name="healthcheck"),
    path("health", healthcheck, name="healthcheck_no_slash"),  # Add without trailing slash
    path("static-test/", static_test, name="static_test"),
    path("media-test/", media_test, name="media_test"),
    path('admin/', admin.site.urls),
    # Redirect favicon requests to static file
    path("favicon.ico", lambda request: HttpResponse(status=302, headers={'Location': '/static/favicon.ico'})),
]

# Serve media files (static files are handled by WhiteNoise)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
