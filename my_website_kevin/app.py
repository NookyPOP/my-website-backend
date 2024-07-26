from flask import Flask, current_app
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
import logging
import os

from my_website_kevin.apis.login.services import User
from my_website_kevin.apis.login.models import UserAuth
from my_website_kevin.database import db, migrate
from my_website_kevin.config import Config
from my_website_kevin.apis import api

from dotenv import load_dotenv

load_dotenv(".env")  # from .env file
# configure root logger
logging.basicConfig(level=logging.INFO)

config = Config()
login_manager = LoginManager()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    # flask-jwt-extended get the secret key from config of flask app

    # api.add_namespace(login_namespace)
    api.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    # 用户登陆管理
    login_manager.init_app(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    username, password = user_id.split("-")
    return User(username, password)


# when create a new token and invoke user_identity_lookup
# for get_jwt_identity method
@jwt.user_identity_loader
def user_identity_lookup(user):
    print("user_identity_loader", user)
    print(user.__dict__)
    return user.id


# when loads a user from your database whenever a protected route is accessed.
# for get_current_user method
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    print("user_lookup_loader", jwt_data)
    identity = jwt_data["sub"]
    print(1, identity)
    print(2, db.session.query(UserAuth).filter_by(id=identity).one_or_none())
    return db.session.query(UserAuth).filter_by(id=identity).one_or_none()
