.PHONY: run fmt lint typecheck test check clean

run:
	docker-compose up

lint:
	poetry run ruff check app tests

fmt:
	poetry run ruff format app tests
	poetry run ruff check --fix app tests

typecheck:
	poetry run mypy app tests

test:
	poetry run pytest -v -s

check: fmt lint typecheck test

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
