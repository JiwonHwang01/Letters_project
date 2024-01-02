from .base import *

ALLOWED_HOSTS = ['43.201.2.126']

STATICFILES_DIRS = [
    # 경로 추가, 필요에 따라 더 추가
    os.path.join(BASE_DIR, 'static'),
]

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles/'