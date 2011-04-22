#!/usr/bin/env python
import sys

from os.path import abspath, dirname, join

from django.conf import settings
from django.core.management import setup_environ, execute_from_command_line
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))

try:
    import settings as settings_mod # Assumed to be in the same directory.
except ImportError, e:
    sys.stderr.write("Error importing module 'settings.py': %r \n" % str(e))
    sys.exit(1)

# setup the environment before we start accessing things in the settings.
setup_environ(settings_mod)

sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

if __name__ == "__main__":
    execute_from_command_line()
