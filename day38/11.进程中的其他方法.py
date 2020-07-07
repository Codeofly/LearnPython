import time
from multiprocessing import Process

def func():
    print('wahaha')
    time.sleep(20)
    print('wahaha end')
if __name__ == '__main__':
    p = Process(target=func)
    p.start()
    print(p.is_alive())
    time.sleep(1)
    p.terminate()    # 在主进程中结束一个子进程
    print(p.is_alive())
    time.sleep(0.5)
    print(p.is_alive())
    # print(p.pid)
    # print(p.name)