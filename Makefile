APP=upload-service
PORT=5000

venv:
	python3 -m venv .venv

install:
	.venv/bin/pip install -r requirements.txt

install-dev:
	.venv/bin/pip install -r requirements-dev.txt

run:
	PORT=$(PORT) .venv/bin/python run.py

test:
	.venv/bin/pytest tests/

lint:
	.venv/bin/flake8 app/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
