import os

from capmonster_python import RecaptchaV2Task
from retry import retry
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver


def find_sitekey(driver: webdriver.Chrome) -> str:
    return str(
        WebDriverWait(driver, 10)
        .until(EC.element_to_be_clickable((By.CLASS_NAME, "g-recaptcha")))
        .get_attribute("data-sitekey")
    )


def recaptcha_set_result(
    driver: webdriver.Chrome,
    result: str,
    element_id: str,
) -> None:

    driver.execute_script(
        f"""
        document.getElementById("{element_id}").style.display = 'block';
        """
    )

    driver.execute_script(
        f"""
        document.getElementById("{element_id}").value = arguments[0];
        """,
        result,
    )


@retry(tries=3)
def solve_recaptcha(driver: webdriver.Chrome) -> None:
    url = driver.current_url

    sitekey = find_sitekey(driver)

    print("reCAPTCHA sitekey:", sitekey)

    capmonster = RecaptchaV2Task(os.environ["CAPMONSTER_TOKEN"])
    task_id = capmonster.create_task(website_key=sitekey, website_url=url)
    result = capmonster.join_task_result(task_id)

    print("reCAPTCHA result:", result)

    recaptcha_set_result(driver, result, "g-recaptcha-response")
