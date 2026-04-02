import json 
from model import Product


with open('clean html/clean1.json','r',encoding='utf-8') as f:
    all_data = json.load(f)


responce = all_data.get('RESPONSE',[])
item_page = responce.get('pageData')
all_price = []
all_ratings = {}
all_hlt = {}
manu_delt ={}
product_image = []



if item_page :
    brand= item_page.get('pageContext').get('brand')
    prices = item_page.get('pageContext').get('pricing').get('prices')

    for p in prices:
        all_price.append({
            'name':p.get('name'),
            'value':p.get('value')
        })

    image_count = item_page.get('pageContext').get('productImagesCount')
    product_name = item_page.get('pageContext').get('titles').get('title')
    sub_title = item_page.get('pageContext').get('titles').get('subtitle')
    seller_name = item_page.get('pageContext').get('trackingDataV2').get('sellerName')
    seller_rating = item_page.get('pageContext').get('trackingDataV2').get('sellerRating')
    product_id = item_page.get('pageContext').get('productId')

    if item_page.get('pageContext').get('rating'):
        all_ratings['rating'] = item_page.get('pageContext').get('rating').get('average')
        all_ratings['rating_count'] = item_page.get('pageContext').get('rating').get('count')
        all_ratings['review_count'] = item_page.get('pageContext').get('rating').get('reviewCount')
    else:
        all_ratings = None

    
    for r in responce.get('slots'):

        if r.get('elementId') == '25-COMPOSED_SWATCH':
            image_path = r.get('widget').get('data').get('swatchComponent').get('value').get('products')[product_id].get('images')
            for image in image_path:
                product_image.append(image.get('url'))


        if r.get('elementId') == '61-PRODUCT_DETAILS':

            hilights_path = r.get('widget').get('data').get('renderableComponent').get('value').get('specification')
            for h in hilights_path:
                if h:
                    all_hlt[h.get('name') if h.get('name').strip() else None] = h.get('values')[0]

            manufacture_detailes = r.get('widget').get('data').get('listingManufacturerInfo').get('value').get('detailedComponents')
            for m in manufacture_detailes:
                if m:
                    manu_delt[ m.get('value').get('title')] = m.get('value').get('callouts')[0]

            manufacture_detailes_2= r.get('widget').get('data').get('listingManufacturerInfo').get('value').get('mappedCards')
            for m2 in manufacture_detailes_2:
                if m2:
                    manu_delt[ m2.get('key')] = m2.get('values')[0]




data = {
    'item_name':product_name,
    'subtitle':sub_title,
    'image':product_image,
    'brand':brand,
    'price':all_price,
    'rating':all_ratings,
    'product_highlights':all_hlt,
    'manufacture':manu_delt
}

validate = Product(**data)

with open('clean_html1.json','w') as f:
    json.dump(validate.model_dump(),f,indent=4,default=str)
