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
        CREATE TABLE IF NOT EXISTS movie(
            m_id INT AUTO_INCREMENT PRIMARY KEY,
            movie_name VARCHAR(255),
            score VARCHAR(255),
            description TEXT,
            img TEXT,
            reviews_count VARCHAR(255),
            videos JSON,
            want_to_know TEXT,
            cast JSON,
            reviews JSON
        )
    """)

    conn.commit()
    conn.close()