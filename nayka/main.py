from featch import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

all_url = urls('https://www.nykaafashion.com')

task = [
    {
        'category': a.get('catagory'),
        'url': page_url
    }
    for a in all_url
    for page_url in get_page_url(a)
]

def fetch_products(t):
    category = t['category']
    page_url = t['url']

    product_urls = get_products(page_url)

    return category, product_urls



with ThreadPoolExecutor(max_workers=6) as executor:
    results = executor.map(fetch_products,task)


category_map = {}

for category, urls_list in results:
    if category not in category_map:
        category_map[category] = set()

    category_map[category].update(urls_list)


all_products = [
    {
        "category": cat,
        "url": list(urls)
    }
    for cat, urls in category_map.items()
]


with open('1.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, indent=4, default=str)