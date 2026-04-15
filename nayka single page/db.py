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
        CREATE TABLE IF NOT EXISTS

    """)