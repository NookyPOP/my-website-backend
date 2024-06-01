from flask_restx import fields, Namespace

login_namespace = Namespace("auth")

login_model = login_namespace.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)
