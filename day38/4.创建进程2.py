import os
import time
from multiprocessing import Process

def process1(n,name,num = 20):
    print('process1 : ',os.getpid())
    print('n : ',n,name,num)
    time.sleep(10)

if __name__ == '__main__':
    print(os.getpid())
    p = Process(target=process1,args=[1,'alex',30])
    p.start()