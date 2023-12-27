SHEET_ENDPOINT = "https://api.sheety.co/46c8b7ad7bb6cc467f7090aa26bd7ebd/flightDeals/prices"




from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = SHEET_ENDPOINT

# Get the destination spreadsheet.
# Update the destination IATA code on the spreadsheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}
    # Get the destination sheet using the `requests` module, parsing the 'Sheety API'.
    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        print(f"DATA MANAGER RAISE STATUS CODE: {response.raise_for_status}")
        data = response.json()
        self.destination_data = data["prices"]
        #print(data)
        return self.destination_data


    #In the DataManager Class make a PUT request and use the row id  from sheet_data
    # to update the Google Sheet with the IATA codes
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            #print(response.text)