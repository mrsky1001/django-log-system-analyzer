#!/bin/bash
python3.7 manage.py collectstatic --noinput --clear 
python3.7 manage.py collectstatic --noinput
python3.7 manage.py runserver
