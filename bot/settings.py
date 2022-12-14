"""
Django settings for bot project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-m-bt*s#vh9(54c%w%z7%%7&ueb4anfy_^%em29lgsfw=h_b273')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ


ALLOWED_HOSTS = [
    # 'line-bot-python-foodie.onrender.com'
]
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'foodlinebot.apps.FoodlinebotConfig',
    'triplinebot.apps.TriplinebotConfig',
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

ROOT_URLCONF = 'bot.urls'

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

WSGI_APPLICATION = 'bot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'Trip',
    #     'USER': 'postgres',
    #     'PASSWORD': '1',
    #     'HOST': 'localhost',
    #     'PORT': '5432'
    # }
    'default': dj_database_url.config(
        default='postgresql://postgres:postgres@localhost:5432/foodbot',
        conn_max_age=600
    )
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# access line channel

# foodlinebot
LINE_CHANNEL_FOOD_ACCESS_TOKEN = '37yjxW6FseHGQIRf46wR0QaY4aL0RNlO6qlP/mK28JHT77wOwxwcSTvgfDtEGPKDmbJ7DF4mzenryCsNCSu374quABh53ltt2Z8QXtyeSMrUCMLGleN9tdTL3tzWjJT+bvuerQWUUNIqkLFO7QREwQdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_FOOD_SECRET = 'aec3c95c144d3983aebd63c0f4034c0c'

# triplinebot
LINE_CHANNEL_TRIP_ACCESS_TOKEN = '66VHFpXy1ZpFFIc8fDsV5m7BjTisF85paPolkdlfWdAYESSsxeqRV8sKuT1TYBzUNjVeECWMRo/+e0Ph0lK26uAH+4kFp+pmuHRzyawzYCZKf4S+jltU8ZMTYeSjzZ05niwinDZ1iMXGir4jg0WEywdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_TRIP_SECRET = '7c3076f0a3134549258e64de3b6b53d7'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')