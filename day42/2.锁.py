# GIL
# 锁
import time
from threading import Thread,Lock
def func(lock):
    global n
    # lock.acquire()
    temp =+ n
    # time.sleep(0.1)
    n = temp -1
    # lock.release()
n = 100
t_lst = []
lock = Lock()   # 锁
for i in range(100):
    t = Thread(target=func,args=(lock,))
    t.start()
    t_lst.append(t)
for t in t_lst:t.join()
print(n)
# 数据是不隔离