web: python manage.py collectstatic --noinput
release: python manage.py migrate
web: gunicorn Dns_Lookup_web.wsgi --log-file -