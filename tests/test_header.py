import os
import unittest

from bs4 import BeautifulSoup

from epidoc.header import _History, _ProfileDesc

TESTDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata")


class TestHistory(unittest.TestCase):
    def test_all(self):
        tests = [
            (
                "1.xml",
                [{"text": "30. Jan. 3 v.Chr.", "when": "-0003-01-30",}],
                {"text": "Paimis (Oxyrhynchites)",},
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
                },
            ),
            (
                "2.xml",
                [{"notafter": "0909", "notbefore": "0881", "text": "881 - 909",}],
                {"text": "Found: Middle Egypt (Egypt); written: Middle Egypt (Egypt)",},
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
                },
            ),
            (
                "3.xml",
                [{"notafter": "0225", "notbefore": "0101", "precision": "low", "text": "II - Anfang III",}],
                {"text": "unbekannt (Hermopolites ?)",},
                {
                    "found": [{"text": "unbekannt"}],
                    "located": [
                        {"cert": "low", "subtype": "nome", "text": "Hermopolites", "type": "ancient",},
                        {"subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                },
            ),
            (
                "4.xml",
                # TODO: Parse certainty
                [{"text": "9. Okt. 141 (Monat und Tag unsicher)", "when": "0141-10-09",}],
                {"text": "Soknopaiu Nesos (Arsinoites)",},
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
                },
            ),
            (
                "5.xml",
                [{"notafter": "0143", "notbefore": "0142", "text": "142 - 143",}],
                {"text": "unbekannt (Oberägypten)",},
                {"found": [{"text": "unbekannt"}], "located": [{"subtype": "region", "text": "Oberägypten", "type": "ancient",}],},
            ),
            (
                "6.xml",
                [{"notafter": "0400", "notbefore": "0001", "precision": "low", "text": "I - IV",}],
                {"text": "unbekannt"},
                {},
            ),
            (
                "7.xml",
                [{"notafter": "0710", "notbefore": "0709", "text": "ṣafar 91 AH",}],
                {"ref": "http://www.trismegistos.org/place/237", "text": "Išqawh",},
                {"located": [{"ref": ["http://www.trismegistos.org/place/237"], "text": "Išqawh",}],},
            ),
            (
                "8.xml",
                [{"notafter": "1132", "notbefore": "1132", "text": "2nd decade of muḥarram 527 AH",}],
                {"ref": "http://www.trismegistos.org/place/332", "text": "unknown (al-Fayyūm)",},
                {"located": [{"ref": ["http://www.trismegistos.org/place/332"], "text": "unknown (al-Fayyūm)",}],},
            ),
            (
                "9.xml",
                [{"cert": "low", "precision": "medium", "text": "ca. 340 (?)", "when": "0340",}],
                {"text": "Hermopolites",},
                {
                    "located": [
                        {"subtype": "nome", "text": "Hermopolites", "type": "ancient",},
                        {"subtype": "region", "text": "Ägypten", "type": "ancient",},
                    ],
                },
            ),
            (
                "10.xml",
                [{"cert": "low", "notafter": "-0001", "notbefore": "-0200", "precision": "low", "text": "II - I v.Chr. (?)",}],
                {"text": "unbekannt"},
                {},
            ),
            ("11.xml", [{"text": "unbekannt"}], {"text": "unbekannt"}, {}),
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
                {"text": "Oxyrhynchos",},
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
                },
            ),
            (
                "13.xml",
                [{"notafter": "0162-01", "notbefore": "0161-09", "text": "ca. Sept. 161 - Jan. 162",}],
                {"text": "Oxyrhynchos",},
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
                },
            ),
            (
                "14.xml",
                [{"notafter": "0750", "notbefore": "0701", "precision": "low", "text": None,}],
                {"text": "Theben",},
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
                },
            ),
        ]
        for (filename, want_origin_dates, want_origin_place, want_provenances) in tests:
            with open(os.path.join(TESTDATA_DIR, "header-history", filename)) as f:
                elem = BeautifulSoup(f.read(), features="lxml").history
            actual_origin_dates = _History.origin_dates(elem)
            self.assertEqual(want_origin_dates, actual_origin_dates, msg=f"{filename} origin dates")
            actual_origin_place = _History.origin_place(elem)
            self.assertEqual(want_origin_place, actual_origin_place, msg=f"{filename} origin place")
            actual_provenances = _History.provenances(elem)
            self.assertEqual(want_provenances, actual_provenances, msg=f"{filename} provenances")


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
            actual_terms = _ProfileDesc.keyword_terms(elem)
            self.assertEqual(want_terms, actual_terms, msg=f"{filename} terms")
            actual_langs = _ProfileDesc.lang_usage(elem)
            self.assertEqual(want_langs, actual_langs, msg=f"{filename} langs")
