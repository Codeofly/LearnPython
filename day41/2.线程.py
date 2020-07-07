# 进程
# 操作系统管理进程
# 进程是执行任务
# 资源的隔离
# 在一个操作系统中 同一时间 有多个任务
# 多个任务之间的内存必须隔离开
# 使用qq的时候 还能使用微信

# 并发的要求日益增加
# 聊天 —— 开子进程
# 你可以看电影 —— 开子进程
# 缓存其他电影

# 开启一个子进程的开销 是很大的
# 操作系统在进程之间的切换 时间开销也很大

# 进程之间的通信
# 数据共享 ： 时间开销
# 如果多个子进程之间的数据共享量过多的时候，
# 就不应该将这些数据隔离开

# 一个进程 —— 实现不了并发
# 你既不希望数据隔离，还要实现并发的效果
# 线程

# 线程是轻量级的进程
# 线程的创建和销毁所需要的时间开销都非常小
# 线程直接使用进程的内存
# 线程不能独立存在，要依赖于进程

# 进程 —— 资源分配的最小单位
# 线程 —— CPU调度的最小单位
    # 轻型进程 ： 创建、销毁、切换 开销比进程小
    # 数据不隔离
    # 可以并发
    # 依赖进程
# 每一个进程里至少有一个线程
# 进程负责管理资源、线程负责执行代码
# def func(exp):
#     # 2+3*5-6
#     return eval(exp)



# python程序运行起来 —— 进程
# 进程 —— 管理整个程序的内存，
         # 存储全局的变量 : 内置的函数 全局的名字
# 线程 —— 执行代码

# 多个线程 —— 同时执行 —— 并发效果
# 利用python开启多线程 —— 并发
# import os
# import time
# from threading import Thread
# from multiprocessing import Process
# def func(i):
#     print('-->',os.getpid())
#     time.sleep(1)
#     print('*'*i)
#
# if __name__ == '__main__':
#     print(os.getpid())
#     start = time.time()
#     thread_lst = []
#     for i in range(20):
#         t = Thread(target=func,args=(i,))
#         t.start()
#         print('-->',t.name,t.ident)
#         thread_lst.append(t)
#     for t in thread_lst:t.join()
#     print(time.time()-start)

    # start = time.time()
    # process_lst = []
    # for i in range(20):
    #     p  = Process(target=func,args=(i,))
    #     p.start()
    #     process_lst.append(p)
    # for p in process_lst: p.join()
    # print(time.time()-start)

# 效率问题 : 线程快 进程慢
# 同一个进程下的多个线程进程号相同 : 线程号不同
# if __name__ == '__main__' : 开启进程 必须有这句话 但是开启线程不需要
    # 这种现象只在windows操作系统上才出现
# 数据的共享问题：在进程之间数据隔离，在线程之间数据共享

# def manager():
#     global n
#     n = 0
#
# from threading import Thread
# n = 100
# t = Thread(target=manager)
# t.start()
# t.join()
# print('--->',n)


# python代码 --> 字节码 ——> 机器码
# c语言 java c++
# 字节码 --> 机器码

# python 代码的计算效率 —— 高计算性
# python
# 高IO型的程序 ： web网站 爬虫

# python的程序就不能充分的利用CPU了呢？？？
# 多进程 —— 开启和销毁的时候慢 操作系统切换的时候慢

# GIL —— 全局解释器锁
    # 锁线程 ：在计算的时候 同一时刻只能有一个线程访问CPU
    # 线程锁限制了你对CPU的使用，但是不影响web类或者爬虫类代码的效率
    # 我们可以通过启动多进程的形式来弥补这个问题

# 买电脑的时候
# 4核8线程
    # 4核 —— 4个CPU  —— 4个
    # 4核8线程 -- 4个cpu -- 8个线程可以同时在cpu上运行的效果
    # 8核的


# 守护线程
import time
from threading import Thread
def func1():       # 守护线程
    while True:
        time.sleep(1)
        print('子线程')

def func2():
    time.sleep(5)
    print('子线程2')

t = Thread(target=func1)
t2 = Thread(target=func2)
t.setDaemon(True)
t.start()
t2.start()
print('主线程')
# 主进程的守护进程是在主进程的代码结束，守护进程就结束了
# 主线程的守护线程会在非守护线程的所有线程执行完毕之后才结束

# ftp继续


# cpu同一时刻只能执行一个进程
    # 是
# cpu同一时刻只能执行一个进程中的线程
# 单线程的程序

















