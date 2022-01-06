import os
from os.path import dirname

BASE_DIR = dirname(dirname(dirname(os.path.abspath(__file__))))

DEBUG = os.getenv("DEBUG")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = os.getenv("CSRF_SESSION_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
