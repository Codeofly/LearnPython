import os
import time
from multiprocessing import Process

def process(n):
    print(os.getpid(),os.getppid())
    time.sleep(1)
    print(n)
if __name__ == '__main__':
    p_lst = []
    for i in range(10):
        p = Process(target=process,args=[i,])
        p.start()
        p_lst.append(p)
    for p in p_lst:p.join()   # 检测p是否结束 如果没有结束就阻塞直到结束 如果已经结束了就不阻塞
    print('求和')