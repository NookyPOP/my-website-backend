from my_website_kevin.app import create_app
from my_website_kevin.apis import api
from my_website_kevin.apis.login.schemas import ns as login_namespace


app = create_app()

if __name__ == "__main__":
    api.add_namespace(login_namespace)
    app.run(host="0.0.0.0", port=5099, debug=True)
