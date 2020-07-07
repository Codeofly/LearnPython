import os
from multiprocessing import Process

def func(exp):
    print(os.getpid(),os.getppid())
    result = eval(exp)
    with open('file','w') as f:
        f.write(str(result))

if __name__ == '__main__':
    print(os.getpid(),os.getppid())  # process id,parent process id
    # 3*5+5/6
    p = Process(target=func,args=['3*5'])    # func
    p.start()
    ret = 5/6
    p.join()  # join方法能够检测到p进程是否已经执行完了，阻塞知道p执行结束
    with open('file') as f:
        result = f.read()
    ret = ret + int(result)
    print(ret)
