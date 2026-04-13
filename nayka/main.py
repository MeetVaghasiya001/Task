from featch import * 
import queue
import threading

main_q = queue.Queue(maxsize=20)
inner_queue = queue.Queue(maxsize=100)

all_url = urls('https://www.nykaafashion.com')

def process():
    url = main_q.get()
    print(url)
    main_q.task_done()

thread = []
for t in range(4):
    t = threading.Thread(target=process)
    t.start()
    thread.append(t)

for u in all_url:
    main_q.put(u)



for _ in thread:
    main_q.put(None)

main_q.join()

for t in range(len(thread)):
    t.join()



