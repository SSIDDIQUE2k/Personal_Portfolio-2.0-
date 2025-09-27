"""
URL configuration for the portfolio app.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import models

# Import the views from app.views
from app.views import theme_api, home_view, about_view

urlpatterns = [
    path("", home_view),
    path("about/", about_view),
    path("api/theme/", theme_api, name="theme_api"),
    path('admin/', admin.site.urls),
]
