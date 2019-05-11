# Django settings for tna.
import os
import socket

import re
import subprocess

FRONT_END_URL = 'http://127.0.0.1:4200/'
BACK_END_URL = 'http://127.0.0.1:8000/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_DIR = os.path.dirname(BASE_DIR)

if "127.0.0.1" not in FRONT_END_URL:
    DEBUG = False
    ALLOWED_HOSTS = ['.firebaseapp.com', 'www.turkunepal.fi', 'turkunepal.fi', '137.74.168.114', '.turkunepal.fi', ]
else:
    DEBUG = True
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", ]

TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Helsinki'

USE_I18N = True

USE_L10N = False

CORS_ORIGIN_ALLOW_ALL = True

COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)

ROOT_URLCONF = 'tna.urls'

WSGI_APPLICATION = 'wsgi.application'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'v2x^#lrv$(xp3ost97tbr4wvodd6l6obm_f3s%a^6pdmpxhw=g'

JWT_SECRET_KEY = 'turkunepal358'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    'sorl.thumbnail',
    'autofixture',
    'django_cron',
    'tnaapp',
    'authentication',
    'rest_framework',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tna.db'),
    }
}

CRON_CLASSES = [
    "tnaapp.cronjob.ValidateEvent",
]

DATE_FORMAT = "Y-m-d"

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (STATIC_PATH,)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FIXTURE_DIRS = ('fixtures',)
FILE_UPLOAD_PERMISSIONS = 0644

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if "127.0.0.1" not in FRONT_END_URL:
    FRONT_END_URL = 'https://turkunepal.fi/'
    #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'turkunepal@gmail.com'
EMAIL_HOST_PASSWORD = "TurkuNepal2015"
DEFAULT_EMAIL_FROM = 'turkunepal@gmail.com'
