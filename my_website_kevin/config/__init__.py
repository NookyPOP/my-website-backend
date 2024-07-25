import urllib.parse


class Config(object):
    DEBUG = True
    SQL_HOST = "101.133.159.192"
    SQL_USERNAME = "root"
    SQL_PASSWORD = urllib.parse.quote_plus("Root1234@")
    SQL_PORT = "3306"
    SQL_DB = "practice"
    JSON_AS_ASCII = False
    # config of database
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DB}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_MASK_SWAGGER = False
    RESTX_VALIDATE = False
