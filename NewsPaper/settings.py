"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os.path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3*8rq*y)*ldyh^++23b=##%2a5=9n*1br)-j4yokh6l8@@+2=#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_apscheduler',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'news',
    'sign',
    'protect',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (BASE_DIR / 'static',
                    )

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

APSCHEDULER_RUN_NOW_TIMEOUT = 25

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

load_dotenv()
env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_FORMS = {'signup': 'sign.forms.BasicSignUpForm'}

# E-Mail Service Yandex
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
SERVER_EMAIL = os.getenv('SERVER_EMAIL')
EMAIL_USE_SSL = True

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = [
    ('ADMINS', EMAIL_HOST_USER)
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'WARNING': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(message)s'
        },
        'INFO': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(message)s'
        },
        'ERROR': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(message)s'
        },
        'GENERAL': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        }, 

        'ERROR_FILE': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        }, 

        'MAIL': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },        

    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
         'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },

    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'console': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'WARNING',
        },
        'console': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'ERROR',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'MAIL',
        },
        'file_general': {
        'class': 'logging.FileHandler',
        'level': 'INFO',
        'formatter': 'GENERAL',
        'filename': 'general.log ',
        },
        'file_error': {
        'class': 'logging.FileHandler',
        'level': 'ERROR',
        'formatter': 'ERROR_FILE',
        'filename': 'errors.log ',
        },
        'security': {
        'class': 'logging.FileHandler',
        'formatter': 'GENERAL',
        'filename': 'security.log ',}
    },
    'loggers': {
        'django': {
            'handlers': ['console','file_general'],
            'propagate': True,
            'exc_info' : True,
            'filters': ['require_debug_true']
        },
        'django.request': {
            'handlers': ['console','file_error','mail_admins'],
            'level': 'ERROR',
            'propagate': False,
            'filters': ['require_debug_false']
        },
        'django.server': {
            'handlers': ['console','file_error','mail_admins'],
            'level': 'ERROR',
            'propagate': False,
            'filters': ['require_debug_false']
        },
        'django.template': {
            'handlers': ['console','file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.django.db_backends': {
            'handlers': ['console','file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security'],
            'propagate': False,
        }
    }
}