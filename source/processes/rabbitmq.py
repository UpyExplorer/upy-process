# coding=utf-8

"""
Module Docstring
"""

__all__ = ['BaseRabbitMQ']

import pika

from app.base import BaseApp
from source.processes.callback import CallbackProcess


class BaseRabbitMQ(BaseApp):
    """BaseRabbitMQ
    """
    process_type = 'rabbitmq'

    def __init__(self):
        super().__init__()
        self.rabbitmq_url = self.env("RABBITMQ_URL")

    def channel_initialize(self):
        """Channel Initialize
        """
        params = pika.URLParameters(self.rabbitmq_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)

        return connection.channel()

    def start_queue(self, key):
        """Start Queue
        """
        channel = self.channel_initialize()
        channel.queue_declare(queue=key, durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=key,on_message_callback=CallbackProcess)
        channel.start_consuming()
        
    def search_queue(self, key, exchange=None):
        """Search Queue
        """
        exchange = exchange or "amq.direct"
        try:
            channel = self.channel_initialize()
            response = channel.queue_bind(queue=key, exchange=exchange)
            return {
                "status": 200,
                "message": "ok",
                "quantity": response.channel_number
            }
        except Exception as error:
            return {
                "status": error.args[0],
                "message": error.args[1],
                "quantity": 0
            }
