#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='rh',
    version='1.0',
    description='RapidPro for Health Website',
    long_description='',
    author='Nicolas Lara',
    author_email='nicolas@lincolnloop.com',
    url='https://github.com/rapidpro/rh/',
    packages=find_packages(),
    scripts=[
        'scripts/manage.py'
    ],
    include_package_data=True,
)
