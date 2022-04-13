from unittest import TestCase

from dacsspace.dacsspace import DACSspace


class TestDACSspace(TestCase):

    def test_csv_filepath(self):
        """Asserts that CSV filepath is handled as expected.

        Filepaths are checked to ensure they end with the appropriate file
        extension (.csv) and don't contain any illegal characters.
        """
        DACSspace("csv_filepath.csv")
        with self.assertRaises(ValueError) as err:
            DACSspace("my*file.csv")
        self.assertEqual(str(err.exception),
                         'File name cannot contain the following characters: * ? : " < > | ')
        with self.assertRaises(ValueError) as err:
            DACSspace("myfile")
        self.assertEqual(str(err.exception),
                         "File must have .csv extension")
