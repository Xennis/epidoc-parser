format:
	black --target-version py38 --line-length 132 *.py epidoc/ tests/

check: format-check unittest

format-check:
	black --check --target-version py38 --line-length 132 *.py epidoc/ tests/

unittest:
	python -m unittest discover

publish:
	python setup.py sdist bdist_wheel
