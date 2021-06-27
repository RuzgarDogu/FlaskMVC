import os

class Config(object):
    """docstring for Config."""

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '7bce2ca88c6b82065a42a4ca1bd2ccf6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}/flask".format('root', '', 'localhost')

    MAIL_SERVER = 'srvc115.trwww.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEFAULT_SENDER = 'test@aintensive.com'
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
