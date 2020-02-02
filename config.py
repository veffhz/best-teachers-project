import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    DATA_PATH = 'data'
    TEACHERS_FILE = f'{DATA_PATH}/teachers.json'
    BOOKING_FILE = f'{DATA_PATH}/booking.json'
    GOALS_FILE = f'{DATA_PATH}/goals.json'
    REQUEST_FILE = f'{DATA_PATH}/request.json'

    DB_FILE = BASE_DIR.joinpath('application.db').absolute()
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    #if not SECRET_KEY:
    #    raise ValueError("No SECRET_KEY set for Flask application")


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = '22d126e0f751479d902e15b69fd99939'
