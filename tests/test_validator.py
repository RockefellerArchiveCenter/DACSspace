# from unittest.mock import patch


import json
import unittest

from dacsspace.validator import Validator


class TestValidator(unittest.TestCase):
    def test_validator(self):
        # valid_json = "/Users/aberish/Documents/GitHub/DACSspace/fixtures/valid_resource.json"
        invalid_json = "/Users/aberish/Documents/GitHub/DACSspace/fixtures/invalid_resource.json"
        with open(invalid_json, 'r') as f:
            invalid_json = json.load(f)
            result = Validator().validate_data(invalid_json)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["valid"], False)
        # with open(invalid_json, 'r') as i:
        #     invalid_json = json.load(i)
        #     result = Validator().validate_data(invalid_json)
        # self.assertFalse(isinstance(result, dict))
        # self.assertEqual(result["valid"], False)
