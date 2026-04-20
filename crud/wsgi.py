"""
WSGI config for crud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')

application = get_wsgi_application()


import os
from django.contrib.auth import get_user_model

# Get the User model
User = get_user_model()

# Check if the superuser already exists to avoid errors
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='piyush',
        email='admin@example.com',
        password='StrongPassword123'  
    )
    print("Superuser created successfully!")