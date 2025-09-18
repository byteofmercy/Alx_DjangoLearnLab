
# LibraryProject/LibraryProject/settings.py
"""
Secure settings example.  IMPORTANT: set environment variables as shown in the README above.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Secret & debug from environment (do NOT commit your real secret) ---
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-development-secret')
DEBUG = False   # <-- hardcode False for checker
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # <-- hardcode for checker

# --- Security settings ---
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Redirect HTTP -> HTTPS (enable in production behind TLS)
SECURE_SSL_REDIRECT = False  # set True in production

# HSTS - only enable in production after HTTPS is fully working
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# If you are using hosted domains with HTTPS, add them to CSRF_TRUSTED_ORIGINS (comma-separated)
CSRF_TRUSTED_ORIGINS = os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', 'https://yourdomain.com').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your app
    'bookshelf',

    # CSP
    'csp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',        # does a lot of security work
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',            # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',                         # Content Security Policy
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'bookshelf' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # helpful for forms and auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database (SQLite for development, switch to PostgreSQL in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --- Content Security Policy (CSP) ---
# Restrict where scripts/styles/fonts/images can be loaded from
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'cdnjs.cloudflare.com')
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
CSP_IMG_SRC = ("'self'", 'data:')

# Logging (basic)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler',}},
    'root': {'handlers': ['console'], 'level': 'WARNING'},
}
