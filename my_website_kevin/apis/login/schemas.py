from flask_restx import fields, Namespace

ns = Namespace("auth")

login_model = ns.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)
