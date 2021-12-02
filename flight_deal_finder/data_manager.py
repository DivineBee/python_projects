import requests
from pprint import pprint

API_KEY = ""
SHEETS_ENDPOINT = "https://api.sheety.co/6da7a1218ffd000a3d067839da946459/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETS_ENDPOINT)
        self.destination_data = response.json()["prices"]
        # pprint(destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETS_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)