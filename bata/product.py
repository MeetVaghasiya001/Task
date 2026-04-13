from lxml import html
import json
from parser import request
from featch import urls
from db import create_db
import mysql.connector

all_urls = urls()
print(len(all_urls))
count = 0

create_db()

for u in all_urls:

    def parser(url):
        conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Actowiz",
                    database="mydb"
            )

        cur = conn.cursor()
        global count
        clean_data = None
        all_product = None
        data = request(url)
        tree = html.fromstring(data)
        print('-----------------------------------')
        print(url)
        scripts = tree.xpath("//script[@type='application/ld+json']/text()")
        print('-----------------------------------')

        if scripts:
            for s in scripts:
                data = json.loads(s)

                if data.get('@context'):
                    if data.get('@context').endswith('/'):
                        clean_data = json.loads(s)

        if clean_data:
            all_product = clean_data.get('itemListElement')

        if all_product:
            for p in all_product:
                p_name = p.get('item').get('name')
                p_url = p.get('url')
                p_brand = p.get('item').get('brand').get('name')
                price = p.get('item').get('offers').get('price')
                currency = p.get('item').get('offers').get('priceCurrency')
                sku = p.get('item').get('sku')
                image = p.get('item').get('image')

                count += 1

                cur.execute("""
                    INSERT INTO bata(p_name,p_url,p_brand,p_price,currency,sku,image) VALUES(%s,%s,%s,%s,%s,%s,%s)

                    """,(
                        p_name,
                        p_url,
                        p_brand,
                        price,
                        currency,
                        sku,
                        image
                    ))
                conn.commit()
        conn.close()        
    parser(u)

 



        

