import requests as re

def request(url):
    headers = {
        'Referer': 'https://www.espn.in/cricket/scores/series/8048/season/2025/indian-premier-league',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    }


    responce = re.get(url,headers=headers,timeout=20)

    if responce.status_code == 200:
        return responce.text
    else:
        print(responce.status_code)
        return None
    








