"""clisnap class file."""

import os

from clisnap.cls.logger import Logger
from clisnap.utils import read_json_file, write_json_file

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
                print(f"[{index}] {file[:-5]}")

    def show_cmd(self, tool):
        """
        Show all available CMDs for a given tool.

        Arguments:
            - tool (str): tool name
        """
        cmds = read_json_file(os.path.join(self.cmd_path, tool + ".json"))
        max_cmd_name_length = max(len(f"[{cmd['id']}] {cmd['cmd']}") for cmd in cmds)

        for cmd in cmds:
            cmd_name = f"[{cmd['id']}] {cmd['cmd']}"
            print(f"{cmd_name:<{max_cmd_name_length}} : {cmd['description']}")

    def add_cmd(self, tool, n_cmds):
        """
        Add a CMD to a tool.

        If the tool file does not exist, create it.

        Arguments:
            - tool (str): tool name
            - n_cmds (int): n cmds to add
        """
        cmds = []
        tool_file = os.path.join(self.cmd_path, tool + ".json")
        if os.path.exists(tool_file):
            cmds = read_json_file(tool_file)

        index = 1 if not cmds else cmds[-1]["id"] + 1

        for _ in range(n_cmds):
            cmd = {}

            cmd["id"] = index
            cmd["cmd"] = input(f"[{cmd['id']}] cmd > ")
            cmd["description"] = input(f"[{cmd['id']}] description > ")

            index += 1
            cmds.append(cmd)

        write_json_file(tool_file, cmds)
