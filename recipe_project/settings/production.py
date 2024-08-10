from .base import *
from decouple import config
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database

# DATABASES = {
#     "default": dj_database_url.config(default=config("DATABASE_URL"), conn_max_age=600),
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "recipesDB",
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": config("HOST"),
        "PORT": "5432",
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "recipes" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
