# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os

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


# sheet = DataManager()
# sheet_data = sheet.get_sheet_data()
# for row in sheet_data["prices"]:
#     searcher = FlightSearch()
#     city_data = FlightData(row["iataCode"])
#     try:
#       cheapest_ticket = searcher.search_flight(city_data)
#     except:
#       continue
#     else:
#         price = cheapest_ticket["data"][0]['fare']['adults']
#         lowest_data_price = row["lowestPrice"]
#         if int(lowest_data_price) > int(price):
#             departure_data = int(cheapest_ticket["data"][0]["dTimeUTC"])
#             come_back_data = int(cheapest_ticket["data"][0]["aTimeUTC"])
#             sms = NotificationManager()
#             sms.send_message(f"\n\nprice alert! Only €{price} to fly from Dublin-DUB to {cheapest_ticket['data'][0]['cityTo']}"
#                              f"-{cheapest_ticket['data'][0]['flyTo']}, "
#                              f"from {datetime.utcfromtimestamp(departure_data).strftime('%Y-%m-%d')} UTC "
#                              f"to {datetime.utcfromtimestamp(come_back_data).strftime('%Y-%m-%d')} UTC")

# print(f"{row['city']}:  €{price}")
def add_user():
    sheet_data = DataManager()
    users_sheet_data = sheet_data.get_sheet_data("users")
    print("Welcome to Denys's Flight Club.")
    print("We find the best flight deals and email you")
    f_name = input("What is your first name? ")
    l_name = input("What is your Last name? ")
    email = input("What is your email? ")
    email_confirm = input("Type your email again. ")
    if email == email_confirm and f_name != "" and l_name != "":
        print("You're in the club!")
        sheet.post_sheet_users(f_name, l_name, email)

    elif users_sheet_data["email"]:
        print("ERROR, check your data")


def sent_msg():
    if int(lowest_data_price) > int(price):
        departure_data = int(cheapest_ticket["data"][0]["dTimeUTC"])
        return_data = int(cheapest_ticket["data"][0]["route"][1]["dTimeUTC"])
        sms = NotificationManager()
        sms.send_message(
            f"\n\nprice alert! Only €{price} to fly from Dublin-DUB to {cheapest_ticket['data'][0]['cityTo']}"
            f"-{cheapest_ticket['data'][0]['flyTo']}, "
            f"from {datetime.utcfromtimestamp(departure_data).strftime('%Y-%m-%d')} UTC "
            f"to {datetime.utcfromtimestamp(return_data).strftime('%Y-%m-%d')} UTC")


def send_email():
    if int(lowest_data_price) > int(price):
        departure_data = int(cheapest_ticket["data"][0]["dTimeUTC"])
        return_data = int(cheapest_ticket["data"][0]["route"][1]["dTimeUTC"])
        import smtplib
        with smtplib.SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            user = os.environ["GMAIL"]
            smtp.login(user=user, password=os.environ["PASSWORD"])
            for one_user in sheet_data_users["users"]:
                try:
                    smtp.sendmail(from_addr=user, to_addrs=one_user["email"], msg=f"Subject:Your trip!\n\nPrice alert!"
                                                                                  f" Only {price} Euro to fly "
                                                                                  f"from Dublin-DUB to {cheapest_ticket['data'][0]['cityTo']}"
                                                                                  f"-{cheapest_ticket['data'][0]['flyTo']}, "
                                                                                  f"from {datetime.utcfromtimestamp(departure_data).strftime('%Y-%m-%d')} "
                                                                                  f"UTC to {datetime.utcfromtimestamp(return_data).strftime('%Y-%m-%d')} "
                                                                                  f"UTC, your link: {cheapest_ticket['data'][0]['deep_link']}")
                except:
                    print("Wrong Email address")
                    continue


add_user()
sheet = DataManager()
sheet_data_prices = sheet.get_sheet_data("prices")
sheet_data_users = sheet.get_sheet_data("users")
for row in sheet_data_prices["prices"]:
    searcher = FlightSearch()
    city_data = FlightData(row["iataCode"])
    try:
        cheapest_ticket = searcher.search_flight(city_data)
        print(cheapest_ticket)
        price = cheapest_ticket["data"][0]['fare']['adults']
        print(price)
        lowest_data_price = row["lowestPrice"]
        # sent_msg()
        send_email()
    except IndexError:
        print("There's no races available")
        continue

    else:
        # sent_msg()
        send_email()
