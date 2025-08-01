import os
from decouple import config

# Get the absolute path of the project directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for session management and security
    SECRET_KEY = config('SECRET_KEY')
    # Disable modification tracking for performance
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', default=False, cast=bool)

class DevConfig(Config):
    # Use SQLite for development; store DB in project directory
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'dev.db')}"
    DEBUG = True  # Enable debug mode for development
    SQLALCHEMY_ECHO = True  # Log SQL statements for debugging

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"
    SQLALCHEMY_ECHO = False
    TESTING = True
