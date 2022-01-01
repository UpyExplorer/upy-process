# coding=utf-8

"""
Runserver
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


def initialize_app(app):
    """
    Application preparation before start
    """
    app.config.from_object('config')

    db = SQLAlchemy(app)
    db.init_app(app)

def main():
    """
    Main
    """
    initialize_app(app)
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
        )

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    main()