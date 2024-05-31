from my_website_kevin.apis.login.schemas import login_model, ns
from flask_restx import Resource, reqparse

from flask import jsonify


@ns.route("/login")
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        return {"message": "Login successful"}, 200

    @ns.param("username", type=str, description="Name of login user")
    @ns.param("password", type=str, description="Password of login user")
    @ns.marshal_with(login_model)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)

        args = parser.parse_args()

        response = {
            "username": args["username"] if args["username"] else None,
            "password": args["password"] if args["password"] else None,
        }
        return response


@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}, 200
