import os

from selenium_stealth import stealth
from seleniumwire import webdriver


def get_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()

    if os.environ.get("HEADLESS"):
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--no-zygote")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-accelerated-2d-canvas")
    options.add_argument("--disable-translate")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-permissions-api")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    executable_path = os.environ.get("CHROMEDRIVER_PATH", "chromedriver")

    driver = webdriver.Chrome(
        executable_path,
        options=options,
    )

    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    return driver