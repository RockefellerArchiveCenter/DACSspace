import json
import unittest
from pathlib import Path

from dacsspace.validator import Validator

INVALID_FIXTURE_DIRECTORY = Path("fixtures", "invalid")
VALID_FIXTURE_DIRECTORY = Path("fixtures", "valid")


class TestValidator(unittest.TestCase):
    def test_validator(self):
        valid_fixtures = [
            f for f in VALID_FIXTURE_DIRECTORY.iterdir() if (
                f.is_file() and str(
                    f.name).endswith("json"))]
        for valid in valid_fixtures:
            with open(valid, 'r') as v:
                valid_json = json.load(v)
                result = Validator().validate_data(valid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], True)
        invalid_fixtures = [
            f for f in INVALID_FIXTURE_DIRECTORY.iterdir() if (
                f.is_file() and str(
                    f.name).endswith("json"))]
        for invalid in invalid_fixtures:
            with open(invalid, 'r') as i:
                invalid_json = json.load(i)
                result = Validator().validate_data(invalid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], False)
