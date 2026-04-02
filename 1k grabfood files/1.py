import zipfile
import os
import gzip
import json
import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
)

def read_gzip_file(filepath):
    try:
        with gzip.open(filepath, 'rt', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

start=time.time()
count = 0
folder_path = 'C:/Users/meet.vaghasiya/meet/1k grabfood files/grab_food_pages/grab_food_pages'
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".gz"):
            file_path = os.path.join(root, file)

            content = read_gzip_file(file_path)
            try:
                json_data = json.loads(content)
            except:
                json_data = {}

            data = json_data.get('merchant', {}) or {}

            restaurant_name = data.get('name')
            cuisine = data.get('cuisine')
            timezone = data.get('timeZone')
            opening_hour = data.get('openingHours')
            rating = data.get('rating')
            latlng = data.get('latlng')
            delivery_options = data.get('deliveryOptions')  
            menu_item=data.get('menu',{}).get('categories',[])
            all_items = []

            for category in menu_item:
                all_items.append({
                    'category': category.get('name',{}),
                    'items': [{
                        'name': item.get('name',{}),
                        'price': item.get('priceInMinorUnit',{}),
                        'image': item.get('imgHref',{}),
                        'description': item.get('description',{}),
                        'modifiers': [{
                            'name': modify.get('name',{}),
                            'available': modify.get('available',{}),
                            'all_modifiers': [{
                                'name': i.get('name',{}),
                                'available': i.get('available',{}),
                                'price': {
                                    'amount_in_minor': (i.get('priceV2') or {}).get('amountInMinor'),
                                    'amount_display': (i.get('priceV2') or {}).get('amountDisplay')
                                }
                            } for i in modify.get('modifiers', [])]
                        } for modify in item.get('modifierGroups', [])]
                    } for item in category.get('items', [])]
                })
            count+=1

            cursor=conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS GrabFood")
            cursor.execute("USE GrabFood")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS All_Res (
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

            cursor.execute("""
            INSERT INTO All_Res (
                restaurant_name, cuisine, timezone,
                opening_hour, rating, latlng,
                delivery_options, all_items, file_path
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                restaurant_name,
                cuisine,
                timezone,
                json.dumps(opening_hour) if opening_hour else None,
                rating,
                json.dumps(latlng) if latlng else None,
                json.dumps(delivery_options)  if delivery_options else None,
                json.dumps(all_items) if all_items else None,
                file_path
            ))
            conn.commit()
            print(count)
end=time.time()
conn.close()

print(f"Execution time:{end-start}")

            