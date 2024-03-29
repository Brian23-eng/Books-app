import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    '''
    General configuration parent class
    '''
    
    BOOK_API_BASE_URL = 'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={}'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    BOOK_API_KEY = os.environ.get('BOOK_API_KEY')
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
