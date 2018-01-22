#!/usr/bin/env python
import os
import sys
import importlib

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rapidpro_for_health.settings.local")
    settings = os.environ['DJANGO_SETTINGS_MODULE']
    try:
        importlib.import_module(settings)
    except ImportError as e:
        sys.stderr.write('''
    Error: {e}
           Can't import `{settings}` module.
    The settings file is missing or the file has syntax errors. Check the file
    or create a `local.py` file in `rapidpro_for_health/settings/` using the example file aside.
            '''.format(e=str(e), settings=settings))
        sys.exit()

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
