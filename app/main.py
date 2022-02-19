from flask import Flask

from app.blueprints.v1.crawl import blueprint as crawl_blueprint_v1


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(crawl_blueprint_v1, url_prefix="/v1")

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
