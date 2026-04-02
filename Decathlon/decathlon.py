import json
from model import *

with open('Decathlon Product.txt','r',encoding='utf-8') as f:
    data = json.load(f)

all_data = data.get('props').get('initialState')

main_data = json.loads(all_data)


main = main_data.get('reducer')

price_mrp = main.get('productPage').get('size').get('price').get('mrp')
final_price = main.get('productPage').get('size').get('price').get('priceReduction')
redues_amount = main.get('productPage').get('size').get('price').get('reductionAmount')


provider = main.get('productPage').get('size').get('provider')

source = main.get('productPage').get('activeProduct').get('description')


product_name = source.get('productName')
description = source.get('descriptionShort')
gender =  source.get('informationConcept').get('gender')

s_data = source.get('informationConcept').get('structuring')
product_specification = {s.get('name'):s.get('description') for s in s_data}

t_info= source.get('informationConcept').get('technicalInformation')
tech_info= {t.get('name'):t.get('description') for t in t_info}


benifits = source.get('benefits')
all_benifits = {b.get('name'):b.get('description') for b in benifits}

p = main.get('productPage').get('activeProduct')

product_id = p.get('modelId')
brand =  p.get('brand')
made_in = p.get('madeIn')
stock =  p.get('stockNotification').get('message')

r = main.get('productPage').get('activeProduct').get('review')

review = {
    'rating':r.get('averageRating'),
    'rating_count':r.get('count'),
    'recomend_count':r.get('countRecommended')
} 

seller = main.get('productPage').get('activeProduct').get('sellerDetail')

seller_detailes = {
    'seller_name':seller.get('sellerName'),
    'address':seller.get('address'),
    'contact_no':seller.get('phone'),
    'email':seller.get('email')
}


all_article = main.get('productPage').get('activeProduct').get('articles')

all_size = [{
    'a_id':a.get('articleId'),
    'made_in':a.get('madeIn'),
    'size':a.get('attribute').get('attributeValue'),
    'price':{
        'mrp':a.get('price').get('mrp'),
        'final_price':a.get('price').get('priceReduction'),
        'discount':a.get('price').get('reductionAmount')
    },
    'chest_size':a.get('sizeMeasurements').get('sizeMeasure'),
    'provider':a.get('provider')
} for a in all_article]


images =[i.get('url') for i in main.get('productPage').get('activeProduct').get('images')]

other_colors = []

for p in main.get('productPage').get('productsList'):
    if p.get('modelId') != product_id:
        other_colors.append({
            'p_id':p.get('modelId'),
            'product_name':p.get('description').get('productName'),
            'rating':p.get('review').get('averageRating'),
            'review_count':p.get('review').get('count'),
            'final_price':p.get('priceForFront').get('finalPrice'),
            'total_price':p.get('priceForFront').get('slashedPrice'),
            'images':[i.get('url') for i in p.get('images')]
        })


clean_data = {
    'id':product_id,
    'name':product_name,
    'description':description,
    'gender':gender,
    'mrp':price_mrp,
    'final_price':final_price,
    'discount_amount':redues_amount,
    'provider':provider,
    'seller':seller_detailes,
    'images':images,
    'reviews_rating':review,
    'brand':brand,
    'madeIn':made_in,
    'stock':stock,
    'product_specification':product_specification,
    'technical_info':tech_info,
    'benifits':all_benifits,
    'all_size':all_size,
    'other_options':other_colors
}

validate = Product(**clean_data)


with open('clean.json','w',encoding='utf-8') as d:
    json.dump(validate.model_dump(),d,indent=4,default=str)
