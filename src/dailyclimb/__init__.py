from . import parse_args, validate

__project_name__ = "dailyclimb"


def main() -> int:
    args = parse_args.parse_args()
    validate.validate_json(args.schema_file, args.json_file)
    return 0
