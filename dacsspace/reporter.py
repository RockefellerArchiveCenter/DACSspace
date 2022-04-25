import csv


class CSVReporter:
    """Creates CSV reports."""

    def __init__(self, filename, filemode="w"):
        """Sets the filename and filemode."""
        self.filename = filename
        self.filemode = filemode

    def write_report(self, results, invalid_only=True):
        """Writes results to a CSV file.

        Args:
            results (list): A list of dictionaries containing information about validation results.
            invalid_only (boolean): Only report on invalid results.
        """

        if self.filemode.startswith("r"):
            raise ValueError("Filemode must allow write options.")
        with open(self.filename, self.filemode) as f:
            fieldnames = [
                "uri",
                "valid",
                "error_count",
                "explanation"]
            writer = csv.DictWriter(
                f, fieldnames=fieldnames)
            writer.writeheader()
            filtered_results = [
                row for row in results if not row["valid"]] if invalid_only else results
            writer.writerows(filtered_results)
