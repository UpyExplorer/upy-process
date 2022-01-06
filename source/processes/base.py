# coding=utf-8

"""
Função responsável pela orquestração de um processo base
"""

__all__ = ['BaseProcess']

import environ
from threading import Thread
from source.processes.rabbitmq import BaseRabbitMQ


class BaseProcess(object):
    """
    BaseProcess
    """
    process_type = 'base'

    def __init__(self):
        """
        Base Constructor 
        """
        env = environ.Env()
        self.rabbitmq = BaseRabbitMQ(rabbitmq_url=env("RABBITMQ_URL"))

    def initialize(self, key):
        """
        Process Initialization
        """
        channel = self.rabbitmq.channel_initialize()
        self.rabbitmq.start_queue(channel=channel, key=key)

    def finalize(self, **kwargs):
        """
        Process Completion
        """
        pass

    def fail_finalization(self, **kwargs):
        """
        Failed Process Completion
        """
        pass

    def run(self, key, **kwargs):
        """
        Execução
        """
        try:
            process = Thread(target=self.initialize, kwargs={"key": key})
            process.start()
        except:
            self.fail_finalization()
        finally:
            self.finalize()

