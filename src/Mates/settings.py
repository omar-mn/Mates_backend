import os
# import dj_database_url
from pathlib import Path
from datetime import timedelta
from .envVariables import DATABASES_env , SECRET_KEY_env , CORS_ALLOWED_ORIGINS_env , CSRF_TRUSTED_ORIGINS_env , CORS_ALLOW_HEADERS_env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = SECRET_KEY_env

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'corsheaders',

    # apps
    'Rooms',
    'Users',
    'Messages',
    'channels',


    # dj-rest-auth
    'rest_framework',
    'rest_framework.authtoken', 
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'Mates.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'Mates.wsgi.application'

ASGI_APPLICATION = 'Mates.asgi.application'

# Database

DATABASES = DATABASES_env



#custom user model

AUTH_USER_MODEL = 'Users.account'


#SIMPLE JWT AUTH

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

#CORS

CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS_env

CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS_env


CORS_ALLOW_HEADERS = CORS_ALLOW_HEADERS_env

# AUTH

REST_AUTH = {
    'USER_DETAILS_SERIALIZER': 'Users.serializers.UserInfo',
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    'USER_DETAILS_SERIALIZER': 'Users.serializers.CustomUserDetailsSerializer',
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_AUTHENTICATION_METHOD = 'email'  
ACCOUNT_EMAIL_REQUIRED = True           
ACCOUNT_UNIQUE_EMAIL = True
SITE_ID = 2

# EMAIL


# CHANNELS

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR , 'media')

