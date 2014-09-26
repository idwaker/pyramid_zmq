# -*- coding: utf-8 -*-

"""Provide environment variable configured ``DEFAULT_SETTINGS``."""

import os

stub = os.environ.get('ZMQ_KEY', 'ZMQ')

ZMQ_URL = '{0}_URL'.format(stub)


DEFAULT_SETTINGS = {
    'zmq.url': os.environ.get(ZMQ_URL, 'tcp://127.0.0.1:5557'),
}
