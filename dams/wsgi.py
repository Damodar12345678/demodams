"""
WSGI config for dams project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

from dams import WSGIAPP

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dams.settings')

application = MyWSGIApp
application = WhiteNoise(application, root="/path/to/static/files")
application.add_files("/path/to/more/static/files", prefix="more-files/")
#application = get_wsgi_application()

#app=application
