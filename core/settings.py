from pathlib import Path
from decouple import config, Csv
import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env manually
load_dotenv(BASE_DIR / ".env")


# Security settings (Load from `.env`)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# Allowed Hosts (Load from `.env`)
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    "joystick-journalist-3eda94de87b5.herokuapp.com",
    "kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net",
    "8000-kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net",
]


# CSRF Trusted Origins (For Heroku & GitPod)
CSRF_TRUSTED_ORIGINS = [
    "https://127.0.0.1",
    "https://localhost",
    "https://joystick-journalist-3eda94de87b5.herokuapp.com",
    "https://kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net",
    "https://8000-kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net"
]


# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Static files support for Heroku
    'reviews',  # Your custom app
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Root URL configuration
ROOT_URLCONF = 'core.urls'


# Templates
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


# WSGI Application (Required for Deployment)
WSGI_APPLICATION = 'core.wsgi.application'


# Database (PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=900,  # Keep database connection alive
        ssl_require=True   # Force SSL for Heroku & secure connections
    )
}



# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        )
    },
]



# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static Files (Configured for Heroku & Whitenoise)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = (
    'whitenoise.storage.CompressedManifestStaticFilesStorage'
)


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
