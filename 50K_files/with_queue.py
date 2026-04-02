import queue
import gzip
import os
import json
import threading
import mysql.connector
import time

st = time.time()
q = queue.Queue(maxsize=5000)

def create_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
    )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS mydb")
    cur.execute("USE mydb")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS resturant(
        r_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        name TEXT,
        cuisine TEXT,
        timezone TEXT,
        opening_hour JSON,
        rating FLOAT,
        cordinates JSON,
        delivery_options JSON,
        menu JSON,
        file_path TEXT
    )
    """)

    conn.commit()
    conn.close()

create_db()

count = 1
def gz_unzip(filepath):
    try:
        with gzip.open(filepath, 'rt', encoding='utf-8') as d:
            data = json.load(d)

    except Exception as e:
        print(f'Error-{filepath}-{e}')
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


    return (
        merchant.get('name'),
        merchant.get('cuisine'),
        merchant.get('timeZone'),
        json.dumps(merchant.get('openingHours')) if merchant.get('openingHours') else None,
        merchant.get('rating'),
        json.dumps(merchant.get('latlng')) if merchant.get('latlng') else None,
        json.dumps(merchant.get('deliveryOptions')) if merchant.get('deliveryOptions') else None,
        json.dumps(all_items) if all_items else None,
        filepath
    )


def process():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database='mydb'
    )
    cur = conn.cursor()
    batch = []

    while True:
        file = q.get()

        if file is None:
            q.task_done()   
            break

        try:
            row = gz_unzip(file)

            if row:
                batch.append(row)

            if len(batch) >= 500:  
                cur.executemany("""
                    INSERT INTO resturant (
                        name, cuisine, timezone,
                        opening_hour, rating, cordinates,
                        delivery_options, menu, file_path
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, batch)
                conn.commit()
                batch.clear()

        except Exception as e:
            print(f'Error-{file}-{e}')

        q.task_done()

    if batch:
        cur.executemany("""
            INSERT INTO resturant (
                name, cuisine, timezone,
                opening_hour, rating, cordinates,
                delivery_options, menu, file_path
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, batch)
        conn.commit()

    conn.close()


threads = []

for d in range(12):
    t = threading.Thread(target=process)
    t.start()
    threads.append(t)


folder_path = "C:/Users/meet.vaghasiya/Desktop/bif files/all_file/PDP"
for root, dirs, files in os.walk(folder_path):
    for f in files:
        if f.endswith('.gz'):
            q.put(os.path.join(root, f))
            


for _ in threads:
    q.put(None)

q.join()


for t in threads:
    t.join()


et = time.time()

print(f'Total Time:{(et - st)/60:.2f} min')
