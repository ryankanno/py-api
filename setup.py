#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(name='py-api',
      version='0.0.1',
      description='A set of utilities to help write API clients',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=find_packages(),
      long_description=open('README.md').read(),
      url="https://github.com/ryankanno/py-api")

# vim: filetype=python
