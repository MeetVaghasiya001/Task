import threading

lock = threading.Lock()
counter = 0

def task():
    global counter
    for i in range(1000):
        counter += 1

threads = []

for _ in range(2):
    t = threading.Thread(target=task)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(counter)