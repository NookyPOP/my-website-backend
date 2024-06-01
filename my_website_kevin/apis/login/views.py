from apis.login.schemas import login_model, login_namespace
from flask_restx import Resource, reqparse


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
