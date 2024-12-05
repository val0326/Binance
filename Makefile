# Backend REGION START
start_dev:
	poetry run uvicorn  src.main:app --reload

migrations:
	alembic revision --autogenerate

migrate:
	poetry run alembic upgrade head
# Backend REGION END

# Tests
test:
	pytest -v tests

# Linters
format:
	poetry run black src && poetry run isort src
# Linters REGION END

.PHONY: start_dev migrations migrate sort test