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
	$(PYRUN) ruff check --select F --show-files $(SRC) # Optional: strict error-only

lint: mypy ruff

precommit-install:
	uv run pre-commit install

precommit-run:
	uv run pre-commit run --all-files
