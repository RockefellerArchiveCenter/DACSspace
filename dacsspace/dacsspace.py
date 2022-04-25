import re
from configparser import ConfigParser
from os.path import isfile

from .client import ArchivesSpaceClient
from .reporter import CSVReporter
from .validator import Validator


class DACSspace:
    """Base DACSspace class. Fetches data from AS, validates and reports results."""

    def __init__(self, as_config, csv_filepath):
        """Checks CSV and AS config filepaths."""
        if not csv_filepath.endswith(".csv"):
            raise ValueError("File must have .csv extension")
        if re.search(r'[*?:"<>|]', csv_filepath):
            raise ValueError(
                'File name cannot contain the following characters: * ? : " < > | ')
        self.csv_filepath = csv_filepath

        if not isfile(as_config):
            raise IOError(
                "Could not find an ArchivesSpace configuration file at {}".format(as_config))
        config = ConfigParser()
        config.read(as_config)
        self.as_config = (
            config.get('ArchivesSpace', 'baseurl'),
            config.get('ArchivesSpace', 'user'),
            config.get('ArchivesSpace', 'password'),
            config.get('ArchivesSpace', 'repository'))

    def run(self, published_only, invalid_only,
            schema_identifier, schema_filepath):
        client = ArchivesSpaceClient(*self.as_config)
        validator = Validator(schema_identifier, schema_filepath)
        reporter = CSVReporter(self.csv_filepath)
        data = client.get_resources(published_only)
        results = [validator.validate_data(obj) for obj in data]
        reporter.write_report(results, invalid_only)
