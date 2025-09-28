web: gunicorn --bind 0.0.0.0:$PORT wsgi:application
release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py create_superuser && python manage.py populate_data
