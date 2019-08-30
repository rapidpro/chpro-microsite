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
    entry_points={
        "console_scripts": ["manage.py = rh.__main__:manage"],
    },
    include_package_data=True,
)
