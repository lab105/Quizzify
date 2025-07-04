"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

SECRET_KEY = str(os.getenv("SECRET_KEY"))

DEBUG = os.getenv("DEBUG", False)

# SECURITY WARNING: update this when you have the production host domain name
ALLOWED_HOSTS = [".example.com", "www.example.com"]
CORS_ALLOW_CREDENTIALS = (
    True  # If True, cookies will be allowed to be included in cross-site HTTP requests
)

## white list the client apps
CORS_ORIGIN_WHITELIST = (
    "http://localhost:8844",
    "http://localhost:8846",
    "http://localhost:8848",
    # Add the Client URLs here
    "https://quiz1.domain.com",
    "https://quiz2.domain.com",
    "https://quiz3.domain.com",
)

CORS_ORIGIN_ALLOW_ALL = (
    False  # If True, all origins will be allowed(Not recommended for production)
)

# Allow specific headers
CORS_ALLOW_HEADERS = [
    "content-type",
    "content-disposition",
    "content-length",
]

# Allow specific methods
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


INSTALLED_APPS = [
    "quiz.apps.QuizConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Security Settings
# Redirect all non-HTTPS traffic to HTTPS
if not DEBUG:
    SECURE_SSL_REDIRECT = True

    # Use secure session and CSRF cookies in production
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # Set the HttpOnly flag on the session cookie
    SESSION_COOKIE_HTTPONLY = True

    # Define the header that your load balancer or reverse proxy uses to indicate a secure connection
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # HTTP Strict Transport Security settings
    SECURE_HSTS_SECONDS = 31536000  # One year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Prevent client-side JavaScript from accessing the CSRF cookie
    CSRF_COOKIE_HTTPONLY = True

    CSRF_TRUSTED_ORIGINS = [
        # Add the Client URLs here
        "https://quiz1.domain.com",
        "https://quiz2.domain.com",
        "https://quiz3.domain.com",
    ]

    # Ensure your site will only be served over HTTPS and not embedded in a frame
    X_FRAME_OPTIONS = "DENY"
    # Additional headers for added security
    # SECURE_BROWSER_XSS_FILTER = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


MEDIA_URL = "/media/"
MEDIA_ROOT = "/www/app/media/"
STATIC_ROOT = "/www/app/staticfiles/"
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
