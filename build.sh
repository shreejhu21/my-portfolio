#!/usr/bin/env bash
# Triggering fresh deploy to Render
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py populate_data
