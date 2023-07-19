# run_commands.py
import os

# Run migrations
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')

# Load fixtures
os.system('python manage.py loaddata toppings.json')
os.system('python manage.py loaddata sauces.json')
os.system('python manage.py loaddata cheeses.json')
