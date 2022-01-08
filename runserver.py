# coding=utf-8

"""
Runserver
"""

from app import app
from waitress import serve

from source.processes.base import BaseProcess


if __name__ == "__main__":
    station_process = BaseProcess()
    keys = station_process.generate_keys()
    station_process.initialize(list_keys=keys)
    
    host = app.config['HOST']
    port = app.config['PORT']

    app.run(host=host, port=port)
    # serve(app, host=host, port=port)

