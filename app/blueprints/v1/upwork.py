from flask import Blueprint
from flask_pydantic import validate

from app.crawlers.upwork import run as upwork_run
from app.models import RequestBody, User

blueprint = Blueprint("crawl", __name__)


@blueprint.post("/")
@validate()  # type: ignore # because Flask-Pydantic does not have typing
def index(body: RequestBody) -> User:
    return upwork_run(
        body.username,
        body.password,
        body.tries,
        body.secret_answer,
        body.authenticator_secret_key,
    )
