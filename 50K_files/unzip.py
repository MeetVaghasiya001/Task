import gzip
import os 
import time
import json 
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
)

cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS resturant(
                r_id INTEGER AUTO_INCREMENT PRIMARY KEY,
                name varchar(255),
                cuisine varchar(255),
                timezone varchar(255) ,
                opening_hour JSON,
                rating float,
                cordinates JSON,
                delivery_options JSON,
                menu JSON,
                file_path varchar(255)
                )

""")


def unzip_files(filepath):
    try:
        with gzip.open(filepath,'rt',encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f'Error:{e}')
        return None

count = 0
st = time.time()
folder_path = "C:/Users/meet.vaghasiya/Desktop/bif files/all_file/PDP"


for root,dirs,files in os.walk(folder_path):
    for file in files:
        if file.endswith('.gz'):
            file_path = os.path.join(root,file)
            
            try:
                all_data = json.loads(unzip_files(file_path))
            except:
                all_data =  {}

            data =all_data.get('merchant') or {}

            resturant_name = data.get('name')
            cuisine = data.get('cuisine')
            timezone = data.get('timeZone')
            opning_hour = data.get('openingHours')
            rating = data.get('rating')
            latlng = data.get('latlng')
            delivery_options = data.get('deliveryOptions')
            all_menu = data.get('menu',{}).get('categories',[])
            all_items = []

            for category in all_menu:
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
                
                
            cur.execute("""
                    INSERT INTO resturant(name,cuisine,timezone,opening_hour,rating,cordinates,delivery_options,menu,file_path) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (
                    resturant_name,
                    cuisine,
                    timezone, 
                    json.dumps(opning_hour) if opning_hour else None,
                    rating,
                    json.dumps(latlng) if latlng else None,
                    json.dumps(delivery_options) if delivery_options else None,
                    json.dumps(all_items) if all_items else None,
                    file_path
            ))
            count +=1
            if count % 50 == 0:
                print(count)

conn.commit()
conn.close()
et = time.time()
print(f'Time is :{(et - st)/60:.2f}')




    

