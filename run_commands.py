# run_commands.py
import os

# Run migrations
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py runserver')