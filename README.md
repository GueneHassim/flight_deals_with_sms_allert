
In summary, the code development for the project was relatively straightforward, but challenges arose from unclear errors, especially during the transition from PyCharm IDE to a less user-friendly environment. Communication issues with servers and difficulties with API credentials added to the complexity. A persistent problem involved accessing a value in a nested dictionary and list structure, addressed through 'try & except' error handling.

Moreover, the program demonstrates resilience when no flights are available for a specific destination. Instead of encountering an error and halting, the I gracefully captures the error, prints 'No flight for this destination,' and proceeds with the search for other destinations.

Finally, when the program finds flights within specified price criteria, it sends an SMS with flight details, adhering to my search criteria.

### in italiano
Per me non è stato affatto facile portare a realizzazione questo progetto. L'idea era di realizzare un programma che consultasse una lista di destinazioni e prezzi di mio interesse che ho compilato su un file Google Sheet, salvato nel Drive di un mio account Google. Una delle sezioni del programma OOP effettua la lettura e compilazione della cella 'iata' di ogni destinazione. Il codice IATA dell'aeroporto di destinazione e partenza sta per 'International Air Transport Association' ed è il codice identificativo (per così dire) di ogni aeroporto. Lo compilo dunque nello spreadsheet per poterlo usare nella query di richiesta dati voli sulle destinazioni.

Lo sviluppo del codice di per sé è abbastanza semplice; il vero ostacolo che ho incontrato in questo progetto è stato causato da errori non facilmente comprensibili. reso più difficile dalla mia transizione dall'IDE PyCharm, che è molto più amichevole, pulita e chiara nel debugging. Ad esempio, ho dovuto affrontare problemi di comunicazione con vari server e la difficoltà nel capire cosa non andasse con le credenziali delle API.

Il problema più persistente che ho affrontato è stato non riuscire ad accedere al valore di un dizionario in una lista, a sua volta all'interno di un altro dizionario. La struttura era apparentemente semplice:

value = my_dict['key2'][0]['inner_key1']

Nonostante fossi certo che la mia stringa fosse corretta, il compilatore restituiva continuamente 'IndexError: out of index'. Dopo aver compreso la causa dell'errore, ho implementato una gestione dell'errore utilizzando 'try & except'."

dunque in caso non ci fossero voli per una determinata meta il programma invece di bloccarsi in errore, cattura l'errore, stampa 'no flight for this destination', e continua la ricerca sulle altre destinazione.

alla fine se trova voli i quali prezzi rientrano nei miei cliteri di ricerca, mi invia un sms con i dettagli del foto ecc

###################################################################
########################### END ###################################
###################################################################








