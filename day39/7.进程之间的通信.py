# import queue
# # 它能维护一个先进先出的秩序 他不能进行IPC
import time
from multiprocessing import Queue,Process
# 能维护一个先进先出的秩序 也能进行IPC
# def wahaha(q):
#     print(q.get())
#     q.put('aaa')
#
# if __name__ == '__main__':
#     q = Queue()
#     Process(target=wahaha,args=[q,]).start()
#     q.put(1)
#     time.sleep(0.5)
#     print(q.get())

# 生产者消费者模型
# 消费者 消费数据 吃包子
# 生产者 产生数据的人 做包子
# 供销矛盾
# 10  供不应求
# 增加做包子的人
# 同步 ：做一个包子 卖一包子 吃一包子
# 做包子慢 吃包子快
# 生产数据 买淘宝 ---
# 消费数据 阿里 ---  非常高 必须要快速把用户生产的数据消费完
#
import time
import random
from multiprocessing import Process,Queue

def producer(q):
    for i in range(10):
        time.sleep(random.random())
        q.put('包子%s'%i)
        print('\033[1;31m生产了包子%s\033[0m'%i)

def consumer(q):
    for i in range(5):
        food = q.get()
        print(food)
        print('\033[1;32m消费了%s\033[0m' %food)
        time.sleep(random.uniform(1,2))

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=[q])
    p2 = Process(target=consumer,args=[q])
    p3 = Process(target=consumer,args=[q])
    p1.start()
    p2.start()
    p3.start()








