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
    CREATE TABLE IF NOT EXISTS catagories(
            c_id INT AUTO_INCREMENT PRIMARY KEY,
            c_name VARCHAR(255),
            c_url TEXT
            )
""")


cur.execute("""
    CREATE TABLE IF NOT EXISTS product(
            p_id INT AUTO_INCREMENT PRIMARY KEY,
            c_id INT,
            p_name VARCHAR(255),
            p_url VARCHAR(255),
            p_image TEXT,
            FOREIGN KEY (c_id) REFERENCES catagories(c_id)
        )

""")


with open('clean.json','r',encoding='utf-8') as d:
    data = json.load(d)

for c in data.get('product'):
    cur.execute("""
        INSERT INTO catagories(c_name,c_url) VALUES (%s,%s)""",(
            c.get('catagory_name'),
            c.get('catagory_link')
        ))
    c_id = cur.lastrowid

    for p in c.get('products'):
        
        cur.execute("""
            INSERT INTO product(c_id,p_name,p_url,p_image) VALUES (%s,%s,%s,%s)""",(
                c_id,
                p.get('product_name'),
                p.get('product_url'),
                p.get('image_name')
            ))

conn.commit()
conn.close()      
print('Done!!!')
    

