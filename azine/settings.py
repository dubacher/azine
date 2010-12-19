# Django settings for azine project.
import socket, os
DEV = socket.gethostname() in ('sam-imac.local', 'sam-macbookpro.local', 'your-host-here')

DEBUG = DEV
TEMPLATE_DEBUG = DEBUG
gettext = lambda s: s

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'azine'             # Or path to database file if using sqlite3.
DATABASE_USER = 'root'             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


LANGUAGES = (
    ('en', gettext('English')),
    ('de', gettext('Deutsch')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_%hz7+t#x4(!savar%!nbpgdi6r*4_lhsfq_5e7o@ctmlxg1r^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'azine_main.middleware.redirect.UrlRedirectMiddleware',

    'cms.middleware.page.CurrentPageMiddleware', 
    'cms.middleware.user.CurrentUserMiddleware', 
    #'cms.middleware.toolbar.ToolbarMiddleware', 
    'cms.middleware.media.PlaceholderMediaMiddleware',

    #'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'azine.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'azine_main/templates'),
    os.path.join(PROJECT_PATH, 'persistent_messages/templates'),
    os.path.join(PROJECT_PATH, 'user_profiles/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    'south',

    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'mptt',
    'publisher',
    'menus',

    'cms_columns',
    'persistent_messages',
    'user_profiles',
    'azine_main',

)

CMS_TEMPLATES = (
    ('html/base.html', gettext('default')),
)

CMS_PLUGIN_PROCESSORS = (
    'cms_columns.cms_plugin_processors.columns',
)
LOGIN_REDIRECT_URL = (
    '/'
)

LOGIN_URL = (
    '/user/login/'
)

AUTH_PROFILE_MODULE = 'azine_main.UserProfile'

USER_PROFILES_SIGNUP_FORM = 'azine_main.forms.SignupForm'
USER_PROFILES_AUTHENTICATION_FORM = 'azine_main.forms.AuthenticationForm'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# UrlRedirectMiddleware

URL_REDIRECTS = (
    (r'^azine\.me/(.*)$', 'http://www.azine.me/\1'),
    (r'^(www\.)?azine\.ch/(.*)$', 'http://www.azine.me/\1'),
)

MESSAGE_STORAGE = 'persistent_messages.storage.PersistentMessageStorage'

AUTHENTICATION_BACKENDS = (
    'azine_main.auth.EmailAsUsernameModelBackend',
)

USER_PROFILES_URL_FIELD = 'userprofile__hash'