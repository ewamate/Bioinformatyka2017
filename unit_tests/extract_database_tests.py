import unittest
from extract_database import extract_modomics_db
from extract_database import extract_albany_db

class TestExtractingDatabases(unittest.TestCase):

    def test_extract_modomics_db(self):
        dict = extract_modomics_db()
        self.assertEqual(len(dict.keys()), 170)
        self.assertEqual(len(set(sum([[subkey for subkey in dict[key]] for key in dict.keys()], []))), 16)

    def test_extract_albany_db(self):
        dict = extract_albany_db()
        self.assertEqual(len(dict.keys()), 112)
        self.assertEqual(len(set(sum([[subkey for subkey in dict[key]] for key in dict.keys()], []))), 6)


if __name__ == '__main__':
    unittest.main()
