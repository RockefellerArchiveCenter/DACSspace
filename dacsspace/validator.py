import json

from jsonschema import ValidationError, validate


class Validator:
    """Validates data from ArchivesSpace."""

    def __init__(self):
        with open("single_level_required.json", "r") as json_file:
            self.schema = json.load(json_file)

    def validate_data(self, data):
        """Validates data.

        Args:
            data (dict): An ArchivesSpace object to be validated.

        Returns:
           result (dict): The result of the validation. An dictionary with a boolean
           indication of the validation result and, if necessary, an explanation
           of any validation errors. { "valid": False, "explanation": "You are missing the following fields..." }
        """
        try:
            validate(data, self.schema)
            return {"valid": True}
        except ValidationError as error:
            return {"valid": False, "explanation": error.message}
        else:
            print("Something else is wrong")
