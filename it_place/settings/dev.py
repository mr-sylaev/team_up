from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# CACHES = {
#     "default": {
#         "BACKEND": 'redis_cache.RedisCache',
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# BROKER_URL = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
