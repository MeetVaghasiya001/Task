from lxml import html
import json
from parser import request



def urls(main_url):
    data = request(main_url)

    tree = html.fromstring(data['text'])

    links = tree.xpath("//script[@id='__PRELOADED_STATE__']/text()")
    for i in links:
        all_data = json.loads(i)
    
    all_divs = all_data.get('landingpage').get('landingpageData')
    
    for a in all_divs:
        if a.get('inventoryId') == '69d7f01d536836e6da760ad8':
            urls = [{
                'catagory':u.get('params').get('imageLabel'),
                'urls':u.get('params').get('url')
                } for u in a.get('widgetData').get('children')]
            
    return urls


def get_page_url(s_url):
    url = s_url.get('urls')
    data = request(url)

    tree = html.fromstring(data['text'])
    links = tree.xpath("//script[@id='__PRELOADED_STATE__']/text()")
    for i in links:
        all_data = json.loads(i)

    all_divs = all_data.get('landingpage').get('landingpageData')[1]
    
    page_urls = [u.get('params').get('url') for u in all_divs.get('widgetData').get('children')]
    
    return page_urls
    

def get_products(url):
    while True:
        cat_id = url.split("/c/")[1].split("?")[0]
        
        
        api= 'https://www.nykaafashion.com/rest/appapi/V2/categories/products'
        data = request(api)
        if data:
            data['params']['categoryId'] = cat_id 
            page_count = int(data['params']['currentPage'])
            page_count += 1

            print(page_count)
            

            # all_data = json.loads(data['text'])
            # print(all_data)

    

get_products('https://www.nykaafashion.com/women/westernwear/gowns/c/153?transaction_id=969e86fa9d12a1870caba6ed2d2d273f&intcmp=nykaa:other:nf-westernwear:default:categories:SLIDING_WIDGET_V2:2:gowns:-1:969e86fa9d12a1870caba6ed2d2d273f')


        
