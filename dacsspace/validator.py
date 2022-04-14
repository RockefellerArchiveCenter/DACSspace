import json

from jsonschema import Draft202012Validator


class Validator:
    """Validates data from ArchivesSpace."""

    def __init__(self, schema_identifier, schema_filepath):
        """Loads and validates the schema from an identifier or filepath.

        Args:
            schema_identifier (str): a pointer to a schema that is part of
            DACSspace, located in the `schemas` directory.
            schema_filepath (str): a filepath pointing to an external schema.
        """
        self.validator = Draft202012Validator
        if not schema_filepath:
            schema_filepath = f"schemas/{schema_identifier.removesuffix('.json')}.json"
        with open(schema_filepath, "r") as json_file:
            self.schema = json.load(json_file)
        self.validator.check_schema(self.schema)

    def validate_data(self, data):
        """Validates data.

        Args:
            data (dict): An ArchivesSpace object to be validated.

        Returns:
           result (dict): The result of the validation. An dictionary with a boolean
           indication of the validation result and, if necessary, an explanation
           of any validation errors. { "valid": False, "explanation": "You are missing the following fields..." }
        """
        validator = self.validator(self.schema)
        errors_found = [
            error.message for error in validator.iter_errors(data)]
        print(errors_found)
        for error in validator.iter_errors(data):
            print(error.schema_path)
        if len(errors_found):
            return {"valid": False, "explanation": (errors_found)}
        else:
            return {"valid": True}
