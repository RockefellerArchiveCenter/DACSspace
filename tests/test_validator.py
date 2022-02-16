# from unittest.mock import patch
#
# from dacsspace.validator import Validator

import json
import unittest

# HELP: I noticed in other tests there is usually a class, so I added one, but
# I don't know if this is necessary


class TestValidator(unittest.TestCase):
    def test_validator():
        json_file = "/Users/aberish/Documents/GitHub/DACSspace/fixtures/resource.json"
        with open(json_file, 'r') as f:
            json_data = json.load(f)
        return(json_data)


# HELP: I don't know what this does, but I saw it used in other tests
if __name__ == "__main__":
    unittest.main()
