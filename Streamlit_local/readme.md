
```
### Requirements
# Install Streamlit and plotly if not installed earlier
```
```
### Steps  
1. cd to Streamlit_local
2. Copy 3 csv files and place then inside SQL_Exercise 
creating a folder data within it. (SQL_Exercise/data/)
3.  cd to Transformations and run scripts in below order
3.1. Run python data_processing.py
3.2. Run python global_temp.py
3.3. Run python temp_by_country.py
3.4. Run Each Exercise in order of number.
After all these are run. Each script saves an output file to
output folder.
4. cd to Streamlit folder
4.1. run streamlit run app.py

This should open the web page in local host and you are 
good to analyse the data using the visulaisation.

Task:
--See how the visualisations can be further improved.
-- See how we have preprocessed the raw files and understand the 
aggregations used to arrive at the output.
-- See how the streamlit app is configured and different 
elements are used to get the complete view.
```

## Setup Using Docker

### Prerequisites
- Brew (Use homebrew for mac package manager - https://brew.sh/)
- Docker (Use colima for docker - https://github.com/abiosoft/colima) 
- Once Docker is installed, start the docker instance:
```shell 
colima start
docker ps
```

### Usage
