from .base import *

ALLOWED_HOSTS = ['*']

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static/',
]