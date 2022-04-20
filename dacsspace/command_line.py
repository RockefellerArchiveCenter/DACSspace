import argparse

from .dacsspace import DACSspace


def main():
    """Command line entrypoint for DACSspace. Parses arguments received from stdin."""
    parser = argparse.ArgumentParser(
        description="Fetches data from ArchivesSpace, validates and reports results")
    parser.add_argument(
        'csv_filepath',
        help='Filepath for results report (CSV format)',
        type=str)
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
        type=str,
        default='single_level_required.json')
    group.add_argument(
        '--schema_filepath',
        help='Choose schema_identifier or schema_filepath. Schema_filepath default is None, only one of schema_identifier',
        type=str,
        default=None)
    args = parser.parse_args()

    DACSspace(args.csv_filepath).run(
        args.published_only,
        args.invalid_only,
        args.schema_identifier,
        args.schema_filepath)
