# -*- coding: utf-8 -*-

"""Provides a ``ZeroMQFactory`` to get a configured zmq client from a
  settings dictionary, e.g.::

      >>> factory = ZeroMQFactory()
      >>> zmq = factory({'zmq.url': 'redis://127.0.0.1:5557'})

  And ``GetZeroMQ`` which wraps the factory so it can be used as a
  Pyramid request method.
"""

__all__ = [
    'GetZeroMQ',
    'ZeroMQFactory',
]


import logging
logger = logging.getLogger(__name__)
import pyramid.exceptions

from zope.component import getGlobalSiteManager
from zope.interface import Interface
from zope.interface import directlyProvides
from .zmq import ZeroMQ


class IZeroMQConfiguration(Interface):

    """Marker interface provided by ZeroMQConfiguration"""


class ZeroMQConfiguration(dict):

    """Parse the application settings."""

    def __init__(self, **kwargs):
        pass

    def __call__(self, settings):
        """ Unpack the settings. """
        
        if ('zmq.url' in settings and
                settings['zmq.url'] is not None):
            # Unpack.
            url = settings['zmq.url']

            config.update({
                'url': url,
            })
        else:
            raise pyramid.exceptions.ConfigurationError(
                """To use zmq with pyramid, zmq.url should be provided"""
            )
        self.update(config)
        return self


class ZeroMQFactory(object):

    def __init__(self, **kwargs):
        self.get_registry = kwargs.get('get_registry', getGlobalSiteManager)
        self.config = kwargs.get('parse_config', ZeroMQConfiguration())
        self.provides = kwargs.get('provides', directlyProvides)
        self.zmq = kwargs.get('zmq_context', ZeroMQ)

    def __call__(self, settings, registry=None):
        """Returns a ``zmq`` context that uses a configuration
           registered in the ``registry`` provided that is, in turn,
           configured with the ``settings`` provided.
        """

        # If called without a registry, i.e.: not within the context of a
        # Pyramid application, then register the context in a
        # zope.component registry.
        if registry is None:
            registry = self.get_registry()

        # Query the registry for a client_configuration. If it doesn't exist,
        # instantiate and register one for next time.
        zmq_conf = registry.queryUtility(IZeroMQConfiguration)
        if not zmq_conf:
            # update conf
            zmq_conf = self.config(settings)
            self.provides(self.config, IZeroMQConfiguration)
            registry.registerUtility(self.config,
                                     IZeroMQConfiguration)

        # And use it to instantiate a zmq context.
        return self.zmq(**zmq_conf)


class GetZeroMQ(object):

    """Provide the zmq factory as a Pyramid request method."""

    def __init__(self, **kwargs):
        self.zmq_factory = kwargs.get('zmq_factory', ZeroMQFactory())

    def __call__(self, request):
        registry = request.registry
        return self.zmq_factory(registry.settings, registry=registry)
