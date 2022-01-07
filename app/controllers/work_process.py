# coding=utf-8

"""
Module Docstring
"""

__all__ = ['WorkProcessHelper']

from app.controllers.base import ControlerBase
from app.models.work_process import WorkProcess, base_schema, base_schemas


class WorkProcessHelper(ControlerBase):
    """WorkProcess Helper
    """
    def __init__(self, data=None):
        super().__init__()

        self.model_class = WorkProcess
        self.base_schema = base_schema
        self.base_schemas = base_schemas
