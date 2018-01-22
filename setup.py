#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name='rapidpro_for_health',
    version='1.0',
    description='RapidPro for Health Website',
    long_description='',
    author='Nicolas Lara',
    author_email='nicolas@lincolnloop.com',
    url='https://github.com/rapidpro/rapidpro_for_health/',
    packages=find_packages(),
    scripts=[
        'scripts/manage.py'
    ],
    package_data={
        'rapidpro_for_health': ['templates/*.*'],
        'docs': ['*'],
        'client': ['*'],
    },
    include_package_data=True,
    install_requires=[
        # Requirements need to be installed separately using pip.
        # Refer the docs.
    ],
    extras_require={
        'tests': [
            'coverage',
            'djangocms_testing',
        ]
    },
    dependency_links=[
        'git+https://github.com/nicolaslara/djangocms_testing.git@master#egg=djangocms_testing',
    ]
)
