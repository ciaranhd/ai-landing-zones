.PHONY: mypy lint precommit-install precommit-run

SRC ?= src/data_product_1

help:
	@echo "Targets:"
	@echo "  make mypy"
	@echo "  make lint"
	@echo "  make precommit-install"
	@echo "  make precommit-run"

mypy:
	uv run mypy $(SRC)

lint: mypy

precommit-install:
	uv run pre-commit install

precommit-run:
	uv run pre-commit run --all-files
