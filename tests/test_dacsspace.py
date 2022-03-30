# import os
from unittest import TestCase

from dacsspace import DACSspace

# from unittest.mock import patch


class TestDACSspace(TestCase):
    def test_csv_filepath(self):
        DACSspace("csv_filepath.csv")
        with self.assertRaises(ValueError) as err:
            DACSspace("my*file.csv")
        self.assertEqual(str(err.exception),
                         'File name cannot contain the following characters: \\ / * ? : " < > | ')
        with self.assertRaises(ValueError) as err:
            DACSspace("myfile")
        self.assertEqual(str(err.exception),
                         "File must have .csv extension")
