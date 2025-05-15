import os

from dotenv import load_dotenv

load_dotenv()

CONFIG__SECRET_KEY = os.getenv("CONFIG__SECRET_KEY")
CONFIG__DEBUG = os.getenv("CONFIG__DEBUG")

CONFIG__ALLOWED_HOSTS = os.getenv("CONFIG__ALLOWED_HOSTS")

CONFIG__DB_NAME = os.getenv("CONFIG__DB_NAME")
CONFIG__DB_USER = os.getenv("CONFIG__DB_USER")
CONFIG__DB_PASS = os.getenv("CONFIG__DB_PASS")
CONFIG__DB_HOST = os.getenv("CONFIG__DB_HOST")
CONFIG__DB_PORT = os.getenv("CONFIG__DB_PORT")
CONFIG__DB_OPTIONS = os.getenv("CONFIG__DB_OPTIONS")
CONFIG__DB_ATOMIC_REQUESTS = os.getenv("CONFIG__DB_ATOMIC_REQUESTS")