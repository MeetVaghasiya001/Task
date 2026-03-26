import json
from model import *

with open('data-2026218105913 (1).json','r',encoding='utf-8') as f:
    data = json.load(f)

all_data = data.get('data').get('cards')
items = {}

for item in all_data:
    card = item.get('card').get('card').get('gridElements').get('infoWithStyle')

    if card :
        for i in card.get('items'):
            for v in i.get('variations'):
                if v.get('category') not in items:
                    items[v.get('category')] = [{
                        'id':v.get('skuId'),
                        'item':v.get('displayName'),
                        'short_description':v.get('shortDescription'),
                        'brand':v.get('brandName'),
                        'images':v.get('imageIds'),
                        'total_price':v.get('price').get('mrp').get('units'),
                        'offer_price':v.get('price').get('offerPrice').get('units'),
                        'dicount':v.get('price').get('offerApplied').get('listingDescription'),
                        'discount_value':v.get('price').get('discountValue').get('units'),
                        'weight':v.get('weightInGrams'),
                    }] 

                else:
                    items[v.get('category')].append({
                        'id':v.get('skuId'),
                        'item':v.get('displayName'),
                        'short_description':v.get('shortDescription'),
                        'brand':v.get('brandName'),
                        'images':v.get('imageIds'),
                        'total_price':v.get('price').get('mrp').get('units'),
                        'offer_price':v.get('price').get('offerPrice').get('units'),
                        'dicount':v.get('price').get('offerApplied').get('listingDescription'),
                        'discount_value':v.get('price').get('discountValue').get('units'),
                        'weight':v.get('weightInGrams')
                    })



data = {
    'items':items
}

validate = Item(**data)
with open('clean.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)         