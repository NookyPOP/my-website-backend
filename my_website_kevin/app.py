from flask import Flask
from flask_login import LoginManager
from my_website_kevin.apis.login.services import User
from my_website_kevin.apis import api
from my_website_kevin.config import Config
from my_website_kevin.database import db
import logging

# configure root logger
logging.basicConfig(level=logging.INFO)


config = Config()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # api.add_namespace(login_namespace)
    api.init_app(app)

    db.init_app(app)
    # 用户登陆管理
    login_manager.init_app(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    username, password = user_id.split("-")
    return User(username, password)
