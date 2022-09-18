install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=training

lint:
	poetry run flake8 --ignore F405,F403

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

.PHONY: install test lint selfcheck check build