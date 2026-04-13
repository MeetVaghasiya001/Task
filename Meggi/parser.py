import requests as re 

url="https://www.maggi.in/en/our-range/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Cookie': 'gig_bootstrap_3_-OR1oJYHfAEgaWv3pMMpp0YjJKvZ5am9XHCqHQKCjRxNsIPZZvHkz66KzgCiPxLB=login_ver4; OptanonAlertBoxClosed=2026-04-07T08:53:49.219Z; _ga=GA1.1.201285022.1775552002; _ga_81PZZ5C7CJ=GS2.1.s1775552001$o1$g0$t1775552029$j60$l0$h0; _ga_LWVJC60CMJ=GS2.1.s1775552002$o1$g0$t1775552029$j60$l0$h0; FPID=FPID2.2.qdG%2Bu2v%2Fw9JCOxCF9emXS1i21ofw9%2FsPjxkGMMYIFPE%3D.1775552002; FPAU=1.2.95429146.1775552029; FPLC=eWGCbjM8ytt4N7U8kR3s4qKOK6f7%2BOFkObocKfagTWxmZdcp%2BEnWS06e%2FYPjlIUdGbdsdjjS38QXwrt51WTC2gYhqPkPfeBt8w1p3xjdD%2F%2BIf53rnunZaBKwARUSxw%3D%3D; _gcl_au=1.1.659354101.1775552030; _ga_YLKEE47XNN=GS2.1.s1775552002$o1$g1$t1775552030$j59$l0$h1871999491; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Apr+07+2026+14%3A23%3A50+GMT%2B0530+(India+Standard+Time)&version=202603.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=aaa6c05d-b062-4143-8214-16b498aee6bd&interactionCount=2&isAnonUser=1&prevHadToken=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&crTime=1775552030568&intType=1; _fbp=fb.1.1775552033084.153876025374276534; _cls_v=d2bcdc0a-3849-4b8e-a879-dffaa24b5aa9; _cls_s=290f2c4d-1af4-4444-adfd-bee851442a4b:0; rto=c0'
}

response = re.get(url, headers=headers)

if response.status_code == 200:
    print('Success!!')

    with open('magiie.html','w',encoding='utf-8') as f:
        f.write(response.text)

else:
    print(f"Failed. Status Code: {response.status_code}")
    print(response.text[:500])