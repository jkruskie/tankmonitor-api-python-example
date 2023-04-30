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
ROOT_URL = 'http://localhost:5000/api'

# URL to send the leak report
URL = ROOT_URL + '/Monitors/' + monitor_guid + '/DropData'

# Print the monitor guid
print(monitor_guid)

# Headers without Content-Type since requests library will set it automatically
HEADERS = {
    'User-Agent': 'TankMonitorAPI/1.0.0',
    'Authorization': 'Bearer ' + config_data['accessToken']
}

data = [
    {
        "TankId": 1,
        "ReportTime": "2023-03-29T08:00:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 2,
        "ReportTime": "2023-03-29T08:05:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 3,
        "ReportTime": "2023-03-29T08:10:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 4,
        "ReportTime": "2023-03-29T08:15:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 5,
        "ReportTime": "2023-03-29T08:20:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 6,
        "ReportTime": "2023-03-29T08:25:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 7,
        "ReportTime": "2023-03-29T08:30:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    },
    {
        "TankId": 8,
        "ReportTime": "2023-03-29T08:35:00.0000000",
        "StartTime": "2023-03-29T08:00:00.0000000",
        "EndTime": "2023-03-30T08:00:00.0000000",
        "StartVolume": 421342,
        "EndVolume": 9842852,
        "StartWaterHeight": 0.00,
        "EndWaterHeight": 0.00,
        "StartTemp": 35.85,
        "EndTemp": 39.34,
        "StartHeight": 82.22,
        "EndHeight": 94.42
    }
]

# POST request to send the leak report
response = requests.post(
    URL,
    headers=HEADERS,
    json=data
)

# Get the response data
# response_data = response.json()

print(response.content)

# Check if the response status code is 200
# if response.status_code == 200:
#     # Print the response data
#     print(response_data)
# else:
#     # Print the error message
#     print(response_data)
