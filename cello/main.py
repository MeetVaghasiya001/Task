from request_data import request
from lxml import html
import json
import re
all_data = request('https://celloworld.com/products/duro-kent-flask-nw')

tree = html.fromstring(all_data)


script=tree.xpath("//script[contains(text(),'$Lf')]/text()")
for s in script:
    matches = re.findall(r'push\(\[.*?,\s*"(.*?)"\]\)', s)
    for m in matches:
        cleaned = re.sub(r'^\d+:', '', m)

        cleaned = cleaned.encode().decode('unicode_escape')

        data = json.loads(cleaned)
        real_data=data[0][3]

product_name = real_data.get('productData').get('title')
vendor = real_data.get('productData').get('vendor')
description = real_data.get('productData').get('description')
product_max_price = real_data.get('productData').get('priceRange').get('maxVariantPrice').get('amount')
product_min_price = real_data.get('productData').get('priceRange').get('minVariantPrice').get('amount')
product_images = [i.get('node').get('url') for i in real_data.get('productData').get('images').get('edges')]


all_page_data = {
    'name':product_name,
    'vendor':vendor,
    'description':description if description else None,
    'product_max_price':product_max_price,
    'product_min_price':product_min_price,
    'product_images':product_images
}

with open('clean.json','w',encoding='utf-8') as f:
    json.dump(all_page_data,f,indent=4,default=str)