.PHONY: clean format lint test run

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
	mypy $(APP_DIR) --ignore-missing-imports --strict

test:
	pytest --cov=$(APP_DIR) -vvv -s tests

run: format lint type test
	gunicorn --bind :3000 --timeout 0 --reload app.main:app
