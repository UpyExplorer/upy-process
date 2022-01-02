# coding=utf-8

"""
Função responsável pela orquestração de um processo base
"""

__all__ = ['BaseProcess']

from app import app


class BaseProcess():
    """
    BaseProcess
    """
    process_type = 'base'

    def __init__(self):
        """
        Base Constructor 
        """
        rabbitmq_url = app.config['RABBITMQ_URL']

    def initialize(self):
        """
        Process Initialization
        """
        print("Process Initialization")

    def execute(self, target):
        """
        Process Execution
        """
        print("Process Execution")

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

    def run(self, **kwargs):
        """
        Execução
        """
        print("Execution")
