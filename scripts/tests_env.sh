#!/usr/bin/env bash

# Set of env variables to run the testsuite.

# Disable migrations
export DISABLE_MIGRATIONS=1

# Python coverage test run
export DJANGO_SETTINGS_MODULE=rh.settings.tests

echo "Test ENV variables set. Ready to run the testsuite."
echo "DJANGO_SETTINGS_MODULE set to \"$DJANGO_SETTINGS_MODULE\""
echo "To manually run the testsuite, call it with:"
echo ""
echo "    scripts/manage.py test rh.tests -v3 --noinput"
echo ""
