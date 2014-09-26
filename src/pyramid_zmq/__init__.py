# -*- coding: utf-8 -*-

"""Provide a Pyramid confguration entry point."""

import logging
logger = logging.getLogger(__name__)

from .config import DEFAULT_SETTINGS


class IncludeMe(object):
    """Unpack the settings and provide ``request.zmq``."""

    def __init__(self, **kwargs):
        self.default_settings = kwargs.get('default_settings', DEFAULT_SETTINGS)
        self.get_zmq = kwargs.get('get_zmq', None)

    def __call__(self, config):
        settings = config.get_settings()
        for key, value in self.default_settings.items():
            settings.setdefault(key, value)
        config.add_request_method(self.get_zmq, 'zmq', reify=True)


includeme = IncludeMe().__call__
