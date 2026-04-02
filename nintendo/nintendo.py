import json
import re

with open('sample2.json','r',encoding='utf-8') as f:
    data = json.load(f)

all_data = data.get('props').get('pageProps')
images = {}



if all_data:
    product_name = all_data.get('analytics').get('pageName')
    sku_id = all_data.get('analytics').get('product').get('sku')
    discription = all_data.get('meta').get('description')
    images = {
        'open_image':all_data.get('openGraph')
    }

    for i in all_data.get('linkedData'):
        if type(i) == dict:
            if i.get('offers'):
                price = i.get('offers').get('price')
                currecny = i.get('offers').get('priceCurrency')
                seller = i.get('offers').get('seller').get('name')
                category = i.get('category')
                game_platform = i.get('gamePlatform')
                genre = i.get('genre')
                game_editor = i.get('gameEdition')
                play_mode = i.get('playMode')
                number_of_playes = {
                        'min':i.get('numberOfPlayers',{}).get('minValue',{}) or 0,
                        'max':i.get('numberOfPlayers',{}).get('maxValue',{}) or  0
                    }
                publisher = i.get('publisher',{}).get('name',{}) or None
        elif type(i) == list:
            images['other_images'] = [item.get('contentUrl') for item in i if item.get('contentUrl') != images['open_image']]

    suggested_detailes = all_data.get('initialApolloState')

    result = []
    for key,value in suggested_detailes.items():
        if key.startswith('Product'):
            if suggested_detailes.get(key).get('size') != None:
                result.append({
                    'name':suggested_detailes.get(key).get('name'),
                    'size':suggested_detailes.get(key).get('size'),
                    'sku':suggested_detailes.get(key).get('sku'),
                    'price':{
                        'regular_price':suggested_detailes.get(key).get('prices({\"personalized\":false})').get('regularPrice'),
                        'final_price':suggested_detailes.get(key).get('prices({\"personalized\":false})').get('finalPrice'),
                    }
                })
            
print(result)

data = {
    'product_name':product_name,
    'discription':discription,
    'sku_id':sku_id,
    'images':images,
    'price':price,
    'currecny':currecny,
    'seller':seller,
    'catagory':category,
    'game_platform':game_platform,
    'genre':genre,
    'play_mode':play_mode,
    'number_of_playes':number_of_playes,
    'publisher':publisher,
    'all_sizes':result if result else None
}

with open('clean.json','w') as e:
    json.dump(data,e,indent=4,default=str)
