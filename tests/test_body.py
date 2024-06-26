import os
import unittest

from bs4 import BeautifulSoup

from epidoc.body import _Edition, _Head

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
        for filename, want_language, want_foreign_languages in tests:
            with self.subTest(filename):
                with open(os.path.join(TESTDATA_DIR, "body", filename)) as f:
                    elem = BeautifulSoup(f.read(), features="lxml")
                actual_language = _Edition.language(elem)
                self.assertEqual(want_language, actual_language, msg="language")
                actual_foreign_languages = _Edition.foreign_languages(elem)
                self.assertEqual(want_foreign_languages, actual_foreign_languages, msg="foreign languages")


class HeadTest(unittest.TestCase):
    def test_all(self):
        tests = [
            (
                "3.xml",
                ["p.oxy;10;1271", "chla;4;266"],
                [],
            ),
            (
                "4.xml",
                [],
                ["c.ep.lat;;213"],
            ),
        ]
        for filename, want_reprint_from, want_reprint_in in tests:
            with self.subTest(filename):
                with open(os.path.join(TESTDATA_DIR, "body", filename)) as f:
                    elem = BeautifulSoup(f.read(), features="lxml")
                actual_reprint_from = _Head.reprint_from(elem)
                self.assertEqual(want_reprint_from, actual_reprint_from, msg="reprint from")
                actual_reprint_in = _Head.reprint_in(elem)
                self.assertEqual(want_reprint_in, actual_reprint_in, msg="reprint in")
