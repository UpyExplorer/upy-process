import os
import environ

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

env = environ.Env()
environ.Env.read_env(BASE_DIR+"/.env")

FLASK_ENV = env("FLASK_ENV")

if FLASK_ENV == 'production':
    from app.conf.production import *
else:
    from app.conf.development import *
