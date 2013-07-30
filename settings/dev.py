"""
settings for development mode
"""
#from django.conf.global_settings import STATICFILES_FINDERS
from common import *

DATA_DIR = os.path.join(PROJECT_DIR, 'data')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'urls.project.dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(DATA_DIR, 'teracy.db'), # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6a$a#-i&rfv^*vtjm2e38r#v)w!0&=av^)g7ifwoi!uor2kr4c'

#TODO enable this?
#
#STATICFILES_FINDERS += (
#    'compressor.finders.CompressorFinder',
#)

INSTALLED_APPS += (
    'django.contrib.admin',
    'debug_toolbar',
)
