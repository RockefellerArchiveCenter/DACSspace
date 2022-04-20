import os
from unittest import TestCase
from unittest.mock import patch

from dacsspace.reporter import CSVReporter


class CSVReporterTest(TestCase):

    def setUp(self):
        """Sets filename and data attributes for test file.

        Checks if test file exists, then deletes it.
        """
        self.filename = "DACSSpace_results"
        self.results = [{"valid": True, "error count": 0, "explanation": None},
                        {"valid": False, "error count": 1, "explanation": "No title"}]
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test_CSV(self):
        """Asserts that the results are correctly written to the file.

        Raises an error if the file has an incorrect filemode and asserts that the filemode must allow write options.
        """
        CSVReporter(self.filename).write_report(self.results)
        self.assertTrue(self.filename)
        with self.assertRaises(ValueError) as err:
            CSVReporter(self.filename, "r").write_report(self.results)
        self.assertEqual(str(err.exception),
                         "Filemode must allow write options.")

    @patch("csv.DictWriter.writerows")
    def test_invalid(self, mock_writerows):
        """Mocks writing only invalid results and valid results to file."""
        CSVReporter(self.filename).write_report(self.results)
        mock_writerows.assert_called_with(
            [{"valid": False, "error count": 1, "explanation": "No title"}])
        CSVReporter(
            self.filename).write_report(
            self.results,
            invalid_only=False)
        mock_writerows.assert_called_with(self.results)

    def tearDown(self):
        """Tears down test file.

        Checks if test file exists, then deletes it."""
        if os.path.isfile(self.filename):
            os.remove(self.filename)
