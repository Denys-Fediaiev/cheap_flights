import os

import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_url = "https://api.sheety.co/636f489255bef7e9a415099266b12b0b/flightDeals"
        self.params = {}
        self.headers = {
            "Authorization": os.environ["AUTHORIZATION"]
        }
        self.kiwi_headers = {
            "apikey": os.environ["KIWI_API_KEY"]
        }

    def get_sheet_data(self, sheet):
        if sheet == "prices":
            response = requests.get(f"{self.api_url}/prices")
            data = response.json()
            return data
        elif sheet == "users":
            response = requests.get(f"{self.api_url}/users")
            data = response.json()
            return data

    def post_sheet_price(self, city, iatacode, lowest_price):
        self.params = {
            "price": {
                "city": city,
                "iataCode": iatacode,
                "lowestPrice": lowest_price
            }
        }
        self.response = requests.post(url=f"{self.api_url}/prices", json=self.params, headers=self.headers)
        self.data = self.response.json()

    def post_sheet_users(self, f_name, l_name, email):
        self.params = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }
        self.response = requests.post(url=f"{self.api_url}/users", json=self.params, headers=self.headers)

    def update_sheet_price(self, object_id, city=None, iatacode=None, lowest_price=None):
        self.api_url = f"https://api.sheety.co/636f489255bef7e9a415099266b12b0b/flightDeals/prices/{object_id}"

        self.params = {
            "price": {
                "city": city,
                "iataCode": iatacode,
                "lowestPrice": lowest_price
            }
        }
        self.response = requests.put(url=self.api_url, json=self.params, headers=self.headers)
        self.data = self.response.json()

    def get_sheet_iata(self, city_name):
        kiwi_api_url = "https://api.tequila.kiwi.com"

        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{kiwi_api_url}/locations/query", params=query, headers=self.kiwi_headers)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code


# sheety = DataManager()
# print(sheety.get_sheet_iata("Paris"))



# print(sheety.data)