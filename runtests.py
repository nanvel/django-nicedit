import sys

from django.conf import settings


def main():
    settings.configure(
        INSTALLED_APPS=(
            'nicedit',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        SITE_ID=1,
    )

    from django.test.simple import DjangoTestSuiteRunner

    test_runner = DjangoTestSuiteRunner(verbosity=1)
    failures = test_runner.run_tests(['nicedit',])
    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    main()
