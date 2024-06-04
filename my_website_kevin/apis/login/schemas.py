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

address_model = login_namespace.model(
    "Address",
    {
        "addr1": fields.String(attribute="address"),
        "city": fields.String,
        "state": fields.String,
        "zip": fields.String,
    },
)

family_model = login_namespace.model(
    "Family", {"id": fields.Integer, "name": fields.String}
)
parent_model = login_namespace.model("Parent", {"name": fields.String})
child_model = login_namespace.clone("Child", parent_model, {"age": fields.Integer})


class AllCapsString(fields.Raw):
    def format(self, value):
        return value.upper()


person_model = login_namespace.model(
    "Person",
    {
        "id": fields.Integer(required=True, description="ID"),
        "name": fields.String(required=True, description="Name"),
        "sex": fields.String(required=True, description="Sex"),
        "age": fields.Integer(required=True, description="Age"),
        "billing_address": fields.Nested(address_model),
        "shipping_address": fields.Nested(address_model),
        # person is the endpoint name when you called api.route()
        # "uri": fields.Url("person", absolute=True),
        "first_names": fields.List(fields.String),
        "family_list": fields.List(fields.Nested(family_model)),
        "all_caps_name": AllCapsString(attribute="name"),
    },
)

resource_fields = {"name": fields.String, "first_names": fields.List(fields.String)}

type_info_model = login_namespace.model(
    "TypeInfo",
    {
        "rate": fields.Integer,
        "name": fields.String,
        "User-Agent": fields.String,
        "*": fields.Wildcard(fields.String),
    },
)
