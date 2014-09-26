# -*- coding: utf-8 -*-

"""

"""

import zmq


class ZeroMQ(object):
    
    """ zmq context object """

    def __init__(self, **kwargs):
        """ get all settings params """
        print(kwargs)
        self.context = zmq.Context()
        print(self.context)
    
    def push(self):
        """ should return a zmq PUSH socket """
        pass
    
    def pull(self):
        """ should return a zmq PULL socket """
        pass