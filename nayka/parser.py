from curl_cffi import requests as re

def request(url):
    headers = {
        'domain': 'NYKAA_FASHION',
        'sec-ch-ua-platform': '"Windows"',
        'x-csrf-token': 'fKIo7hJhisJSzCZc',
        'Referer': 'https://www.nykaafashion.com/women/westernwear/c/3?f=new_tags_filter%3Dlatestseason_new_&transaction_id=643cdec843c4973bb7a115efd685f8bb&intcmp=nykaa%3Aother%3Anf-westernwear%3Adefault%3Acategories%3ASLIDING_WIDGET_V2%3A2%3Anew%3A-1%3A643cdec843c4973bb7a115efd685f8bb',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
    }

    params = {
        'PageSize': '36',
        'filter_format': 'v2',
        'apiVersion': '6',
        'currency': 'INR',
        'country_code': 'IN',
        'deviceType': 'WEBSITE',
        'sort': 'popularity',
        'device_os': 'desktop',
        'categoryId': '0',
        'currentPage': '1',
        'new_tags_filter': 'latestseason_new',
    }
    

    responce = re.get(url,params=params,headers=headers,impersonate='edge99')

    if responce.status_code == 200:
        print('Done')
        return {'text':responce.text,'params':params}
    else:
        print(responce.status_code)
        return 'error'
    








