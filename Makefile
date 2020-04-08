format:
	black --line-length 132 epidoc/ tests/

check: format-check unittest

format-check:
	black --check --line-length 132 epidoc/ tests/

unittest:
	python -m unittest discover

publish:
	python setup.py sdist bdist_wheel
