TEQUILA_AFILID = "YOUR TEQUILA ID"
TEQUILA_KEY = "YOUR TEQUILA API KEY"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
SHEET_ENDPOINT = "https://api.sheety.co/46c8b7ad7bb6cc467f7090aa26bd7ebd/flightDeals/prices"


SHEETY_PRICES_ENDPOINT = SHEET_ENDPOINT

import requests
import json
from datetime import *
from flight_data import FlightData

class FlightSearch:

    # Receive input for 'city_name' from the google spreedsheet.
    # Output the related IATA code.

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        print(f"TEQUILA STATUS CODE: {response.raise_for_status}")
        results = response.json()["locations"]
        #print(f"RESULT={response.json()}")
        code = results[0]["code"]
        return code
    
    def check_flight(self, departure_airport_code, arrival_airport_code, from_date, to_date):
        # setting tequila search endpoint query and apikey value for the endpoint header
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_KEY }

        query = {
            "fly_from":departure_airport_code,
            "fly_to": arrival_airport_code,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR" } 
        
        
        # Trying and checking if there are flights based on the parsed query.
        try:
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            print(f"TEQUILA REQUESTS FLIGHT RESEARCH STATUS CODE: {response.raise_for_status}")
            tequila_data = response.json()["data"][0]

        # If there is no flight, catch the 'IndexError' and print the cause of the error.
        except IndexError:
            print(f"no fly for the destination: {arrival_airport_code}")
            return None
        
        # If everything is okay, use the flight data query, which contains the data of interest
        # taken from the Tequila flight search response. Return it as the result of the function.
        else:
            flight_data = FlightData(
                price=tequila_data["price"],
                origin_city=tequila_data["route"][0]["cityFrom"],
                origin_airport=tequila_data["route"][0]["flyFrom"],
                destination_city=tequila_data["route"][0]["cityTo"],
                destination_airport=tequila_data["route"][0]["flyTo"],
                out_date=tequila_data["route"][0]["local_departure"].split("T")[0],
                return_date=tequila_data["route"][1]["local_departure"].split("T")[0]
                )

            print(f"{flight_data.destination_city}: {flight_data.price}")
            return flight_data












