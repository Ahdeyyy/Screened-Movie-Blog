"""
Django settings for screened_movie_blog project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    "django_summernote",
    "taggit",
    'blog',
    'user',
]

AUTH_USER_MODEL = "user.CustomUser"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'screened_movie_blog.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
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

WSGI_APPLICATION = 'screened_movie_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': env("DB_USER"),
    'USER': env("DB_USER"),
    'PASSWORD': env("DB_PASSWORD"),
    'HOST': env("DB_HOST"),
    'PORT': 5432
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = "blog:home"
LOGIN_URL = "user:login"
LOGOUT_URL = "user:logout"
LOGOUT_REDIRECT_URL = "blog:home"

# Email settings

# EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
# ANYMAIL = {
#         "MAILJET_API_KEY": os.getenv('MAILJET_API_KEY'),
#         "MAILJET_SECRET_KEY": os.getenv('MAILJET_API_SECRET'),
#     }
# DEFAULT_FROM_EMAIL = 'screenedmovieblog@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'screenedmovieblog@gmail.com'
EMAIL_HOST_PASSWORD = 'bujtvebmfcdfuvsn'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

X_FRAME_OPTIONS = "SAMEORIGIN"


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Summernote settings
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    "iframe": True,
    # You can put custom Summernote settings
    "summernote": {
        # As an example, using Summernote Air-mode
        "airMode": False,
        # Change editor size
        "width": "100%",
        "height": "980",
        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "clear"]],
            ["fontname", ["fontname"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["table", ["table"]],
            ["insert", ["link", "picture", "video"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
        # Or, explicitly set language/locale for editor
        "lang": "en-US",
        "codemirror": {
            "mode": "htmlmixed",
            "lineNumbers": "true",
        },
    },
    # Require users to be authenticated for uploading attachments.
    "attachment_require_authentication": True,
    # You can completely disable the attachment feature.
    "disable_attachment": False,
    # Set to `True` to return attachment paths in absolute URIs.
    "attachment_absolute_uri": False,
    # Lazy initialization
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    "lazy": True,
}
