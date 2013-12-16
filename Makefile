.PHONY: nosetests test flake8

help:
	@echo 'Usage:                                               '
	@echo '   make test                Run tests                '
	@echo '                                                     '

test: nosetests flake8

nosetests:
	@echo '========== Running nosetests =========='
	@echo ''
	@nosetests --with-doctest
	@echo ''

flake8:
	@echo '========== Running flake8 =========='
	@echo ''
	@flake8 py_api tests
	@echo ''
