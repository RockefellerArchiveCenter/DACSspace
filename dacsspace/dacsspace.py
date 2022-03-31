import argparse

from .client import ArchivesSpaceClient
from .reporter import CSVReporter
from .validator import Validator


class DACSspace:
    """Base DACSspace class. Fetches data from AS, validates and reports results."""

    def run(self, published_only, invalid_only):
        client = ArchivesSpaceClient()
        validator = Validator()
        reporter = CSVReporter()
        data = client.get_resources(published_only)
        results = []
        for obj in data:
            result = validator.validate(obj)
            results.append(result)
        reporter.write_report(results, invalid_only)


parser = argparse.ArgumentParser(
    description="Fetches data from AS, validates and reports results")
parser.add_argument(
    '--published_only',
    help='Fetches only published records from AS',
    action='store_true')
parser.add_argument(
    '--invalid_only',
    help='Reports only invalid data',
    action='store_false')
parser.add_argument()
args = parser.parse_args()

DACSspace().run(args.published_only, args.invalid_only)
