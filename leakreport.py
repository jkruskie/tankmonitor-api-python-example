import requests  # Import the requests library
import json
import yaml

# Function to read the YAML configuration file
def read_config_file(file_path):
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data

# Read the config.yml file
config_file_path = 'config.yml'
config_data = read_config_file(config_file_path)

# Get the monitor guid
monitor_guid = config_data['monitor']['guid']

# Root api url
ROOT_URL = 'https://tankmonitorapi.dumbdevelopers.com/api'

# URL to send the leak report
URL = ROOT_URL + '/Monitors/' + monitor_guid + '/LeakReport'

# Print the monitor guid
print(monitor_guid)

# Headers without Content-Type since requests library will set it automatically
HEADERS = {
    'User-Agent': 'TankMonitorAPI/1.0.0',
    'Authorization': 'Bearer ' + config_data['accessToken']
}

# Use 'with' statement to ensure the file is closed after reading
with open('leakdata.txt', 'rb') as file:
    # POST request to send the leak report
    response = requests.post(
        URL,
        headers=HEADERS,
        files={'file': file}  # Send the file as 'multipart/form-data'
    )

# Get the response data
response_data = response.json()

# Check if the response status code is 200
if response.status_code == 200:
    # Print the response data
    print(response_data)
else:
    # Print the error message
    print(response_data)