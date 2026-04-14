from request_data import * 
from lxml import html
import json

data = request('https://www.nykaafashion.com/little-collars-reindeer-ethnic-jacket-kurta-pajama-for-boys-cream-set-of-3/p/16717340')

tree = html.fromstring(data)

script = tree.xpath("//script[@id='__PRELOADED_STATE__']/text()")

for s in script:
    all_data = json.loads(s)
with open('p_json.json','w',encoding='utf-8') as f:
    json.dump(all_data,f,indent=4,default=str)
p_data = all_data.get('details').get('skuData').get('product')

title = p_data.get('title')
p_name = p_data.get('subTitle')
product_image = [i.get('url')  for i in p_data.get('productMedia')]
sku = p_data.get('sku')
p_price = p_data.get('price')
discount_price = p_data.get('discountedPrice')
catagory_id = p_data.get('categoryId')
color = p_data.get('color').get('name')
tages = [i.get('title') for i in p_data.get('tag_list')]

product_detail = {}

for p in p_data.get('pdp_sections'):
    if p.get('widget_id') == 'PD01':
        for i in p.get('child_widgets'):
            if i.get('widget_type') == 'attribute_columnize_widget':
                attributes = {a.get('label'):a.get('value') for a in i.get('attributes')}
                product_detail['attribute'] = attributes
    
            if i.get('widget_type') == 'plain_widget':
                product_detail[i.get('title')] = i.get('value')

    if p.get('widget_id') == 'KYP01':
        product_detail[p.get('title')] = p.get('value')

    if p.get('widget_id') == 'VD01':
        vendor = {i.get('label'):i.get('value') for i in p.get('attributes')}

    if p.get('widget_id') == 'REP01':
        product_detail[p.get('title')] = p.get('value')

product_detail['return_period'] = p_data.get('return_period')

color_option = [{
    'sku':i.get('sku'),
    'in_stock':i.get('in_stock'),
    'color':i.get('name')
} for i in p_data.get('colorOptions')]

policies = {i.get('policy_name'):i.get('text') for i in p_data.get('ecom_policies')} 

size = [{
    'sku':i.get('sku'),
    'price':i.get('price'),
    'size':i.get('sizeName')
} for i in p_data.get('sizeOptions').get('options') if i]


data = {
    'product':p_name,
    'brand':title,
    'product_image':product_image,
    'sku':sku,
    'p_price':p_price,
    'discount_price':discount_price,
    'catagory_id':catagory_id,
    'color':color,
    'tages':tages,
    'product_detail':product_detail,
    'color_option':color_option,
    'size':size,
    'policies':policies
}

with open('clean.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,default=str,ensure_ascii=False)