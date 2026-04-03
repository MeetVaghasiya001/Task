import os
import time
import queue
import threading
import json
from parser import gz_unzip
import mysql.connector

FOLDER_PATH = "C:/Users/meet.vaghasiya/Desktop/bif files/pdp"
DB_CONFIG = {
    'host': "localhost",
    'user': "root",
    'password': "Actowiz",
    'database': "mydb"
}
BATCH_SIZE = 1500

file_queue = queue.Queue(maxsize=2000)
data_queue = queue.Queue(maxsize=8000)

def create_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            name TEXT,
            brand TEXT,
            price INT,
            weight VARCHAR(50),
            currency TEXT,
            product_varient JSON,
            Gallary JSON,
            attributes JSON
        )
    ''')
    conn.commit()
    conn.close()


def worker():
    while True:
        file_path = file_queue.get()
        if file_path is None:
            file_queue.task_done()
            break
        row = gz_unzip(file_path)
        if row:
            data_queue.put(row)
        file_queue.task_done()

def db_worker():
    batch = []
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    while True:
        row = data_queue.get()
        if row is None:
            data_queue.task_done()
            break
        batch.append(row)

        if len(batch) >= BATCH_SIZE:
            try:
                cursor.executemany('''
                    INSERT INTO products (name, brand, price, weight, currency, product_varient, Gallary, attributes)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ''', batch)
                conn.commit()
                print(f"Inserted batch of {len(batch)} rows")
            except Exception as e:
                print(f"DB insert error: {e}")
            batch.clear()
        data_queue.task_done()
        
    if batch:
        try:
            cursor.executemany('''
                INSERT INTO products (name, brand, price, weight, currency, product_varient, Gallary, attributes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', batch)
            conn.commit()
            print(f"Inserted final batch of {len(batch)} rows")
        except Exception as e:
            print(f"DB insert error: {e}")
    conn.close()


st = time.time()

create_db()

threads = []

for _ in range(8):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

db=[]
for _ in range(2):
    t = threading.Thread(target=db_worker)
    t.start()
    db.append(t)

for root, _, files in os.walk(FOLDER_PATH):
    for f in files:
        if f.endswith('.gz'):
            file_queue.put(os.path.join(root, f))

file_queue.join()
for _ in threads:
    file_queue.put(None)

for t in threads:
    t.join()

data_queue.join()

for _ in db:
    data_queue.put(None)

for t in db:
    t.join()

et = time.time()
print(f"Total time: {(et - st)/60:.2f} minutes")

