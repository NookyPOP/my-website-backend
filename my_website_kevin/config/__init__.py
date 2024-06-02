class Config(object):
    DEBUG = True
    SECRET_KEY = "123456"
    SQL_HOST = "127.0.0.1"
    SQL_USERNAME = "root"
    SQL_PASSWORD = "root1234"
    SQL_PORT = "3306"
    SQL_DB = "practice"
    JSON_AS_ASCII = False
    # config of database
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DB}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
