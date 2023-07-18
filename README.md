# data_dynamos_exercise

There are two ways to setup and run the code in this repository:

1. [Setup Directly on the Machine](#setup-directly-on-the-machine): Install all the Software directly on your machine and run the code.
2. [Setup Using Docker](#setup-using-docker): Use a pre-built Docker image containing all the Software already and run the code inside Docker container.

## Setup Directly on the Machine

### Prerequisites

- Pyenv
- Python
- Poetry

#### Install Pyenv v2.3.22

```shell
curl https://pyenv.run | PYENV_GIT_TAG=v2.3.22 bash
```

##### Load pyenv automatically

###### For bash

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec "$SHELL"
```

###### For Zsh

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
```

If you are using shells other than bash or Zsh refer: https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv

#### Install Python 3.8.16

```shell
pyenv --version
pyenv install 3.8.16
pyenv versions # should list Python 3.8.16 version
```

#### Install Poetry 1.5.1

```shell
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.1 python3 -
```

##### Add Poetry bin directory to PATH

###### For bash:

```shell
echo 'export PATH="$HOME/.local/bin/:$PATH"' >> ~/.bashrc
exec "$SHELL"
```

###### For Zsh:

```shell
echo 'export PATH="$HOME/.local/bin/:$PATH"' >> ~/.zshrc
exec "$SHELL"
```

### Usage

#### Create virtualenv and Install Dependencies

```shell
# setup virtualenv and install the dependencies
poetry install

# run a command inside the virtualenv
poetry run dbt --version

# start a virtualenv shell and run commands inside it
poetry shell
dbt --version

# install dbt packages
cd data_transformation
dbt deps
```

#### Data Transformations

```shell
poetry shell

export SNOWFLAKE_ACCOUNT='<your-snowflake-account-name>'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

cd data_transformation
dbt debug # should connect to snowflake successfully
```

#### Data Visualizations

```shell
poetry shell

export SNOWFLAKE_ACCOUNT='<your-snowflake-account-name>'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

cd data_visualization
streamlit run app.py # should be able to access the UI
```

## Setup Using Docker

### Prerequisites

- Docker

### Usage

> **Note:** The code will be mounted inside the container so whatever changes you make in your local machine will be synced to the container.

#### Data Transformations

- Start the container

```shell
docker run --rm -it -v $PWD:/opt/data_dynamos_exercise quay.io/data-dynamos/data_dynamos_exercise bash
```

- Run the code inside the container

```shell
export SNOWFLAKE_ACCOUNT='<your-snowflake-account-name>'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

cd data_transformation
dbt debug # should connect to snowflake successfully
```

#### Data Visualizations

- Start the container

```shell
docker run --rm -it -v $PWD:/opt/data_dynamos_exercise quay.io/data-dynamos/data_dynamos_exercise -p 8501:8501 bash
```

- Run the code inside the container

```shell
export SNOWFLAKE_ACCOUNT='<your-snowflake-account-name>'
export SNOWFLAKE_DATABASE='<your-database-name>'
export SNOWFLAKE_USER='<your-user-name>'
export SNOWFLAKE_PASSWORD='<your-password>'

cd data_visualization
streamlit run app.py # should be able to access the UI
```
