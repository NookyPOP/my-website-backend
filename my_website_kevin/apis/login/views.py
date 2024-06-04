from apis.login.schemas import (
    login_model,
    login_namespace,
    user_model,
    emails,
    person_model,
    resource_fields,
    type_info_model,
)
from flask_restx import Resource, reqparse, marshal, inputs
from apis.login.models import User, Emalis, Person
import json
from werkzeug.datastructures import FileStorage
import PyPDF2
from werkzeug.utils import secure_filename


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
        if not user_name:
            user = User.query.filter_by(nickname=user_name).first()
            if not user:
                login_namespace.abort(404)
            return {
                "username": user.nickname,
                "mobile": user.mobile,
                "sex": user.sex,
            }, 200

        else:
            user_list = User.query.all()
            if not user_list:
                login_namespace.abort(404)
            return user_list, 200


@login_namespace.route("/emails")
class EmailInfo(Resource):
    @login_namespace.marshal_with(emails)
    def get(self):
        email_list = Emalis.query.all()
        return email_list


@login_namespace.route("/person")
class PersonInfo(Resource):
    @login_namespace.marshal_with(person_model)
    def get(self):
        person_list = Person.query.all()
        print(person_list[0].first_names)
        # data = {"name": "Bougnazal", "first_names": ["Emile", "Raoul"]}
        if not person_list:
            login_namespace.abort(404)
        else:
            return [person for person in person_list]
            # return marshal(data, resource_fields)


@login_namespace.route("/type")
class TypeInfo(Resource):
    # @login_namespace.param("rate", type=int, description="rate")
    # @login_namespace.param("name", type=str, description="name")
    @login_namespace.marshal_with(type_info_model)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("rate", type=int, help="rate error")
        parser.add_argument(
            "name", type=str, help="name error", action="split", dest="public_name"
        )
        parser.add_argument("User-Agent", location="headers")
        parser.add_argument("session_id", location="cookies")

        args = parser.parse_args()
        resposne = {
            "rate": args["rate"] if args["rate"] else None,
            "name": args["public_name"] if args["public_name"] else None,
            "User-Agent": args["User-Agent"],
            "session_id": args["session_id"],
        }
        print(args)
        return resposne, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, location="form")
        parser.add_argument("flag", type=inputs.boolean)

        args = parser.parse_args()
        print(args)
        return args, 200


@login_namespace.route("/upload")
class Upload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("file", location="files", type=FileStorage, required=True)
        args = parser.parse_args()
        uploaded_file = args["file"]
        print(uploaded_file)

        # with open(uploaded_file, "rb") as pdf_file:
        #     pdf_reader = PyPDF2.PdfReader(pdf_file)
        #     num_pages = len(pdf_reader.pages)

        #     page = pdf_reader.pages[0]
        #     content = page.extract_text()
        #     print(content)
