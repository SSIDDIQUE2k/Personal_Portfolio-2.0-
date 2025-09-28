"""
Django settings for the Single-Page-Django-App project.
"""

import os
from pathlib import Path

# ----------------------------------------------------
# Paths
# ----------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent  # flat layout

# ----------------------------------------------------
# Security
# ----------------------------------------------------
import os
SECRET_KEY = os.environ.get('SECRET_KEY', "dev-secret-key-change-me")
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', "127.0.0.1,localhost,*").split(',')

# ----------------------------------------------------
# Applications
# ----------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",  # your app
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add WhiteNoise for static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "app.middleware.AdminAccessMiddleware",  # Temporarily disabled for testing
    # comment this out if you don't actually have it
    # "app.middleware.LocalhostCOOPMiddleware",
]

ROOT_URLCONF = "urls"

# ----------------------------------------------------
# Templates
# ----------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # absolute path
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"

# ----------------------------------------------------
# Database
# ----------------------------------------------------
if os.environ.get('DATABASE_URL'):
    # Production database (Railway PostgreSQL)
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # Development database (SQLite)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ----------------------------------------------------
# Password validation
# ----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------------------------------
# Internationalization
# ----------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----------------------------------------------------
# Static files
# ----------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# WhiteNoise configuration for static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------------------------------------------
# Media files
# ----------------------------------------------------
if os.environ.get('RAILWAY_ENVIRONMENT'):
    # Production: Use Railway's persistent volume for media files
    MEDIA_ROOT = BASE_DIR / "storage"
    MEDIA_URL = "/media/"
else:
    # Development: Use local media directory
    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"

# ----------------------------------------------------
# Default PK
# ----------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----------------------------------------------------
# CSRF Configuration
# ----------------------------------------------------
# Get Railway domain from environment or use default
RAILWAY_DOMAIN = os.environ.get('RAILWAY_PUBLIC_DOMAIN', 'web-production-8f88a.up.railway.app')
CSRF_TRUSTED_ORIGINS = [
    f'https://{RAILWAY_DOMAIN}',
    'https://web-production-8f88a.up.railway.app',  # Your current Railway domain
    'http://localhost:8000',  # For local development
    'http://127.0.0.1:8000',  # For local development
]

# Additional CSRF settings for production
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript access for AJAX requests
CSRF_USE_SESSIONS = False

# ----------------------------------------------------
# Security headers (disabled for local dev)
# ----------------------------------------------------
SECURE_CROSS_ORIGIN_OPENER_POLICY = None

# ----------------------------------------------------
# Logging: ensure output is visible in console
# ----------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

# Production Security Settings
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # Disable SSL redirect for Railway (Railway handles SSL termination)
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
