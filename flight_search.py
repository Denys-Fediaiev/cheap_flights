import datetime
from datetime import *

from flight_data import *
class FlightSearch:
    #This class is responsible for talking to the Flight Search API. Kivi takes
    def __init__(self):
        #self.flight_data = flight_data
        self.search_api_url = "https://api.tequila.kiwi.com"
        self.headers = {
            "apikey": "api"
        }
        self.params = {}
        # self.data_time = datetime.datetime.now().strftime()

    def search_flight(self, flight_data: FlightData):
        self.params = {
            #"apikey": "api",
            "fly_from": flight_data.departure_airport_code,
            "fly_to": flight_data.arrive_to,
            "date_from": flight_data.date_from,
            "date_to": flight_data.date_to,
            "nights_in_dst_from": flight_data.nights_in_dst_from,
            "nights_in_dst_to": flight_data.nights_in_dst_to,
            "one_for_city": 1
        }

        response = requests.get(url=f"{self.search_api_url}/search", params=self.params, headers=self.headers)
        data = response.json()
        return data

# m = FlightSearch()
# p = FlightData("PAR")
# print(m.search_flight(p))

