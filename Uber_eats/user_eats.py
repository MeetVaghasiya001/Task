import json
from model import *

with open('uber-eats.json','r',encoding='utf-8') as f:
    all_data = json.load(f)

meta = all_data['data']['metaJson']
meta_json = json.loads(meta)

name = all_data['data']['title']
location = {
    'address':all_data['data']['location']['address'],
    'street_address':all_data['data']['location']['streetAddress'],
    'city':all_data['data']['location']['city'],
    'country':all_data['data']['location']['country'],
    'postal_code':all_data['data']['location']['postalCode'],
    'region':all_data['data']['location']['region'],
    'latitude':all_data['data']['location']['latitude'],
    'longitude':all_data['data']['location']['longitude']

}

cuisine = meta_json['servesCuisine']
telephone = meta_json['telephone']
menu = all_data['data']['catalogSectionsMap']['0ad5db85-c10f-5ad6-897c-f8ef6bd5cc78']

all_menu = []

for items in menu:
    all_items = items['payload']['standardItemsPayload']['catalogItems']
    all_menu.append({
        'catagory':items['payload']['standardItemsPayload']['title']['text'],
        'item':[{
            'name': i.get('title'),
            'description': i.get('itemDescription') or None,
            'price': i['price'],
            'avalible':i.get('isAvailable'),
            'item_image': i.get('imageUrl') or None
        } for i in all_items]
    })
    



image = meta_json.get('image',[])
data = {
    'name':name,
    'location': location,
    'rating':all_data['data']['rating'] or None,
    'cuisine':cuisine,
    'image' : image,
    'telephone':telephone,
    'menu':all_menu
}

validate = Uber(**data)

with open('clean.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)
    




