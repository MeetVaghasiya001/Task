from request_data import request
import json
from lxml import html
from urllib.parse import urljoin
import json
import requests as re



def find_url(url):
    res = re.get(url)
    all_json = json.loads(res.text)

    return all_json


def main(url):
    main_url = 'https://www.rottentomatoes.com/'
    all_data = request(url)
    tree = html.fromstring(all_data)

    script = tree.xpath("//script[@type='application/ld+json']/text()")
    for s in script:
        full_json = json.loads(s)
    page_1 = full_json.get('itemListElement').get('itemListElement')
    all_movie_data = [{
        'movie_name':i.get('name'),
        'date':i.get('dateCreated'),
        'image':i.get('image'),
        'url':i.get('url')
    } for i in page_1]
    unique = tree.xpath("//script[contains(@id,'pageInfo')]/text()")[0]
    end_cursor = json.loads(unique)
    unique_key = end_cursor.get('endCursor')

    while True:
        api_url = f'https://www.rottentomatoes.com/cnapi/browse/movies_in_theaters/sort:newest?after={unique_key}'
        other_page = find_url(api_url)
        cursor = other_page.get('pageInfo').get('endCursor')

        if not cursor:
            break

        unique_key = cursor

        all_movie_data.extend([{
            'movie_name':i.get('title'),
            'date':i.get('releaseDateText'),
            'image':i.get('posterUri'),
            'url':urljoin(main_url,i.get('mediaUrl'))
        } for i in other_page.get('grid').get('list')])
    
    with open('all_movies.json','w',encoding='utf-8') as f:
        json.dump(all_movie_data,f,indent=4,default=str)

        
    

main("https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest")

# find_url('https://www.rottentomatoes.com/cnapi/browse/movies_in_theaters/sort:newest?after=Mjg%3D')
