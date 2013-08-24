import sys
import os

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
        ROOT_URLCONF='nicedit.urls',
        MEDIA_ROOT=os.path.join(os.path.dirname(__file__), 'app_media'),
        SITE_ID=1,
    )

    from django.test.simple import DjangoTestSuiteRunner

    test_runner = DjangoTestSuiteRunner(verbosity=1)
    failures = test_runner.run_tests(['nicedit',])
    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    main()
