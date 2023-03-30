#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import *
from flight_search import *
from flight_data import *
from notification_manager import *


# sheet = DataManager()
# sheet_data = sheet.get_sheet_data()
# for s in sheet_data["prices"]:
#     if s["iataCode"] == '':
#         iata = sheet.get_sheet_iata(s["city"])
#         sheet.update_sheet_data(s["id"], iatacode=iata)


sheet = DataManager()
sheet_data = sheet.get_sheet_data()
for row in sheet_data["prices"]:
    searcher = FlightSearch()
    city_data = FlightData(row["iataCode"])
    cheapest_ticket = searcher.search_flight(city_data)
    price = cheapest_ticket["data"][0]['fare']['adults']
    lowest_data_price = row["lowestPrice"]
    if int(lowest_data_price) > int(price):
        departure_data = int(cheapest_ticket["data"][0]["dTimeUTC"])
        come_back_data = int(cheapest_ticket["data"][0]["aTimeUTC"])
        sms = NotificationManager()
        sms.send_message(f"\n\nprice alert! Only €{price} to fly from Dublin-DUB to {cheapest_ticket['data'][0]['cityTo']}"
                         f"-{cheapest_ticket['data'][0]['flyTo']}, "
                         f"from {datetime.utcfromtimestamp(departure_data).strftime('%Y-%m-%d')} UTC "
                         f"to {datetime.utcfromtimestamp(come_back_data).strftime('%Y-%m-%d')} UTC")

        # print(f"{row['city']}:  €{price}")


