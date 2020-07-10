from marshmallow import Schema, validates_schema


class SchemaError(Exception):
    pass


class BaseSchema(Schema):

    def handle_error(self, exc, data):
        """Log and raise our custom exception when (de)serialization fails."""
        raise SchemaError('An error occurred with input: {0} \n {1}'.format(data, exc.messages))