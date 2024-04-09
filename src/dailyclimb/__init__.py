import sys

from . import main2, validate

__project_name__ = "dailyclimb"


def main() -> int:
    validate.validate_json()

    return 0
