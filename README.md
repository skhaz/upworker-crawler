
## Goals

* Docker for containerization, including Chrome and chromedriver
* Flask with blueprints for better code organization
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

### Using the API

I am using HTTPie because is more simple than cURL JSON.

Getting the name and surname of an user without OTP:

``` shell
http http://localhost:3000/v1/ username=username password=password secret_answer=secret
```

Getting the same information of an user with OTP:

``` shell
http http://localhost:3000/v1/ username=username password=password authenticator_secret_key="AAAA BBBB CCCC DDD"
```
