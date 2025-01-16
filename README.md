# data_dynamos_exercise

There are two ways to setup and run the code in this repository:

1. [Setup Directly on the Machine](#setup-directly-on-the-machine): Install all the Software directly on your machine and run the code.
2. [Setup Using Docker](#setup-using-docker): Use a pre-built Docker image containing all the Software already and run the code inside Docker container.

## Setup Directly on the Machine

### Prerequisites
Ensure you have Git installed on your machine. If not, you can download it from git-scm.com.

### Navigate to the directory where you want to clone the project. For example:
```shell
cd path/to/your/directory
```

### Clone the repository using this command:
```shell
git clone https://github.com/Data-Dynamos/data_dynamos_exercise.git
cd data_dynamos_exercise
```

### Run the scripts for ontime setup
```shell
./scripts/streamlit_snowflake_setup.sh  
```

### To start streamlit instance - run
```shell
./scripts/stearmlit_snowflake_startup.sh
```

## Setup Using Docker

### Prerequisites

- Docker (Use colima for docker - https://github.com/abiosoft/colima)

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
docker run -p 8501:8501 --rm -it -v $PWD:/opt/data_dynamos_exercise quay.io/data-dynamos/data_dynamos_exercise bash
```

- Run the code inside the container
 
```shell

./scripts/stearmlit_snowflake_startup.sh

```
