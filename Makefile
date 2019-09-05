IMAGE_NAME='Forge-JWTValidate'
BUILD=1
VERSION=0.1.$(BUILD)

.DEFAULT: help
help:
	@echo "make init"
	@echo "   prepare development environment and create virtualenv"
	@echo "make lint"
	@echo "   run lint and pytype only"

init:
	rm -rf .venv
	virtualenv --python=python3 --always-copy .venv
	( \
    . .venv/bin/activate; \
    pip3 install -r requirements.txt; \
    )

lint: python-build

python-build:
	( \
    . .venv/bin/activate; \
    pylint -j 4 --rcfile=pylintrc jwtvalidate.py; \
	pylint -j 4 --rcfile=pylintrc jwtvalidate_logic; \
    )
