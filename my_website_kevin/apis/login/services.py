from flask_login import login_user, UserMixin, logout_user
from my_website_kevin.database import db
from my_website_kevin.apis.login.models import UserAuth
from sqlalchemy import func
from flask_jwt_extended import create_access_token, get_jwt
from datetime import datetime, timezone, timedelta
from my_website_kevin.apis.login.models import JWTToken
import my_website_kevin.utils as utils
from dateutil import parser


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
        self.access_token = ""
        self.message = ""

    def validate_auth_user(self):
        user = db.session.query(UserAuth).filter_by(username=self.username).first()
        if user and user.check_password(self.password):
            self.auth_status = True
            self.message = "Login successful"
        elif user and not user.check_password(self.password):
            self.auth_status = False
            self.message = "Wrong password"
        else:
            self.auth_status = False
            self.message = "User does not exist"
        return user

    def login(self):
        user = self.validate_auth_user()
        if self.auth_status:
            self.access_token = access_token.create_token(user)
        return self.message, self.auth_status, self.access_token

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
        self.status_code = 0

    def registry(self):
        user = db.session.query(UserAuth).filter_by(username=self.username).first()
        if user and user.id:
            self.message = "User already exists"
            self.status_code = 400
            return self.message, self.status_code
        user = db.session.query(UserAuth).filter_by(email=self.email).first()
        if user and user.id:
            self.message = "Email already exists"
            self.status_code = 400
            return self.message, self.status_code
        user = UserAuth(
            username=self.username, email=self.email, mobile=self.mobile, sex=self.sex
        )
        user.set_password(password=self.password)
        db.session.add(user)
        db.session.commit()
        if user.id:
            self.status_code = 201
            self.message = "Registry successful"
        return self.message, self.status_code


class AccessTokenService:
    def create_token(self, user):
        expires = timedelta(days=1)
        access_token = create_access_token(
            identity=user, expires_delta=expires, additional_claims={"claim": "value"}
        )
        exp = str(datetime.now(timezone.utc) + expires)
        timestamp = int(parser.isoparse(exp).timestamp())
        expired_at = datetime.fromtimestamp(timestamp, tz=timezone.utc)
        jwt_id = utils.generate_random_string()
        jwt_new_token = JWTToken(jti=jwt_id, user_id=user.id, expired_at=expired_at)

        db.session.add(jwt_new_token)
        db.session.commit()
        return access_token

    def revoke_token(self, jti):
        jwt_token = db.session.query(JWTToken).filter_by(jti=jti).first()
        if jwt_token and not jwt_token.revoked:
            jwt_token.revoked = True
            db.session.commit()
            return True
        return False

    def is_token_revoked(self, jti):
        jwt_token = db.session.query(JWTToken).filter_by(jti=jti).first()
        return jwt_token.revoked if jwt_token else False


access_token = AccessTokenService()
