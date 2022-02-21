#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations --noinput
python manage.py migrate
python manage.py loaddata category.json
python manage.py loaddata ingredient.json
python manage.py loaddata recipe.json
python manage.py loaddata ingredients.json
python manage.py loaddata permissions.json
python manage.py loaddata groups.json
python manage.py loaddata users.json


exec "$@"