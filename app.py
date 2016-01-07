import sys
import os
from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY="very_secret",
    ROOT_URLCONF="main.urls",
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        "django.contrib.staticfiles",
        "main",
    ),
    TEMPLATES=(
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
        },
    ),
    STATIC_URL="/static/",
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, "content"),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
