import requests as re 
from lxml import html

url = 'https://stores.burgerking.in/location/gujarat/ahmedabad'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Cookie': '_ga_KQE6QVSPD1=GS2.1.s1775220825$o1$g0$t1775220825$j60$l0$h0; _gcl_au=1.1.1858699311.1775220827; _gid=GA1.2.2056579981.1775220827; _gat_gtag_UA_196801382_1=1; _gat_UA-196801382-1=1; _ga_51NSXH673Q=GS2.1.s1775220827$o1$g0$t1775220827$j60$l0$h0; _ga=GA1.1.1029212621.1775220825; _fbp=fb.1.1775220827721.140316780402130918; _ga_CRJBK2R8LM=GS2.1.s1775220828$o1$g0$t1775220828$j60$l0$h0'
}

response = re.get(url, headers=headers)

if response.status_code == 200:
    print('Success!!')

    with open('burger.html','w',encoding='utf-8') as f:
        f.write(response.text)

else:
    print(f"Failed. Status Code: {response.status_code}")
    print(response.text[:500])
