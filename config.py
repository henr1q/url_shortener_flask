import os
# from dotenv import load_dotenv

# load_dotenv()

class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'secr3t'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./database/urls.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True