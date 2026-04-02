import gzip 
import json 
from model import *



def gz_unzip(filepath):
    try:
        with gzip.open(filepath, 'rt', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f'{filepath}-{e}')
        return None

    all_data = data.get('response', {}).get('snippets', [])
    video = []
    images = []
    product = {}
    product_varient = []
    attributes = {}

    seo = data.get('response', {}).get('tracking', {}).get('le_meta', {}).get('custom_data', {}).get('seo', {})
    all_att = seo.get('attributes', [])
    brand = seo.get('brand')

    for d in all_att:
        attributes[d.get('name')] = d.get('value')

    for s_data in all_data:
        items = s_data.get('data', {}).get('itemList')
        if items:
            for image in items:
                media = image.get('data', {}).get('media_content', {})
                if media.get('media_type') == 'video':
                    video.append(media.get('video', {}).get('url'))
                if media.get('media_type') == 'image':
                    images.append(media.get('image', {}).get('url'))

        identity = s_data.get('data', {}).get('identity')
        if identity and identity.get('id') == 'variant_horizontal_rail':
            variants = s_data.get('data', {}).get('horizontal_item_list', [])
            for v in variants:
                product_varient.append({
                    'name': v.get('tracking', {}).get('click_map', {}).get('name'),
                    'weight': v.get('data', {}).get('title', {}).get('text'),
                    'price': v.get('tracking', {}).get('click_map', {}).get('price'),
                    'is_selected': v.get('data', {}).get('selection_config', {}).get('is_selected')
                })

    if product_varient:
        for s_product in product_varient:
            if s_product.get('is_selected'):
                product['name'] = s_product.get('name')
                product['weight'] = s_product.get('weight')
                product['price'] = s_product.get('price')
                product['currency'] = 'INR'
    else:
        product['name'] = seo.get('product_name')
        product['price'] = seo.get('price')
        product['weight'] = attributes.get('Unit')
        product['currency'] = 'INR'

    photos = {'video': video, 'images': images}

    data = {
        'name':product.get('name'),
        'brand':brand,
        'price':product.get('price'),
        'weight':product.get('weight'),
        'currency':product.get('currency'),
        'product_varient':product_varient,
        'Gallary':photos,
        'attributes':attributes
    }

    validate = Product(**data)

    if validate:
        return (
            data.get('name'),
            data.get('brand'),
            data.get('price'),
            data.get('weight'),
            data.get('currency'),
            json.dumps(data.get('product_varient') or {}),
            json.dumps(data.get('Gallary') or {}),
            json.dumps(data.get('attributes') or {})
        )
    else:
        return None
