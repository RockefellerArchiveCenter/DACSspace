import json
import os
import unittest
from pathlib import Path

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

    def validate_files(self, fixtures, schema, valid):
        """Validates files.

        Args:
            fixtures (list): filenames of fixtures to be validated.
            schema (str): a schema to validate against.
            valid (boolean): the expected outcome of the validation process.
        """
        for fixture in fixtures:
            with open(Path('fixtures', fixture), 'r') as v:
                data = json.load(v)
                result = Validator(schema, None).validate_data(data)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], valid, result)

    def test_single_level_required_schema(self):
        """Asserts that the single_level_required schema validates fixtures as expected."""
        VALID_FIXTURES = ['valid_resource.json']
        INVALID_FIXTURES = ['invalid_resource.json', 'minimum_to_save.json',
                            'no_accessrestrict.json', 'no_metadata_rights.json',
                            'userestrict_only.json']
        self.validate_files(VALID_FIXTURES, 'single_level_required', True)
        self.validate_files(INVALID_FIXTURES, 'single_level_required', False)

    def test_rac_schema(self):
        """Asserts that the RAC schema validates fixtures as expected."""
        VALID_FIXTURES = ['valid_resource_rac.json']
        INVALID_FIXTURES = ['invalid_resource.json', 'minimum_to_save.json',
                            'no_accessrestrict.json', 'userestrict_only.json',
                            'missing_acqinfo.json', 'missing_arrangement.json',
                            'missing_bioghist.json', 'missing_userestrict.json']
        self.validate_files(VALID_FIXTURES, 'rac', True)
        self.validate_files(INVALID_FIXTURES, 'rac', False)
