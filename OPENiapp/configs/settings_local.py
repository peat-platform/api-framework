__author__ = 'mpetyx'


# Django settings for OPENiapp project.
import os

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# os.environ['HTTPS'] = "on"
# APPEND_SLASH = False

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

CLOUDLET_SERVER = "https://localhost/api/v1/cloudlets"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v*=yxp=ti5*71c*yq=50n6otga)9s1+la)fdasorkwoal392432403432f(05diuah$uwjr4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # "request.middleware.RequestMiddleware",
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'OPENiapp.urls'
TASTYPIE_SWAGGER_API_MODULE = 'OPENiapp.APIS.urls.api'
TASTYPIE_DEFAULT_FORMATS = ['json']

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'OPENiapp.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
# os.path.join(PROJECT_ROOT, "Objects/Photo/templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.amazon',
    # 'allauth.socialaccount.providers.angellist',
    # 'allauth.socialaccount.providers.bitbucket',
    # 'allauth.socialaccount.providers.bitly',
    'allauth.socialaccount.providers.dropbox',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.flickr',
    'allauth.socialaccount.providers.foursquare',
    # 'allauth.socialaccount.providers.feedly',
    # 'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.hubic',
    'allauth.socialaccount.providers.instagram',
    # 'allauth.socialaccount.providers.linkedin',
    # 'allauth.socialaccount.providers.linkedin_oauth2',
    # 'allauth.socialaccount.providers.openid',
    # 'allauth.socialaccount.providers.persona',
    # 'allauth.socialaccount.providers.soundcloud',
    # 'allauth.socialaccount.providers.stackexchange',
    # 'allauth.socialaccount.providers.tumblr',
    # 'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.vimeo',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.windowslive',
    # 'allauth.socialaccount.providers.xing',

    'OPENiapp',
    'OPENiapp.APIS',

    # Activity API
    'OPENiapp.APIS.Activity',
    'OPENiapp.APIS.Activity.Badge',
    'OPENiapp.APIS.Activity.Checkin',
    'OPENiapp.APIS.Activity.Event',
    'OPENiapp.APIS.Activity.Measurement',
    'OPENiapp.APIS.Activity.Note',
    'OPENiapp.APIS.Activity.Notebook',
    'OPENiapp.APIS.Activity.Nutrition',
    'OPENiapp.APIS.Activity.Question',
    'OPENiapp.APIS.Activity.Sleep',
    'OPENiapp.APIS.Activity.Status',
    'OPENiapp.APIS.Activity.Game',
    'OPENiapp.APIS.Activity.Workout',

    # Context API
    'OPENiapp.APIS.Context',

    # Location API implementation
    'OPENiapp.APIS.Location',
    'OPENiapp.APIS.Location.Place',
    'OPENiapp.APIS.Location.Route',
    'OPENiapp.APIS.Location.Travel',

    # Media API implementation
    'OPENiapp.APIS.Media',
    'OPENiapp.APIS.Media.Article',
    'OPENiapp.APIS.Media.Audio',
    'OPENiapp.APIS.Media.File',
    'OPENiapp.APIS.Media.Page',
    'OPENiapp.APIS.Media.Photo',
    'OPENiapp.APIS.Media.Playlist',
    'OPENiapp.APIS.Media.Video',

    # Product and Services API
    'OPENiapp.APIS.Products_and_Services',
    'OPENiapp.APIS.Products_and_Services.Card',
    'OPENiapp.APIS.Products_and_Services.Cart',
    'OPENiapp.APIS.Products_and_Services.Order',
    'OPENiapp.APIS.Products_and_Services.Product',
    'OPENiapp.APIS.Products_and_Services.Service',
    'OPENiapp.APIS.Products_and_Services.Shop',
    'OPENiapp.APIS.Products_and_Services.Wallet',

    # Profile API
    'OPENiapp.APIS.Profile',
    'OPENiapp.APIS.Profile.Account',
    'OPENiapp.APIS.Profile.Application',
    'OPENiapp.APIS.Profile.Group',
    'OPENiapp.APIS.Profile.User',

    # Secondary API
    'OPENiapp.APIS.Secondary',
    'OPENiapp.APIS.Secondary.Comment',
    'OPENiapp.APIS.Secondary.Delivery',
    'OPENiapp.APIS.Secondary.Dislike',
    'OPENiapp.APIS.Secondary.Favorite',
    'OPENiapp.APIS.Secondary.Friendship',
    'OPENiapp.APIS.Secondary.Invoice',
    'OPENiapp.APIS.Secondary.Like',
    'OPENiapp.APIS.Secondary.Offer',
    'OPENiapp.APIS.Secondary.Payment',
    'OPENiapp.APIS.Secondary.QuestionOption',
    'OPENiapp.APIS.Secondary.Refund',
    'OPENiapp.APIS.Secondary.Review',
    'OPENiapp.APIS.Secondary.RSVP',
    'OPENiapp.APIS.Secondary.Score',
    'OPENiapp.APIS.Secondary.Shipping',
    'OPENiapp.APIS.Secondary.Tag',

    # 'OPENiapp.cloudletClient',
    # 'cloudletClient.client'
    'cloudletClient',

    'tastypie',
    'tastypie_swagger',
    # 'south',
    #'request',
    'corsheaders',


)

# https://github.com/pennersr/django-allauth#when-i-sign-up-i-run-into-connectivity-errors-connection-refused-et-al
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'apiplatform.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
         {'SCOPE': ['email', 'publish_stream', 'user_photos', 'create_event'],
          #'SCOPE': ['public_profile', 'user_friends', 'email', 'user_about_me', 'user_activities', 'user_birthday', 'user_education_history', 'user_events', 'user_groups', 'user_hometown', 'user_interests', 'user_likes', 'user_location', 'user_photos', 'user_relationships', 'user_relationship_details', 'user_religion_politics', 'user_status', 'user_tagged_places', 'user_videos', 'user_website', 'user_work_history', 'read_friendlists', 'read_insights', 'read_mailbox', 'read_stream', 'create_event', 'manage_notifications', 'publish_actions', 'rsvp_event', 'publish_actions', 'user_actions.books', 'user_actions.fitness', 'user_actions.music', 'user_actions.news', 'user_actions.video', 'manage_pages', 'read_page_mailboxes'],
          'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
          'METHOD': 'oauth2'
         },
     'instagram':
        {'SCOPE': ['comments', 'relationships', 'likes'],
          'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
          'METHOD': 'oauth2'
        },
     'flickr':
        {'SCOPE': ['write', 'read', 'delete'],
          'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
          'METHOD': 'oauth'
        }
    }
