from pathlib import Path
import os
from decouple import AutoConfig
import dj_database_url

# === Project Paths ===
BASE_DIR = Path(__file__).resolve().parent.parent
config = AutoConfig(BASE_DIR)

# === Security ===
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
IS_HEROKU = "DYNO" in os.environ

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    "joystick-journalist-3eda94de87b5.herokuapp.com",
    "kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net",
    "8000-kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net",
]

CSRF_TRUSTED_ORIGINS = [
    "https://127.0.0.1",
    "https://127.0.0.1:8000",
    "https://localhost:8000",
    "https://joystick-journalist-3eda94de87b5.herokuapp.com",
    "https://kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net",
    "https://8000-kc85-joystickjournali-po74vp49ye6.ws.codeinstitute-ide.net"
]

# === HTTPS Security (Heroku Only) ===
SECURE_SSL_REDIRECT = IS_HEROKU
SESSION_COOKIE_SECURE = IS_HEROKU
CSRF_COOKIE_SECURE = IS_HEROKU
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
DEBUG_PROPAGATE_EXCEPTIONS = False

# === Installed Apps ===
INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',  # 🔐 Required for allauth
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Auth & 2FA
    'allauth',
    'allauth.account',
    'allauth_2fa',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',

    # Brute Force Protection
    'axes',

    # Utilities
    'django_extensions',
    'whitenoise.runserver_nostatic',

    # Custom Apps
    'reviews',
    'widget_tweaks',
]

SITE_ID = 1

# === Authentication Backends ===
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',  # Protects from brute-force attacks
    'django.contrib.auth.backends.ModelBackend',  # Default Django backend
]

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'reviews.login_middleware.LoginRequiredMiddleware',
]

# === Templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === Root & WSGI ===
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

# === Database ===
DATABASE_URL = config('DATABASE_URL', default=None)
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is missing.")
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=900, ssl_require=True)
}

# === Password Validators ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === i18n & Timezone ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# === Static Files ===
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# === Default PK ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === Login/Logout Redirects ===
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# === Allauth Settings ===
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# === Email ===
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.yahoo.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_yahoo_email@yahoo.com'
EMAIL_HOST_PASSWORD = 'your_yahoo_app_password'
DEFAULT_FROM_EMAIL = 'your_yahoo_email@yahoo.com'

# === Axes (Brute Force Protection) ===
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = 'reviews/lockout.html'
AXES_RESET_ON_SUCCESS = True

# === Logging (Production) ===
if not DEBUG:
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
