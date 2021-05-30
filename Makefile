PROJECT = shopping-manager
VENV_DIR = .venv
PYTHON = python3
PI = . $(VENV_DIR)/bin/activate ;
PY_TEST = pytest

.DEFAULT_GOAL := init

venv_init:
	@if [ ! -f "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv $(VENV_DIR) --prompt $(PROJECT); \
	fi
	cp .etc/default/simple_env .env
venv: venv_init
	$(PI) pip install -r requirements.txt

init: venv

clean:
	rm -rf $(VENV_DIR)
	rm -rf .pytest_cache

test: venv
	$(PI) $(PY_TEST)
