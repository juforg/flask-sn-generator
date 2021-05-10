#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Flask Serial Number Generator
-------------

Flask extension for generating serial number.
"""
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'flask',
    'flask-redis>=0.4.0',
    # TODO: put package requirements here
]

test_requirements = [
    'pytest',

    # TODO: put package test requirements here
]

setup(
    name='flask_sn_generator',
    version='0.1.0',
    description="generate global unique increased serial number",
    long_description=readme + '\n\n' + history,
    author="juforg",
    author_email='juforg@gmail.com',
    url='https://github.com/juforg/flask_sn_generator',
    packages=[
        'flask_sn_generator',
    ],
    package_dir={'flask_sn_generator':
                 'flask_sn_generator'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_sn_generator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
