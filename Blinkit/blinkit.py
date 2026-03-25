import json
from model import *


with open('blinkit_4700BC.json','r',encoding='utf-8') as f:
    data = json.load(f)

all_data = data.get('response').get('snippets')


video = []
images = []
product = {}
product_varient = []
attributes = {}



seo = data.get('response').get('tracking').get('le_meta').get('custom_data').get('seo')

if data.get('response').get('tracking'):
    all_att = seo.get('attributes')
    brand = seo.get('brand')
    for d in all_att:
        attributes[d.get('name')]=d.get('value')

else:
    print('Key not found')

for s_data in all_data:

    if s_data.get('data').get('itemList'):
        for image in s_data.get('data').get('itemList'):
            path = image.get('data').get('media_content').get('media_type')
            if path == 'video':
                video.append(image.get('data').get('media_content').get('video').get('url'))
            if path == 'image':
                images.append(image.get('data').get('media_content').get('image').get('url'))


    identity = s_data.get('data').get('identity')
    if identity:
        if identity.get('id') == 'variant_horizontal_rail':
            variants = s_data.get('data').get('horizontal_item_list')
            for v in variants:
                product_varient.append({
                    'name':v.get('tracking').get('click_map').get('name'),
                    'weight':v.get('data').get('title').get('text'),
                    'price' : v.get('tracking').get('click_map').get('price'),
                    'is_selected':v.get('data').get('selection_config').get('is_selected')
                })


if product_varient:
    for s_product in product_varient:
        if s_product.get('is_selected') == True:
            product['name'] = s_product.get('name')
            product['weight'] = s_product.get('weight')
            product['price'] = s_product.get('price')
            product['currency'] = 'INR'
else:
    product['name'] = seo.get('product_name')
    product['price'] = seo.get('price')
    product['weight'] = attributes.get('Unit')
    product['currency'] = 'INR'
                
photos = {
    'video':video,
    'images':images
} 

data = {
    'name':product['name'],
    'brand':brand,
    'price':product['price'],
    'weight':product['weight'],
    'currency':product['currency'],
    'product_varient' : product_varient,
    'Gallary': photos,
    'attributes':attributes
}

validate = Product(**data)

with open('clean.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)


