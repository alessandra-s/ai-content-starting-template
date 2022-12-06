
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
##enviorment variable set on operating system rather than within application
OPENAI_API_KEY = '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'
