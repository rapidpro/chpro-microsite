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
    os.path.join(PROJECT_DIR, 'client', 'static'),
    os.path.join(VAR_ROOT),
]

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', MEDIA_ROOT)
if 'AWS_ACCESS_KEY_ID' in os.environ:
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # Amazon S3 settings.
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
    AWS_AUTO_CREATE_BUCKET = False
    AWS_HEADERS = {"Cache-Control": "public, max-age=86400"}
    AWS_S3_FILE_OVERWRITE = False
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_SECURE_URLS = True
    AWS_REDUCED_REDUNDANCY = False
    AWS_IS_GZIPPED = False

    MEDIA_ROOT = '/'
    MEDIA_URL = '//s3.amazonaws.com/%s/'.format(AWS_STORAGE_BUCKET_NAME)

if 'SENDGRID_API_KEY' in os.environ:
    SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']
    EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
