# data_dynamos_exercise

## Prerequisites

- Pyenv
- Python
- Poetry

### Install Pyenv v2.3.22

```shell
curl https://pyenv.run | PYENV_GIT_TAG=v2.3.22 bash
```

#### Load pyenv automatically

##### For bash

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
```

##### For Zsh

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

If you are using shells other than bash or Zsh refer: https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv

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

#### Add Poetry bin directory to PATH 

##### For bash:

```shell
echo 'export PATH="$HOME/.local/bin/:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

##### For Zsh:

```shell
echo 'export PATH="$HOME/.local/bin/:$PATH"' >> ~/.zshrc
source ~/.zshrc
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
cd data_transformations
dbt deps
```

### Data Transformations

```shell
poetry shell

export SNOWFLAKE_ACCOUNT='<your-snowflake-account-name>'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

cd data_transformations
dbt debug # should connect successfully
```

### Data Visualizations

```shell
poetry shell

export SNOWFLAKE_ACCOUNT='<your-snowflake-account-name>'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

cd data_visualization
streamlit run app.py
```
