
from jsonschema import ValidationError, validate


class Validator:
    """Validates data from ArchivesSpace."""
# Creates a simple schema to validate json against

    def get_schema(self):
        schema = {
            "type": "object",
            "title": "DACSspace schema",
            "required": [
                "title",
                "id_0"
            ],
            "properties": {
                "title": {
                    "type": "string"
                }
            }
        }
        return schema

# Checks data against schema
    def validate_data(self, data):
        """Validates data.

        Args:
            data (dict): An ArchivesSpace object to be validated.

        Returns:
           result (dict): The result of the validation. An dictionary with a boolean
           indication of the validation result and, if necessary, an explanation
           of any validation errors. { "valid": False, "explanation": "You are missing the following fields..." }
        """
        schema = self.get_schema()
        # print(data)
        try:
            validate(data, schema)
            return {"valid": True}
        except ValidationError as error:
            # print(error.message)
            return {"valid": False, "explanation": error.message}
            # continue
        else:
            print("Something else is wrong")


# Validator.validate_data(json_data, schema)
