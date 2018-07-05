import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    USERS_SERVICE_URL = os.environ.get("USERS_SERVICE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Base configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    """Base configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")


class StagingConfig(BaseConfig):
    """Staging configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class ProductionConfig(BaseConfig):
    """Base configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
