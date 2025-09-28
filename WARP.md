# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

Project scope and goals
- This is a single-app Django project (flat layout) for a personal portfolio. The code intentionally keeps the project structure minimal while still using Django’s capabilities (admin, models, middleware, templating).

Common commands
- Environment setup (Pipenv)
  - pip install --user pipenv
  - pipenv install
- Database setup and migrations
  - pipenv run python manage.py makemigrations app
  - pipenv run python manage.py migrate
- Run development server
  - pipenv run python manage.py runserver 127.0.0.1:8000
- Create an admin user (required to access /admin/)
  - pipenv run python manage.py createsuperuser
- Test helpers in repo
  - (Test files have been removed for production deployment)
- Run a single Django test (when tests are added under a tests module)
  - pipenv run python manage.py test app.tests.test_module.TestCaseClass.test_method

Key endpoints
- /            Renders templates/index.html
- /about/      Simple HTML response
- /api/theme/  JSON API combining ThemeSettings, SiteSettings, Skill, Project, Experience, Education
- /admin/      Django admin (restricted to staff/superusers by middleware)

High-level architecture and structure
- Flat Django project
  - Root-level settings.py, urls.py, wsgi.py, manage.py (no nested project folder). ROOT_URLCONF = "urls".
  - Database: SQLite at BASE_DIR/db.sqlite3.
  - Templates: settings.TEMPLATES points to BASE_DIR/templates and app templates.
  - Static: STATIC_URL="/static/"; STATICFILES_DIRS includes BASE_DIR/static if present.
- Single Django app: app
  - Models (app/models.py)
    - ThemeSettings: Centralized theme configuration (colors, typography, layout, animations, custom CSS). Enforces single active theme by deactivating others on save.
    - SiteSettings: Site-wide metadata and personal details (title, description, contact, social links, toggles). Enforces a singleton-like behavior on save and via admin permissions.
    - Skill: Name, category, proficiency, ordering, active flag.
    - Project: Portfolio projects with description, image, tech list, links, ordering, active flag.
    - Experience: Work history with dates, current flag, ordering, active flag.
    - Education: Education history with dates, ordering, active flag.
  - Admin (app/admin.py)
    - All key models registered with curated list_display, filters, search, ordering, and grouped fieldsets.
    - ThemeSettings admin renders color previews.
    - SiteSettings admin restricts to a single instance and prevents deletion.
    - Admin site branding customized (headers/titles).
  - Views (app/views.py)
    - home_view: Renders index.html.
    - about_view: Simple HttpResponse.
    - theme_api: Aggregates data across ThemeSettings, SiteSettings, Skill, Project, Experience, Education into a single JSON payload; creates defaults if none exist.
  - Middleware (app/middleware.py)
    - AdminAccessMiddleware: Restricts /admin/ to authenticated staff/superusers; allows /admin/login/ and /admin/logout/; otherwise 403 or redirect to login. This enforces that only admin users can see the Django administration page.
    - LocalhostCOOPMiddleware: Optional helper to set Cross-Origin-Opener-Policy for localhost; disabled in default MIDDLEWARE (see settings.py).
- URL routing (urls.py)
  - Maps "", "about/", "api/theme/", and "admin/" to views and admin site.
- Server helpers
  - simple_server.py demonstrates booting Django and simple health checks, including exercising the theme_api via RequestFactory.

Important notes and behaviors
- Admin access is enforced by middleware (not just Django’s default permissions). To enter /admin/, ensure the user has is_staff (or is_superuser) and is authenticated.
- Image fields exist on SiteSettings and Project; MEDIA settings are not configured in settings.py. If you plan to upload media via admin, you may need to add MEDIA_URL and MEDIA_ROOT and wire up serving in development.
- Security headers: SECURE_CROSS_ORIGIN_OPENER_POLICY is explicitly disabled for local development; COOP header can be reintroduced via LocalhostCOOPMiddleware if needed for browser popup workflows.

What’s in README.md
- States that this repo is a “Single Page Django App” inspired by Adam Johnson’s comparison of Flask and Django single-file applications. It does not contain operational commands; this WARP.md consolidates the practical workflow above.
