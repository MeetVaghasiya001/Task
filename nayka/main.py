from featch import *
from concurrent.futures import ThreadPoolExecutor

all_url = urls('https://www.nykaafashion.com')

def process_page(args):
    category, page_url = args
    try:
        links = get_products(page_url)
        print(category, len(links))
        return {'catagory': category, 'url': links} if links else None
    except:
        return None

tasks = [
    (a.get('catagory'), p)
    for a in all_url
    for p in get_page_url(a)
]

products = []

with ThreadPoolExecutor(max_workers=10) as executor:
    for r in executor.map(process_page, tasks):
        if r:
            products.append(r)
            print(r)

print(len(products))
print(products)