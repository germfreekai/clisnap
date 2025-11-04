"""clisnap class file."""

import os

from clisnap.cls.logger import Logger
from clisnap.utils import delete_file, read_json_file, write_json_file

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
                print(f"[{index+1}] {file[:-5]}")

    def show_cmd(self, tool):
        """
        Show all available CMDs for a given tool.

        Arguments:
            - tool (str): tool name
        """
        cmds = read_json_file(tool, os.path.join(self.cmd_path, tool + ".json"))

        max_cmd_name_length = 0
        for index, data in cmds.items():
            length = len(f"[{index}] {data['cmd']}")
            max_cmd_name_length = max_cmd_name_length if length < max_cmd_name_length else length

        for index, data in cmds.items():
            cmd_name = f"[{index}] {data['cmd']}"
            print(f"{cmd_name:<{max_cmd_name_length}} : {data['description']}")

    def add_cmd(self, tool, n_cmds):
        """
        Add a CMD to a tool.

        If the tool file does not exist, create it.

        Arguments:
            - tool (str): tool name
            - n_cmds (int): n cmds to add
        """
        cmds = {}
        tool_file = os.path.join(self.cmd_path, tool + ".json")
        if os.path.exists(tool_file):
            cmds = read_json_file(tool, tool_file)

        index = 1 if not cmds else len(cmds) + 1

        for _ in range(n_cmds):
            cmd = input(f"[{index}] cmd > ")
            description = input(f"[{index}] description > ")
            cmds[index] = {"cmd": cmd, "description": description}
            index += 1

        write_json_file(tool, tool_file, cmds)

    def delete_cmd(self, tool, cmd_id):
        """
        Delete a CMD from a tool.

        If option ID not provided, delete file.

        Arguments:
            - tool (str): tool name
            - id (int): id to delete
        """
        tool_file = os.path.join(self.cmd_path, tool + ".json")
        if not cmd_id:
            delete_file(tool, tool_file)
            return
        cmds = read_json_file(tool, tool_file)

        if cmd_id in cmds:
            LOGGER.info(f"Removed CMD: {cmds[str(cmd_id)]["cmd"]}")
            del cmds[cmd_id]
        else:
            LOGGER.error("ID not found.")
            return

        tmp = {}
        index = 1
        for _, data in cmds.items():
            tmp[index] = {"cmd": data["cmd"], "description": data["description"]}
            index += 1

        write_json_file(tool, tool_file, tmp)
