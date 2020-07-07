import os
import time
import random
from multiprocessing import Lock     # 锁
from multiprocessing import Process

def work(n,lock):
    lock.acquire()
    print('%s: %s is running' %(n,os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' %(n,os.getpid()))
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p=Process(target=work,args=(i,lock))
        p.start()

# 同步控制
# 只要用到了锁 锁之内的代码就变成同步的了
# 锁 ：控制一段代码 同一时间 只能被一个进程执行













