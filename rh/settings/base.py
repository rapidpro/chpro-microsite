"""Base settings shared by all environments"""

# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *  # pylint: disable=W0614,W0401

# ==============================================================================
# Calculation of directories relative to the project module location
# ==============================================================================

import os
import sys
import rh as project_module

# Set a specific folder containing the 'var' directory where static and media
# files are uploaded later.
VAR_ROOT = os.environ.get('VAR_ROOT', None)
PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

# Otherwise try to create a /var folder inside the current, active virtualenv.
# All this code is just to determine the venv path.
if not VAR_ROOT:
    PYTHON_BIN = os.path.dirname(sys.executable)
    ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))

    # Assume that the presence of 'activate_this.py' in the python bin/
    # directory means that we're running in a virtual environment.
    if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
        # We're running with a virtualenv python executable.
        VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
    elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
                                                 'activate_this.py')):
        # We're running in [virtualenv_root]/src/[project_name].
        VAR_ROOT = os.path.join(ve_path, 'var')
    else:
        # Set the variable root to a path in the project which is
        # ignored by the repository.
        VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

# ==============================================================================
# Generic Django project settings
# ==============================================================================

DEBUG = False

WSGI_APPLICATION = 'rh.wsgi.application'

# Treat all incoming requests as SSL, redirect if necessary.
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Render all internal links with HTTPS. Can be turned of e.g. for
# local runserver or testserver, which doesn't support SSL.
HTTPS_LINKS = True

# Add security headers. Also apply to upstream proxy.
SECURE_HSTS_SECONDS = 31536000
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
PUBLIC_KEY_PINS = ('base64==',)

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'djangocms_admin_style',  # Needed by Django CMS before the admin
    'django.contrib.admin',
    'django.contrib.redirects',

    # Django CMS
    'cms',
    'menus',
    'treebeard',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'django_countries',

    # Plugins
    'djangocms_text_ckeditor',
    'djangocms_link',
    'cmsplugin_filer_image',

    # Third-Party
    'django_select2',
    'storages',

    # RapidPro Health
    'rh.apps.meta',
    'rh.apps.content',
    'rh.apps.icons',
    'rh.apps.case_studies',
    'rh.apps.steps',
]

MIDDLEWARE = [
    # Security
    'django.middleware.security.SecurityMiddleware',

    # Django
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # required by Django CMS
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',

    # Django CMS
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    'rh.middleware.BetterCurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
]

ROOT_URLCONF = 'rh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Django CMS
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

MANAGERS = [
    ('Join', 'join@rapidpro.io'),
]

# ==============================================================================
# Django CMS
# ==============================================================================
CMS_TEMPLATES = [
    ('base.html', 'Generic Template'),
    ('subpage.html', 'Subpage Template'),
    ('subpage_wsidebar.html', 'Subpage w/Sidebar Template'),
    ('simple.html', 'Simple Content Template'),
    ('simple_wsidebar.html', 'Simple Content w/Sidebar Template'),
]

CMS_PLACEHOLDER_CONF = {
}

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

DJANGOCMS_LINK_USE_SELECT2 = True

# ===============================2===============================================
# Project URLS and media settings
# ==============================================================================

ROOT_URLCONF = 'rh.urls'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'client', 'dist'),
    os.path.join(PROJECT_DIR, 'client', 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '.data', 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, '.data', 'uploads')
STATIC_CACHE_ROOT = os.path.join(VAR_ROOT, 'static_cache')

STATIC_URL = '/static/'

# ==============================================================================
# Miscellaneous project settings
# ==============================================================================
import logging.config

# LOGGING_CONFIG = None  # disables Django handling of logging
logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'simple': {'format': '%(levelname)s %(message)s', },
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',

        },
        # Uncomment this to add a Handler for Sentry for `warning` and above
        # 'sentry': {
        #     'level': 'WARNING',
        #     'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        # },
    },
    'loggers': {
        # Default logger defaults to ERROR
        '': {'level': 'WARNING', 'handlers': ['console']},

        # This application
        'rh': {'level': 'INFO', 'handlers': ['console'], 'propagate': False},

        # Common Django logger
        # 'django.requests': {'level': 'DEBUG', 'handlers': ['console']},
        # 'django.template': {'level': 'ERROR', 'handlers': ['console']},
        # 'django.db': {'level': 'WARNING', 'handlers': ['console']},

        # Disable `RemovedInDjango110Warning` warnings
        'py.warnings': {'level': 'ERROR', 'handlers': ['console']},

        'commands': {'level': 'INFO', 'handlers': ['console']},
    },
})

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# ==============================================================================
# Caching
# ==============================================================================
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': [os.environ.get('CACHE_URL', 'redis://localhost:6379/1')],
#         'OPTIONS': {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
#             "SOCKET_TIMEOUT": 5,  # in seconds
#             "MAX_CONNECTIONS": 1000,
#             "PICKLE_VERSION": -1,
#             "IGNORE_EXCEPTIONS": True,
#         },
#     },
# }

# ==============================================================================
# i18n and Locales
# ==============================================================================

TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True

# Automatically append a slash to each url, and redirect if necessary.
APPEND_SLASH = True

# To have a default /en/ prefix in front of all domains or not.
I18N_PREFIX_DEFAULT_LANGUAGE = False

LANGUAGE_CODE = 'en'

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
)
