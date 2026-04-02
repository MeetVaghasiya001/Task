import json
from model import Product


with open('toters_3680_-15753_-62974_1.html','r',encoding='utf-8') as f:
    data = json.load(f)

all_data = data.get('data')

products = []

for a in all_data:
    products.append({
        'name':a.get('title'),
        'decription':a.get('description') if a.get('description') else None,
        'image':a.get('image'),
        'weight':a.get('measurement_value')+a.get('measurement_unit') ,
        'price':a.get('original_price'),
        'currency':a.get('local_currency'),
        'store_id':a.get('store_id'),
        'stock':a.get('stock_level') if a.get('stock_level') else 0,
        'is_popular':a.get('is_popular'),
        'is_available':a.get('is_available'),
        'offer_price':a.get('offers') if a.get('offers') else None

    })


clean = {
    "products" : products
}


validate = Product(**clean)

with open('clean.json','w') as d:
    json.dump(validate.model_dump(),d,indent=4,default=str)