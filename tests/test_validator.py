# from unittest.mock import patch


import json
import unittest

from dacsspace.validator import Validator


class TestValidator(unittest.TestCase):
    def test_validator(self):
        valid_json = "fixtures/valid_resource.json"
        multiple_invalid = "fixtures/invalid_resource.json"
        with open(valid_json, 'r') as v:
            valid_json = json.load(v)
            result = Validator().validate_data(valid_json)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["valid"], True)
        with open(multiple_invalid, 'r') as i:
            multiple_invalid = json.load(i)
            result = Validator().validate_data(multiple_invalid)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["valid"], False)
