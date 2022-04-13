release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py createsuperuser --noinput
web: gunicorn gettingstarted.wsgi
