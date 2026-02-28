#!/bin/bash
set -e

echo "Running migrations..."
python /app/manage.py migrate --noinput

echo "Collecting static files..."
python /app/manage.py collectstatic --noinput

echo "Starting supervisord..."
exec "$@"