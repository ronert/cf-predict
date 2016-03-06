import logging
from logging import StreamHandler
import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True


class UnitTestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'data-test.sqlite'))
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True


class IntegrationTestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @classmethod
    def init_app(cls, app):
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    "development": DevelopmentConfig,
    "unit_testing": UnitTestingConfig,
    "integration_testing": IntegrationTestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
