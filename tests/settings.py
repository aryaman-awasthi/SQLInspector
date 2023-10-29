SECRET_KEY = "IIEUE&^%^&**85"
ROOT_URLCONF = ""
INSTALLED_APPS = [
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "test_app",
]

MIDDLEWARE = (
      "django.middleware.common.CommonMiddleware",
      "sql-inspector.middleware.querychecker_middleware"
)

DATABASES = {
      "default": {
            "ENGINE": "django.db.backends.sqlite3",
      }
}

USE_TZ = False