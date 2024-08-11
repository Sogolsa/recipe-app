from .base import *

import dj_database_url


SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "recipe-app-79zp.onrender.com", "heroku.com"]


# Database

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "recipes" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
