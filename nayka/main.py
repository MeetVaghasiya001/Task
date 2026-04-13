from featch import * 
import queue
import threading

main_q = queue.Queue(maxsize=20)
inner_queue = queue.Queue(maxsize=100)

all_url = urls('https://www.nykaafashion.com')
all_products = []
def worker():
    while True:
        inner_url = inner_queue.get()

        if inner_url is None:
            inner_queue.task_done()
            break
        try:
            page_url = get_page_url(inner_url)
            products = get_products(page_url)
            print(f'{page_url} was done')
            all_products.append(products)

        except Exception as e:
            print(f'Error-{e}')
        
        inner_queue.task_done()

def process():
    while True:
        url = main_q.get()
        
        if url is None:
            main_q.task_done()
            break

        inner_queue.put(url)
        print(url)

        main_q.task_done()

thread = []
for t in range(4):
    t = threading.Thread(target=process)
    t.start()
    thread.append(t)

inner_thread = []
for i in range(3):
    t = threading.Thread(target=worker)
    t.start()
    inner_thread.append(t)


for u in all_url:
    main_q.put(u['urls'])
    

for _ in thread:
    main_q.put(None)


main_q.join()

for _ in inner_thread:
    inner_queue.put(None)

inner_queue.join()

for t in thread:
    t.join()

for t in inner_thread:
    t.join()



