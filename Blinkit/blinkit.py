import json
from model import *
import os
from parser import gz_unzip
import time
import queue
import threading
import mysql.connector

st = time.time()

q = queue.Queue(maxsize=5000)
r = queue.Queue(maxsize=10000)

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER AUTO_INCREMENT PRIMARY KEY ,
            name TEXT,
            brand TEXT,
            price INT,
            weight varchar(50),
            currency TEXT,
            product_varient JSON,
            Gallary JSON,
            attributes JSON
        )
    ''')
    conn.commit()
    conn.close()

create_db()


def add_db():
    batch = []

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

    cursor = conn.cursor()

    while True:
        db_data = r.get()

        if db_data is None:
            break

        if db_data:
            batch.append(db_data)
        
        try:
            if len(batch) >= 500:
                cursor.executemany('''
                    INSERT INTO products (name, brand, price, weight, currency, product_varient, Gallary, attributes)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ''', batch)

                conn.commit()
                batch.clear()
                print('500 data enter')
        except Exception as e:
            print(f'error-{e}')
        
        r.task_done()

    if batch:
        cursor.executemany('''
            INSERT INTO products (name, brand, price, weight, currency, product_varient, Gallary, attributes)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', batch)
        conn.commit()
    conn.close()


def process():
    while True:
        file = q.get()
        if file is None:
            q.task_done()
            break

        row = gz_unzip(file)

        
        try:
            if row:
                r.put(row)
        except Exception as e:
            print(f'error-{e}')

        q.task_done()  
        

folder_path = "C:/Users/meet.vaghasiya/Desktop/bif files/pdp"

threads = []
for _ in range(10):
    t = threading.Thread(target=process)
    t.start()
    threads.append(t)

db = []
for _ in range(2):
    db_thread = threading.Thread(target=add_db)
    db_thread.start()
    db.append(db_thread)

for root, dirs, files in os.walk(folder_path):
    for f in files:
        if f.endswith('.gz'):
            q.put(os.path.join(root, f))


q.join()

for _ in threads:
    q.put(None)

for t in threads:
    t.join()

r.join()

for _ in db:
    r.put(None)

for d in db:
    d.join()

et = time.time()


print(f'Time: {(et - st) / 60:.2f} minutes')