# Description: Makefile for the project

.PHONY: venv dependencies update-dependencies

venv:
	python3 -m venv .env

dependencies:
	pip install -r requirements.txt

update-dependencies:
	pip install pip-tools
	pip-compile --upgrade --output-file requirements.txt requirements.in

run:
	python3 main.py