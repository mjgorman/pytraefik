#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wininst upload -r pypi')
    sys.exit()

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='pytraefik',
    version='0.0.1',
    description='Traefik API Client.',
    long_description=readme,
    author='Michael J Gorman',
    author_email='michael@michaeljgorman.michaeljgorman',
    url='https://github.com/mjgorman/pytraefik',
    packages=['pytraefik'],
    package_data={'': ['LICENSE']},
    package_dir={'pytraefik': 'pytraefik'},
    install_requires=['requests'],
    license=license,
)
