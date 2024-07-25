from my_website_kevin.database import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserAuth(db.Model):
    __tablename__ = "user_list"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    mobile = db.Column(db.String(80), unique=False, nullable=False)
    sex = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f"<User {self.username}>"

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


class Emalis(db.Model):
    __tablename__ = "email_info"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    status_code = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


class Person(db.Model):
    __tablename__ = "person_info"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    sex = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    address1 = db.Column(db.String(80), unique=False, nullable=False)
    address2 = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    zip = db.Column(db.Integer, unique=False, nullable=False)
    first_names = db.Column(db.JSON, unique=False, nullable=False)
    billing_address = db.Column(db.JSON, nullable=False, unique=False)
    shipping_address = db.Column(db.JSON, nullable=False, unique=False)
    family_list = db.Column(db.JSON, nullable=False, unique=False)

    def __repr__(self):
        return f"<User {self.name}>"
