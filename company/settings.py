# -*- coding: utf-8 -*-
import os.path
import posixpath
SITE_ID = 1

TIME_FORMAT="H:i"

DEFAULT_HTTP_PROTOCOL = "http"
SITE_URL = "localhost:8000"
SITE_NAME = "Bio-Tech"

SOUTH_TESTS_MIGRATE = False
DEBUG = True

TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

NOTIFICATION_LANGUAGE_MODULE = "account.Account"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                             # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
        "TEST_NAME": ":memory:",
    }
}

CONTACT_EMAIL = "office@biotech.at"

ADMINS = [
     ("Philipp Wassibauer", "philipp.wassibauer@gmail.com"),
]

MANAGERS = ADMINS

INTERNAL_IPS = [
    "127.0.0.1",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "3vs@$=9vk93(+p9##9iew_yl-&fq^9u+jp@#i(me$je5sx@1*)"

#PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
FIXTURE_DIRS = (os.path.join(PROJECT_ROOT, 'fixtures'),)
#CMS_ROOT = os.path.abspath(os.path.dirname(cms.__file__))

# tells Pinax to use the default theme
#PINAX_THEME = "default"

TEST_RUNNER = "django_nose.run_tests"

gettext = lambda s: s

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'biotechsender@gmail.com'
EMAIL_HOST_PASSWORD = 'bio*tech'
EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = "biotechsender@gmail.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#import logging
#import logging.handlers
#log_filename = os.path.join(PROJECT_ROOT, "logs", "biotech.log")
#logging.basicConfig(
#    level = logging.ERROR,
#    format = "%(asctime)s %(levelname)s: %(filename)s %(lineno)d %(message)s",
#    filemode = "w",
#    handler =  logging.handlers.RotatingFileHandler(log_filename, maxBytes=20, backupCount=5)
#)

TIME_ZONE = "Europe/Vienna"

LANGUAGE_CODE = "de"
LANGUAGES = (
    ("de", gettext("German")),
    ("en", gettext("English")),
)


USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = "/site_media/media/"

LOGIN_URL = "/"
ACCOUNT_USER_DISPLAY = lambda x: x.username

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"


CMS_MEDIA_ROOT = os.path.join(STATIC_ROOT, "cms/")
CMS_MEDIA_URL  = STATIC_URL + "cms/"
CMS_REDIRECTS = True
CMS_HIDE_UNTRANSLATED = False

CMS_TEMPLATES = (
        ("cms_base.html", gettext("default")),
)

# Additional directories which hold static files
from imp import find_module
STATICFILES_DIRS = (
    ('', os.path.join(PROJECT_ROOT, "media")),
    ('', os.path.join(os.path.abspath(find_module("cms")[1]), 'media')),
    #('', os.path.join(CMS_ROOT, "media")),
)

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL

AVATAR_STORAGE_DIR = "avatars"
AVATAR_DEFAULT_URL = "img/default/user_big.png"
AVATAR_GRAVATAR_BACKUP = False
AVATAR_MAX_SIZE = 1024 * 1024 * 5

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

#CACHE_BACKEND = 'locmem://'
#CACHE_BACKEND = 'db://cachetable'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#COMPRESS_CACHE_BACKEND = CACHE_BACKEND

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

TEMPLATE_TAGS = ( "uni_form.templatetags.uni_form_tags",
                  "django.templatetags.i18n",
                  "easy_thumbnails.templatetags.thumbnail",
                  "avatar.templatetags.avatar_tags",
)

DJANGO_BUILTIN_TAGS = (
    'native_tags.templatetags.native',
)

NATIVE_TAGS = (
    # Extra native contrib tags to test
    'native_tags.contrib.comparison',
    'native_tags.contrib.context',
    'native_tags.contrib.generic_content',
    'native_tags.contrib.generic_markup',
    'native_tags.contrib.hash',
    'native_tags.contrib.serializers',
    'native_tags.contrib.baseencode',
    'native_tags.contrib.regex',
    'native_tags.contrib.mapreduce',
    'native_tags.contrib.cal',
    'native_tags.contrib.math_',
    'native_tags.contrib.rand',
    #'native_tags.contrib.smart_if',

    # Native tags with dependencies
    'native_tags.contrib.gchart', # GChartWrapper
    'native_tags.contrib.pygmentize', # Pygments
    'native_tags.contrib.feeds', # Feedparser
)


AUTHENTICATION_BACKENDS = (
    "pinax.apps.account.auth_backends.EmailModelBackend",
    "django.contrib.auth.backends.ModelBackend",
)

AUTH_PROFILE_MODULE = "profiles.Profile"

MIDDLEWARE_CLASSES = [
    #"django.middleware.cache.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "cms.middleware.multilingual.MultilingualURLMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.doc.XViewMiddleware",

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    #"pinax.middleware.security.HideSensistiveFieldsMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
    #'pagination.middleware.PaginationMiddleware',
    #"django.middleware.cache.FetchFromCacheMiddleware",
    #"django.middleware.gzip.GZipMiddleware",
]

ROOT_URLCONF = "company.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    'cms.context_processors.media',
    # exports CONTACT_EMAIL, SITE_NAME, STATIC_URL
    #"pinax.core.context_processors.pinax_settings",
    #"pinax.apps.account.context_processors.account", # used in messages

    #"support.context_processors.ticket_count",
    #'notification.context_processors.notification',
]

SKIP_SOUTH_TESTS = True


AVATAR_CACHE_TIMEOUT = 60*60

INSTALLED_APPS = [

    # Django
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.comments",
    "django.contrib.staticfiles",

    # cms
    "cms",
    "cms.plugins.text",
    "cms.plugins.picture",
    "cms.plugins.link",
    "cms.plugins.file",
    "cms.plugins.snippet",
    "cms.plugins.googlemap",
    "mptt",
    "menus",
    "publisher",
    "reversion",

    # external
    #"ajax_validation",
    #"avatar",
    #"compressor",
    #"debug_toolbar",
    "django_extensions",
    "django_nose",
    "easy_thumbnails",
    "gunicorn",
    #"notification",
    
    "rosetta",
    'biotech',
]

DJANGO_MEMCACHED_REQUIRE_STAFF = True

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/%s/" % o.username,
}

ACCOUNT_EMAIL_AUTHENTICATION = True
ACCOUNT_REQUIRED_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = True
UNIQUE_EMAIL = True
EMAIL_CONFIRMATION_DAYS = 3
ACCOUNT_OPEN_SIGNUP = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = True



DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

try:
    from local_settings import *
except ImportError:
    pass


#if DEBUG:
#    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
