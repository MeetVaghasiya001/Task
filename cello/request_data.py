import requests as re

def request(url):
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'referer':'https://www.google.com/'
    }


    responce = re.get(url,headers=headers,timeout=20)

    if responce.status_code == 200:
        return responce.text
    else:
        print(responce.status_code)
        return None
    








