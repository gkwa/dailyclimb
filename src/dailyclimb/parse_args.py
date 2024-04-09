import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="JSON Schema Validator")
    parser.add_argument(
        "--schema-file",
        type=str,
        default="person.schema.json",
        help="Path to the JSON Schema file",
    )
    parser.add_argument(
        "--json-file",
        type=str,
        default="person.json",
        help="Path to the JSON file to validate",
    )
    return parser.parse_args()
