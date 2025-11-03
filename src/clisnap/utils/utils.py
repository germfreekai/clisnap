"""Utils file."""

import json
import os
import sys

from clisnap.cls.logger import Logger

LOGGER = Logger()


def read_json_file(file, file_path):
    """
    Read JSON file.

    Arguments:
        - file_path (str): File abs path.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as pfile:
            cmds = json.load(pfile)
    except FileNotFoundError:
        LOGGER.error(f"Tool not found: {file}")
        sys.exit(1)
    except (ValueError, IOError, PermissionError) as err:
        LOGGER.error(err)
        sys.exit(1)
    return cmds


def write_json_file(file, file_path, cmds):
    """
    Write JSON file.

    Arguments:
        - file (str): File name
        - file_path (str): File abs path.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as pfile:
            json.dump(cmds, pfile, indent=4)
    except FileNotFoundError:
        LOGGER.error(f"Tool not found: {file}")
        sys.exit(1)
    except (ValueError, IOError, PermissionError) as err:
        LOGGER.error(err)
        sys.exit(1)


def delete_file(file, file_path):
    """
    Delete JSON file.

    Arguments:
        - file (str): File name
        - file_path (str): File abs path.
    """
    try:
        os.remove(file_path)
        LOGGER.info(f"Removed file: {file}")
    except FileNotFoundError:
        LOGGER.error(f"Tool not found: {file}")
        sys.exit(1)
    except (ValueError, IOError, PermissionError) as err:
        LOGGER.error(err)
        sys.exit(1)
