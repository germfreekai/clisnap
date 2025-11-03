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
    tool_options.add_argument("-l", "--list", action="store_true", help="List all available tools.")

    read_options = parser.add_argument_group("Read options")
    read_options.add_argument("-s", "--show-cmd", type=str, help="Show all CMDs for a tool.")

    write_options = parser.add_argument_group("Write options")
    write_options.add_argument(
        "-a", "--add-cmd", type=str, help="Add CMDs for a tool, create new one or update existing."
    )
    write_options.add_argument(
        "-n", "--n-cmds", type=int, default=1, help="Number of CMDS to add, default only 1."
    )

    delete_options = parser.add_argument_group("Delete options")
    delete_options.add_argument(
        "-d",
        "--delete",
        type=str,
        help="Delete CMDs for a tool. If option -i not provided, deletes all.",
    )
    delete_options.add_argument("-i", "--id", type=str, help="CMD ID to delete.")

    return parser.parse_args()


def main():
    """
    Tool's main logic.
    """
    if "-h" in sys.argv or "--help" in sys.argv:
        print_banner(TOOL_NAME)

    args = parse_args()

    cmd_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "cmds")

    clisnap = Clisnap(cmd_path)

    if args.list:
        clisnap.list_all()

    if args.show_cmd:
        clisnap.show_cmd(args.show_cmd)

    if args.add_cmd:
        clisnap.add_cmd(args.add_cmd, args.n_cmds)

    if args.delete:
        if len(sys.argv) > 3 and not args.id:
            LOGGER.error("Only use argument -i for delete operations.")
            sys.exit(1)
        clisnap.delete_cmd(args.delete, args.id)


if __name__ == "__main__":
    main()
