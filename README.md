# data_dynamos_exercise

## Prerequisites

- Pyenv
- Python
- Poetry

### Install Pyenv v2.3.22

```shell
curl https://pyenv.run | PYENV_GIT_TAG=v2.3.22 bash
```

- Load pyenv automatically by adding following lines to your shell configuration `~/.zshrc` or `~/.bashrc`

```shell
# Load pyenv automatically
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

If you are using shells other than bash or zsh refer: https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv

### Install Python 3.8.16

```shell
pyenv --version
pyenv install 3.8.16
pyenv versions # should list Python 3.8.16 version
```

### Install Poetry 1.5.1

```shell
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
```

## Usage

### Create virtualenv and Install Dependencies

```shell
# setup virtualenv and install the dependencies
poetry install

# run a command inside the virtualenv
poetry run dbt --version

# start a virtualenv shell and run commands inside it
poetry shell
dbt --version

# install dbt packages
dbt deps
```

### Configure Credentials and Connect to Snowflake

```shell
export SNOWFLAKE_ACCOUNT='ni10825.ap-south-1.aws'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

dbt debug # should connect successfully
```
