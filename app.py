import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="very_secret",
    ROOT_URLCONF="site.urls",
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        "django.contrib.staticfiles",
        "site"
    ),
    TEMPLATES=(
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True
        },
    ),
    STATIC_URL="/static/"
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
