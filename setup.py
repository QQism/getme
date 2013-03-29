#!/usr/bin/env python

import os
import sys

import getme

try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

packages = ['getme',]

requires = [
    'beautifulsoup4>=4.1.3',
]

setup(
    name='getme',
    version=getme.__version__,
    description='AN HTML extractor by a simple template',
    long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    license=open('LICENSE').read(),
    author='Quang Quach',
    author_email='me@quang.be',
    packages=packages,
    package_data={'': ['LICENSE',]},
    package_dir={'getme': 'getme'},
    install_requires=requires,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ),
)
