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
from app.views import theme_api, home_view, about_view

urlpatterns = [
    path("", home_view),
    path("about/", about_view),
    path("api/theme/", theme_api, name="theme_api"),
    path('admin/', admin.site.urls),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
