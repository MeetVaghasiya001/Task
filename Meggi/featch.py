import json
from lxml import html

with open('magiie.html','r') as f:
    data = f.read()

tree = html.fromstring(data)

products = []

all_data = tree.xpath("//section[contains(@class,'mg-teaser-carousel')]")
for m in all_data:
    c_name = ''.join(m.xpath(".//div/h2/text()"))
    c_link = m.xpath('.//a[contains(@class,"mg-btn")]/@href')
    c_link = c_link[0].strip() if c_link else None
    product_nodes = m.xpath(".//div[contains(@class,'mg-product-card')]")

    temp_products = [{
        'product_name': ''.join(p.xpath(".//h3/text()")).strip(),
        'product_url': p.xpath(".//a/@href")[0].strip() if p.xpath(".//a/@href") else None,
        'image_name': p.xpath(".//img/@data-src | .//img/@src")[0].strip() if p.xpath(".//img/@data-src | .//img/@src") else None
    } for p in product_nodes]

    seen = set()
    unique_products = []
    for item in temp_products:
        name = item['product_name'].strip().lower()
        if name not in seen:
            seen.add(name)
            unique_products.append(item)

    products.append({
        'catagory_name': c_name,
        'catagory_link': c_link,
        'products': unique_products
    })

data = {
    'product': products
}

with open('clean.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,default=str,ensure_ascii=False)