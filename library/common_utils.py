from jsonschema import validate, ValidationError
from ptest.plogger import preporter


def validate_schema(response_body_schema, expected_schema):
    try:
        validate(response_body_schema, expected_schema)
        return True
    except ValidationError as e:
        preporter.info("Schema is not matched" + str(e))
        return False


def build_resource_endpoint(base_url, path, resource=None):
    if resource is None:
        return base_url+path
    else:
        return base_url + path + "/" + resource

