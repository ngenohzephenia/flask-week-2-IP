import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=d4df65110d1448f28e60b32fe558da44'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=d4df65110d1448f28e60b32fe558da44'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # NEWS_API_BASE_URL ='http://newsapi.org/v2/everything?/{}?api_key={}'

    

    @staticmethod
    def init_app(app):w
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
  