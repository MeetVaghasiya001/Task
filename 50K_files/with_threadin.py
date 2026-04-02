import gzip
import os
import threading
import time
import json
import mysql.connector

st = time.time()
BATCH_SIZE = 1000
lock = threading.Lock()

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz"
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS mydb")
    cur.execute("USE mydb")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS resturant (
        id INT AUTO_INCREMENT PRIMARY KEY,
        restaurant_name VARCHAR(255),
        all_items JSON,
        cuisine VARCHAR(255),
        timezone VARCHAR(255),
        opening_hour JSON,
        rating FLOAT,
        latlng JSON,
        delivery_options JSON,
        file_path VARCHAR(255)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

create_db()
batch = []

def unzip_get_and_insert(file_path):
    try:
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return None

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

    with lock:
        batch.append((
            merchant.get('name'),
            merchant.get('cuisine'),
            merchant.get('timeZone'),
            json.dumps(merchant.get('openingHours')) if merchant.get('openingHours') else None,
            merchant.get('rating'),
            json.dumps(merchant.get('latlng')) if merchant.get('latlng') else None,
            json.dumps(merchant.get('deliveryOptions')) if merchant.get('deliveryOptions') else None,
            json.dumps(all_items) if all_items else None,
            file_path
        ))

        if len(batch) >= 300:

            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Actowiz"
            )
            cur = conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS mydb")
            cur.execute("USE mydb")
            cur.executemany("""
            INSERT INTO resturant (
                restaurant_name, cuisine, timezone,
                opening_hour, rating, latlng,
                delivery_options, all_items, file_path
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, batch)
            conn.commit()
            batch.clear()
            cur.close()
            conn.close()

count = 0
folder_path = "C:/Users/meet.vaghasiya/Desktop/bif files/all_file/PDP"
threads = []
for root,dirs,files in os.walk(folder_path):
    for file in files:
        if file.endswith('.gz'):
            t = threading.Thread(target=unzip_get_and_insert, args=(os.path.join(root, file),))
            t.start()
            threads.append(t)

            if len(threads) >= 15:
                for t in threads:
                    t.join()
                threads = []

            count += 1
            print(f'Processed {count} files')

for t in threads:
    t.join()

if batch:
    with lock:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Actowiz"
        )
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS mydb")
        cur.execute("USE mydb")
        cur.executemany("""
            INSERT INTO resturant (
                restaurant_name, cuisine, timezone,
                opening_hour, rating, latlng,
                delivery_options, all_items, file_path
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, batch)
        conn.commit()
        cur.close()
        conn.close()
        batch.clear()

et = time.time()
print(f'Time taken: {(et - st)/60} minutes')