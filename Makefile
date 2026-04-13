.PHONY: run fmt lint typecheck test check create_db clean

run:
	docker-compose up

lint:
	poetry run ruff check app tests scripts

fmt:
	poetry run ruff format app tests scripts
	poetry run ruff check --fix app tests scripts

typecheck:
	poetry run mypy app tests scripts

test:
	poetry run pytest -v -s

check: fmt lint typecheck test

create_db:
	poetry run python -m scripts.create_db
	
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
