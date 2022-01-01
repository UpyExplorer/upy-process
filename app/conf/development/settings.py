import os
import environ
from os.path import dirname

BASE_DIR = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

DEBUG = env.bool("DEBUG", False)
PORT = env("PORT")
HOST = env("HOST")

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI")

CSRF_ENABLED = False
CSRF_SESSION_KEY = env("CSRF_SESSION_KEY")
SECRET_KEY = env("SECRET_KEY")