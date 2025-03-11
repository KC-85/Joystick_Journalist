from pathlib import Path
from decouple import AutoConfig, Csv
import dj_database_url
# from dotenv import load_dotenv

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent
config = AutoConfig(BASE_DIR)

# Load .env manually
# load_dotenv(BASE_DIR / ".env")


# Security settings (Load from `.env`)
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

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

# Site Security Hardening
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
DEBUG_PROPOGATE_EXCEPTIONS =False

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'whitenoise.runserver_nostatic',  # Static files support for Heroku
    'axes',  # Protects against Brute-Force attacks
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
    'axes.middleware.AxesMiddleware',  # Protects login attempts
    'reviews.login_middleware.LoginRequiredMiddleware',
]

# ✅ AXES: Brute-Force Protection Settings
AXES_ENABLED = True  # Ensures django-axes is active
AXES_FAILURE_LIMIT = 5  # Allow only 5 failed attempts before locking out
AXES_COOLOFF_TIME = 1  # Lock out for 1 hour (set in hours)
AXES_LOCKOUT_TEMPLATE = 'reviews/lockout.html'  # Custom lockout page

# ✅ Automatically unlock after cooldown time (optional)
AXES_RESET_ON_SUCCESS = True

# ✅ New Authentication Backend for Axes
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # Required for Axes brute-force protection
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication
]

# Root URL configuration
ROOT_URLCONF = 'core.urls'


# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ Ensure Django looks in the "templates" directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # ✅ This must be present!
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI Application (Required for Deployment)
WSGI_APPLICATION = 'core.wsgi.application'

# Yahoo SMTP Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_yahoo_email@yahoo.com'  # Replace with your Yahoo email
EMAIL_HOST_PASSWORD = 'your_yahoo_app_password'  # Use an app-specific password
DEFAULT_FROM_EMAIL = 'your_yahoo_email@yahoo.com'

# Database (PostgreSQL)
DATABASE_URL = config('DATABASE_URL', default=None)

if not DATABASE_URL:
    raise ValueError("❌ ERROR: DATABASE_URL is missing. PostgreSQL is required!")

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=900, ssl_require=True)
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
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12  # ✅ Sets minimum password length to 12
        }
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
    }
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


# Ensure absolute paths for redirects
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


import logging

if not DEBUG:  # Only log errors in production
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": BASE_DIR / "django_error.log",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "ERROR",
                "propagate": True,
            },
        },
    }
