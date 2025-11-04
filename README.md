# clisnap
---
This CLI tool came to solve a simple issue. Having frequently used commands with different options or arguments, that I could not always remember.

As a result I constantly wrote them down in notes or a txt file to remember them after some time. 

I didn't want to always look through all the options at '-h' for a command or tool but rather quickly now exactly how to execute a command or set of commands for a goal.

This tool aims for that specific cases where commands are either too verbose or too many to remember but the goal does not merit a script.

## Install the tool globally
Using a python development environment is recommended. Refer to the following steps:
- Clone the Repo
```bash
$ git clone <repo_url>
$ cd clisnap
```
- Create and start the environment
```bash
$ python3 -m venv env
$ source env/bin/activate
```
- Install package and dependencies
```bash
$ pip install .
```
- Deactivate
```bash
$ deactivate
```
- Create a symlink, assuming you have `~/.local/bin`
```bash
$ readlink -f env/bin/clisnap   # copy stdout
# example /home/jon/clisnap/env/bin/clisnap
$ cd ~/.local/bin
$ ln -s /home/jon/clisnap/env/bin/clisnap clisnap
```
Now the tool should be available globally.
## How to use this tool?
- Tool options
```bash
$ clisnap -h                                                
 _____  _       ______  ______  _    _  _____  ______ 
|   __|| |     |__  __||   ___|| \  | ||     ||      |
|  |   | |        ||   |  |___ |  \ | ||  ▄  ||    ▄ |
|  |   | |        ||   |___   ||   \| ||     ||  ____|
|  |__ | |____  __||__  ___|  || |\   ||  |  || |     
|_____||______||______||______||_| \__||__|__||_|     
usage: clisnap [-h] [-l] [-s SHOW_CMD] [-a ADD_CMD] [-n N_CMDS] [-d DELETE] [-i ID]

clisnap. Quickly remember your most used commands.

options:
  -h, --help            show this help message and exit

clisnap options:
  -l, --list            List all available tools.

Read options:
  -s, --show-cmd SHOW_CMD
                        Show all CMDs for a tool.

Write options:
  -a, --add-cmd ADD_CMD
                        Add CMDs for a tool, create new one or update existing.
  -n, --n-cmds N_CMDS   Number of CMDS to add, default only 1.

Delete options:
  -d, --delete DELETE   Delete CMDs for a tool. If option -i not provided, deletes all.
  -i, --id ID           CMD ID to delete.

Happy Hacking!
```
Example:
A dummy example for remember specific `find` options
```bash
# create tool
$ clisnap -a find-options -n 3
[1] cmd > find /srv -type f -user alice -group devs -exec chmod 640 {} \;
[1] description > Find files owned by a specific user 
[2] cmd > find ~/projects -type f -mtime +3 -mtime -10
[2] description > Find files modified at a given time frame
[3] cmd > find ~/projects -type d -empty
[3] description > Find empty directories

# show saved cmds
$ clisnap -s find-options
[1] find /srv -type f -user alice -group devs -exec chmod 640 {} \; : Find files owned by a specific user
[2] find ~/projects -type f -mtime +3 -mtime -10                    : Find files modified at a given time frame
[3] find ~/projects -type d -empty                                  : Find empty directories
```
