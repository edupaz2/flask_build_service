#!/bin/bash

set -e #Fail in case if any commands fail
set -E #Print errtrace in case of failure
set -T #Print functrace in case of failure

function echo_red {
    local MESSAGE=$1
    echo -e "\033[1;31m${MESSAGE}\033[0m"
}

function echo_green {
    local MESSAGE=$1
    echo -e "\033[1;32m${MESSAGE}\033[0m"
}

function echo_yellow {
    local MESSAGE=$1
    echo -e "\033[1;33m${MESSAGE}\033[0m"
}

function echo_dark_blue {
    local MESSAGE=$1
    echo -e "\033[1;34m${MESSAGE}\033[0m"
}

function echo_variable {
    local VARIABLE=$1
    local VALUE=$2
    echo -e "\033[1;33m$VARIABLE = \033[0m$VALUE"
}

function echo_build_step {
    local MESSAGE=$1
    echo -e "\033[1;35m--> $MESSAGE...\033[0m"
}

function echo_step_succeeded {
    local MESSAGE=$1
    echo -e "\033[1;32m--> $MESSAGE...\033[0m"
}

export CURRENT_DIR=`pwd`

echo_build_step "Create Python VE"
python3 -m venv $CURRENT_DIR/local-ve
source $CURRENT_DIR/local-ve/bin/activate

echo_build_step "Installing requirements"
pip install -r requirements.txt

echo_build_step "Running the app"
python3 app.py

echo_step_succeeded "EXIT"