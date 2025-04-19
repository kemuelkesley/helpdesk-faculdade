"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


# import dos temas e configurações
from .jazmmin import JAZZMIN_SETTINGS
from .tweaks import JAZZMIN_UI_TWEAKS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l0bg5x-wcl!11=*(j40pcz4#)-s7s%mj(!f5*1fog_g2(72-4s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Lembrar de o host correto 'helpdesk-libk.onrender.com'
# Se For testar local tirar o 'helpdesk-libk.onrender.com' e deixar apenas vazio []
ALLOWED_HOSTS = ['helpdesk-libk.onrender.com']


# Application definition

INSTALLED_APPS = [    
    'jazzmin',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helpdesk.apps.HelpdeskConfig',
    'cadastro.apps.CadastroConfig',
    'usuarios.apps.UsuariosConfig',
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

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'setup.wsgi.application'


# Database Rodar com SQLite Server
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Rodar com SQL Server da microsoft
# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'NAME': 'teste_django',
#         'USER': 'sa',
#         'PASSWORD': 'bandal',
#         'HOST': 'pc-gamer',
#         'PORT': '',

#         'OPTIONS': {
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }

# set this to False if you want to turn off pyodbc's connection pooling
#DATABASE_CONNECTION_POOLING = True



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'setup/static')
# ]


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

# Diretório onde o Django procura por arquivos estáticos durante o desenvolvimento
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static'),
]

# Diretório onde os arquivos estáticos serão coletados durante o deploy (necessário no render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')





# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_SETTINGS = {
    "site_icon": "favicon.ico",
}

# Import default Jazzmin settings
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS

JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

# Alterar o caminho de redirecionamento do logout
LOGOUT_REDIRECT_URL = 'login'