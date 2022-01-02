# coding=utf-8

"""
Função responsável pela orquestração de um processo base
"""

__all__ = ['BaseProcess']

import pika
import time
from threading import Thread
from flask import current_app as app


class BaseProcess(object):
    """
    BaseProcess
    """
    process_type = 'base'

    def __init__(self):
        """
        Base Constructor 
        """
        rabbitmq_url = app.config['RABBITMQ_URL']

        params = pika.URLParameters(rabbitmq_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        self.channel = connection.channel()

    def initialize(self, key):
        """
        Process Initialization
        """
        print("Process Initialization")
        self.channel.queue_declare(queue=key, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=key,on_message_callback=self.execute)
        self.channel.start_consuming()

    def execute(self, ch, method, properties, body):
        """
        Process Execution
        """
        print("Process Execution")
        print(" [x] Received %r" % body.decode())
        time.sleep(10)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def finalize(self, **kwargs):
        """
        Process Completion
        """
        print("Process Completion")

    def fail_finalization(self, **kwargs):
        """
        Failed Process Completion
        """
        print("Failed Process Completion")

    def run(self, key, **kwargs):
        """
        Execução
        """
        print("Execution")
        try:
            t1 = Thread(target=self.initialize, kwargs={"key": key})
            t1.start()
        except:
            self.fail_finalization()
        finally:
            self.finalize()

