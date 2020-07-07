import os
import time
from multiprocessing import Process

def process1():
    print('process1 : ',os.getpid())
    time.sleep(10)

if __name__ == '__main__':
    print(os.getpid())
    p = Process(target=process1)
    p.start()
