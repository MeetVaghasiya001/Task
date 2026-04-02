
import gzip
import os
import json
import mysql.connector
import time
from concurrent.futures import ThreadPoolExecutor
import threading

st = time.time()

lock = threading.Lock()
batch = []

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
    )

    cur = conn.cursor()
    cur.execute("""CREATE DATABASE IF NOT EXISTS mydb""")
    cur.execute("""USE mydb""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS resturant(
        r_id INTEGER AUTO_INCREMENT PRIMARY KEY ,
        name TEXT,
        cuisine TEXT,
        timezone TEXT,
        opening_hour JSON,
        rating REAL,
        cordinates JSON,
        delivery_options JSON,
        menu JSON,
        file_path TEXT
    )
    """)

    conn.commit()
    conn.close()

create_db()

def insert_db():
    global batch

    if not batch:
        return

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
    )
    cur = conn.cursor()
    cur.execute("""CREATE DATABASE IF NOT EXISTS mydb""")
    cur.execute("""USE mydb""")
    cur.executemany("""
        INSERT INTO resturant (name, cuisine, timezone, opening_hour, rating, cordinates, delivery_options, menu, file_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", batch)  

    print('Done')
    conn.commit()
    conn.close()
    batch.clear()

def gz_unzip(file_path):
    global batch

    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f'{file_path}-{e}')

    merchant = data.get('merchant') or {}

    all_menu = merchant.get('menu', {}).get('categories', [])
    all_items = []

    for category in all_menu:
        all_items.append({
            'category': category.get('name'),
            'items': [{
                'name': item.get('name'),
                'price': item.get('priceInMinorUnit'),
                'image': item.get('imgHref'),
                'description': item.get('description')
            } for item in category.get('items', [])]
        })

    row = (
        merchant.get('name'),
        merchant.get('cuisine'),
        merchant.get('timeZone'),
        json.dumps(merchant.get('openingHours')) if merchant.get('openingHours') else None,
        merchant.get('rating'),
        json.dumps(merchant.get('latlng')) if merchant.get('latlng') else None,
        json.dumps(merchant.get('deliveryOptions')) if merchant.get('deliveryOptions') else None,
        json.dumps(all_items) if all_items else None,
        file_path
    )

    with lock:
        batch.append(row)

        if len(batch) >= 1000:
            insert_db()

folder_path = "C:/Users/meet.vaghasiya/Desktop/bif files/all_file/PDP"

files = []
for root, dirs, fs in os.walk(folder_path):
    for f in fs:
        if f.endswith('.gz'):
            files.append(os.path.join(root, f))

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(gz_unzip, files)


with lock:
    insert_db()

et = time.time()
print(f'Time taken: {(et - st)/60} minutes')