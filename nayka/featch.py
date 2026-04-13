from lxml import html
import json
from parser import request
from urllib.parse import urljoin



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

for u in urls('https://www.nykaafashion.com'):
    print('---------------------------------------')
    print(u)

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
    main_url = 'https://www.nykaafashion.com'
    all_p_url = []
    count = 1
    cat_id = url.split("/c/")[1].split("?")[0]
    
    while True:
        params = {
            'PageSize': '36',
            'filter_format': 'v2',
            'apiVersion': '6',
            'currency': 'INR',
            'country_code': 'IN',
            'deviceType': 'WEBSITE',
            'sort': 'popularity',
            'device_os': 'desktop',
            'categoryId': cat_id,
            'currentPage': count,
            'new_tags_filter': 'latestseason_new',
        }
        
        api= 'https://www.nykaafashion.com/rest/appapi/V2/categories/products'
        data = request(api,params)
        if data:
            all_data = json.loads(data['text'])

            all_products = all_data.get('response').get('products')

            if not all_products:
                print('No more products')
                break

            count += 1
            for p in all_products:
                all_p_url.append(urljoin(main_url,p.get('actionUrl')))
        else:
            break
    

    return all_p_url
    




        
