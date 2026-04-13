import json 
import mysql.connector


def create_db():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Actowiz",
    database="mydb"
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS bata(
                p_id INT AUTO_INCREMENT PRIMARY KEY,
                p_name VARCHAR(255),
                p_url TEXT,
                p_brand VARCHAR(255),
                p_price INT,
                currency VARCHAR(50),
                sku VARCHAR(255),
                image TEXT
                )
        """)
    
    conn.commit()
    conn.close()


