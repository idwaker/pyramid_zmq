#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, join as join_path
from setuptools import setup, find_packages


def _read(file_name):
    sock = open(file_name)
    text = sock.read()
    sock.close()
    return text


setup(
    name = 'pyramid_zmq',
    version = '0.0.1',
    description = 'Integrate zeromq with a Pyramid application.',
    author = 'Diwaker Ghimire',
    author_email = 'username: idwaker, domain: gmail.com',
    url = 'http://github.com/idwaker/pyramid_zmq',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license = _read('UNLICENSE').split('\n')[0],
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False,
    install_requires=[
        'pyzmq>=14.3.1',
        'zope.component',
        'zope.interface',
    ]
)
