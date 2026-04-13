from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

with open('hunter.html','r',encoding='utf-8') as f:
    data = BeautifulSoup(f,'html.parser')

product = {}
url = 'https://hunterboots.com/'
for l in data.find_all("a"):
    href = l.get('href',' ')
    

    if '/collections/' in href:
        href = urljoin(url,href)
        name = ''.join(l.get_text().split())

        if name:
            product[name] = href 



with open('clen.json','w',encoding='utf-8') as d:
    json.dump(product,d,indent=4,default=str,ensure_ascii=True)

