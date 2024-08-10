from .base import *

import dj_database_url


SECRET_KEY = os.getenv("SECRET_KEY", default="default_secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
    ),
}

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "recipes" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
