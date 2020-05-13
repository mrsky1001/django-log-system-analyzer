#!/bin/bash
source /home/mrsky1001/devel/virtualenv/django-rrd-virtual/bin/activate
python3.7 manage.py collectstatic --noinput --clear
python3.7 manage.py collectstatic --noinput
python3.7 manage.py runserver
deactivate