import requests
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

# Get the monitor mac address
mac_address = config_data['monitor']['macAddress']

# Get the location guid
location_guid = config_data['location']['guid']

# Root api url
ROOT_URL = 'https://tankmonitorapi.dumbdevelopers.com/api'

# Authentication Route
AUTHENTICATION_ROUTE = '/monitor/authenticate'

# Authentication url
AUTHENTICATION_URL = ROOT_URL + AUTHENTICATION_ROUTE

# Headers
HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'TankMonitorAPI/1.0.0'
}

# POST request to authenticate using the monitor mac address and location guid
post_data = {
    'macAddress': mac_address,
    'locationGuid': location_guid
}

# Print the post data
print(post_data)

response = requests.post(
    AUTHENTICATION_URL, 
    json=post_data,  # Use the json parameter to pass the post_data as JSON
    headers=HEADERS
)

# Get the response data
response_data = response.json()

# Check if the response status code is 200
if response.status_code == 200:
    # Print the response data
    print(response_data)
    # Save the token to the config.yml file
    config_data['accessToken'] = response_data['accessToken']
    # Write the config.yml file
    with open(config_file_path, 'w') as file:
        yaml.dump(config_data, file)
else:
    # Print the error message
    print(response_data)