#!/usr/bin/env sh

# Runs the Python Testsuite. Usage:
#
#   ./scripts/runtests.sh

source `dirname "$0"`/tests_env.sh

pipenv run coverage run scripts/manage.py test -v3 ${1:-rapidpro_for_health.tests}
pipenv run coverage html
pipenv run coverage report
echo "\nCoverage report is located in: /tmp/coverage_reports/rapidpro_for_health/index.html\n"
