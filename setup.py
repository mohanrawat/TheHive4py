#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='thehive4py',
    version='1.0.0',
    description='Python API for TheHive.',
    long_description=open('README.MD').read(),
    author='TheHive-Project',
    author_email='support@thehive-project.org',
    maintainer='TheHive-Project',
    url='https://github.com/CERT-BDF/thehive4py',
    license='AGPL-V3',
    packages=['thehive4py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['requests']
)
