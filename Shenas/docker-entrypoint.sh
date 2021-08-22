#!/usr/bin/env bash

cd /usr/shenas/
echo "Working directory is: $PWD"

python manage.py migrate --noinput
python manage.py collectstatic
if [ $? -ne 0 ]; then
    echo "Migration failed." >&2
    exit 1
fi

python manage.py runserver