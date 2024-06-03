from flask_restx import fields, Namespace

login_namespace = Namespace("auth")

login_model = login_namespace.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)

user_model = login_namespace.model(
    "User",
    {
        "username": fields.String(required=True, description="Username"),
        "mobile": fields.String(required=True, description="Mobile"),
        "sex": fields.String(required=True, description="Sex"),
    },
)


class SentItem(fields.Raw):
    def format(self, value):
        return "Sent" if value & 0x01 else "Not sent"


class ReceivedItem(fields.Raw):
    def format(self, value):
        return "Received" if value & 0x02 else "Not received"


class SpamItem(fields.Raw):
    def format(self, value):
        return "Spam" if value & 0x04 else "Not spam"


emails = login_namespace.model(
    "Emails",
    {
        "id": fields.Integer(required=True, description="ID"),
        "email": fields.String(required=True, description="Email"),
        "sent_status": SentItem(attribute="status_code"),
        "received_status": ReceivedItem(attribute="status_code"),
        "spam_status": SpamItem(attribute="status_code"),
    },
)

person_model = login_namespace.model(
    "Person",
    {
        "id": fields.Integer(required=True, description="ID"),
        "name": fields.String(required=True, description="Name"),
        "sex": fields.String(required=True, description="Sex"),
        "age": fields.Integer(required=True, description="Age"),
        "address": {
            "line 1": fields.String(attribute="address1"),
            "line 2": fields.String(attribute="address2"),
            "city": fields.String,
            "state": fields.String,
            "zip": fields.String,
        },
    },
)
