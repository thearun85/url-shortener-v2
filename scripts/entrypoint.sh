#!/bin/sh
set -e

echo "Running database setup..."
python -m scripts.create_db

echo "Starting gunicorn..."
exec gunicorn run:app --bind 0.0.0.0:8080 --workers 2
