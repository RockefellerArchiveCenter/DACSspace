import re

from .client import ArchivesSpaceClient
from .reporter import CSVReporter
from .validator import Validator


class DACSspace:
    """Base DACSspace class. Fetches data from AS, validates and reports results."""

    def __init__(self, csv_filepath):
        """Checks csv filepath to make sure it has the proper extension and characters."""
        if not csv_filepath.endswith(".csv"):
            raise ValueError("File must have .csv extension")
        if re.search(r'[*?:"<>|]', csv_filepath):
            raise ValueError(
                'File name cannot contain the following characters: * ? : " < > | ')

    def run(self, published_only, invalid_only,
            schema_identifier='single_level_required.json', schema_filepath=None):
        client = ArchivesSpaceClient()
        validator = Validator(schema_identifier, schema_filepath)
        reporter = CSVReporter()
        data = client.get_resources(published_only)
        results = []
        for obj in data:
            result = validator.validate(obj)
            results.append(result)
        reporter.write_report(results, invalid_only)


# These variables should eventually be passed as arguments in the command line
# published_only = False
# invalid_only = True
# schema_identifier - should default to single_level_required.json
# schema_filepath - should default to None, only one of schema_identifier
# or schema_filepath allowed
