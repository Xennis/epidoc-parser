import glob
import os
import unittest

import epidoc

# Note: git clone https://github.com/papyri/idp.data.git testdata/idp.data
TESTDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata", "idp.data")


class TestIntegration(unittest.TestCase):
    def load_all(self, path):
        assert os.path.exists(path), f"path {path} exists"
        for filename in glob.glob(os.path.join(path, "**", "*.xml"), recursive=True):
            with open(filename) as f:
                try:
                    epidoc.load(f)
                except Exception as e:
                    self.fail(f"{filename} has error {e.__class__.__name__}: {e}")

    def test_apd(self):
        self.load_all(os.path.join(TESTDATA_DIR, "APD"))

    def test_apis(self):
        self.load_all(os.path.join(TESTDATA_DIR, "APIS"))

    def test_dclp(self):
        self.load_all(os.path.join(TESTDATA_DIR, "DCLP"))

    def test_hgv_meta(self):
        self.load_all(os.path.join(TESTDATA_DIR, "HGV_meta_EpiDoc"))

    def test_hgv_trans(self):
        self.load_all(os.path.join(TESTDATA_DIR, "HGV_trans_EpiDoc"))

    def test_ddb(self):
        self.load_all(os.path.join(TESTDATA_DIR, "DDB_EpiDoc_XML"))
