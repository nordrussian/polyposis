#!/bin/bash

while ! nc -z $DB_HOST $DB_PORT; do
  echo "Waiting for Postgres at $DB_HOST:$DB_PORT..."
  sleep 2
done

echo "Run migrations"
python npass/manage.py migrate

python npass/manage.py collectstatic --noinput

exec "$@"