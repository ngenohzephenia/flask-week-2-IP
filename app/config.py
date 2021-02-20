class config:
    '''
    General configuration parent class
    '''

    pass


class ProdConfig(config):
    '''
    Production configuration child class

    Args:
       Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(config):
   '''
   Development configuration child class

   Args:
       Config: The parent configuration settings
    '''

    DEBUG = True  