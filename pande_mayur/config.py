import os


class Config:

    """Config class to set flask app parameters"""

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = '\x1b\x01\x8a&\x9c\xc0\xcd\x9d\xc1{\x88Y4\xc6\xac\x00\x8c\xc6\xcc&\xc7reF'
