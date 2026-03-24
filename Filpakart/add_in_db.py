import mysql.connector
import json

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
)

cur = conn.cursor()

with open('clean.json','r') as f:
    data = json.load(f)


try:
    cur.execute("""
         CREATE TABLE IF NOT EXISTS product(
	            PRODUCT_ID INTEGER AUTO_INCREMENT PRIMARY KEY,
	            NAME VARCHAR(50) NOT NULL,
                DESCRIPTION TEXT NOT NULL,
                IMAGES JSON ,
                ITEAM_CATAGORY VARCHAR(50) NOT NULL,
                BRAND VARCHAR(50) NOT NULL,
                PRICE JSON,
                RATINGS JSON,
                POLICY VARCHAR(50),
                PRODUCT_DETAILES JSON,
                SELLER_DETAILES JSON
                )
        """)
    
    cur.execute("""
            INSERT INTO product(NAME,DESCRIPTION,IMAGES,ITEAM_CATAGORY,BRAND,PRICE,RATINGS,POLICY,PRODUCT_DETAILES,SELLER_DETAILES) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(
                data.get('name'),
                data.get('description'),
                json.dumps(data.get('item_images')),
                data.get('item_catagory'),
                data.get('brand'),
                json.dumps(data.get('price')),
                json.dumps(data.get('ratings')),
                data.get('policy'),
                json.dumps(data.get('product_detailes')),
                json.dumps(data.get('seller_detailes'))
            ))
    print('Done!')
   
    conn.commit()

except Exception as err:
    print("An Error:", err)

finally:
    conn.close()