from .base import *

ALLOWED_HOSTS = ['223.130.134.73']

STATICFILES_DIRS = [
    # 경로 추가, 필요에 따라 더 추가
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles/'