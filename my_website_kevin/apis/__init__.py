from flask_restx import Api
from apis.login.views import login_namespace as ns

api = Api(
    title="My Title",
    version="1.0",
    description="A description",
)

# the namespace must be added resources and routes
api.add_namespace(ns)
