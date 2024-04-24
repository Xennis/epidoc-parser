format:
	black --target-version py39 --line-length 132 --exclude tests/testdata/ *.py epidoc/ tests/

check: format-check type-check unittest

format-check:
	black --check --target-version py39 --line-length 132 --exclude tests/testdata/ *.py epidoc/ tests/

type-check:
	mypy epidoc

unittest:
	python -m unittest discover

integrationtest:
	python -m unittest discover -p "integration_*.py"

publish:
	python setup.py sdist bdist_wheel
