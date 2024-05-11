from my_website_kevin.app import create_app
from my_website_kevin.apis import api

app = create_app()

if __name__ == "__main__":
    api.init_app(app)
    app.run(host="0.0.0.0", port=5099, debug=True)
