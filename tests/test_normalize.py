import unittest

from epidoc.normalize import _normalize


class TestNormalize(unittest.TestCase):
    def test_string(self):
        self.assertEqual("hallo world", _normalize("  Hallo World  "))

    def test_not_string(self):
        self.assertEqual(12, _normalize(12))
