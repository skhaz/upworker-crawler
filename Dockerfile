FROM python:3.9 AS base

ENV PATH "/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

FROM base AS test
WORKDIR /tests
RUN python -m venv /opt/venv
COPY requirements requirements
RUN pip install --no-cache-dir --upgrade pip --requirement requirements/tests.txt
COPY app app
COPY tests tests
RUN python -m pytest tests

FROM base AS builder
RUN python -m venv /opt/venv
COPY requirements requirements
RUN pip install --no-cache-dir --upgrade pip --requirement requirements/common.txt

FROM base

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN apt-get install -yqq unzip
RUN wget -qO /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

COPY --from=builder /opt/venv /opt/venv
COPY app/ app/

ENV DISPLAY=:1

ENV HEADLESS=1

ARG PORT=3000
ENV PORT $PORT
EXPOSE $PORT

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app.main:app