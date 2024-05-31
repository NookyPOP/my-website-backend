from flask import Flask
from flask_login import LoginManager
from apis.login.services import User
from my_website_kevin.apis import api

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    # 用户登陆管理
    login_manager.init_app(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    username, password = user_id.split("-")
    return User(username, password)
