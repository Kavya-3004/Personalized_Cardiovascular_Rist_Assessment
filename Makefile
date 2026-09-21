.PHONY: help install test run clean docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install      : Install dependencies"
	@echo "  make test         : Run unit and integration tests"
	@echo "  make run          : Launch Streamlit web interface"
	@echo "  make clean        : Remove Python bytecode and caches"
	@echo "  make docker-build : Build the Docker image"
	@echo "  make docker-run   : Run the Docker container"

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	python -m unittest discover tests

run:
	streamlit run app.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

docker-build:
	docker build -t cardio-risk-app .

docker-run:
	docker run -p 8501:8501 cardio-risk-app
