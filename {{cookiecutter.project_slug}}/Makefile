.PHONY: clean clean-test clean-pyc clean-build
.DEFAULT_GOAL := help

export PYTHONPATH:=.:${PYTHONPATH}

VENV_NAME?=.venv

SOURCE_DIR={{cookiecutter.project_slug}}

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr .mypy_cache/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-venv: ## remove virtualenv
	rm -rf ${VENV_NAME}

venv: $(VENV_NAME)/bin/activate pip-sync

$(VENV_NAME)/bin/activate:
	test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -U pip pip-tools

pip-compile: ## compile requirements with pip-compile
	$(VENV_NAME)/bin/pip-compile --quiet \
		--upgrade \
		--output-file requirements.txt  \
		setup.py requirements*.in

pip-sync: ## sync venv
	$(VENV_NAME)/bin/pip-sync requirements*.txt

test-all: venv pip-sync ## run tests on every Python version with tox
	$(VENV_NAME)/bin/tox

lint: venv ## check style with pylint
	$(VENV_NAME)/bin/black ${SOURCE_DIR}
