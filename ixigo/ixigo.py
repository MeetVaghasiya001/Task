import json
import mysql.connector
import re
from datetime import datetime,time
from model import *

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
)

cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS ixigo(
                flight_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                flight_from VARCHAR(30) NOT NULL,
                flight_to VARCHAR(30) NOT NULL,
                flight_no VARCHAR(50)NOT NULL,
                flight_duration VARCHAR(50) NOT NULL,
                date DATE,
                price INTEGER NOT NULL,
                departure_time TIME ,
                arrival_time TIME,
                baggege VARCHAR(50) NOT NULL,
                hand_baggege VARCHAR(50) NOT NULL,
                offer VARCHAR(50) NOT NULL,
                layover JSON
                )
    """)


with open('ixigo_flight.json','r',encoding='utf-8') as f:
    data = json.load(f)

all_flight = data.get('data').get('flightJourneys')


for all_detailes in all_flight:
    date1 = all_detailes.get('key')
    for f_date in date1:
        flight_date = f_date.get('date')
        correct_date = datetime.strptime(flight_date,'%d%m%Y').strftime('%Y-%m-%d')

    for flight in all_detailes.get('flightFare'):
        for fare in flight.get('fares'):
            price = fare.get('fareDetails').get('displayFare')
            for i in fare.get('fareMetadata'):
                check_in_baggage = i.get('baggageDetails').get('checkInBaggage')
                hand_baggage = i.get('baggageDetails').get('handBaggage')
                flight_class = i.get('cabinClass')

            offer = fare.get('offerText')
        main_offer = re.sub('<.*?>','',offer)

        for j in flight.get('flightDetails'):
            flight_from = j.get('origin')
            flight_to = j.get('destination')
            flight_duration = j.get('duration').get('text')


            departure_time_str = j.get('departureTime')
            departure_time = datetime.strptime(departure_time_str,'%H:%M').time()

            arrival_time_str = j.get('arrivalTime')
            arrival_time = datetime.strptime(arrival_time_str,'%H:%M').time()
            
            flight_no = j.get('subHeaderTextWeb')
            
            flight_name = j.get('headerTextWeb')

            all_layovers = []
            if len(j.get('layover')) > 0:
                for i in j.get('layover'):
                    all_layovers.append(i)
            else:
                all_layovers = None
        
        data = {
            'date':correct_date,
            'name':flight_name,
            'flight_from':flight_from,
            'to':flight_to,
            'flight_duration':flight_duration,
            'flight_no':flight_no,
            'price':price,
            'departure_time':departure_time,
            'arrival_time':arrival_time,
            'baggege':check_in_baggage,
            'hand_baggege':hand_baggage,
            'offer':main_offer,
            'layover':all_layovers
        }

        is_validate = False
        if data:
            validate = Ixigo(**data)
            is_validate = True
            if is_validate:
                cur.execute("""
                INSERT INTO ixigo(name,flight_from,flight_to,flight_no,flight_duration,date,price,departure_time,arrival_time,baggege,hand_baggege,offer,layover) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """,(
                    data.get('name'),
                    data.get('flight_from'),
                    data.get('to'),
                    data.get('flight_no'),
                    data.get('flight_duration'),
                    data.get('date'),
                    data.get('price'),
                    data.get('departure_time'),
                    data.get('arrival_time'),
                    data.get('baggege'),
                    data.get('hand_baggege'),
                    data.get('offer'),
                    json.dumps(data.get('layover')),
                ))

                
        else:
            print('data was error!')

conn.commit()
conn.close()

    
        
    
    













