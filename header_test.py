import os
import unittest

from bs4 import BeautifulSoup

from header import History, ProfileDesc

TESTDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata")


class TestHistory(unittest.TestCase):
    def test_all(self):
        tests = [
            (
                "1.xml",
                [{"text": "30. Jan. 3 v.Chr.", "when": "-0003-01-30",}],
                {
                    "located": [
                        {
                            "ref": ["http://pleiades.stoa.org/places/736986", "http://www.trismegistos.org/place/2869",],
                            "text": "Paimis",
                            "type": "ancient",
                        },
                        {"subtype": "nome", "text": "Oxyrhynchites", "type": "ancient",},
                        {"subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                    "text": "Paimis (Oxyrhynchites)",
                },
            ),
            (
                "2.xml",
                [{"notafter": "0909", "notbefore": "0881", "text": "881 - 909",}],
                {
                    "composed": [
                        {
                            "ref": ["https://www.trismegistos.org/place/2800"],
                            "subtype": "region",
                            "text": "Middle Egypt",
                            "type": "ancient",
                        },
                        {"subtype": "region", "text": "Egypt", "type": "ancient",},
                    ],
                    "found": [
                        {
                            "ref": ["https://www.trismegistos.org/place/2800"],
                            "subtype": "region",
                            "text": "Middle Egypt",
                            "type": "ancient",
                        },
                        {"subtype": "region", "text": "Egypt", "type": "ancient",},
                    ],
                    "text": "Found: Middle Egypt (Egypt); written: Middle Egypt (Egypt)",
                },
            ),
            (
                "3.xml",
                [{"notafter": "0225", "notbefore": "0101", "precision": "low", "text": "II - Anfang III",}],
                {
                    "found": [{"text": "unbekannt"}],
                    "located": [
                        {"cert": "low", "subtype": "nome", "text": "Hermopolites", "type": "ancient",},
                        {"subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                    "text": "unbekannt (Hermopolites ?)",
                },
            ),
            (
                "4.xml",
                # TODO: Parse certainty
                [{"text": "9. Okt. 141 (Monat und Tag unsicher)", "when": "0141-10-09",}],
                {
                    "located": [
                        {
                            "ref": ["http://pleiades.stoa.org/places/737053", "http://www.trismegistos.org/place/2157",],
                            "text": "Soknopaiu Nesos",
                            "type": "ancient",
                        },
                        {"subtype": "nome", "text": "Arsinoites", "type": "ancient",},
                        {"subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                    "text": "Soknopaiu Nesos (Arsinoites)",
                },
            ),
            (
                "5.xml",
                [{"notafter": "0143", "notbefore": "0142", "text": "142 - 143",}],
                {
                    "found": [{"text": "unbekannt"}],
                    "located": [{"subtype": "region", "text": "Oberägypten", "type": "ancient",}],
                    "text": "unbekannt (Oberägypten)",
                },
            ),
            ("6.xml", [{"notafter": "0400", "notbefore": "0001", "precision": "low", "text": "I - IV",}], {"text": "unbekannt"},),
            (
                "7.xml",
                [{"notafter": "0710", "notbefore": "0709", "text": "ṣafar 91 AH",}],
                {
                    "located": [{"ref": ["http://www.trismegistos.org/place/237"], "text": "Išqawh",}],
                    "ref": "http://www.trismegistos.org/place/237",
                    "text": "Išqawh",
                },
            ),
            (
                "8.xml",
                [{"notafter": "1132", "notbefore": "1132", "text": "2nd decade of muḥarram 527 AH",}],
                {
                    "located": [{"ref": ["http://www.trismegistos.org/place/332"], "text": "unknown (al-Fayyūm)",}],
                    "ref": "http://www.trismegistos.org/place/332",
                    "text": "unknown (al-Fayyūm)",
                },
            ),
            (
                "9.xml",
                [{"cert": "low", "precision": "medium", "text": "ca. 340 (?)", "when": "0340",}],
                {
                    "located": [
                        {"subtype": "nome", "text": "Hermopolites", "type": "ancient",},
                        {"subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                    "text": "Hermopolites",
                },
            ),
            (
                "10.xml",
                [{"cert": "low", "notafter": "-0001", "notbefore": "-0200", "precision": "low", "text": "II - I v.Chr. (?)",}],
                {"text": "unbekannt"},
            ),
            ("11.xml", [{"text": "unbekannt"}], {"text": "unbekannt"},),
            (
                "12.xml",
                [
                    {
                        "cert": "low",
                        "notafter": "0358",
                        "notbefore": "0357",
                        "text": "ca. 357 - 358 (?)",
                        "xml:id": "datealternativex",
                    },
                    {
                        "cert": "low",
                        "notafter": "0373",
                        "notbefore": "0372",
                        "text": "ca. 372 - 373 (?)",
                        "xml:id": "datealternativey",
                    },
                ],
                {
                    "located": [
                        {
                            "ref": [
                                "http://pleiades.stoa.org/places/736982",
                                "http://www.trismegistos.org/place/2722",
                                "http://www.trismegistos.org/place/1524",
                            ],
                            "text": "Oxyrhynchos",
                            "type": "ancient",
                        }
                    ],
                    "text": "Oxyrhynchos",
                },
            ),
            (
                "13.xml",
                [{"notafter": "0162-01", "notbefore": "0161-09", "text": "ca. Sept. 161 - Jan. 162",}],
                {
                    "located": [
                        {
                            "ref": [
                                "http://pleiades.stoa.org/places/736982",
                                "http://www.trismegistos.org/place/2722",
                                "http://www.trismegistos.org/place/1524",
                            ],
                            "text": "Oxyrhynchos",
                            "type": "ancient",
                        }
                    ],
                    "text": "Oxyrhynchos",
                },
            ),
            (
                "14.xml",
                [{"notafter": "0750", "notbefore": "0701", "precision": "low", "text": None,}],
                {
                    "located": [
                        {
                            "ref": [
                                "http://pleiades.stoa.org/places/991398",
                                "http://www.trismegistos.org/place/2983",
                                "http://www.trismegistos.org/place/1281",
                            ],
                            "text": "Theben",
                            "type": "ancient",
                        },
                        {"key": "aegyptus", "subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                    "text": "Theben",
                },
            ),
        ]
        for (filename, want_origin_dates, want_places) in tests:
            with open(os.path.join(TESTDATA_DIR, "header-history", filename)) as f:
                elem = BeautifulSoup(f.read(), features="lxml").history
            actual_dates = History.origin_dates(elem)
            self.assertEqual(want_origin_dates, actual_dates, msg=f"{filename} dates")
            actual_places = History.places(elem)
            self.assertEqual(want_places, actual_places, msg=f"{filename} places")


class TestProfileDesc(unittest.TestCase):
    def test_all(self):
        tests = [
            (
                "1.xml",
                [
                    {"text": "prose"},
                    {"text": "gospel"},
                    {"text": "literature", "type": "culture"},
                    {"text": "christian", "type": "religion"},
                    {"text": "New Testament, Johannes evang.; gospel Joh. 1.25-28, 33-38, 42-44", "type": "overview"},
                ],
                {"en": "English", "grc": "Greek"},
            ),
            (
                "2.xml",
                [
                    {"text": "prose"},
                    {"text": "novel"},
                    {"text": "literature", "type": "culture"},
                    {"text": "classical", "type": "religion"},
                    {"text": "Panionis (novel)", "type": "overview"},
                ],
                {"en": "English", "grc": "Greek"},
            ),
            (
                "3.xml",
                [{"text": "doc"}],
                {
                    "de": "Deutsch",
                    "el": "Griechisch",
                    "en": "Englisch",
                    "es": "Spanisch",
                    "fr": "Französisch",
                    "it": "Italienisch",
                    "la": "Latein",
                },
            ),
            (
                "4.xml",
                [{"text": None}],
                {
                    "de": "Deutsch",
                    "el": "Griechisch",
                    "en": "Englisch",
                    "es": "Spanisch",
                    "fr": "Französisch",
                    "it": "Italienisch",
                    "la": "Latein",
                },
            ),
            (
                "5.xml",
                [
                    {"text": "Auszug aus Akten des Besitzarchivs; Briefe (amtlich)"},
                    {"text": "Stratege"},
                    {"text": "Präfekt; Liturgie"},
                    {"text": "Verschuldung gegenüber dem Staat"},
                    {"text": "Konfiskation"},
                    {"text": "Verkauf aus Staatsbesitz"},
                    {"text": "Versteigerung"},
                ],
                {
                    "de": "Deutsch",
                    "el": "Griechisch",
                    "en": "Englisch",
                    "es": "Spanisch",
                    "fr": "Französisch",
                    "it": "Italienisch",
                    "la": "Latein",
                },
            ),
            (
                "6.xml",
                [
                    {"n": "1", "text": "Zahlung"},
                    {"n": "2", "text": "Auftrag"},
                    {"n": "3", "text": "Anagnostes"},
                    {"n": "4", "text": "Notar"},
                    {"n": "5", "text": "Kollektarios"},
                    {"n": "6", "text": "Geld"},
                ],
                {
                    "de": "Deutsch",
                    "el": "Griechisch",
                    "en": "Englisch",
                    "es": "Spanisch",
                    "fr": "Französisch",
                    "it": "Italienisch",
                    "la": "Latein",
                },
            ),
            ("7.xml", [], {"egy-egyd": "Demotic", "en": "English", "grc": "Greek"},),
            (
                "8.xml",
                [
                    {"text": "medicine"},
                    {"text": "science", "type": "culture"},
                    {"text": "two medical prescriptions", "type": "overview"},
                ],
                {},
            ),
        ]
        for (filename, want_terms, want_langs) in tests:
            with open(os.path.join(TESTDATA_DIR, "header-profile-desc", filename)) as f:
                elem = BeautifulSoup(f.read(), features="lxml").profiledesc
            actual_terms = ProfileDesc.keyword_terms(elem)
            self.assertEqual(want_terms, actual_terms, msg=f"{filename} terms")
            actual_langs = ProfileDesc.lang_usage(elem)
            self.assertEqual(want_langs, actual_langs, msg=f"{filename} langs")
