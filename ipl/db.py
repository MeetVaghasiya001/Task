import mysql.connector


def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

    cur = conn.cursor()

    return conn,cur 


def create_db():
    conn,cur = connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS matches(
                m_id INT AUTO_INCREMENT PRIMARY KEY,
                match_name VARCHAR(255),
                winner VARCHAR(255),
                date DATETIME,
                score JSON,
                match_url TEXT,
                innings JSON
            )

    """)

    conn.commit()
    conn.close()