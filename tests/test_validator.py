import json
import os
import unittest

from jsonschema.exceptions import SchemaError

from dacsspace.validator import Validator


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
        valid_json = "fixtures/valid_resource.json"
        invalid_fixtures = [
            "fixtures/multiple_invalid.json",
            "fixtures/no_metadata_rights.json"]
        with open(valid_json, 'r') as v:
            valid_json = json.load(v)
            result = Validator(
                'single_level_required',
                None).validate_data(valid_json)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["valid"], True)
        for f in invalid_fixtures:
            with open(f, 'r') as i:
                invalid_json = json.load(i)
                result = Validator(
                    'single_level_required',
                    None).validate_data(invalid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], False)
