import argparse

from .client import ArchivesSpaceClient
from .reporter import CSVReporter
from .validator import Validator


class DACSspace:
    """Base DACSspace class. Fetches data from AS, validates and reports results."""

    def run(self, published_only, invalid_only,
            schema_identifier, schema_filepath):
        client = ArchivesSpaceClient()
        validator = Validator(schema_identifier, schema_filepath)
        reporter = CSVReporter()
        data = client.get_resources(published_only)
        results = []
        for obj in data:
            result = validator.validate(obj)
            results.append(result)
        reporter.write_report(results, invalid_only)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Fetches data from AS, validates and reports results")
    parser.add_argument(
        '--published_only',
        help='Fetches only published records from AS',
        action='store_true')
    parser.add_argument(
        '--invalid_only',
        help='Reports only invalid data',
        action='store_true')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--schema_identifier',
        help='Choose schema_identifier or schema_filepath. schema_identifier default is single_level_required.json',
        type=str, default='single_level_required.json')
    group.add_argument(
        '--schema_filepath',
        help='Choose schema_identifier or schema_filepath. Schema_filepath default is None, only one of schema_identifier',
        type=str, default=None)
    args = parser.parse_args()

    DACSspace().run(
        args.published_only,
        args.invalid_only,
        args.schema_identifier,
        args.schema_filepath)
