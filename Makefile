help:
	@echo 'Usage:                                               '
	@echo '   make test                Run tests                '
	@echo '                                                     '

test:
	@nosetests-2.7 --with-doctest
