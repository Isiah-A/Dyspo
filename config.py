from os import path

basedir = path.abspath(path.dirname(__file__))

class Config:

    SECRET_KEY = 'isiah'
    FLASK_APP = 'Dyspop.app'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///dyspo.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://isiah:zipcode0@localhost/dyspo'

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False