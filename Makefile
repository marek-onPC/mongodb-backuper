.PHONY: run, test


run:
	poetry run python main.py

test:
	PYTHONPATH=. pytest

test-print:
	PYTHONPATH=. pytest -s
