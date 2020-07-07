# 主进程
# 子进程
# 父进程
import os
import time
from multiprocessing import Process

def func():
    print(os.getpid(),os.getppid())
    time.sleep(1)

if __name__ == '__main__':
    print(os.getpid(),os.getppid())  # process id,parent process id
    Process(target=func).start()    # func
    print('*'*20)
    time.sleep(0.5)
    print('*'*40)
    # p = Process(target=func)
    # p.start()

# 主进程默认会等待子进程执行完毕之后才结束
# 主进程和子进程之间的代码是异步的
# 为什么主进程要等待子进程结束 回收一些子进程的资源
# 开启一个进程是有时间开销的 ：操作系统响应开启进程指令，给这个进程分配必要的资源

