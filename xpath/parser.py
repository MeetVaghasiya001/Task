from lxml import html
import json

with open('A Light in the Attic _ Books to Scrape - Sandbox.html','r',encoding='utf-8') as f:
    data = f.read()

tree = html.fromstring(data)

page_name = tree.xpath("//header/div[@class='page_inner']/div[@class='row']/div[contains(@class,col-sm-8)]/a/text()")




image = tree.xpath("//article/div[@class='row']/div/div/div/div/div/img/@src")
p_name = tree.xpath("//article/div[@class='row']/div[@class='col-sm-6 product_main']/h1/text()")
stock = tree.xpath("//article/div[@class='row']/div[@class='col-sm-6 product_main']/p[@class='instock availability']/text()")[1].strip()
price = tree.xpath("//article/div[@class='row']/div[@class='col-sm-6 product_main']/p[@class='price_color']/text()")
warning = tree.xpath("//article/div[@class='row']/div[@class='col-sm-6 product_main']/div[@class='alert alert-warning']/text()")
description = tree.xpath("//article/p/text()")

table = tree.xpath("//article/table/tr")

p_info = {}
for t in table:
    p_info[t.xpath(".//th/text()")[0]] = t.xpath(".//td/text()")[0]

data = {
    'name':p_name,
    'image':image,
    'price':price,
    'stock':stock,
    'warning':warning,
    'description':description,
    'product_information':p_info
}

with open('clean.json','w') as f:
    json.dump(data,f,indent=4,default=str,ensure_ascii=False)