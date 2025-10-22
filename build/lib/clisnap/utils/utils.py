"""Utils file."""

import os
import json

def read_json_file(file_path):
    """
    Read JSON file.
    
    Arguments:
        - file_path (str): File abs path
    """
    with open(file_path, 'r', encoding="utf-8") as pfile:
        cmds = json.load(pfile)
    return cmds
