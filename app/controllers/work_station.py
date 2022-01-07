# coding=utf-8

"""
Module Docstring
"""

__all__ = ['WorkStationHelper']

from app.controllers.base import ControlerBase
from app.models.work_station import WorkStation, base_schema, base_schemas


class WorkStationHelper(ControlerBase):
    """WorkStation Helper
    """
    def __init__(self, data=None):
        super().__init__()

        self.model_class = WorkStation
        self.base_schema = base_schema
        self.base_schemas = base_schemas
