# coding=utf-8

"""
Runserver
"""

from app import app
from waitress import serve


if __name__ == "__main__":
    host = app.config['HOST']
    port = app.config['PORT']

    app.run(host=host, port=port)
    # serve(app, host=host, port=port)
