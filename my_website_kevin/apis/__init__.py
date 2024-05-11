from flask_restx import Api

from my_website_kevin.apis.login.schemas import login_namespace

api = Api(
    version="1.0",
    title="My Website",
    description="This is a simple API for my website",
    prefix="/api"
    # base_path="/api/v1"
    # default="api"
    # default_label="My Website API"
    # default_mediatype="application/json"
    # validate=True
    # mask_headers=True
)

api.add_namespace(login_namespace)
