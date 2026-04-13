from bs4 import BeautifulSoup 
from urllib.parse import urljoin


def urls():
    url = 'https://www.bata.com/'
    with open('bata.html','r',encoding='utf-8') as f:
        data = BeautifulSoup(f,'html.parser')

    url_list= []
    for a in data.find_all('a'):
        href = a.get("href")
        print(href)
        if href != None:
            if '/collections/' in href:
                if not href.endswith('.html'):
                    href = urljoin(url,href)
                    url_list.append(href)
    # return url_list