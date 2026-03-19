import json

def feach_info(data):
    result = []
    full_location = ''
    resturant_name = data.get('restaurant',{}).get('name',{})
    rating = data.get('restaurant',{}).get('rating',{})
    location = data.get('restaurant',{}).get('location',{})

    for loc in location.values():
        full_location += str(loc) +'\t'

    menu = data.get('restaurant',{}).get('menu',{})
    for catagory in menu:
        catagory_name = catagory.get('catagory')

        for item in catagory.get('items',[]):
            result.append({
                'restaurant':resturant_name,
                'rating':rating,
                'Location':location,
                'item_name':item.get('name'),
                'price':item.get('price')
            })
    return result

with open('data.json') as f:
    data = json.load(f)

parse_data = feach_info(data)

with open('clean.json','w') as f:
    clean_data = json.dump(parse_data,f,indent=4,default=str)

