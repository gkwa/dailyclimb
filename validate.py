import json

import jsonschema

with open("person.schema.json") as file:
    schema = json.load(file)

with open("person.json") as file:
    data = json.load(file)

jsonschema.validate(instance=data, schema=schema)

print("JSON data is valid!")
