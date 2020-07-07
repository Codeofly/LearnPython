# 操作系统中的IO多路复用的机制select :
    #  windows操作系统提供给你的一种
    # 监听接收数据IO的一个代理
# select模块：
    # python使用操作系统select机制的功能
# import socket
# import select
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.setblocking(False)
# sk.listen()
#
# l = [sk]                         # sk.accept
# while True:                     #
#     r,w,x = select.select(l,[],[])   # 阻塞
#     for obj in r:
#         if obj is sk:
#             conn,addr = obj.accept()
#             l.append(conn)                   # conn.recv
#         else:
#             msg = obj.recv(1024)
#             if not msg:
#                 obj.close()
#                 l.remove(obj)
#                 continue
#             print(msg)
#             obj.send(b'bye')



# select  - windows/linux/ios
# poll - linux/ios   内部采用了一种数据结构的优化，让能监听的数据量变多了
# epoll -linux  # 回调函数

# socketserver
# IO多路复用 + 多线程 实现的
# 源码


# 垃圾回收机制
# —— python解释器
# C语言
# 引用计数 —— 机制
# 一个变量在引用计数为0的时候并不会立刻被解释器删掉
# 三条链表 == 三个容器
# 每个容器里 可以存放700个变量
# 数据是有池 持久
# 一直在的
# 过一段时间就不用了
# 生命周期最短的列表中
# 700个变量 == 清理一次（引用计数）
# 第二代 -->
# 三个链表都会做一次大清理
# a = []
# b = []
# a.append(b) +1
# b.append(a) +1
# ...
#

# 循环引用
# 链表关系解决了循环引用的计数统计问题







# z = (lambda x:x*i for i in range(3))
# # 生成器表达式和列表推导式的区别
# # 生成器表达式是要一个值计算一个值
# # 列表表达式是一次把所有的值都拿出来
# x = [o(2) for o in z]
# print(x)  # [0,2,4]

# i = None
# def func(x):
#     return x*i
# z = []
# # for i in range(3):
# #     z.append(func)
# i = 0
# z.append(func)
# i = 1
# z.append(func)
# i = 2
# z.append(func)
# print(z)
# for o in z:
#     o(2)
# [4,4,4]

i = None
def func(x):
    return x*i
def gen():
    global i
    for i in range(3):
        yield func
z = gen()
for o in z:
    print(o(2))

# for循环
# lambda循环

