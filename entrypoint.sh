#!/bin/sh

python manage.py makemigrations
python manage.py migrate

## note -- you may need to find the absolute path of gunicorn for this to work
exec gunicorn -w 3 -b 0.0.0.0:8000 stevebrownlee.wsgi
