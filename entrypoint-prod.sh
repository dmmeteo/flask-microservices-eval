#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z eval-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

gunicorn -b 0.0.0.0:5000 manage:app

