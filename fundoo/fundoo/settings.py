import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q484cut7o3)27rt(1qfke15g+dhy-i*cwj194ryfjxk3g)+2gu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# AUTH_USER_MODEL = "fundooapp.user"

ALLOWED_HOSTS = ['*']


# Email verification
EMAIL_USE_TLS = True            # Email Tools true
EMAIL_HOST = 'smtp.gmail.com'   # SMTP protocol for mail transfer
EMAIL_HOST_USER = 'abc@gmail.com'   # email to be send from user
EMAIL_HOST_PASSWORD = 'jskdnsndask'                   # password
EMAIL_PORT = 587                                       # default email port
DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'  # subject for email


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# django sample app
# django.core.mail.backends.smtp.EmailBackend
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'rest_auth',
    'fundooapp',
    'channels',
    'chat',
    'rest_framework.authentication',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fundoo.urls'

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

WSGI_APPLICATION = 'fundoo.wsgi.application'
# Channels
ASGI_APPLICATION = 'fundoo.routing.application'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'user',
        'PASSWORD': 'dsfdsfbdspfus',
        'HOST': 'endpoint.google.com',
        'PORT': '1234',
    }
}
#sagar kadam
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# LOGIN_REDIRECT_URL = 'sign_in'
# LOGOUT_REDIRECT_URL = 'logout'
CSRF_COOKIE_SECURE = False
