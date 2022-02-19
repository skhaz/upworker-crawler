.PHONY: clean format lint run test

export PYTHONPATH=.

APP_DIR := "app/"

clean:
	find . -type f -name "*.py[c|o]" -exec rm -f {} +
	find . -type d -name  "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache
	rm -rf .coverage htmlcov
	rm -rf .mypy_cache

format:
	isort $(APP_DIR)
	black $(APP_DIR)

lint:
	flake8 --max-line-length=88 $(APP_DIR)

type:
	mypy $(APP_DIR) --strict

run:
	gunicorn --bind :3000 --reload app.main:app

test:
	pytest --cov=$(APP_DIR) -vvv -s tests
