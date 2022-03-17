
from jsonschema import Draft7Validator


class Validator:
    """Validates data from ArchivesSpace."""

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
        validator = Draft7Validator(schema)
        errors_found = []
        for error in validator.iter_errors(data):
            errors_found.append(error.message)
        if len(errors_found):
            return {"valid": False, "explanation": "\n".join(errors_found)}
        else:
            return {"valid": True}
