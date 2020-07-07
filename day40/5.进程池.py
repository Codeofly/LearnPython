import time
import random
from multiprocessing import Pool
def func(i):
    print('func%s' % i)
    time.sleep(5)
    return i**2
if __name__ == '__main__':
    p = Pool(5)
    ret_l = []
    for i in range(15):
        # p.apply(func=func,args=(i,))    # 同步调用
        ret = p.apply_async(func=func,args=(i,))# 异步调用
        ret_l.append(ret)
    for ret in ret_l : print(ret.get())
    # 主进程和所有的子进程异步了
