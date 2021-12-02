import requests
from datetime import datetime

USERNAME = "" # any username
TOKEN = "" # some random password like
GRAPH_ID = "b33"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# requests.post(url=graph_endpoint, json=graph_params, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes you coded?"),
}

requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "30"
}

# requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# requests.delete(url=delete_pixel_endpoint, headers=headers)