[{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
404


paramters = {
    "endpoint": "search",
    "fly_from=city": "DUS",
    "fly_to=city": "PRG",
    "date_from": (25/12/2023),
    "date_to": (25/1/2024)
}

MacBook-Pro-di-Hassim:flight-deals-start guenemacbook$ /usr/local/bin/python3 /Users/guenemacbook/Developments/Python/flight-deals-start/test_main.py
<bound method Response.raise_for_status of <Response [200]>>

{'search_id': '9252add3-e508-3483-22a6-2b89110be2dd', 'currency': 'GBP', 'fx_rate': 0.867801, 'data': [{'id': '1262145c4dac00003bb25f7d_0|145c12624dbb0000e3f07fce_0', 'flyFrom': 'DUS', 'flyTo': 'PRG', 'cityFrom': 'Düsseldorf', 'cityCodeFrom': 'DUS', 'cityTo': 'Prague', 'cityCodeTo': 'PRG', 'countryFrom': {'code': 'DE', 'name': 'Germany'}, 'countryTo': {'code': 'CZ', 'name': 'Czechia'}, 'local_departure': '2024-06-10T07:00:00.000Z', 'utc_departure': '2024-06-10T05:00:00.000Z', 'local_arrival': '2024-06-10T08:15:00.000Z', 'utc_arrival': '2024-06-10T06:15:00.000Z', 'nightsInDest': 15, 'quality': 140.796275, 'distance': 544.44, 'duration': {'departure': 4500, 'return': 4500, 'total': 9000}, 'price': 84, 'conversion': {'EUR': 96.79638534641006, 'GBP': 84}, 'fare': {'adults': 84, 'children': 84, 'infants': 84}, 'discount_data': None, 'fare_locks': {'EUR': [{'default': False, 'duration': 'P7D', 'itinerary_price_limit': 296.796385, 'itinerary_price_remaining': 96.796385, 'fare_lock_kind': 'fee', 'price': 25, 'rule_instance_id': 26750, 'version': 'v1'}, {'default': False, 'duration': 'P1D', 'itinerary_price_limit': 296.796385, 'itinerary_price_remaining': 96.796385, 'fare_lock_kind': 'fee', 'price': 5, 'rule_instance_id': 26749, 'version': 'v1'}, {'default': True, 'duration': 'P3D', 'itinerary_price_limit': 296.796385, 'itinerary_price_remaining': 96.796385, 'fare_lock_kind': 'fee', 'price': 10, 'rule_instance_id': 26748, 'version': 'v1'}], 'GBP': [{'default': False, 'duration': 'P7D', 'itinerary_price_limit': 257.560199699385, 'itinerary_price_remaining': 83.999999699385, 'fare_lock_kind': 'fee', 'price': 21.695025, 'rule_instance_id': 26750, 'version': 'v1'}, {'default': False, 'duration': 'P1D', 'itinerary_price_limit': 257.560199699385, 'itinerary_price_remaining': 83.999999699385, 'fare_lock_kind': 'fee', 'price': 4.339005, 'rule_instance_id': 26749, 'version': 'v1'}, {'default': True, 'duration': 'P3D', 'itinerary_price_limit': 257.560199699385, 'itinerary_price_remaining': 83.999999699385, 'fare_lock_kind': 'fee', 'price': 8.67801, 'rule_instance_id': 26748, 'version': 'v1'}]}, 'bags_price': {'1': 67.688478, '2': 262.943703}, 'baglimit': {'hand_height': 40, 'hand_length': 55, 'hand_weight': 8, 'hand_width': 23, 'hold_dimensions_sum': 158, 'hold_height': 52, 'hold_length': 78, 'hold_weight': 23, 'hold_width': 28, 'personal_item_height': 30, 'personal_item_length': 40, 'personal_item_weight': 8, 'personal_item_width': 25}, 'availability': {'seats': 9}, 'airlines': ['EW'], 'route': [{'id': '1262145c4dac00003bb25f7d_0', 'combination_id': '1262145c4dac00003bb25f7d', 'flyFrom': 'DUS', 'flyTo': 'PRG', 'cityFrom': 'Düsseldorf', 'cityCodeFrom': 'DUS', 'cityTo': 'Prague', 'cityCodeTo': 'PRG', 'local_departure': '2024-06-10T07:00:00.000Z', 'utc_departure': '2024-06-10T05:00:00.000Z', 'local_arrival': '2024-06-10T08:15:00.000Z', 'utc_arrival': '2024-06-10T06:15:00.000Z', 'airline': 'EW', 'flight_no': 9772, 'operating_carrier': 'E6', 'operating_flight_no': '', 'fare_basis': '', 'fare_category': 'M', 'fare_classes': '', 'return': 0, 'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None, 'vehicle_type': 'aircraft'}, {'id': '145c12624dbb0000e3f07fce_0', 'combination_id': '145c12624dbb0000e3f07fce', 'flyFrom': 'PRG', 'flyTo': 'DUS', 'cityFrom': 'Prague', 'cityCodeFrom': 'PRG', 'cityTo': 'Düsseldorf', 'cityCodeTo': 'DUS', 'local_departure': '2024-06-25T20:25:00.000Z', 'utc_departure': '2024-06-25T18:25:00.000Z', 'local_arrival': '2024-06-25T21:40:00.000Z', 'utc_arrival': '2024-06-25T19:40:00.000Z', 'airline': 'EW', 'flight_no': 4238, 'operating_carrier': 'E6', 'operating_flight_no': '', 'fare_basis': '', 'fare_category': 'M', 'fare_classes': 'E', 'return': 1, 'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None, 'vehicle_type': 'aircraft'}], 'booking_token': 'GuwwCnkz99tGiHFQnkIHgu1MmF7R6OU9mYK4zqcNQeVwJygDDoQP7p6uUimpeD8q-HUkZ5-TNc6vabhsXIyUyOcVD5gpnbSPD1ZK25eOYSONLzt0seL-mAGiDAO7ivH9V3OXHb7reLh6D-__u5y12fBzl3oqyd-gz96sIyl07wLh8Up2F_f__XKJjtK70NJgWDmJOf1KTOT8nWAkDKD9kZDOUtx2hDTx08hvqeGhoHOdm1PFF_3Dve3JF7R5XEIPxnXhqX3UIXBEwHtBdSScSjGTd_FqxsbPvdn8Yw64xEYw6ifFqG2wgx68P7So4-f2NNPIFBIUl7DGcJcqWqsZqq3vlhmtsqou03V7IQp1dfEwpVYUEPQ7oOcnlPdCynF5Nr58bchJoRG_umGxZwuilrpIWTodpEpXLWuvkKMrsk3Hlln3-wonOLkX5nkQYm7PZWaBIZXDTngvcwrMAx-jgyin-QnmbLgqkz_xYmcui_mv46Y7XQji7qEoUNEupVrgjpFNR4ys2ygm8MiMqJfGkUzerEsonN_VeVeII4kER2ek-mFCK5Cyg9FJZrBEvJmZjpRbCZsGA-15DVx12OJzM3tb_86N5XfaipWFnfARtM9BISbhE9e9T2zTYitulH_ZnB6faVCDqtriGRxKfBLIFEUAuwif8pEnLxRC-QhZrvqr7vVA_3ZaJWub4OqH3sAu_b6GQxA4b_DPEuRwVcBtw7WrrXtiZcIe1g9vwuShKyCBQUc7x8CMxg3BJ5vq2UgB54rLz0uz9-WCJrVejNuHMMHB1lqST66UI3Hcegrbzw6a39vDBmhjwAMGXtnPpVT8U', 'deep_link': 'https://www.kiwi.com/deep?affilid=appbrewerystudent4rf4flightsearcher&currency=GBP&flightsId=1262145c4dac00003bb25f7d_0%7C145c12624dbb0000e3f07fce_0&from=DUS&lang=en&passengers=1&to=PRG&booking_token=GuwwCnkz99tGiHFQnkIHgu1MmF7R6OU9mYK4zqcNQeVwJygDDoQP7p6uUimpeD8q-HUkZ5-TNc6vabhsXIyUyOcVD5gpnbSPD1ZK25eOYSONLzt0seL-mAGiDAO7ivH9V3OXHb7reLh6D-__u5y12fBzl3oqyd-gz96sIyl07wLh8Up2F_f__XKJjtK70NJgWDmJOf1KTOT8nWAkDKD9kZDOUtx2hDTx08hvqeGhoHOdm1PFF_3Dve3JF7R5XEIPxnXhqX3UIXBEwHtBdSScSjGTd_FqxsbPvdn8Yw64xEYw6ifFqG2wgx68P7So4-f2NNPIFBIUl7DGcJcqWqsZqq3vlhmtsqou03V7IQp1dfEwpVYUEPQ7oOcnlPdCynF5Nr58bchJoRG_umGxZwuilrpIWTodpEpXLWuvkKMrsk3Hlln3-wonOLkX5nkQYm7PZWaBIZXDTngvcwrMAx-jgyin-QnmbLgqkz_xYmcui_mv46Y7XQji7qEoUNEupVrgjpFNR4ys2ygm8MiMqJfGkUzerEsonN_VeVeII4kER2ek-mFCK5Cyg9FJZrBEvJmZjpRbCZsGA-15DVx12OJzM3tb_86N5XfaipWFnfARtM9BISbhE9e9T2zTYitulH_ZnB6faVCDqtriGRxKfBLIFEUAuwif8pEnLxRC-QhZrvqr7vVA_3ZaJWub4OqH3sAu_b6GQxA4b_DPEuRwVcBtw7WrrXtiZcIe1g9vwuShKyCBQUc7x8CMxg3BJ5vq2UgB54rLz0uz9-WCJrVejNuHMMHB1lqST66UI3Hcegrbzw6a39vDBmhjwAMGXtnPpVT8U', 'facilitated_booking_available': True, 'pnr_count': 2, 'has_airport_change': False, 'technical_stops': 0, 'throw_away_ticketing': False, 'hidden_city_ticketing': False, 'virtual_interlining': False}], '_results': 1}



{'prices': [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]}


{'id': '145c20a14d924da16ac64c8e_0|145c20a14d924da16ac64c8e_1', 'flyFrom': 'PRG', 'flyTo': 'JFK', 'cityFrom': 'Prague', 'cityCodeFrom': 'PRG', 'cityTo': 'New York', 'cityCodeTo': 'NYC', 'countryFrom': {'code': 'CZ', 'name': 'Czechia'}, 'countryTo': {'code': 'US', 'name': 'United States'}, 'local_departure': '2024-05-15T12:30:00.000Z', 'utc_departure': '2024-05-15T10:30:00.000Z', 'local_arrival': '2024-05-15T15:55:00.000Z', 'utc_arrival': '2024-05-15T19:55:00.000Z', 'nightsInDest': 15, 'quality': 813.993449, 'distance': 6558.32, 'duration': {'departure': 33900, 'return': 30600, 'total': 64500}, 'price': 561, 'conversion': {'EUR': 646.6605343421699, 'GBP': 561}, 'fare': {'adults': 561, 'children': 561, 'infants': 561}, 'discount_data': None, 'fare_locks': {'EUR': [{'default': False, 'duration': 'P7D', 'itinerary_price_limit': 846.660534, 'itinerary_price_remaining': 646.660534, 'fare_lock_kind': 'fee', 'price': 161.665133, 'rule_instance_id': 26750, 'version': 'v1'}, {'default': True, 'duration': 'P3D', 'itinerary_price_limit': 846.660534, 'itinerary_price_remaining': 646.660534, 'fare_lock_kind': 'fee', 'price': 64.666053, 'rule_instance_id': 26748, 'version': 'v1'}, {'default': False, 'duration': 'P1D', 'itinerary_price_limit': 846.660534, 'itinerary_price_remaining': 646.660534, 'fare_lock_kind': 'fee', 'price': 32.333027, 'rule_instance_id': 26749, 'version': 'v1'}], 'GBP': [{'default': False, 'duration': 'P7D', 'itinerary_price_limit': 734.506799703156, 'itinerary_price_remaining': 560.999999703156, 'fare_lock_kind': 'fee', 'price': 140.249999492022, 'rule_instance_id': 26750, 'version': 'v1'}, {'default': True, 'duration': 'P3D', 'itinerary_price_limit': 734.506799703156, 'itinerary_price_remaining': 560.999999703156, 'fare_lock_kind': 'fee', 'price': 56.099999623302004, 'rule_instance_id': 26748, 'version': 'v1'}, {'default': False, 'duration': 'P1D', 'itinerary_price_limit': 734.506799703156, 'itinerary_price_remaining': 560.999999703156, 'fare_lock_kind': 'fee', 'price': 28.050000245418, 'rule_instance_id': 26749, 'version': 'v1'}]}, 'bags_price': {'1': 164.959855032, '2': 362.38456741199997}, 'baglimit': {'hand_height': 35, 'hand_length': 56, 'hand_weight': 10, 'hand_width': 23, 'hold_dimensions_sum': 157, 'hold_height': 52, 'hold_length': 78, 'hold_weight': 23, 'hold_width': 27, 'personal_item_height': 30, 'personal_item_length': 40, 'personal_item_weight': 3, 'personal_item_width': 10}, 'availability': {'seats': 9}, 'airlines': ['VS'], 'route': [{'id': '145c20a14d924da16ac64c8e_0', 'combination_id': '145c20a14d924da16ac64c8e', 'flyFrom': 'PRG', 'flyTo': 'JFK', 'cityFrom': 'Prague', 'cityCodeFrom': 'PRG', 'cityTo': 'New York', 'cityCodeTo': 'NYC', 'local_departure': '2024-05-15T12:30:00.000Z', 'utc_departure': '2024-05-15T10:30:00.000Z', 'local_arrival': '2024-05-15T15:55:00.000Z', 'utc_arrival': '2024-05-15T19:55:00.000Z', 'airline': 'VS', 'flight_no': 4088, 'operating_carrier': 'DL', 'operating_flight_no': '79', 'fare_basis': 'NYL6TALA', 'fare_category': 'M', 'fare_classes': 'T', 'return': 0, 'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None, 'vehicle_type': 'aircraft'}, {'id': '145c20a14d924da16ac64c8e_1', 'combination_id': '145c20a14d924da16ac64c8e', 'flyFrom': 'JFK', 'flyTo': 'PRG', 'cityFrom': 'New York', 'cityCodeFrom': 'NYC', 'cityTo': 'Prague', 'cityCodeTo': 'PRG', 'local_departure': '2024-05-30T20:00:00.000Z', 'utc_departure': '2024-05-31T00:00:00.000Z', 'local_arrival': '2024-05-31T10:30:00.000Z', 'utc_arrival': '2024-05-31T08:30:00.000Z', 'airline': 'VS', 'flight_no': 4099, 'operating_carrier': 'DL', 'operating_flight_no': '78', 'fare_basis': 'NYL6TALA', 'fare_category': 'M', 'fare_classes': 'T', 'return': 1, 'bags_recheck_required': False, 'vi_connection': False, 'guarantee': False, 'equipment': None, 'vehicle_type': 'aircraft'}], 'booking_token': 'Gx02QXk_7NOAueCn2sZPY-YKxltaj0DFZ3euI3VgdCxCuVHO3P55-T8I7rLn3KlebUUtoaDGCVM7BG4iqJfJIfSIY-prUFQYR0UOfFcwk4eRbdDddrrLvqe9OZJ2tiQ8jt3chsWtWF_Ee6PC9rcKU2O_uoGzBzzpsjkulmP6yppD7o7tElQimXO54PNjdw9epTDg0pdrV_jZFmxoXg2tCbhsfFuBT8hSmQj3WQOE5i2AW_DhdD0eRg0afwQYQPFKHSdvEjzgr67HOhUCUtN3SGlRVRXDZa91KScDfFWLh05Phnw19L6YlXhu8raA4mToXjcv_f6fktcv-wsgHhQ8pgTR8riDHaK7zknXVy_BB5wNQXGDBEVZXWZZ4jq-X4xOaaM2y92S7qcp1KOsG6PDyfnPXdVbqHsv3MkWxHlHGP6quxyyW5o9qSurPwEZOQvHD6g4wrbRIUYOXf-nLD2UIOTeTrAJ9f5kAlO8A9-ztbx8Yb6SNBx3L7IGIlKgAsJM6TeG91VjGq-nhL9IbRKCBL3-Sr0C-qqhPdoJ5g6sfLjH2WnAekGL4myHvb9Li6DYODgmVYM3KNftnifXgtvI_Hb0HeeRHlSZv4w6fx1_u8BRta8DvtzUul8K3PoVZWvIOBQKCdlztuot0NyXQD_55-pZ8d8FdwNHmzWOOW4Kciskqp7MUiat-2zdl_Oty6T0Kg4MAyJKYWlyd7Xlo3w0XWThCLARPDAIlJFRdDEE6dSgfFwJFFquRxaKr_Zl3xqAPJc6UmTNsUarmpx-W8FqMbZkBpFjm24wDEp8gmflxrYQ=', 'deep_link': 'https://www.kiwi.com/deep?affilid=appbrewerystudent4rf4flightsearcher&currency=GBP&flightsId=145c20a14d924da16ac64c8e_0%7C145c20a14d924da16ac64c8e_1&from=PRG&lang=en&passengers=1&to=JFK&booking_token=Gx02QXk_7NOAueCn2sZPY-YKxltaj0DFZ3euI3VgdCxCuVHO3P55-T8I7rLn3KlebUUtoaDGCVM7BG4iqJfJIfSIY-prUFQYR0UOfFcwk4eRbdDddrrLvqe9OZJ2tiQ8jt3chsWtWF_Ee6PC9rcKU2O_uoGzBzzpsjkulmP6yppD7o7tElQimXO54PNjdw9epTDg0pdrV_jZFmxoXg2tCbhsfFuBT8hSmQj3WQOE5i2AW_DhdD0eRg0afwQYQPFKHSdvEjzgr67HOhUCUtN3SGlRVRXDZa91KScDfFWLh05Phnw19L6YlXhu8raA4mToXjcv_f6fktcv-wsgHhQ8pgTR8riDHaK7zknXVy_BB5wNQXGDBEVZXWZZ4jq-X4xOaaM2y92S7qcp1KOsG6PDyfnPXdVbqHsv3MkWxHlHGP6quxyyW5o9qSurPwEZOQvHD6g4wrbRIUYOXf-nLD2UIOTeTrAJ9f5kAlO8A9-ztbx8Yb6SNBx3L7IGIlKgAsJM6TeG91VjGq-nhL9IbRKCBL3-Sr0C-qqhPdoJ5g6sfLjH2WnAekGL4myHvb9Li6DYODgmVYM3KNftnifXgtvI_Hb0HeeRHlSZv4w6fx1_u8BRta8DvtzUul8K3PoVZWvIOBQKCdlztuot0NyXQD_55-pZ8d8FdwNHmzWOOW4Kciskqp7MUiat-2zdl_Oty6T0Kg4MAyJKYWlyd7Xlo3w0XWThCLARPDAIlJFRdDEE6dSgfFwJFFquRxaKr_Zl3xqAPJc6UmTNsUarmpx-W8FqMbZkBpFjm24wDEp8gmflxrYQ=', 'facilitated_booking_available': True, 'pnr_count': 1, 'has_airport_change': False, 'technical_stops': 0, 'throw_away_ticketing': False, 'hidden_city_ticketing': False, 'virtual_interlining': False}