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


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'data-test.sqlite'))
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
