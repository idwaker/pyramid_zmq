# -*- coding: utf-8 -*-

"""
zmq helpers to create PUSH/PULL, PUB/SUB sockets
"""

import zmq


class ZeroMQ(object):
    
    """ zmq context object """

    def __init__(self, **kwargs):
        """ get all settings params """
        self.context = zmq.Context()
        self.pushpull_url = kwargs.get('pushpull_url')
        self.pubsub_url = kwargs.get('pubsub_url')
    
    def push(self):
        """ should return a zmq PUSH socket """
        socket = self.context.socket(zmq.PUSH)
        socket.bind(self.pushpull_url)
        return socket
    
    def pull(self):
        """ should return a zmq PULL socket """
        socket = self.context.socket(zmq.PULL)
        socket.connect(self.pushpull_url)
        return socket
    
    def pub(self):
        """ should return a zmq PUB socket """
        socket = self.context.socket(zmq.PUB)
        socket.bind(self.pubsub_url)
        return socket
    
    def sub(self, topic=''):
        """ should return a zmq SUB socket """
        socket = self.context.socket(zmq.SUB)
        socket.connect(self.pubsub_url)
        if topic:
            socket.setsockopt(zmq.SUBSCRIBE, topic)
        return socket
