# from multiprocessing import Process,Queue
# q = Queue(10) # 创建一个只能放10个值的队列
# try:
#     q.get_nowait()  # web qq 长轮询
# except:
#     print('queue.Empty')

# q.get()
# for i in range(10):
#     q.put(i)
# print(q.qsize())
# print(q.full())
# q.put(1111)
# print('*'*10)
# print(q.empty())
# print(q.full())

# 队列可以在创建的时候制定一个容量
# 如果在程序运行的过程中，队列已经有了足够的数据，再put就会发生阻塞
# 如果队列为空，在get就会发生阻塞
# 内存 —— 制定容量
# put
# get
# qsize 不准
# full 不准
# empty 不准
# import time
# from multiprocessing import Process,Queue
# def wahaha(q):
#     print(q.get())
#     q.put(2)
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=wahaha,args=[q,])
#     p.start()
#     q.put(1)
#     time.sleep(0.1)
#     print(q.get())
# 在进程中使用队列可以完成双向通信

# import time
# import random
# from multiprocessing import Process,Queue
# 生产者消费者模型
# 解决数据供需不平衡的情况
# 队列是进程安全的 内置了锁来保证队列中的每一个数据都不会被多个进程重复取
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if food == 'done':break
#         time.sleep(random.random())
#         print('%s吃了%s'%(name,food))
#
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.random())
#         print('%s生产了%s%s'%(name,food,i))
#         q.put('%s%s'%(food,i))
#
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer,args=[q,'Egon','泔水'])
#     p2 = Process(target=producer,args=[q,'Yuan','骨头鱼刺'])
#     p1.start()
#     p2.start()
#     Process(target=consumer,args=[q,'alex']).start()
#     Process(target=consumer,args=[q,'wusir']).start()
#     p1.join()
#     p2.join()
#     q.put('done')
#     q.put('done')


import time
import random
from multiprocessing import Process,JoinableQueue
def consumer(q,name):
    while True:
        food = q.get()
        time.sleep(random.random())
        print('%s吃了%s'%(name,food))
        q.task_done()

def producer(q,name,food):
    for i in range(10):
        time.sleep(random.random())
        print('%s生产了%s%s'%(name,food,i))
        q.put('%s%s'%(food,i))
    q.join()   # 等到所有的数据都被taskdone才结束

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=producer,args=[q,'Egon','泔水'])
    p2 = Process(target=producer,args=[q,'Yuan','骨头鱼刺'])
    p1.start()
    p2.start()
    c1 = Process(target=consumer,args=[q,'alex'])
    c2 = Process(target=consumer,args=[q,'wusir'])
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()

# producer
    # put
    # 生产完全部的数据就没有其他工作了
    # 在生产数据方 ： 允许执行q.join
    # join会发起一个阻塞，直到所有当前队列中的数据都被消费
# consumer
    # get 获取到数据
    # 处理数据
    # q.task_done()  告诉q，刚刚从q获取的数据已经处理完了

# consumer每完成一个任务就会给q发送一个taskdone
# producer在所有的数据都生产完之后会执行q.join()
# producer会等待consumer消费完数据才结束
# 主进程中对producer进程进行join
# 主进程中的代码会等待producer执行完才结束
# producer结束就意味着主进程代码的结束
# consumer作为守护进程结束

# consumer中queue中的所有数据被消费
# producer join结束
# 主进程的代码结束
# consumer结束
# 主进程结束

