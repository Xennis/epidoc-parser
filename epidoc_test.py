import os
import unittest

from epidoc import EpiDoc, load

TESTDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata")


class TestLoad(unittest.TestCase):
    def test_all(self):
        tests = [
            (
                os.path.join("ddb", "chla.3.198.xml"),
                EpiDoc.create(
                    title="chla.3.198",
                        idno={
                            "ddb-hybrid": "chla;3;198",
                            "ddb-perseus-style": "0279;3;198",
                            "filename": "chla.3.198",
                            "hgv": "114844",
                            "tm": "114844",
                        },
                        terms=[],
                        languages={"en": "English", "la": "Latin"},
                ),
            ),
            (
                os.path.join("ddb", "p.coles.16.xml"),
                EpiDoc.create(
                        title="p.coles.16",
                        idno={"ddb-hybrid": "p.coles;;16", "filename": "p.coles.16", "hgv": "697551", "tm": "697551",},
                        terms=[],
                        languages={"en": "English", "grc": "Greek"},
                ),
            ),
            (
                os.path.join("dlcp", "26761.xml"),
                EpiDoc.create(
                        title="Sb. 16 13045",
                        idno={"dclp": "26761", "dclp-hybrid": "sb;16;13045", "filename": "26761", "ldab": "5148", "tm": "26761",},
                        material="papyrus",
                        dates=[{"text": "100 - 299", "notbefore": "0100", "notafter": "0299",}],
                        places={
                            "text": "Found: Egypt; written: Egypt",
                            "found": [{"text": "Egypt", "type": "ancient", "subtype": "region",}],
                            "composed": [{"text": "Egypt", "type": "ancient", "subtype": "region",}],
                        },
                        terms=[
                            {"text": "medicine"},
                            {"type": "culture", "text": "science"},
                            {"type": "overview", "text": "two medical prescriptions"},
                        ],
                        languages={},
                ),
            ),
            (
                os.path.join("dlcp", "135858.xml"),
                EpiDoc.create(
                        title="TM 135858",
                        idno={
                            "dclp": "135858",
                            "dclp-hybrid": "tm;;135858",
                            "filename": "135858",
                            "ldab": "135858",
                            "tm": "135858",
                        },
                        material="parchment",
                        dates=[{"text": "550 - 649", "notbefore": "0550", "notafter": "0649",}],
                        places={
                            "text": "Found: Naqlun (Arsinoites, Egypt); written: Naqlun (Arsinoites, Egypt)",
                            "found": [
                                {"text": "Arsinoites", "type": "ancient", "subtype": "nome",},
                                {"text": "Egypt", "type": "ancient", "subtype": "region",},
                                {"text": "Naqlun", "type": "ancient", "ref": ["https://www.trismegistos.org/place/1418"],},
                            ],
                            "composed": [
                                {"text": "Arsinoites", "type": "ancient", "subtype": "nome",},
                                {"text": "Egypt", "type": "ancient", "subtype": "region",},
                                {"text": "Naqlun", "type": "ancient", "ref": ["https://www.trismegistos.org/place/1418"],},
                            ],
                        },
                        terms=[
                            {"text": "bible"},
                            {"text": "prose"},
                            {"text": "letter"},
                            {"type": "culture", "text": "literature"},
                            {"type": "religion", "text": "christian"},
                            {"type": "overview", "text": "New Testament: Paulus apost.; Coloss. 2.8-19"},
                        ],
                        languages={"en": "English", "cop": "Coptic"},
                ),
            ),
            (
                os.path.join("hgv", "13003.xml"),
                EpiDoc.create(
                        title="Taxing - list",
                        idno={
                            "filename": "13003",
                            "tm": "13003",
                            "ddb-perseus-style": "0198;2;371v",
                            "ddb-filename": "p.ryl.2.371v",
                            "ddb-hybrid": "p.ryl;2;371v",
                        },
                        material="papyrus",
                        dates=[{"text": "134 - 135", "notbefore": "0134", "notafter": "0135",}],
                        places={
                            "text": "Philopator alias Theogenus (Arsinoites)",
                            "located": [
                                {
                                    "text": "Philopator alias Theogenus",
                                    "type": "ancient",
                                    "ref": ["http://pleiades.stoa.org/places/741563", "http://www.trismegistos.org/place/1776",],
                                },
                                {"text": "Arsinoites", "type": "ancient", "subtype": "nome",},
                                {"text": "Ägypten", "type": "ancient", "subtype": "region",},
                            ],
                        },
                        terms=[{"text": "Erklärung (Steuer)"}],
                        languages={
                            "fr": "Französisch",
                            "en": "Englisch",
                            "de": "Deutsch",
                            "it": "Italienisch",
                            "es": "Spanisch",
                            "la": "Latein",
                            "el": "Griechisch",
                        },
                ),
            ),
            (
                os.path.join("hgv", "74005.xml"),
                EpiDoc.create(
                        title="Ordre de paiement",
                        idno={
                            "filename": "74005",
                            "tm": "74005",
                            "ddb-perseus-style": "0022;4;452",
                            "ddb-filename": "o.douch.4.452",
                            "ddb-hybrid": "o.douch;4;452",
                        },
                        material="ostrakon",
                        dates=[{"text": "IV - Anfang V", "notbefore": "0301", "notafter": "0425", "precision": "low",}],
                        places={
                            "text": "Kysis (Oasis Magna)",
                            "located": [
                                {
                                    "text": "Kysis",
                                    "type": "ancient",
                                    "ref": ["http://pleiades.stoa.org/places/776191", "http://www.trismegistos.org/place/2761",],
                                },
                                {"text": "Oasis Magna", "type": "ancient", "subtype": "region",},
                            ],
                        },
                        terms=[
                            {"text": "Anweisung"},
                            {"text": "Zahlung"},
                            {"text": "Militär"},
                            {"text": "Fleisch"},
                            {"text": "Getreide"},
                        ],
                        languages={
                            "fr": "Französisch",
                            "en": "Englisch",
                            "de": "Deutsch",
                            "it": "Italienisch",
                            "es": "Spanisch",
                            "la": "Latein",
                            "el": "Griechisch",
                        },
                ),
            ),
        ]

        for (filename, want) in tests:
            with open(os.path.join(TESTDATA_DIR, "full", filename)) as f:
                try:
                    actual = load(f)
                except Exception as e:
                    self.fail(f"{filename} has error {e.__class__.__name__}: {e}")
            self.assertEqual(want, actual, msg=filename)
