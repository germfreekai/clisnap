"""clisnap class file."""

from clisnap.cls.logger import Logger
from clisnap.utils import read_json_file

import os

LOGGER = Logger()


class Clisnap:
    """Clisnap class."""

    def __init__(self, cmd_path):
        """Initialize clixnap."""
        self.cmd_path = cmd_path

    def list_all(self):
        """
        List all available softwares.
        """
        for _, _, files in os.walk(self.cmd_path):
            for index, file in enumerate(files):
                print(f"[{index}] {file}")

    def list_cmds(self, tool):
        """
        Show all available CMDs for a given tool.
        
        Arguments:
            tool (str): tool name
        """
        cmds = read_json_file(os.path.join(self.cmd_path, tool))
        max_cmd_name_length = max(len(f"[{cmd['id']}] {cmd['cmd']}") for cmd in cmds)

        for cmd in cmds:
            cmd_name = f"[{cmd['id']}] {cmd['cmd']}"
            print(f"{cmd_name:<{max_cmd_name_length}} : {cmd['description']}")
