from flask import Blueprint, jsonify
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from werkzeug import Response

from app.providers import get_driver

blueprint = Blueprint("crawl", __name__)

URL = "https://www.upwork.com/ab/account-security/login"


@blueprint.route("/")
def index() -> Response:
    driver = get_driver()

    driver.get(URL)

    return jsonify({"source": driver.page_source})
