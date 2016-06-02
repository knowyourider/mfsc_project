"""
Production Django settings for impression project.
"""
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mfscdb',
        'USER': 'mfscdb_user',
        'PASSWORD': 'eco$523',
        'HOST': 'postgres11311-env-6285052.dal.jelastic.vps-host.net',
        'PORT': '5432',
    }
}

#STATIC_ROOT = os.path.join(DATA_DIR, 'ROOT', 'static')
# dirname(file) get parent dir
STATIC_ROOT = os.path.join(dirname(dirname(BASE_DIR)), 'static')
