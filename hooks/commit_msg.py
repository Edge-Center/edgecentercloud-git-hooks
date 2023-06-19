#!/usr/bin/python3

"""
This git hook checks the commit message for compliance with the `Conventional Commits` format.
See https://www.conventionalcommits.org
"""

import re
import sys

EDGE_CENTER_CLOUD_CONVENTIONAL_TYPES = [
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "test",
    "chore",
    "build",
]


class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[96m"
    RESTORE = "\033[0m"


class Result:
    SUCCESS = 0
    FAIL = 1


def is_conventional(commit_message: str) -> bool:
    """
    Checked that the commit message matches `Conventional Commits` formatting.
    See https://www.conventionalcommits.org

    :param commit_message: Message that will be checked.
    :return: True, if input matches Conventional Commits formatting, else False.
    """
    lines = commit_message.strip().split("\n")
    first_line_ = lines[0]
    if not _first_line_is_valid(first_line=first_line_):
        return False

    if len(lines) == 1:
        return True

    second_line_ = lines[1]
    if not _second_line_is_valid(second_line=second_line_):
        return False

    return True  # Anything can go after the second line


def _first_line_is_valid(first_line: str) -> bool:
    first_line_pattern = f"^({_r_types()}){_r_task_tag()}{_r_delimiter()}{_r_description()}$"
    return bool(re.fullmatch(first_line_pattern, first_line))


def _second_line_is_valid(second_line: str) -> bool:
    return second_line == ""  # Second line should be empty!


def _r_types() -> str:
    """
    Join types with pipe "|" to form regex ORs.

    Examples: `feat`, `fix`, `test`
    """
    return "|".join(EDGE_CENTER_CLOUD_CONVENTIONAL_TYPES)


def _r_task_tag() -> str:
    """
    Regex str for task tag.

    Examples: `(CLOUD-123)`, `(EICM-75)`
    """
    return r"\(\w+-\d+\)"


def _r_delimiter() -> str:
    """
    Regex str for optional breaking change indicator and colon delimiter.

    Examples: `:`, `!:`
    """
    return r"!?:"


def _r_description() -> str:
    """
    Regex str for description line.

    Examples: `Create new repository`, `fix client bag with buy button`
    """
    return r" .+"


def validate_commit_message():
    commit_message_filepath = sys.argv[1]
    with open(commit_message_filepath, mode="r", encoding="utf-8") as file:
        commit_message_ = file.read()

    if is_conventional(commit_message=commit_message_):
        sys.exit(Result.SUCCESS)

    commit_message_with_tabs = "".join(f"\t{line}\n" for line in commit_message_.split("\n")).rstrip()
    print(
        f"{Color.RESTORE}Bad Commit message:\n"
        f"{Color.RED}{commit_message_with_tabs}{Color.RESTORE}\n"
        f"Your commit message does not follow `Conventional Commits` formatting:\n"
        f"\tSee {Color.BLUE}https://www.conventionalcommits.org/{Color.RESTORE}\n"
        f"ㅤ\n"
        f"Edge Center conventional template:\n"
        f"{Color.YELLOW}\t<type>(<task_tag>): <description>{Color.RESTORE}\n"
        f"ㅤ\n"
        f"{Color.YELLOW}\t[optional body]{Color.RESTORE}\n"
        f"{Color.YELLOW}\t[optional footnotes]{Color.RESTORE}\n"
        f"Available conventional types:\n"
        f"{Color.GREEN}\t{' '.join(EDGE_CENTER_CLOUD_CONVENTIONAL_TYPES)}{Color.RESTORE}\n"
        f"ㅤ\n"
        f"Example commit message adding a feature:\n"
        f"{Color.GREEN}\tfeat(CLOUD-123): implement new API{Color.RESTORE}\n"
        f"Example commit message fixing an issue:\n"
        f"{Color.GREEN}\tfix(EICM-763): remove infinite loop{Color.RESTORE}\n"
        f"Example commit message that includes optional body:{Color.RESTORE}\n"
        f"{Color.GREEN}\tfix(CLOUD-125): maintain separate unit, integration and e2e tests{Color.RESTORE}\n"
        f"ㅤ\n"
        f"{Color.GREEN}\tTestPlatformSwitchStatus is a e2e test in fact.{Color.RESTORE}\n"
        f"{Color.GREEN}\tTornado probe handlers must be tested with `http_server_client` (integration tests).{Color.RESTORE}\n"
        f"{Color.GREEN}\tThe `start_probe_server` needs just unit tests.{Color.RESTORE}\n"
    )
    sys.exit(Result.FAIL)


if __name__ == "__main__":
    validate_commit_message()
