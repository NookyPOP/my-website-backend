from flask_login import login_user, UserMixin, logout_user
from my_website_kevin.database import db
from my_website_kevin.apis.login.models import UserAuth
from sqlalchemy import func


class User(UserMixin):
    def __init__(self, username) -> None:
        self.username = username
        self.id = f"{username}"

    def get_id(self):
        return self.id

    @property
    def detail(self):
        user_info = (
            db.session.query(
                UserAuth.username, UserAuth.mobile, UserAuth.sex, UserAuth.email
            )
            .filter(func.lower(UserAuth.username) == self.username.lower())
            .first()
        )
        if not user_info:
            raise ValueError("User does not exist")
        username, mobile, email = user_info
        return {"username": username, "mobile": mobile, "email": email}


class LoginService:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.auth_status = False
        self.message = ""

    def validate_auth_user(self):
        user = db.session.query(UserAuth).filter_by(username=UserAuth.username).first()
        if user and user.check_password(self.password):  # type: ignore
            self.auth_status = True
            self.message = "Login successful"
        else:
            self.auth_status = False
            self.message = "User does not exist"
        return self

    def login(self):
        self.validate_auth_user()
        if self.auth_status:
            _user = User(self.username)
            login_user(_user)

        return self.auth_status, self.message

    def logout(self):
        user = User(self.username, self.password)
        logout_user(user)
        return self
