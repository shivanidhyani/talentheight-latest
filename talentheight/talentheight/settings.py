
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'px+*$^ubd&izfe-er7&ejfl%atzv9%@84-_!fk@@dx_xde$%ud'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition
#Added by jiya

INSTALLED_APPS = [
    #default_app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 

    #third_party_app
    'social_django',
    's3direct', 

    #local_app
    'web.apps.WebConfig', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Added by jiya
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

#Added by jiya
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2'
    
)

ROOT_URLCONF = 'talentheight.urls'

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

                #added by jiya
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect', 
            ],
        },
    },
]

WSGI_APPLICATION = 'talentheight.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


AWS_ACCESS_KEY_ID = 'AKIAQAVJJC47RLK7Z5XD'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'talenttom'
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_ENDPOINT_URL = 'https://talentom.s3.ap-south-1.amazonaws.com'

S3DIRECT_DESTINATIONS = {
    'primary_destination': {
        'key': 'uploads/',
        'allowed': ['image/jpg', 'image/jpeg', 'image/png', 'video/mp4'],
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

#Added by jiya
LOGIN_REDIRECT_URL = 'dashboard'

SOCIAL_AUTH_FACEBOOK_KEY = '297416638621088' 
SOCIAL_AUTH_FACEBOOK_SECRET = '7824a666d3d379005b88ff8ee9d5faab'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '712617305715-t82fp7ltume37kee407bm9j7j1eqmkop.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'c1TO4hyZ4m03rjz-41DjzlV-'

