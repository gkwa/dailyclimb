import json
from jsonschema import validate

with open('person.schema.json') as file:
   schema = json.load(file)

with open('person.json') as file:
   data = json.load(file)

validate(instance=data, schema=schema)

print("JSON data is valid!")

