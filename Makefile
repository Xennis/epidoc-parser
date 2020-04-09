format:
	black --target-version py38 --line-length 132 --exclude tests/testdata/ *.py epidoc/ tests/

check: format-check unittest

format-check:
	black --check --target-version py38 --line-length 132 --exclude tests/testdata/ *.py epidoc/ tests/

unittest:
	python -m unittest discover

integrationtest:
	python -m unittest discover -p "integration_*.py"

publish:
	python setup.py sdist bdist_wheel
