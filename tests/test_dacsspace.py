from unittest import TestCase
from unittest.mock import patch

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

    @patch('dacsspace.client.ArchivesSpaceClient.__init__')
    @patch('dacsspace.client.ArchivesSpaceClient.get_resources')
    @patch('dacsspace.validator.Validator.__init__')
    @patch('dacsspace.reporter.CSVReporter.__init__')
    @patch('dacsspace.reporter.CSVReporter.write_report')
    def test_args(self, mock_write_report, mock_reporter_init,
                  mock_validator_init, mock_get_resources, mock_client_init):
        """Asserts that arguments are passed to the correct methods."""
        mock_reporter_init.return_value = None
        mock_validator_init.return_value = None
        mock_client_init.return_value = None
        mock_get_resources.return_value = []
        for csv_filepath, published_only, invalid_only, schema_identifier, schema_filepath in [
                ('myfile.csv', False, True, 'single_level_required.json', None),
                ('test.csv', True, True, None, 'filepath/to/schema.json'),
                ('testfile.csv', False, False, 'single_level_required', None),
                ('file.csv', True, False, 'rac.json', None)]:
            DACSspace(csv_filepath).run(
                published_only,
                invalid_only,
                schema_identifier,
                schema_filepath)
            mock_validator_init.assert_called_with(
                schema_identifier, schema_filepath)
            mock_reporter_init.assert_called_with(csv_filepath)
            mock_get_resources.assert_called_with(published_only)
            mock_write_report.assert_called_with([], invalid_only)
