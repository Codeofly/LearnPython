# 协程的特点
# 冻结当前程序/任务的执行状态 —— 技能解锁
# 可以规避IO操作的时间

# def func():
#     a = 'aaa'
#     b = 'bbb'
#     print(1)
#     yield a
#     print(2)
#     yield b
#     print(3)
#     yield 'ccc'
#
# g = func()
# next(g)
import time
def producer():
    res = []
    for i in range(10000000):
        res.append(i)
    return res

def consumer(res):
    for i in res:pass

start = time.time()
res = producer()
consumer(res)
print(time.time() - start)

# def producer():
#     for i in range(1000000):
#         yield i
# def consumer():
#     g = producer()
#     for i in g:pass
# start = time.time()
# consumer()
# print(time.time() - start)

# def func():
#     x = yield 1
#     print(x)
#     yield 2
#
# g = func()
# print(next(g))
# print(g.send('aaa'))

import time
def consumer():
    while True:
        x=yield

def producer():
    g=consumer()
    next(g)
    for i in range(10000000):
        g.send(i)
start = time.time()
producer()
print(time.time() - start)

# 单纯的切换 还是要耗费一些时间的  记住当前执行的状态
# 用时间换了空间