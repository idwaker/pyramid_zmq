# -*- coding: utf-8 -*-

"""Provide a Pyramid confguration entry point."""

import logging
logger = logging.getLogger(__name__)

from .config import DEFAULT_SETTINGS
from .hooks import ZeroMQFactory


def zeromq_maker():
    factory = ZeroMQFactory()
    return factory(DEFAULT_SETTINGS)


def _zeromq(request):
    registry = request.registry
    factory = ZeroMQFactory()
    return factory(registry.settings, registry=registry)


def includeme(config):
    settings = config.get_settings()
    for key, value in DEFAULT_SETTINGS.items():
        settings.setdefault(key, value)
    config.add_request_method(_zeromq, 'zmq', reify=True)
