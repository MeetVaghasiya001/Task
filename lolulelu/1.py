import threading
import time

def task(n):
    print(f"Start:{n}")
    time.sleep(2)
    print(f"End:{n}")

def task2(n):
    print(f"Start:{n}")
    time.sleep(2)
    print(f"End:{n}")

thread=[]

for i in range(3):
    t=threading.Thread(target=task,args=(i,))
    t2=threading.Thread(target=task2,args=(i,))
    thread.extend([t,t2])
    t.start()
    t2.start()
    
for i in thread:
    i.join()
    
print('ok')