import json
from model import *

with open('grabfood.json','r',encoding='utf-8') as f:
    all_data = json.load(f)


data =all_data.get('merchant')

resturant_name = data.get('name')
cuisine = data.get('cuisine')
timezone = data.get('timeZone')
opning_hour = data.get('openingHours')
rating = data.get('rating')
latlng = data.get('latlng')
delivery_options = data.get('deliveryOptions')


menu = data.get('menu').get('categories')

all_menu = []

for catagory in menu:
    all_menu.append({
        'catagory':catagory.get('name'),
        'items':[{
            'name':item.get('name'),
            'price':item.get('priceInMinorUnit'),
            'image':item.get('imgHref'),
            'description':item.get('description'),
            'modifires':[{
                'name':modify.get('name'),
                'available':modify.get('available'),
                'all_modifires':[{
                    'name':i.get('name'),
                    'available':i.get('available'),
                    'price':{
                        'amount_in_mirror':i.get('priceV2').get('amountInMinor'),
                        'amount_display':i.get('priceV2').get('amountDisplay')
                    }
                } for i in modify.get('modifiers')]
                } for modify in item.get('modifierGroups',{})]
        }for item in catagory.get('items')]
    })


all_menu_2 = all_menu[1::]


data = {
    'name':resturant_name,
    'cuisine':cuisine,
    'timezone':timezone,
    'opning_hour':opning_hour,
    'rating':rating,
    'cordinates':latlng,
    'delivery_options':delivery_options,
    'menu':all_menu_2
}

validate = Resturant(**data)

with open('clean.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)
