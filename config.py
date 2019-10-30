import os


class Config:
    '''
    General configuration parent class
    '''
    
    BOOK_API_BASE_URL = 'https://www.goodreads.com/search?key={}&q={}'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:1234@localhost/book'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig
}
