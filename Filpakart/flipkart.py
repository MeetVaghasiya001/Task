import json
from model import *

with open('flipkart_data.json','r',encoding='utf-8') as f:
    data = json.load(f)

schema = data.get('multiWidgetState').get('pageDataResponse').get('seoData').get('schema')[0]


name = schema.get('name')
description = schema.get('description')
item_images = schema.get('image')
item_catagory = schema.get('category')
brand = schema.get('brand').get('name')


price ={
   'value':schema.get('offers').get('price'),
   'currency' : schema.get('offers').get('priceCurrency')
}

ratings = {
    'rating':schema.get('aggregateRating').get('ratingValue'),
    'rating_count': schema.get('aggregateRating').get('ratingCount'),
    'review_count':schema.get('aggregateRating').get('reviewCount')
}
 

policy = schema.get('offers').get('hasMerchantReturnPolicy').get('description')

sections = data.get('multiWidgetState').get('widgetsData').get('slots')

product_detailes = {}

for section in sections:
    if section.get('slotData').get('id') == 29:
        values = section.get('slotData').get('widget').get('data').get('dlsData').get('product-details-grid_0').get('value').get('gridData_0').get('value')
        for val in values:
            val_path = val.get('value') or {}
            if val_path.get('label_0',{}):
                v = val_path.get('label_1').get('value').get('text')
            if val_path.get('label_0',{}):
                k = val_path.get('label_0',{}).get('value').get('text')
                product_detailes[k.replace(' ','_')] = v[0]
            else:
                continue
    
    if section.get('slotData').get('id') == 23:
        values = section.get('slotData').get('widget').get('data').get('dlsData').get('default_fk_pp_delivery_widget_seller_2').get('value')
        rating = values.get('label_1').get('value').get('text')
        seller_name = values.get('label_0').get('value').get('text')
        start = values.get('label_3').get('value').get('text')

seller_detailes ={
    'name':seller_name,
    'rating':rating,
    'start':start
}

data ={
    'name':name,
    'description':description,
    'item_images':item_images,
    'item_catagory':item_catagory,
    'brand':brand,
    'price':price,
    'ratings':ratings,
    'policy':policy,
    'product_detailes':product_detailes,
    'seller_detailes':seller_detailes
}

validate = Product(**data)

with open('clean.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)