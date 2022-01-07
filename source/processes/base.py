# coding=utf-8

"""
Module Docstring
"""

__all__ = ['BaseProcess']

import environ
from threading import Thread
from source.processes.rabbitmq import BaseRabbitMQ
from app.controllers.base import ControlerBase
from app.models.work_user import WorkUser
from app.models.work_station import WorkStation
from app.models.work_process import WorkProcess


class BaseProcess(ControlerBase):
    """BaseProcess
    """

    def __init__(self, data=None):
        super().__init__()

        env = environ.Env()
        self.rabbitmq = BaseRabbitMQ(rabbitmq_url=env("RABBITMQ_URL"))
        self.work_station = env("WORK_STATION")

    def generate_keys(self):
        """Queue key list generation
        """
        query_work_station = WorkStation.query.filter(
            WorkStation.key == self.work_station,
            WorkStation.status == True
        ).first()
        
        query_users = WorkUser.query.join(
                WorkProcess,
                WorkProcess.work_user_id == WorkUser.id
            ).filter(
                WorkProcess.work_station_id == query_work_station.id,
                WorkProcess.status == True,
                WorkUser.status == True
            ).all()

        task_name = "task_" + str(self.work_station) + "_"
        
        list_queue = []
        if query_users:
            for user in query_users:
                key = task_name+str(user.company_data_id)
                list_queue.append(key)
                print(key)

            return list_queue

        return None

    def initialize(self, list_keys):
        """Process Initialization
        """
        try:
            for key in list_keys:
                channel = self.rabbitmq.channel_initialize()
                process = Thread(
                    target=self.rabbitmq.start_queue,
                    kwargs={
                        "channel": channel,
                        "key": key
                    }
                )
                process.start()
        except:
            self.fail_finalization()
        finally:
            self.finalize()

    def finalize(self, **kwargs):
        """Process Completion
        """
        pass

    def fail_finalization(self, **kwargs):
        """Failed Process Completion
        """
        pass
