import json

from jsonschema import validate


def validate_json(schema_file, json_file):
    with open(schema_file) as file:
        schema = json.load(file)

    with open(json_file) as file:
        data = json.load(file)

    validate(instance=data, schema=schema)

    print("JSON data is valid!")
