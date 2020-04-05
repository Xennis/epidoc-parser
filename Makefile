format:
	black --line-length 132 *.py

check: format-check unittest

format-check:
	black --check --line-length 132 *.py

unittest:
	python -m unittest discover -p '*_test.py'
