import sys
import os

from django import setup
from django.conf import settings


def main():
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'nicedit',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            },
        },
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware'
        ),
        ROOT_URLCONF='nicedit.urls',
        MEDIA_ROOT=os.path.join(os.path.dirname(__file__), 'app_media'),
        SITE_ID=1,
    )

    setup()

    from django.test.runner import DiscoverRunner

    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['nicedit',])
    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    main()
