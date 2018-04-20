#
# Test Specific settings.
#
import dj_database_url
from .base import *  # pylint: disable=W0614,W0401

sys.stdout.write('Using test settings in rh.settings.tests\n')

DEBUG = False
SITE_ID = 1
SECRET_KEY = os.environ.get('SECRET_KEY', 'not-a-secret-key')

# Don't use SSL within the tests
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
HTTPS_LINKS = False

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/rh')
}

# Static Export
STATIC_CACHE_ROOT = os.path.join(VAR_ROOT, 'static_cache_test')
STATIC_CACHE_PROTOCOL = 'http'

# Disable strong password hashing
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


INSTALLED_APPS += [
    'djangocms_testing',
]

# Disable Migrations if `DISABLE_MIGRATIONS=1` env variable is present
class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


DISABLE_MIGRATIONS = os.environ.get('DISABLE_MIGRATIONS', '0')
if DISABLE_MIGRATIONS == '1':
    sys.stdout.write('Django DB Migrations disabled!\n')
    MIGRATION_MODULES = DisableMigrations()
