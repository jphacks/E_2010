rm -rf "$1"/migrations/*
touch "$1"/migrations/__init__.py

python manage.py makemigrations
python manage.py migrate
