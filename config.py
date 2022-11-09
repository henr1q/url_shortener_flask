# from os import environ
# from dotenv import load_dotenv
#
# load_dotenv()

class Config:
    """Base config."""
    SECRET_KEY = 'Sec3333t'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOAD_FOLDER = 'flask_api/static/profile_pics'
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./database/urls.db'
    DEBUG = True
