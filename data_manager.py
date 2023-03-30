import requests


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_url = "https://api.sheety.co/636f489255bef7e9a415099266b12b0b/flightDeals/prices"
        self.params = {}
        self.headers = {
            "Authorization": "Basic key=="
        }
        self.kiwi_headers = {
            "apikey": "api"
        }
        self.response = requests.get(self.api_url)
        self.data = self.response.json()

    def get_sheet_data(self):
        return self.data

    def post_sheet_data(self, city, iatacode, lowest_price):
        self.params = {
            "price": {
                "city": city,
                "iataCode": iatacode,
                "lowestPrice": lowest_price
            }
        }
        self.response = requests.post(url=self.api_url, json=self.params, headers=self.headers)
        self.data = self.response.json()

    def update_sheet_data(self, object_id, city=None, iatacode=None, lowest_price=None):
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