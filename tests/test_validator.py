# from unittest.mock import patch


import json
import unittest

from dacsspace.validator import Validator


class TestValidator(unittest.TestCase):
    def test_validator(self):
        json_file = "/Users/aberish/Documents/GitHub/DACSspace/fixtures/resource.json"
        with open(json_file, 'r') as f:
            json_data = json.load(f)
            result = Validator().validate_data(json_data)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(result["valid"], "True")
