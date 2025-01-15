#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Set Poetry HTTP timeout to 120 seconds
export POETRY_HTTP_TIMEOUT=120

# Function to display usage message
usage() {
    echo "Usage: $0"
    echo "This script sets up Pyenv, Python 3.8.16, and Poetry 1.5.1."
    exit 1
}

# Function to check for required commands
check_command() {
    for cmd in "$@"; do
        if ! command -v $cmd >/dev/null 2>&1; then
            echo "$cmd is required but not installed. Please install it first."
            exit 1
        fi
    done
}

# Function to determine the shell configuration file based on the current shell
determine_shell_rc() {
    case $SHELL in
        */bash)
            shell_rc="$HOME/.bashrc"
            ;;
        */zsh)
            shell_rc="$HOME/.zshrc"
            ;;
        *)
            echo 'Please choose a valid Shell Mode (bash/zsh)'
            exit 1
            ;;
    esac
}

# Function to install Pyenv
install_pyenv() {
    if ! command -v pyenv >/dev/null 2>&1; then
        rm -rf ~/.pyenv
        curl -s https://pyenv.run | PYENV_GIT_TAG=v2.3.22 bash
        if [ $? -ne 0 ]; then
            echo "Failed to install pyenv"
            exit 1
        fi
    else
        echo "Pyenv is already installed"
    fi
}

# Function to configure Pyenv
configure_pyenv() {
    {
        echo 'export PYENV_ROOT="$HOME/.pyenv"'
        echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"'
        echo 'eval "$(pyenv init -)"'
    } >> "$shell_rc"
}

# Function to install Poetry
install_poetry() {
    if ! command -v poetry >/dev/null 2>&1; then
        curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
        if [ $? -ne 0 ]; then
            echo "Failed to install Poetry"
            exit 1
        fi
    else
        echo "Poetry is already installed"
    fi
}

# Function to configure Poetry
configure_poetry() {
    if ! grep -q 'export PATH="$HOME/.local/bin/:$PATH"' "$shell_rc"; then
        echo 'export PATH="$HOME/.local/bin/:$PATH"' >> "$shell_rc"
    fi
}

# Function to install Python version using Pyenv
install_python() {
    if ! pyenv versions | grep -q "3.8.16"; then
        pyenv install 3.8.16
    else
        echo "Python 3.8.16 is already installed"
    fi
    pyenv versions # should list Python 3.8.16 version
}

# Function to create and activate a virtual environment using Poetry
create_and_activate_venv() {
    poetry env use python3.8
    VENV_PATH=$(poetry env info --path)/bin/activate
    if [ -f "$VENV_PATH" ]; then
        source "$VENV_PATH"
        if [ $? -ne 0 ]; then
            echo "Failed to activate the virtual environment"
            exit 1
        fi
    else
        echo "Virtual environment activation script not found"
        exit 1
    fi
}

# Function to install dependencies using Poetry
install_dependencies() {
    if ! poetry install; then
        echo "Failed to install dependencies with Poetry"
        exit 1
    fi
}

# Main script execution
main() {
    check_command curl python3
    determine_shell_rc
    install_pyenv
    configure_pyenv
    #source "$shell_rc"
    install_python
    install_poetry
    configure_poetry
    create_and_activate_venv
    install_dependencies
    echo 'Setup complete'
}