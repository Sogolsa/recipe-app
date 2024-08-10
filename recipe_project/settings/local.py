from .base import *

# import dj_database_url
import environ


env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env("SECRET_KEY", default="default_secret_key")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
