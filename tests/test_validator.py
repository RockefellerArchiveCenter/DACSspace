# from unittest.mock import patch


import json
import unittest

from dacsspace.validator import Validator


class TestValidator(unittest.TestCase):
    def test_validator(self):
        valid_json = "fixtures/valid_resource.json"
        invalid_fixtures = [
            "fixtures/multiple_invalid.json",
            "fixtures/no_metadata_rights.json",
            "fixtures/no_accessrestrict.json"]
        with open(valid_json, 'r') as v:
            valid_json = json.load(v)
            result = Validator().validate_data(valid_json)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["valid"], True)
        for f in invalid_fixtures:
            with open(f, 'r') as i:
                invalid_json = json.load(i)
                result = Validator().validate_data(invalid_json)
            self.assertTrue(isinstance(result, dict))
            self.assertEqual(result["valid"], False)
