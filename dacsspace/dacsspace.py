from client import ArchivesSpaceClient
from reporter import CSVReporter
from validator import Validator


class DACSspace:
    """Base DACSspace class. Fetches data from AS, validates and reports results."""
    client = ArchivesSpaceClient()
    validator = Validator()
    reporter = CSVReporter()
    data = client.get_resources(published_only)
    results = []
    for obj in data:
        result = validator.validate(obj)
        results.append(result)
    reporter.write_report(results, invalid_only)


# Args to pass in command line
# - published_only
# - invalid_only
