import concurrent.futures
import glob
import os
import unittest

from git import Repo

import epidoc

TESTDATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata", "idp.data")


class TestIntegration(unittest.TestCase):
    def setUp(self):
        super().setUp()
        if os.path.exists(TESTDATA_DIR):
            return
        Repo.clone_from("https://github.com/papyri/idp.data.git", TESTDATA_DIR, branch="master", depth=1)

    @staticmethod
    def load(filename):
        with open(filename) as f:
            try:
                epidoc.load(f)
            except Exception as e:
                # Raised exception are ignored by executor.map
                return Exception(f"{filename} has error {e.__class__.__name__}: {e}")

    def load_all(self, path):
        assert os.path.exists(path), f"path {path} exists"
        with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
            for result in executor.map(TestIntegration.load, glob.glob(os.path.join(path, "**", "*.xml"), recursive=True)):
                if isinstance(result, Exception):
                    self.fail(result)

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
