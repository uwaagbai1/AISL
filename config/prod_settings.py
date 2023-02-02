import os
import environ
from pathlib import Path

from django.contrib.messages import constants as messages

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'm)=8ny_3(evz1tgg5ja*(qdlqll#2q!rw4f%xpkf_2rq)$)f2%'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
    'django_extensions',
    'django_summernote',
    'taggit',
]

SITE_ID=1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rehoboth_school',
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'

SUMMERNOTE_THEME = 'bs4'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GOOGLE_RECAPTCHA_SITE_KEY = '6Lc3WAQkAAAAAHr91nsfl27Ctm6f7ClxPbppI033'
GOOGLE_RECAPTCHA_SECRET_KEY = '6Lc3WAQkAAAAAAa1oGhPNVFQyRs4vBHIFHz-Uyb_'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# HTTPS settings
SECURE_PROXY_SSL_HOSTS = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000 #1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'danger',
}