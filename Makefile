install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C patient.py

test:
	python -m pytest -vv

format:
	black *.py

all:
	install lint test format
