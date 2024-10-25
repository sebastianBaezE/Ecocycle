#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python3 manage.py collectstatic --no-input

python3 manage.py migrate

python3 manage.py seed_database

python3 manage.py create_superuser