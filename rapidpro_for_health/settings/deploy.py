import dj_database_url
from .base import *  # pylint: disable=W0614,W0401

DEBUG = os.environ.get('DEBUG', 'False').lower() != 'false'

SITE_ID = int(os.environ.get('SITE_ID', 1))

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {'default': dj_database_url.config()}

if 'USE_HTTP' in os.environ:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    HTTPS_LINKS = False

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'client', 'dist'),
    os.path.join(VAR_ROOT),
]

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', MEDIA_ROOT)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
