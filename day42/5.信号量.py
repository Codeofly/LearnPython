import time
from threading import Thread,Semaphore
def func(sem,i):
    sem.acquire()
    print(i)
    time.sleep(1)
    sem.release()

sem = Semaphore(5)
for i in range(20):
    Thread(target=func,args=(sem,i)).start()