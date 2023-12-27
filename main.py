
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from twilio.rest import Client


ORIGINAL_IATA_CITY = "CRL"
MY_SENDING_NUMBER = "+YOUR TWILLIO SENDING NUMBER"
MY_RECEIVING_NUMBER = "YOUR RECEIVING NUMBER"
TWILLIO_SID = "YOUR TWILLIO SID"
TWILLIO_AUTHTOKEN = "YOUR TWILLIO AUTHTOKEN"


def send_sms():
    global message
    client = Client(TWILLIO_SID, TWILLIO_AUTHTOKEN)
    message = client.messages.create(body=message_text, from_= MY_SENDING_NUMBER, to= MY_RECEIVING_NUMBER)
    

#  Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


#print(sheet_data)

#Get the list of flights I want to search from the Google Sheet.
#Here, I'm retrieving the content from this sheet using the `requests` module.
#Then, I extract the 'IATA Code' (International Air Transport Association) from it to parse into the 
#flight departure airport field in the parameters of the requests query i will call the function to check the flight
if sheet_data[0]["iataCode"] == "":  
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    #print(sheet_data)
    
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


# date_to is the variable that contains the number of days to extend the range of flight ticket research
# creating date values for flight check query
days_to = 30 * 6
now = datetime.now()
date_from = now.strftime("%d/%m/%Y")
date_to = (now.date() + timedelta(days=days_to)).strftime("%d/%m/%Y")

#check for the flight passing to it required input
for destination in sheet_data: 
    flight_search = FlightSearch()
    flight = flight_search.check_flight(
                                        departure_airport_code=ORIGINAL_IATA_CITY,
                                        arrival_airport_code=destination["iataCode"], 
                                        from_date=date_from, 
                                        to_date=date_to
                                        )
    print(f"flight data type:{flight.price}")
    # Check the price of the flight.
    # If it's equal or lower then equal to the price I have on the Google Sheet, send me an SMS with some information about the flight.
    if flight.price <= destination["lowestPrice"]:
        message_text = (f"Price: {flight.price} \nDeparture City Name: {flight.origin_city} \nDeparture Airport IATA Code: {flight.destination_airport} \nArrival City Name: {flight.destination_city}")
        send_sms()
        print(f"sms sent at {now}")