import json
from datetime import datetime
import mysql.connector
import os
import time

# DB Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS flights(
    flight_id INTEGER AUTO_INCREMENT PRIMARY KEY,
    source VARCHAR(50),
    destination VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    airline_code VARCHAR(50) NOT NULL,
    departure_time TIME,
    arrival_time TIME
)
""")

folder_path = 'C:/Users/meet.vaghasiya/meet/Threading/flight_json_100000'

batch_size = 1000
batch = []

insert_query = """
INSERT INTO flights(source, destination, price, airline_code, departure_time, arrival_time)
VALUES (%s, %s, %s, %s, %s, %s)
"""

def process_file(file_path):
    rows = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for journey in data.get('data', {}).get('flightJourneys', []):
            for fare_block in journey.get('flightFare', []):

                price = None
                for p in fare_block.get('fares', []):
                    price = p.get('fareDetails', {}).get('displayFare')

                for flight in fare_block.get('flightDetails', []):
                    try:
                        flight_from = flight.get('origin')
                        flight_to = flight.get('destination')
                        airline_code = flight.get('airlineCode')

                        departure_time = datetime.strptime(
                            flight.get('departureTime'), "%H:%M"
                        ).time()

                        arrival_time = datetime.strptime(
                            flight.get('arrivalTime'), "%H:%M"
                        ).time()

                        rows.append((
                            flight_from,
                            flight_to,
                            price,
                            airline_code,
                            departure_time,
                            arrival_time
                        ))

                    except Exception as e:
                        print(f"Inner Error: {e}")

    except Exception as e:
        print(f"File Error ({file_path}): {e}")

    return rows


def insert_batch(rows):
    global batch

    batch.extend(rows)

    if len(batch) >= batch_size:
        cur.executemany(insert_query, batch)
        conn.commit()
        batch.clear()


def main():
    start_time = time.time()

    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    for file_path in files:
        rows = process_file(file_path)
        if rows:
            insert_batch(rows)


    if batch:
        cur.executemany(insert_query, batch)
        conn.commit()

    conn.close()

    end_time = time.time()
    print(f"Done! Time taken: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()