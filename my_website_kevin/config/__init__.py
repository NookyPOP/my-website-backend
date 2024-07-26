import urllib.parse
import os


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
    # SECRET_KEY = os.environ.get("SECRET_KEY")  # flask 使用这个 key 来加密
    # JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", SECRET_KEY)
    # jwt 使用这个 key来加密和解密，是一种对称加密
    # JWT 密钥用于对 JWT 进行加密和解密。使用对称加密算法时，相同的密钥用于加密和解密，而使用非对称加密算法时，需要使用公钥加密，私钥解密。
    # 或者在主机环境中设置环境变量，如: export JWT_SECRET_KEY=123456
