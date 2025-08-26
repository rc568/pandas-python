.PHONY: install install-dev run test format

.venv/bin/activate:
	@# suprime la salida
	@test -d .venv || uv venv .venv --python=3.10.11  

install: .venv/bin/activate
	uv sync

install-dev: .venv/bin/activate
	uv sync --dev

run:
	uv run src/main.py

test:
	uv test tests/

lint:
	uv run ruff check src/
