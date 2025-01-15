#!/bin/bash

# Check for required commands
for cmd in curl python3; do
    if ! command -v $cmd >/dev/null 2>&1; then
        echo "$cmd is required but not installed. Please install it first."
        exit 1
    fi
done

# Determine the shell configuration file based on the current shell
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

# Install Pyenv v2.3.22
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

# Add pyenv initialization to the shell configuration file
{
    echo 'export PYENV_ROOT="$HOME/.pyenv"'
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"'
    echo 'eval "$(pyenv init -)"'
} >> "$shell_rc"

# Add Poetry bin directory to PATH if not already present
if ! grep -q 'export PATH="$HOME/.local/bin/:$PATH"' "$shell_rc"; then
    echo 'export PATH="$HOME/.local/bin/:$PATH"' >> "$shell_rc"
fi

# Source the shell configuration file to apply changes
source "$shell_rc"

# Install Python 3.8.16
if ! pyenv versions | grep -q "3.8.16"; then
    pyenv install 3.8.16
else
    echo "Python 3.8.16 is already installed"
fi
pyenv versions # should list Python 3.8.16 version

# Install Poetry 1.5.1
if ! command -v poetry >/dev/null 2>&1; then
    curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
    if [ $? -ne 0 ]; then
        echo "Failed to install Poetry"
        exit 1
    fi
else
    echo "Poetry is already installed"
fi

# Create a virtual environment using Poetry
poetry env use python3.8

# Activate the virtual environment and run commands within it
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

# Install dependencies with Poetry
if ! poetry install; then
    echo "Failed to install dependencies with Poetry"
    exit 1
fi


echo 'Setup complete'