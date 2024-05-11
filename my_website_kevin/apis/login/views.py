from my_website_kevin.apis.login.schemas import login_model, login_namespace
from flask_restx import Resource, reqparse
from my_website_kevin.apis import api
from flask import jsonify


@login_namespace.route("/login-info")
class Login(Resource):
    @login_namespace.expect(login_model)
    def post(self):
        return {"message": "Login successful"}

    @login_namespace.param("username", type=str, description="Name of login user")
    @login_namespace.param("password", type=str, description="Password of login user")
    @login_namespace.param("email", type=str, description="Email of login user")
    @login_namespace.param("phone", type=str, description="Phone of login user")
    @login_namespace.param("address", type=str, description="Address of login user")
    @login_namespace.marshal_with(login_model)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("phone", type=str)
        parser.add_argument("address", type=str)

        args = parser.parse_args()

        response = {
            "username": args["username"] if args["username"] else None,
            "password": args["password"] if args["password"] else None,
            "email": args["email"] if args["email"] else None,
            "phone": args["phone"] if args["phone"] else None,
            "address": args["address"] if args["address"] else None,
        }
        return response


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


@api.route("/")
class HelloWorld(Resource):
    def get(self):
        return jsonify({"hello": "world"})
