"""
Django settings for game7api project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2!7#8u3*@k!a$)9z=g&y)*suxyb65pm_1a_31=ce6cn3)ljz@&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '192.168.1.104', '192.168.122.1', '192.168.1.106', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'corsheaders',
    'rest_framework',


    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'game7api.urls'

CORS_ORIGIN_ALLOW_ALL = True

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

WSGI_APPLICATION = 'game7api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        # MINHA CASA
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'game7api',
        'USER':'lovieira',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'5432'

        # # INPE
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'game7api',
        # 'USER':'lovieira',
        # 'PASSWORD':'28310189',
        # 'HOST':'localhost',
        # 'PORT':'5432'

        # NOTEBOOK RUIVA
		#  'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #  'NAME': 'manager36_v4',
        #  'USER':'postgres',
        #  'PASSWORD':'123456',
        #  'HOST':'localhost',
        #  'PORT':'5432'

        # HEROKU
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'dcpii3702fg0v7',
        # 'USER':'axgjcyllpmgrvc',
        # 'PASSWORD':'Sw8zsX3mvfUxWTP5s1Ae1Rnaqp',
        # 'HOST':'ec2-54-243-249-154.compute-1.amazonaws.com',
        # 'PORT':'5432'

        # HOME HOST
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'NAME': 'luk14236_game7',
        # 'USER':'luk14236',
        # 'PASSWORD':'28310189',
        # 'HOST':'177.85.98.245'
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(PROJECT_ROOT, 'media'),
    # os.path.join(PROJECT_ROOT, '../diretoria/static'),
    # os.path.join(PROJECT_ROOT, '../diretoria/static/angular'),
    # os.path.join(PROJECT_ROOT, '../diretoria/static/css'),
    # os.path.join(PROJECT_ROOT, '../diretoria/static/fonts'),
    # os.path.join(PROJECT_ROOT, '../diretoria/static/img'),
    # os.path.join(PROJECT_ROOT, '../diretoria/static/js'),
    # '/var/www/static/',
)