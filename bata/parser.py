import requests as re


def request(url):

    header={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        'accept-language':'en-US,en;q=0.9'
    }

    responce = re.get(url,headers=header)

    if responce.status_code == 200:
        return responce.text
        
    else:
        return None