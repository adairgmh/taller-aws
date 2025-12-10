from .base import *
import os

DEBUG = False

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("Falta DJANGO_SECRET_KEY en producción")

ALLOWED_HOSTS = [
    os.environ.get("SERVER_IP"), 
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    f"http://{os.environ.get('SERVER_IP')}",
    f"https://{os.environ.get('SERVER_IP')}",
]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 0

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}