from dotenv import load_dotenv
from flask import Flask

from app.blueprints.v1.upwork import blueprint as upwork_blueprint_v1

load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(upwork_blueprint_v1, url_prefix="/v1")

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
