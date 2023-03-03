#!/bin/sh


echo -e "\033[32mDJANGO_SERVICE: App Task Tree Menu\033[0m"
python manage.py collectstatic --no-input
python manage.py migrate

if [ "$DEBUG" == "True" ]; then
  python manage.py runserver 0.0.0.0:"$PORT"
else
  exec "$@"
fi