import json
from model import Products

with open('lululemon.json','r',encoding='utf-8') as f:
    data = json.load(f)

product = []
product_path = data.get('data').get('itemToItems').get('products')


for p in product_path:
    product.append({
        'product_id':p.get('id'),
        'product_skuId':p.get('skuId'),
        'product_name':p.get('displayName'),
        'on_sale':'Yes' if p.get('productOnSale') else 'No',
        'price':p.get('listPrice')[0],
        'currency':p.get('currencyCode'),
        'sale_price':p.get('salePrice')[0] if p.get('salePrice') else 0,
        'product_images' : p.get('skuImages'),
        'colors':[{
            'color_name':i.get('colorName'),
            'color_image':i.get('colorGroup')
        } for i in p.get('skuStyleOrder')]
    })

data = {
    'product':product
}

validate = Products(**data)


with open('clean.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)