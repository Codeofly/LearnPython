import time
from multiprocessing import Process

def func():
    print('son start')
    while True:
        time.sleep(1)
        print('son')

def func2():
    print('start :in func2')
    time.sleep(5)
    print('end : in func2')
if __name__ == '__main__':
    p = Process(target=func)
    # 在一个进程开启之前可以设置它为一个守护进程
    p.daemon = True
    p.start()
    Process(target=func2).start()
    time.sleep(2)
    print('在主进程中')



# 分析：
    # 主进程的代码 大概在2s多的时候就结束了
    # p2子进程实在5s多的时候结束
    # 主进程结束
    # p是在什么时候结束的？
        # p是在主进程的代码执行完毕之后就结束了



    # 主进程会等待子进程的结束而结束
    # 守护进程的意义：
        # 子进程会随着主进程代码的执行结束而结束
        # 注意：守护进程不会关系主进程什么时候结束，我只关心主进程中的代码什么时候结束
    # 守护进程的作用：
        # 守护主进程，程序报活
        # 主进程开启的时候 建立一个守护进程
        # 守护进程只负责每隔1分钟 就给检测程序发一条消息