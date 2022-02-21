
## Goals

* Docker for containerization, including Chrome and chromedriver
* Flask for API with blueprints
* Pydantic for models and input validation
* Selenium Wire and Stealth for avoid website block
* Mypy for typing check
* Flake8 for linting
* Pytest for unit testing
* Black for pep8 auto-format
* Clean code
* Makefile for common tasks

### Running

#### Build and run with docker

Build:

``` shell
DOCKER_BUILDKIT=0 docker build --tag crawler:latest .
```

Run:

``` shell
docker run -p 3000:3000 -it crawler:latest
```

#### Build and run with virtualenv

In order to run locally, Google Chrome and `chromedriver` is requred in the PATH.

First, create a new virtual env:

``` shell
python3 -m venv venv
source venv/bin/activate
```

Then, install the dependencies:

``` shell
pip install -r requirements/development.txt
```

Run with Makefile:

``` shell
make run
```

`make run` will run lint, mypy, tests and format.

### What is missing?

I tried to solve the reCAPTCHA using capmonster but had no luck, every time that a captcha was solved, the website shows again and again.

And tests, more tests!