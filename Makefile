PROJECT = shopping-manager
DB_NAME = shopping_manager
SRC_DIR := app
VENV_DIR = .venv
PYTHON := python3
RUN := . $(VENV_DIR)/bin/activate;
PY_TEST := $(RUN) pytest
PIP_C := $(RUN) pip-compile
PIP_S := $(RUN) pip-sync
.DEFAULT_GOAL := init

venv_init:
	@if [ ! -f "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv $(VENV_DIR) --prompt $(PROJECT); \
	fi
	$(RUN) pip install pip-tools

venv: venv_init install
	$(RUN) pip install -r requirements.txt
	mkdir -p app/static

lock:
	$(PIP_C) --output-file=.etc/packages .etc/requirements.in
	$(PIP_C) --output-file=.etc/packages.dev .etc/requirements.dev .etc/requirements.in

install:
	$(PIP_S) .etc/packages.dev

install_no_dev:
	$(PIP_S) .etc/packages
init: venv

lint: flake black mypy isort

black:
	$(RUN) black --config pyproject.toml . --check

black-fix:
	$(RUN) black --config pyproject.toml .

flake:
	$(RUN) flake8 .

mypy:
	$(RUN) mypy .

isort:
	$(RUN) isort . --check --profile=black

isort-fix:
	$(RUN) isort . --profile=black

fixcode: black-fix isort-fix
	


clean:
	rm -rf $(VENV_DIR)
	rm -rf .pytest_cache

force_test:
	$(PY_TEST) --cov-config=.coveragerc --cov=$(SRC_DIR) --cov-report html:.testcov

test: lint force_test

upgrade_db:
	$(RUN) $(PYTHON) manage.py migrate

create_migration:
	$(RUN) $(PYTHON) manage.py migration --msg "$(msg)"

