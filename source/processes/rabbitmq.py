# coding=utf-8

"""
Module Docstring
"""

__all__ = ['BaseRabbitMQ']

import pika
from source.processes.callback import CallbackProcess


class BaseRabbitMQ(object):
    """
    BaseProcess
    """
    process_type = 'rabbitmq'

    def __init__(self, rabbitmq_url):
        """
        Constructor 
        """
        self.rabbitmq_url = rabbitmq_url

    def channel_initialize(self):
        """
        Channel Initialize
        """
        params = pika.URLParameters(self.rabbitmq_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)

        return connection.channel()

    def start_queue(self, channel, key):
        """
        Start Queue
        """
        channel.queue_declare(queue=key, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=key,on_message_callback=CallbackProcess)
        channel.start_consuming()
