release: python manage.py migrate
release: python manage.py createsuperuser --noinput --username testuser
web: gunicorn gettingstarted.wsgi