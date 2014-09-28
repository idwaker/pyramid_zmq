# -*- coding: utf-8 -*-

"""Provide a Pyramid confguration entry point."""

import logging
logger = logging.getLogger(__name__)

from .config import DEFAULT_SETTINGS
from .hooks import GetZeroMQ


def includeme(config):
    settings = config.get_settings()
    for key, value in DEFAULT_SETTINGS.items():
        settings.setdefault(key, value)
    config.add_request_method(GetZeroMQ(), 'zmq', reify=True)
