install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# --cov for details on a function
	# test_*.py → python tests files are prefixed as is
	python -m pytest -vv --cov=ma_fonction test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C patient.py

all:
	install lint test format

# personal and not click-setup-installed commands
api_launch:
	python $(CURDIR)/blueprint_fast_api.py