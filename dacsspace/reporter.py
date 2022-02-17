import csv


class CSVReporter:
    """Creates CSV reports."""

    def __init__(self, filename):
        # TODO: set filepath for CSV
        self.filename = filename

        pass

    def write_report(self, results, invalid_only=True):
        """Writes results to a CSV file.

        Args:
            results (list): A list of dictionaries containing information about validation results.
            invalid_only (boolean): Only report on invalid results.
        """

        with open(self.filename) as f:
            fieldnames = [
                "title",
                "publish",
                "resource",
                "extent",
                "date",
                "language",
                "repository",
                "creator",
                "scope",
                "restrictions"]
            writer = csv.DictWriter(
                f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        pass
