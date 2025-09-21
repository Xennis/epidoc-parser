format:
	black --target-version py39 --line-length 132 --exclude tests/testdata/ *.py epidoc_parser/ tests/

check: format-check type-check unittest

format-check:
	black --check --target-version py39 --line-length 132 --exclude tests/testdata/ *.py epidoc_parser/ tests/

type-check:
	mypy epidoc_parser

unittest:
	python -m unittest discover

integrationtest:
	python -m unittest discover -p "integration_*.py"

publish:
	python setup.py sdist bdist_wheel
