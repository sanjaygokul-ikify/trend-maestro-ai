# Makefile for Maestro AI

install:
	pip install -r requirements.txt

run:
	python maestro.py

docs:
	python -m sphinx docs

clean:
	python -m pip uninstall -y maestro-ai
	rm -rf __pycache__
	rm -rf env
	rm -rf venv
