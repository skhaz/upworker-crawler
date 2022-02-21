from pyotp import TOTP
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver


def wait_for_ready(driver: webdriver.Chrome, timeout: int) -> None:
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def get_otp(secret: str) -> str:
    return TOTP(secret.replace(" ", "")).now()
