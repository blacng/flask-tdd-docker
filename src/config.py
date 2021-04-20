# src/config.py
import os
from os import path

from dotenv import load_dotenv  # new

basedir = path.abspath(os.path.dirname(__file__))  # new
load_dotenv(path.join(basedir, "../.env"))  # new


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")  # new


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")  # new


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # new
    url = os.environ.get("DATABASE_URL")
    if url is not None:
        if url.startswith("postgres://"):
            url = url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = url
