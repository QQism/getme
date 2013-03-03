#!/usr/bin/env python

import os
import sys

import crawy

try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

packages = ['getme',]

requires = [
    'requests>=1.0.0',
    'beautifulsoup4>=4.1.3'
]

setup(
    name='getme',
    version=crawy.__version__,
    description='HTML extraction template',
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    license=open('LICENSE').read(),
    author='Quang Quach',
    author_email='me@quang.be',
    packages=packages
    package_dir={'crawy': 'crawy'},
    install_requires=requires,
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
