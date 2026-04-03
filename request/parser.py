from lxml import html
import json

with open('burger.html','r',encoding='utf-8') as f:
    data = f.read()


tree = html.fromstring(data)

title = tree.xpath("string(//section[@class='storelocator-default']//div[@class='head-wraper']/h3/text())")

all_stores = tree.xpath("//section[@class='storelocator-default']//div//div[@class='outlet-list']//ul")

outlet=[]
for u in all_stores:
    outlet_address = u.xpath("normalize-space(.//li[@class='outlet-address'])")
    outlet_name = u.xpath("normalize-space(.//li[@class='outlet-name'])")
    outlet_phone = u.xpath("normalize-space(.//li[@class='outlet-phone'])")
    outlet_timings = u.xpath("normalize-space(.//li[@class='outlet-timings'])")

    outlet.append({
        "name": outlet_name,
        "address": outlet_address,
        "phone": outlet_phone,
        "timings": outlet_timings
    })




data = {
    'title':title,
    'stores':outlet
}



with open('clean.json','w',encoding='utf-8') as d:
    json.dump(data,d,indent=4,default=str)
