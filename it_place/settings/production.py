from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'it_place',
        'USER': 'it_place_user',
        'PASSWORD': 'sidfid',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@bytehouse.ru'
EMAIL_HOST_PASSWORD = 'eilgyvt4815162342'
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False
SERVER_EMAIL = EMAIL_HOST_USER
