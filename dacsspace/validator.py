# import json

from jsonschema import validate


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
    def validate_data(self, json_data, schema):
        """Validates data.

        Args:
            data (dict): An ArchivesSpace object to be validated.

        Returns:
           result (dict): The result of the validation. An dictionary with a boolean
           indication of the validation result and, if necessary, an explanation
           of any validation errors. { "valid": False, "explanation": "You are missing the following fields..." }
        """
        schema = self.get_schema()
        try:
            validate(json_data, schema)
        except BaseException:
            print("Invalid")
        else:
            print("Something else is wrong")


# Attempting to run the Class so that I can see if it's working
# HELP: Line 47 doesn't work it keeps saying that 'json_data' and 'schema' are undefined
# Validator.validate_data(json_data, schema)
