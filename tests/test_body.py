import os
import unittest

from bs4 import BeautifulSoup

from epidoc.body import _Edition

TESTDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata")


class EditionTest(unittest.TestCase):
    def test_all(self):
        tests = [
            (
                "1.xml",
                "grc",
                {"la": 2},
            ),
            (
                "2.xml",
                "grc",
                {"la": 26},
            ),
        ]
        for (filename, want_language, want_foreign_languages) in tests:
            with self.subTest(filename):
                with open(os.path.join(TESTDATA_DIR, "body", filename)) as f:
                    elem = BeautifulSoup(f.read(), features="lxml")
                actual_language = _Edition.language(elem)
                self.assertEqual(want_language, actual_language, msg="language")
                actual_foreign_languages = _Edition.foreign_languages(elem)
                self.assertEqual(want_foreign_languages, actual_foreign_languages, msg="foreign languages")
