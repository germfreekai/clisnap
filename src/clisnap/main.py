"""
clisnap

Store and read CLI commands.
This tool aims aid a developer to store and remember commands
for any CLI tool. A developer will be able to store commands
with flags and how or why to use it for it's specific needs.
"""

import argparse
import os
import sys

import maginner

from clisnap.cls import Clisnap, Logger

LOGGER = Logger()
TOOL_NAME = "clisnap"


def print_banner(tool_name):
    """
    Print Banner.

    Arguments:
        - tool_name (str): Tool's name.
    """
    maginner.maginner(tool_name)


def parse_args():
    """
    Parse CLI arguments.

    Returns:
        - parser.parse_args: Parsed CLI arguments.
    """
    parser = argparse.ArgumentParser(
        description="clisnap. Quickly remember your most used commands.", epilog="Happy Hacking!"
    )

    tool_options = parser.add_argument_group("clisnap options")

    tool_options.add_argument("-B", action="store_true", help="Show Banner")

    tool_options.add_argument(
        "-l", "--list", action="store_true", help="List all available tools."
    )

    read_options = parser.add_argument_group("Read options")

    read_options.add_argument("-lcs", "--list-cmds", type=str, help="List all CMDs for a tool.")

    read_options.add_argument(
        "-lc",
        "--list-cmd",
        type=str,
        help=(
            "Show only specific CMD for a tool. "
            "Tool name and option ID required as a comma separated argument."
        ),
    )

    write_options = parser.add_argument_group("Write options")

    write_options.add_argument("-ac", "--add-cmd", type=str, help="Add CMD to software")

    return parser.parse_args()


def main():
    """
    Tool's main logic.
    """
    args = parse_args()

    cmd_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "cmds")

    if args.B:
        print_banner(TOOL_NAME)

    clisnap = Clisnap(cmd_path)

    if args.list:
        clisnap.list_all()

    if args.list_cmds:
        clisnap.list_cmds(args.list_cmds)


if __name__ == "__main__":
    main()
