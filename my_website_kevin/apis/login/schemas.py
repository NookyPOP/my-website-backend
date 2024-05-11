from flask_restx import fields, Namespace

login_namespace = Namespace("auth", description="Login related operations")

login_model = login_namespace.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
        "email": fields.String(required=True, description="Email"),
        "phone": fields.String(required=True, description="Phone"),
        "address": fields.String(required=True, description="Address"),
    },
)
