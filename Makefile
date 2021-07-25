.PHONY: install install-dev install-test build-*

ENV ?= .hm-common-venv
RUN = . $(ENV)/bin/activate &&

.hm-common-venv:
	virtualenv $(ENV) --python=python3.8
	touch $@

install: .hm-common-venv requirements.txt
	$(RUN) pip install -r requirements.txt

install-dev: install-test
	$(RUN) pip install -r requirements-dev.txt
	$(RUN) pre-commit install && pre-commit install -t pre-push

install-test: install
	$(RUN) pip install -r requirements-test.txt

clean:
	rm -rf $(ENV)
