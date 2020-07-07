# 明天下午考试 2:30-5:30
    # 装饰器
    # 生成器
    # 内置函数
    # 面向对象
    # 网络编程
    # 并发编程
# 刘洋 —— 网络编程

# 线程
# 什么是线程？
# 线程是cpu调度的最小单位
# 进程是资源分配的最小单位
# 进程和线程是什么关系？
    # 线程是在进程中的 一个执行单位
    # 多进程 本质上开启的这个进程里就有一个线程
    # 多线程 单纯的在当前进程中开启了多个线程
# 线程和进程的区别：
    # 线程的开启 销毁 任务切换的时间开销小
    # 在同一个进程中数据共享
    # 能实现并发，但不能脱离进程
    # 进程负责管理分配资源 线程负责执行代码
# GIL锁 —— 全局解释器锁
# 同一时刻只能有一个线程访问CPU —— 线程锁
# Cpython解释器 ——pypy jpython

# python程序效率下降
# 高计算型 —— 多线程会导致程序的效率下降
# 高IO型的 —— 可以使用多线程

# 多进程
# 分布式计算 —— celery
import time
from threading import Thread,currentThread,enumerate,activeCount

def func():
    print('-->',currentThread())
    time.sleep(0.1)
    print(123)

t = Thread(target=func)
t.start()
print(t.is_alive())
print(t.getName())
t.setName('t1')
print(t.getName())
# print(currentThread())
# print(enumerate())  # 你启动的活着的线程数 + 1（主线程）
print('-->',activeCount())  # 相当于len(enumerate())
# 守护线程
# 守护进程是等待主进程代码结束之后就结束
# 守护线程是等待主线程都结束之后才结束

