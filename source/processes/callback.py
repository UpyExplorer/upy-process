# coding=utf-8

"""
Module Docstring
"""

__all__ = ['CallbackProcess']

import time
from flask import current_app as app


class CallbackProcess(object):
    """CallbackProcess
    """
    process_type = 'callback'

    def __init__(self, channel, method, properties, body):
        """Base Constructor 
        """
        print(" [x] Received %r" % body.decode())
        time.sleep(10)
        print(" [x] Done")
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def initialize(self, key):
        """Process Initialization
        """
        print("Process Initialization")

    def run(self, key, **kwargs):
        """Execution
        """
        print("Execution")
