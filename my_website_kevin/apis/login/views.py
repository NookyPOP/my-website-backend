from apis.login.schemas import (
    login_model,
    login_namespace,
    user_model,
    emails,
    person_model,
)
from flask_restx import Resource, reqparse, marshal
from apis.login.models import User, Emalis, Person


@login_namespace.route("/login")
class Login(Resource):
    @login_namespace.expect(login_model)
    def post(self):
        return {"message": "Login successful"}, 200

    @login_namespace.param("username", type=str, description="Name of login")
    @login_namespace.param("password", type=str, description="Password or")
    @login_namespace.marshal_with(login_model)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)

        args = parser.parse_args()

        respologin_namespacee = {
            "username": args["username"] if args["username"] else None,
            "password": args["password"] if args["password"] else None,
        }
        return respologin_namespacee


@login_namespace.route("/hello")
class HelloWorld(Resource):
    @login_namespace.doc("hello")
    @login_namespace.marshal_with(login_model)
    def get(self):
        return {"hello": "world", "username": "jack"}, 200


@login_namespace.route("/user/<string:user_name>")
class UserInfo(Resource):
    @login_namespace.marshal_with(user_model)
    @login_namespace.doc("user")
    @login_namespace.response(404, "User not found")
    @login_namespace.response(200, "User found")
    def get(self, user_name):
        print(user_name)
        user = User.query.filter_by(nickname=user_name).first()
        if not user:
            login_namespace.abort(404)
        return {"username": user.nickname, "mobile": user.mobile, "sex": user.sex}, 200


@login_namespace.route("/emails")
class EmailInfo(Resource):
    @login_namespace.marshal_with(emails)
    def get(self):
        email_list = Emalis.query.all()
        return email_list


@login_namespace.route("/person")
class PersonInfo(Resource):
    def get(self):
        person_list = Person.query.all()
        return [marshal(person, person_model) for person in person_list]
