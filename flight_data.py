import datetime
from datetime import *
import requests


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, place_to_fly):
        self.price = 0,
        self.departure_airport_code = "DUB"
        self.departure_city = "Dublin"
        self.arrive_to = place_to_fly
        tomorrow = date.today() + timedelta(days=1)
        self.date_from = tomorrow.strftime("%d/%m/%Y")
        # self.date_from = self.date_from.strftime("%d/%m/%Y")
        date_to = tomorrow + timedelta(days=30*6)
        self.date_to = date_to.strftime("%d/%m/%Y")
        self.nights_in_dst_from = 7
        self.nights_in_dst_to = 28
        self.curr = "EUR"
        self.max_stopovers = "1"
# s = FlightData("Paris")



