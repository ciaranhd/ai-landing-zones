.PHONY: mypy lint precommit-install precommit-run
PYRUN = uv run

SRC ?= src/data_product_1

help:
	@echo "Targets:"
	@echo "  make mypy"
	@echo "  make lint"
	@echo "  make precommit-install"
	@echo "  make precommit-run"

mypy:
	uv run mypy $(SRC)

ruff:
	$(PYRUN) ruff check $(SRC)

lint: ruff mypy

bandit:
	uv run bandit -r src/data_product_1 -ll -ii
safety:
	uv run safety check --full-report

license_check:
	uv run pip-licenses
	uv run pip-licenses --fail-on "GPL" --partial-match
# Tests
test:
	uv run pytest tests
coverage:
	uv run pytest --cov=src/data_product_1 --cov-report=term-missing tests



