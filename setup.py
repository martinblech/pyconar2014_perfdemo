#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import perfdemo
version = perfdemo.__version__

setup(
    name='perfdemo',
    version=version,
    author='',
    author_email='martinblech@gmail.com',
    packages=[
        'perfdemo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['perfdemo/manage.py'],
)
