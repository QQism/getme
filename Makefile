.PHONY: all test clean-pyc

all: clean-pyc test

test:
	py.test run-tests.py

test-deps:
	pip install -r requirements.txt

deps: beautifulsoup4

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
