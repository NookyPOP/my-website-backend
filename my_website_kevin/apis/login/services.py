from flask_login import login_user, UserMixin, logout_user


class User(UserMixin):
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.id = f"{username}-{password}"

    def get_id(self):
        return self.id


class LoginService:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def login(self):
        user = User(self.username, self.password)
        login_user(user)
        return self

    def logout(self):
        user = User(self.username, self.password)
        logout_user(user)
        return self
