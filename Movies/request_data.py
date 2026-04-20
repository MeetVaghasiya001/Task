import requests as re

def request(url):
        
    cookies = {
        'akamai_generated_location': '{"zip":"""","city":"AHMEDABAD","state":"GJ","county":"""","areacode":"""","lat":"23.03","long":"72.62","countrycode":"IN"}',
        'akacd_RTReplatform': '2147483647~rv=78~id=9690810e99fb548c46b3e0ff141c7698',
        'eXr91Jra': 'Ay2hg6mdAQAARrr5Bra25Yh9bQ2jLDxrPXIz84_nZ7oGm-YuFflkTBFgxhNFAS1yQYOuco1HwH8AAEB3AAAAAA|1|0|ef3ae0336b973cf366fd0c92081af221d41f0b93',
        '__host_color_scheme': 'buAIlj4I-a-CgLx7UfUqWL-J8p7_fpnCcUO9kiO52NgmZma2_UNU',
        '__host_theme_options': '1776665469977',
        'usprivacy': '1---',
        'algoliaUT': '6e80e25f-aa7d-4dbd-a700-739f2cef62b7',
        'check': 'true',
        'AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg': '1',
        'AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg': '-408604571%7CMCMID%7C03960496742101414882522205583135383127%7CMCAAMLH-1777270273%7C12%7CMCAAMB-1777270273%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776672673s%7CNONE%7CvVersion%7C4.6.0',
        's_cc': 'true',
        'mbox': 'session#e452f3791b1f41f6b69efbb0048d7700#1776667335|PC#e452f3791b1f41f6b69efbb0048d7700.41_0#1839910275',
        '_cb': 'B1Pb2MDy3YFJbTcrs',
        '_chartbeat2': '.1776665475114.1776665475114.1.BSwcM3DRKUe_zLnPbDEQQCyDmaP9D.1',
        '_cb_svref': 'external',
        'sailthru_pageviews': '1',
        '_ALGOLIA': 'anonymous-0f0d7f00-e25d-46f2-ba49-f61d9c4ff677',
        '__gads': 'ID=d96c688598986be9:T=1776665474:RT=1776665474:S=ALNI_Majev4v5eVA5AoqBFd0rbFFtMWVrA',
        '__gpi': 'UID=0000126e1701aadc:T=1776665474:RT=1776665474:S=ALNI_MZ_pYcYNE2_Am1rJttyHU8Se9ZnoQ',
        '__eoi': 'ID=d148455ba3fa3dca:T=1776665474:RT=1776665474:S=AA-AfjZtphvqEa65urZBH2TxKU_r',
        'cto_bundle': '3KPzKl9ISkhnV3BBOERGTkhlOTFpSWZWVnZxeXlmJTJGdlZBbThNcmhlUFJnT3RFRHl1RENCakZrRE41UTd1bWxjRzl0bTc0bDNUMXkwenJjVmtObUdBMzMwZlhWak41VVYyVGIlMkJ3OTVPWk80aUN5TDFwTjg2ekdBYVdWeSUyRndLbyUyQkJLRVdlcFhWclJhYSUyRkF6Wno0MGYxQUpLdXowVERWN2VENjc5WTVESExhdHpVb2lRJTNE',
        '_awl': '2.1776665480.5-fc8d8bbb4b17c8d9e40b45075fd78ad6-6763652d617369612d6561737431-0',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Apr+20+2026+11%3A41%3A26+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=e694253e-24b4-47d7-ac40-dab6b8077b7c&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=https%3A%2F%2Fwww.rottentomatoes.com%2Fbrowse%2Fmovies_in_theaters%2Fsort%3Anewest&groups=1%3A1%2C4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1&crTime=1776665486147',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        # 'cookie': 'akamai_generated_location={"zip":"""","city":"AHMEDABAD","state":"GJ","county":"""","areacode":"""","lat":"23.03","long":"72.62","countrycode":"IN"}; akacd_RTReplatform=2147483647~rv=78~id=9690810e99fb548c46b3e0ff141c7698; eXr91Jra=Ay2hg6mdAQAARrr5Bra25Yh9bQ2jLDxrPXIz84_nZ7oGm-YuFflkTBFgxhNFAS1yQYOuco1HwH8AAEB3AAAAAA|1|0|ef3ae0336b973cf366fd0c92081af221d41f0b93; __host_color_scheme=buAIlj4I-a-CgLx7UfUqWL-J8p7_fpnCcUO9kiO52NgmZma2_UNU; __host_theme_options=1776665469977; usprivacy=1---; algoliaUT=6e80e25f-aa7d-4dbd-a700-739f2cef62b7; check=true; AMCVS_8CF467C25245AE3F0A490D4C%40AdobeOrg=1; AMCV_8CF467C25245AE3F0A490D4C%40AdobeOrg=-408604571%7CMCMID%7C03960496742101414882522205583135383127%7CMCAAMLH-1777270273%7C12%7CMCAAMB-1777270273%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1776672673s%7CNONE%7CvVersion%7C4.6.0; s_cc=true; mbox=session#e452f3791b1f41f6b69efbb0048d7700#1776667335|PC#e452f3791b1f41f6b69efbb0048d7700.41_0#1839910275; _cb=B1Pb2MDy3YFJbTcrs; _chartbeat2=.1776665475114.1776665475114.1.BSwcM3DRKUe_zLnPbDEQQCyDmaP9D.1; _cb_svref=external; sailthru_pageviews=1; _ALGOLIA=anonymous-0f0d7f00-e25d-46f2-ba49-f61d9c4ff677; __gads=ID=d96c688598986be9:T=1776665474:RT=1776665474:S=ALNI_Majev4v5eVA5AoqBFd0rbFFtMWVrA; __gpi=UID=0000126e1701aadc:T=1776665474:RT=1776665474:S=ALNI_MZ_pYcYNE2_Am1rJttyHU8Se9ZnoQ; __eoi=ID=d148455ba3fa3dca:T=1776665474:RT=1776665474:S=AA-AfjZtphvqEa65urZBH2TxKU_r; cto_bundle=3KPzKl9ISkhnV3BBOERGTkhlOTFpSWZWVnZxeXlmJTJGdlZBbThNcmhlUFJnT3RFRHl1RENCakZrRE41UTd1bWxjRzl0bTc0bDNUMXkwenJjVmtObUdBMzMwZlhWak41VVYyVGIlMkJ3OTVPWk80aUN5TDFwTjg2ekdBYVdWeSUyRndLbyUyQkJLRVdlcFhWclJhYSUyRkF6Wno0MGYxQUpLdXowVERWN2VENjc5WTVESExhdHpVb2lRJTNE; _awl=2.1776665480.5-fc8d8bbb4b17c8d9e40b45075fd78ad6-6763652d617369612d6561737431-0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Apr+20+2026+11%3A41%3A26+GMT%2B0530+(India+Standard+Time)&version=202601.2.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=e694253e-24b4-47d7-ac40-dab6b8077b7c&interactionCount=1&isAnonUser=1&prevHadToken=0&landingPath=https%3A%2F%2Fwww.rottentomatoes.com%2Fbrowse%2Fmovies_in_theaters%2Fsort%3Anewest&groups=1%3A1%2C4%3A1%2C6%3A1%2C7%3A1%2COOF%3A1%2CUSP%3A1&crTime=1776665486147',
    }

    response = re.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)
        return None
    








