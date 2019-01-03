#This code sample uses requests (HTTP library)
import requests

params = {
    'access_token': '[YOUR_ACCESS_TOKEN]',
    'device_id': '[YOUR_DEVICE_ID]'
}

try:
    response = requests.post("https://api.netatmo.com/api/getstationsdata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)
