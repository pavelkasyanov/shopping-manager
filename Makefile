PROJECT = shopping-manager
SRC_DIR := app
VENV_DIR = .venv
PYTHON := python
RUN := . $(VENV_DIR)/bin/activate;
PY_TEST := $(RUN) pytest
PIP_C := $(RUN) pip-compile
PIP_S := $(RUN) pip-sync
.DEFAULT_GOAL := init

venv_init:
	@if [ ! -f "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv $(VENV_DIR) --prompt $(PROJECT); \
	fi
	cp .etc/default/sample_env .env
	$(RUN) pip install pip-tools

venv: venv_init install
	$(RUN) pip install -r requirements.txt

lock:
	$(PIP_C) --output-file=.etc/packages .etc/requirements.in
	$(PIP_C) --output-file=.etc/packages.dev .etc/requirements.dev .etc/requirements.in

install:
	$(PIP_S) .etc/packages.dev

install_no_dev:
	$(PIP_S) .etc/packages
init: venv

lint: flake black

black:
	$(RUN) black . --check

flake:
	$(RUN) flake8 .

fixcode:
	$(RUN) black .

clean:
	rm -rf $(VENV_DIR)
	rm -rf .pytest_cache

force_test:
	$(PY_TEST) --cov-config=.coveragerc --cov=$(SRC_DIR) --cov-report html:.testcov

test: venv lint force_test

include .etc/Makefile_docker

