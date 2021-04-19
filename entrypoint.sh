#!/bin/sh

export DATABASE_URL="postgresql://postgres:postgres@api-db:5432/api_dev"

echo "Waiting for postgres..."

while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0