from lxml import html
import json

with open('sigma_product.txt','r',encoding='utf-8') as f:
    data=f.read()

tree=html.fromstring(data)

all_data=tree.xpath("//div[@class='tss-plr0hd-details']/h1[@data-testid='product-name']/span/text()")


script=tree.xpath("//script[@type='application/json']/text()")

for s in script:
    data=json.loads(s)


p_data = data.get('props').get('pageProps').get('data').get('getProductDetail')

name =p_data.get('name')
product_description = p_data.get('description')
brand = p_data.get('brand').get('name')

description = {p.get('label'):p.get('values') for p in p_data.get('descriptions')}

about_item = {s.get('label'):s.get('value') for s in p_data.get('aliases')}

synonyms = p_data.get('synonyms')

attributes = {a.get('label'):a.get('values') for a in p_data.get('attributes')}

clean_data = {
    'name':name,
    'product_description':product_description,
    'brand':brand,
    'synonyms':synonyms,
    'description':description,
    'about_item':about_item,
    'attribute':attributes
}

with open('clean.json','w',encoding='utf-8') as f:
    json.dump(clean_data,f,indent=4,default=str,ensure_ascii=False)