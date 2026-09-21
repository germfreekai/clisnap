#! /usr/bin/bash

# color
RED="\e[32m"
BLUE="\e[36m"

RESET="\e[0m"

HOME_DIR=$(echo ${HOME})
CLISNAP_DIR=${HOME_DIR}/.clisnap

echo -e "${BLUE}[+] Installing clisnap...${RESET}"
echo -e "${BLUE}[+] Creating dir ${CLISNAP_DIR}...${RESET}"

if [ ! -d ${CLISNAP_DIR} ]; then
    if ! $(mkdir ${CLISNAP_DIR}); then
        echo -e "[X] Failed to create dir ${CLISNAP_DIR}${RESET}"
    fi
else
    echo -e "[!] Dir ${CLISNAP_DIR} arleady exits, skipping..."
fi

echo -e "${BLUE}[+] Installing dependencies...${RESET}"
which pip3
pip3 install . || echo -e "[X] Failed to install dependencies${RESET}" && echo -e "${BLUE}[+] Installed...${RESET}"

echo -e "${BLUE}[+] Done!${RESET}"

clisnap -h
