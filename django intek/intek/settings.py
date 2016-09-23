"""
Django settings for intek project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MY_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['intek-service.ru', 'www.intek-service.ru']


# Application definition

INSTALLED_APPS = (
	'grappelli',
	'filebrowser',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'main',
	'django.contrib.sitemaps',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'intek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'intek.wsgi.application'

#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
#)
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'intek',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': os.environ['MY_DB_PASS'],                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = '/opt/myenv/intek/static/static_root/'
STATIC_URL = '/static/static_root/'

MEDIA_ROOT = '/opt/myenv/intek/static/media_root/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/static/media_root/'

TEMPLATE_DIRS = (
    '/opt/myenv/intek/intek/main/templates/main/',
    # Put strings here, like "/home/html/django_templates" or
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.ss
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'intekservice.perm@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['MY_EMAIL_PASS'] 
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT 
FILEBROWSER_MEDIA_URL = MEDIA_URL 
FILEBROWSER_STATIC_ROOT = STATIC_ROOT 
FILEBROWSER_STATIC_URL = STATIC_URL 
URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/' 
PATH_FILEBROWSER_MEDIA = STATIC_ROOT + 'filebrowser/'