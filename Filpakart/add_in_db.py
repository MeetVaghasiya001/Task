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
    cur.execute(
        "INSERT INTO products (name, description, category, brand, policy) VALUES (%s,%s,%s,%s,%s)",
        (
            data.get("name"),
            data.get("description"),
            data.get("item_catagory"),
            data.get("brand"),
            data.get("policy")
        )
    )

    pid = cur.lastrowid

    cur.execute(
        "INSERT INTO price (product_id, value, currency) VALUES (%s,%s,%s)",
        (pid, data.get("price").get("value"), data.get("price").get("currency"))
    )

    r = data.get("ratings", {})
    cur.execute(
        "INSERT INTO ratings (product_id, rating, rating_count, review_count) VALUES (%s,%s,%s,%s)",
        (pid, r.get("rating"), r.get("rating_count"), r.get("review_count"))
    )


    for img in data.get("item_images", []):
        cur.execute(
            "INSERT INTO images (product_id, image_url) VALUES (%s,%s)",
            (pid, img)
        )
    cur.execute(
        "INSERT INTO product_details (product_id, details) VALUES (%s,%s)",
        (pid, json.dumps(data.get("product_detailes", {})))
    )

    seller = data.get('seller_detailes')
    cur.execute("INSERT INTO seller (seller_id,name,RATING,start) VALUES (%s,%s,%s,%s)",(pid,seller.get('name'),seller.get('rating'),seller.get('start')))

    conn.commit()
    print("Done!")

except Exception as err:
    print("An Error:", err)

finally:
    conn.close()