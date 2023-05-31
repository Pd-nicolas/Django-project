"""
WSGI config for restaurante project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler

settings.DEBUG = False


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurante.settings')

application = get_wsgi_application()
