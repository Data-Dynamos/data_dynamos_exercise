# exercise_co2_vs_temperature

## Setup

### Pyenv

- Install pyenv

```shell
export PYENV_GIT_TAG=v2.3.22
curl https://pyenv.run | bash
```

- Load pyenv automatically by adding following lines to your shell configuration `~/.zshrc` or `~/.bashrc`

```shell
# Load pyenv automatically
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

If you are using shells other than bash or zsh refer: https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv

### Python 3.8.16

```shell
pyenv --version
pyenv install 3.8.16
pyenv versions # should list Python 3.8.16 version
```

## Usage

```shell
# setup virtualenv and install the dependencies
poetry install

# run a command inside the virtualenv
poetry run dbt --version

# start a virtualenv shell and run commands inside it
poetry shell
dbt --version
```
