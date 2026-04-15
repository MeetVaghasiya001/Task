import mysql.connector


def connection():
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="nayka"
    )

    cur = conn.cursor()

    return conn,cur

def create_db():
    conn,cur = connection()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS(
                p_id INT AUTO_INCREMENT PRIMARY KEY,
                product VARCHAR(255)
                brand VARCHAR(255),
                rating FLOAT,
                rating_count INT,
                product_image JSON
                sku VARCHAR(255)
                p_price INT,
                discount_price INT,
                catagory_id JSON,
                color VARCHAR(255)
                tages VARCHAR(255)
                color VARCHAR(255)
                color VARCHAR(255)
                color VARCHAR(255)
                )

    """)