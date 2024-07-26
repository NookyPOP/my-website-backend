from my_website_kevin.apis.login.schemas import (
    login_namespace,
    login_model,
    registry_user_model,
    response_model,
)

from flask_restx import Resource, reqparse, marshal, inputs

# from my_website_kevin.apis.login.models import User, Emalis, Person
# import json
# from werkzeug.datastructures import FileStorage
# import PyPDF2
# from werkzeug.utils import secure_filename
from flask import jsonify, make_response
from my_website_kevin.apis.login.services import LoginService, RegistryService
from flask_jwt_extended import jwt_required, current_user


@login_namespace.route("/registry")
class Registry(Resource):
    @login_namespace.param(
        "sex", required=True, type=str, description="Sex of username"
    )
    @login_namespace.param(
        "email", required=True, type=str, description="Email of username"
    )
    @login_namespace.param(
        "mobile", required=True, type=str, description="Mobile of username"
    )
    @login_namespace.param(
        "password", required=True, type=str, description="Password of username"
    )
    @login_namespace.param(
        "username", required=True, type=str, description="Name of Resgistry"
    )
    @login_namespace.marshal_with(response_model)  # response structure
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("mobile", type=str)
        parser.add_argument("sex", type=str)
        args = parser.parse_args()
        registry_user = RegistryService(
            username=args["username"],
            password=args["password"],
            email=args["email"],
            mobile=args["mobile"],
            sex=args["sex"],
        )
        message, status_code = registry_user.registry()
        user_dict = {
            "username": args["username"],
            "email": args["email"],
            "mobile": args["mobile"],
            "sex": args["sex"],
            "message": message,
        }
        return user_dict, status_code


@login_namespace.route("/login")
class Login(Resource):
    @login_namespace.param("password", type=str, description="Password")
    @login_namespace.param("username", type=str, description="Name of login")
    # indicate the username on the swagger_ui
    @login_namespace.marshal_with(response_model)  #
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        args = parser.parse_args()

        login_user = LoginService(
            username=args["username"],
            password=args["password"],
        )
        message, auth_status, access_token = login_user.login()
        user_dict = {
            "username": args["username"],
            "message": message,
            "access_token": access_token,
        }
        if not login_user.auth_status:
            return user_dict, 401

        return user_dict, 200


@login_namespace.route("/logout")
class Logout(Resource):
    @jwt_required()
    def post(self):
        user = current_user
        login_user = LoginService(
            username=user["username"],
            password=user["password"],
        )
        login_user.logout()
        return {"message": "Logout successful"}, 200


@login_namespace.route("/who_am_i")
class WhoAmI(Resource):
    @jwt_required()
    def get(self):
        user = current_user
        print(1111, user)
        # return jsonify({"id": user.id, "username": user.username}) return a flask response with a json object
        # return {"id": user.id, "username": user.username}, 200 return a flask response with a json object and a status code
        response = make_response(
            jsonify({"id": user.id, "username": user.username}), 201
        )
        # use the make_response function to add headers
        response.headers["Content-Type"] = "application/json"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["X-Parachutes"] = "parachutes are cool"
        return response


# def protected():
#     # We can now access our sqlalchemy User object via `current_user`.
#     return jsonify(
#         id=current_user.id,
#         username=current_user.username,
#     )

# @login_namespace.route("/protected")
# class
# user = User.query.get(current_user_id)
# return jsonify(logged_in_as=user.username), 200


""" 
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
    @login_namespace.doc(
        params={"name": "a name", "rate": "a rate", "User-Agent": "User-Agent"}
    )
    # @login_namespace.doc(responses={403: "not authorized"})
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("rate", type=int, help="rate error", required=True)
        parser.add_argument(
            "name",
            type=str,
            help="name error",
            action="split",
            dest="public_name",
            required=True,
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
        # print(args)
        return resposne, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, location="form")
        parser.add_argument("flag", type=inputs.boolean)

        args = parser.parse_args()
        print(args)
        return args, 200


@login_namespace.route("/upload", doc={"deprecated": True})
class Upload(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("file", location="files", type=FileStorage, required=True)
        args = parser.parse_args()
        uploaded_file = args["file"]
        # 获取上传文件的文件的字节流，以二进制形式读取，然后将其转换为字符串，而不是保存到磁盘里，然后读取
        file_stream = uploaded_file.stream
        # try:
        #     # 读取文件
        #     reader = PyPDF2.PdfReader(file_stream)
        #     text = ""
        #     for page in reader.pages:
        #         text += page.extract_text() or ""
        # login_namespace.logger.info("hello from login_name")
        # return {"id": id, "name": name}, 200
        #     print(text)
        #     return {
        #         "message": "File uploaded successfully",
        #         "content": text,
        #     }, 200
        # except UnicodeDecodeError:
        #     return {"message": "File could not be decoded as UTF-8."}, 400

        # with open(uploaded_file, "rb") as pdf_file:
        #     pdf_reader = PyPDF2.PdfReader(pdf_file)
        #     num_pages = len(pdf_reader.pages)

        #     page = pdf_reader.pages[0]
        #     content = page.extract_text()
        #     print(content)


parser = reqparse.RequestParser()
parser.add_argument("id", type=int, required=True, help="An Id is required")
parser.add_argument("name", type=str, required=True, help="Name is required")


@login_namespace.route("/my-resource")
@login_namespace.route(
    "/other-my-resource/<int:id>",
    doc={"description": "alias for /my-resource api", "deprecated": True},
)
class MyResource(Resource):
    # @login_namespace.expect(resource_fields_model) is equivalent to body parameter of doc
    # @login_namespace.response(200, "Success Request") is equivalent to reponses parameter of doc
    @login_namespace.doc(body=resource_fields_model, responses={200: "Response ok"})
    def post(self):
        return {"name": "jack"}, 200

    @login_namespace.expect(parser)  # requiered, the input fields are required
    @login_namespace.doc(
        params={
            "id": {"description": "An Id", "required": True, "type": "integer"},
            "name": {"description": "Name", "required": True, "type": "string"},
        }
    )
    def get(self):
        args = parser.parse_args()
        id = args["id"]
        name = args["name"]
 """
