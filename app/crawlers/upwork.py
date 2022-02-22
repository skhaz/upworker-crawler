from typing import Optional

from retry import retry
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver

from app.helpers import get_otp, wait_for_ready
from app.models import User
from app.providers import get_driver

URL = "https://www.upwork.com/ab/account-security/login"


def fill_username_and_continue(
    driver: webdriver.Chrome,
    wait: WebDriverWait,
    username: str,
) -> None:
    element_id = "login_username"
    element = wait.until(EC.presence_of_element_located((By.ID, element_id)))
    element.send_keys(username)

    button_id = "login_password_continue"
    button = driver.find_element_by_id(button_id)
    button.click()


def fill_password_and_continue(
    driver: webdriver.Chrome,
    wait: WebDriverWait,
    password: str,
) -> None:
    element_id = "login_password"
    element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
    element.send_keys(password)

    button_id = "login_control_continue"
    button = driver.find_element_by_id(button_id)
    button.click()


def fill_secret_answer_and_continue(
    driver: webdriver.Chrome,
    wait: WebDriverWait,
    secret_answer: str,
) -> None:
    element_id = "login_answer"
    element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
    element.send_keys(secret_answer)

    button_id = "login_control_continue"
    button = driver.find_element_by_id(button_id)
    button.click()


def fill_otp_password_and_continue(
    driver: webdriver.Chrome,
    wait: WebDriverWait,
    authenticator_secret_key: str,
) -> None:
    otp = get_otp(authenticator_secret_key)

    element_id = "deviceAuthOtp_otp"
    element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
    element.send_keys(otp)

    button_id = "next_continue"
    button = driver.find_element_by_id(button_id)
    button.click()


def get_fullname(wait: WebDriverWait) -> str:
    button_xpath = "//*[@id='nav-right']/ul/li[9]/button"
    button = wait.until(EC.visibility_of_element_located((By.XPATH, button_xpath)))
    button.click()

    wait.until(EC.visibility_of_element_located((By.ID, "main")))
    xpath = "//*[@id='nav-right']/ul/li[9]/ul/li[2]/ul/li/a/div/div[1]"
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    return str(element.text)


def run(
    username: str,
    password: str,
    tries: int,
    secret_answer: Optional[str],
    authenticator_secret_key: Optional[str],
) -> User:
    @retry(tries=tries)
    def _exec(
        username: str,
        password: str,
        secret_answer: Optional[str],
        authenticator_secret_key: Optional[str],
    ) -> User:
        driver = get_driver()

        driver.get(URL)

        wait_for_ready(driver, 60)

        wait = WebDriverWait(driver, 10)

        fill_username_and_continue(driver, wait, username)

        fill_password_and_continue(driver, wait, password)

        if secret_answer:
            fill_secret_answer_and_continue(driver, wait, secret_answer)

        if authenticator_secret_key:
            fill_otp_password_and_continue(driver, wait, authenticator_secret_key)

        fullname = get_fullname(wait)

        name, surname = fullname.strip().split(" ")

        return User(name=name, surname=surname)

    return _exec(username, password, secret_answer, authenticator_secret_key)
