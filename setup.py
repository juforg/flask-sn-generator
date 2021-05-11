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
    version='0.1.1',
    description="generate global unique increased serial number",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    author="juforg",
    author_email='juforg@gmail.com',
    url='https://github.com/juforg/flask-sn-generator',
    # packages=[
    #     'flask_sn_generator',
    # ],
    py_modules=[
        'flask_sn_generator'
    ],
    # package_dir={'flask_sn_generator':
    #              'flask_sn_generator'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='flask_sn_generator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Environment :: Plugins',
        'Framework :: Flask',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
    ],
    test_suite='tests',
    tests_require=test_requirements
)
