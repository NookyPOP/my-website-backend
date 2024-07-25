from flask_login import login_user, UserMixin, logout_user
from my_website_kevin.database import db
from my_website_kevin.apis.login.models import UserAuth
from sqlalchemy import func
from flask_jwt_extended import create_access_token


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
        user = self.validate_auth_user()
        if self.auth_status:
            access_token = create_access_token(identity=user.id)
        return self.auth_status, self.message, access_token

    def logout(self):
        user = User(self.username, self.password)
        logout_user(user)
        return self


class RegistryService:
    def __init__(self, username, password, email, mobile, sex) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.mobile = mobile
        self.sex = sex
        self.message = ""
        self.access_token = ""
        self.status_code = 0

    def registry(self):
        user = db.session.query(UserAuth).filter_by(username=UserAuth.username).first()
        if user and user.id:
            self.message = "User already exists"
            self.status_code = 400
            return self.message, self.status_code, self.access_token
        user = db.session.query(UserAuth).filter_by(email=UserAuth.email).first()
        if user and user.id:
            self.message = "Email already exists"
            self.status_code = 400
            return self.message, self.status_code, self.access_token
        user = UserAuth(
            username=self.username, email=self.email, mobile=self.mobile, sex=self.sex
        )
        user.set_password(password=self.password)
        db.session.add(user)
        db.session.commit()
        if user.id:
            self.access_token = create_access_token(identity=user.id)
            self.status_code = 201
        return self.message, self.status_code, self.access_token
