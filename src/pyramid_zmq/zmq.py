# -*- coding: utf-8 -*-

"""

"""

import zmq


class ZeroMQ(object):
    
    """ zmq context object """

    def __init__(self, **kwargs):
        """ get all settings params """
        self.context = zmq.Context()
        self.url = kwargs.get('url')
        print(self.url)
    
    def push(self):
        """ should return a zmq PUSH socket """
        socket = self.context.socket(zmq.PUSH)
        socket.bind(self.url)
        return socket
    
    def pull(self):
        """ should return a zmq PULL socket """
        socket = self.context.socket(zmq.PULL)
        socket.connect(self.url)
        return socket