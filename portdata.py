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
URL = ROOT_URL + '/Monitors/' + monitor_guid + '/PortData'

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
        "Gallons": 110,
        "Inches": 72,
        "Water": 0.5,
        "Temperature": 65.4,
        "Ullage": 3000
    },
    {
        "TankId": 2,
        "ReportTime": "2023-03-29T08:05:00.0000000",
        "Gallons": 87,
        "Inches": 60,
        "Water": 0.3,
        "Temperature": 67.2,
        "Ullage": 2800
    },
    {
        "TankId": 3,
        "ReportTime": "2023-03-29T08:10:00.0000000",
        "Gallons": 60,
        "Inches": 48,
        "Water": 0.1,
        "Temperature": 63.8,
        "Ullage": 2400
    },
    {
        "TankId": 4,
        "ReportTime": "2023-03-29T08:15:00.0000000",
        "Gallons": 30,
        "Inches": 36,
        "Water": 0,
        "Temperature": 60.1,
        "Ullage": 2000
    },
    {
        "TankId": 5,
        "ReportTime": "2023-03-29T08:20:00.0000000",
        "Gallons": 62,
        "Inches": 50,
        "Water": 0.2,
        "Temperature": 65.6,
        "Ullage": 2600
    },
    {
        "TankId": 6,
        "ReportTime": "2023-03-29T08:25:00.0000000",
        "Gallons": 75,
        "Inches": 56,
        "Water": 0.4,
        "Temperature": 68.9,
        "Ullage": 2800
    },
    {
        "TankId": 7,
        "ReportTime": "2023-03-29T08:30:00.0000000",
        "Gallons": 91,
        "Inches": 64,
        "Water": 0.3,
        "Temperature": 70.3,
        "Ullage": 3000
    },
    {
        "TankId": 8,
        "ReportTime": "2023-03-29T08:35:00.0000000",
        "Gallons": 55,
        "Inches": 46,
        "Water": 0.1,
        "Temperature": 62.8,
        "Ullage": 2400
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

print(response)

# Check if the response status code is 200
# if response.status_code == 200:
#     # Print the response data
#     print(response_data)
# else:
#     # Print the error message
#     print(response_data)
