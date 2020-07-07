import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def func(i):
    print(i*'*')
    time.sleep(1)
    return i**2

def callb(arg):
    print(arg.result()*'-')

if __name__ == '__main__':
    # thread_pool = ThreadPoolExecutor(5)
    thread_pool = ThreadPoolExecutor(5)
    # ret_lst = []
    for i in range(10):
        thread_pool.submit(func,i).add_done_callback(callb)   # 相当于apply_async
        # ret = thread_pool.submit(func,i).add_done_callback(callable)   # 相当于apply_async
        # ret_lst.append(ret)
    thread_pool.shutdown()           # close+join
    # for ret in ret_lst:
    #     print(ret.result())
    print('wahaha')
    # 回调函数

# 进程池
# 线程池


# 当内存不需要共享，且高计算的时候 用进程
# 当内存需要共享，且高IO的时候 用线程
# 当并发很大的时候
    # 多进程 ： 多个任务 —— 进程池 ：cpu个数、cpu个数+1
    # 多线程 ：多个任务  —— 线程池 ：cpu个数*5
    # 4C  : 4个、5个进程 —— 20条线程/进程   ： 80-100个任务
# 50000