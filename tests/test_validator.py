import json
import os
import unittest
from pathlib import Path

from jsonschema.exceptions import SchemaError

from dacsspace.validator import Validator

INVALID_FIXTURE_DIRECTORY = Path("fixtures", "invalid")
VALID_FIXTURE_DIRECTORY = Path("fixtures", "valid")


class TestValidator(unittest.TestCase):
    def test_schema(self):
        """Asserts schema identifiers and filenames are handled correctly."""

        test_schema_filepath = "test_schema.json"

        # handling for schema identifier
        validator = Validator('single_level_required', None)
        self.assertEqual(validator.schema["$id"], 'single_level_required.json')

        validator = Validator('single_level_required.json', None)
        self.assertEqual(validator.schema["$id"], 'single_level_required.json')

        # passing external filename
        with open(test_schema_filepath, "w") as sf:
            json.dump({"$id": "test_schema.json"}, sf)
        validator = Validator(None, test_schema_filepath)
        self.assertEqual(validator.schema["$id"], test_schema_filepath)

        # invalid external schema
        with open(test_schema_filepath, "w") as sf:
            json.dump({"type": 12}, sf)
        with self.assertRaises(SchemaError):
            validator = Validator(None, test_schema_filepath)

        # cleanup
        os.remove(test_schema_filepath)

    def test_validator(self):
        valid_fixtures = [
            f for f in VALID_FIXTURE_DIRECTORY.iterdir() if (
                f.is_file() and str(
                    f.name).endswith("json"))]
        for valid in valid_fixtures:
            with open(valid, 'r') as v:
                valid_json = json.load(v)
                result = Validator(
                    'single_level_required',
                    None).validate_data(valid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], True)
        invalid_fixtures = [
            f for f in INVALID_FIXTURE_DIRECTORY.iterdir() if (
                f.is_file() and str(
                    f.name).endswith("json"))]
        for invalid in invalid_fixtures:
            with open(invalid, 'r') as i:
                invalid_json = json.load(i)
                result = Validator(
                    'single_level_required',
                    None).validate_data(invalid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], False)
        for valid in valid_fixtures:
            with open(valid, 'r') as v:
                valid_json = json.load(v)
                result = Validator(
                    'single_level_required',
                    None).validate_data(valid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], True)
