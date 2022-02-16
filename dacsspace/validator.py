import json

from jsonschema import validate

# Gets JSON file called resource.json
# I know this is probably not correct but it was the only was I found to sucessfully load the .json file since it's in a different directory.
json_file = "/Users/aberish/Documents/GitHub/DACSspace/fixtures/resource.json"


class Validator:
    """Validates data from ArchivesSpace."""
# Creates a simple schema to validate json against
    def get_schema():
        schema = {
            "type": "object",
            "title": "resource",
            "required": [
                "title"
            ],
            "properties": {
                "title": {
                    "type": "string"
                }
            }
        }
        return schema

# Checks data from resource.json against schema
    def validate_data(self, data, schema):
        """Validates data.

        Args:
            data (dict): An ArchivesSpace object to be validated.

        Returns:
           result (dict): The result of the validation. An dictionary with a boolean
           indication of the validation result and, if necessary, an explanation
           of any validation errors. { "valid": False, "explanation": "You are missing the following fields..." }
        """

        try:
            validate(data, schema)
        except BaseException:
            print("Invalid")
        else:
            print("Something else is wrong")


# Opens the JSON file so it can be used in validate_data
f = open(json_file)
data = json.load(f)

schema = Validator()

# Attempting to run the Class so that I can see if it's working
check_valid = Validator()
print(check_valid.validate_data(data, schema))

# Ignore this, I was trying out different ways of opening the JSON and this worked but seemed more complex than line 50-51
# with open(json_file, 'r') as f:
#    data = json.load(f)
# return data
