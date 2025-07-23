.PHONY: install install-dev run test format

.venv/bin/activate:
	@# suprime la salida
	@test -d .venv || uv venv .venv --python=3.10.11  

install: .venv/bin/activate
	uv sync

install-dev: .venv/bin/activate
	uv sync --dev

run:
	python src/main.py

test:
	pytest tests/

format:
	ruff check . --fix
