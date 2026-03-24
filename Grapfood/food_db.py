import mysql.connector
import json 


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
)

cur = conn.cursor()

with open('clean.json','r',encoding='utf-8') as f:
    data = json.load(f)

try:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Resturant(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                cuisine VARCHAR(50),
                menu JSON,
                timezone VARCHAR(50),
                opning_hours JSON,
                rating FLOAT,
                cordinates JSON,
                delivery_option JSON
                
        )

    """)

    cur.execute("""
        INSERT INTO Resturant(name,cuisine,menu,timezone,opning_hours,rating,cordinates,delivery_option) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
        (
            data.get('name'),
            data.get('cuisine'),
            json.dumps(data.get('menu')),
            data.get('timezone'),
            json.dumps(data.get('opning_hour')),
            data.get('rating'),
            json.dumps(data.get('cordinates')),
            json.dumps(data.get('delivery_options'))

        )
        )

    conn.commit()
    conn.close()

except Exception as e :
    print(f'Error is :{e}')
