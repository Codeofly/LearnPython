# 生成器：生成器本质上是迭代器。
# l = [1,2,3]
# l.__iter__()
# 生成器的产生方式：
# 1，生成器函数构造。
# 2，生成器推导式构造。
# 3，数据类型的转化。

# def func1():
#     print(111)
#     print(222)
#     print(333)
#     return 666
#
#
# print(func1())
#
# g = func1()

# def func1():
#     # print(111)
#     # print(222)
#     # print(333)
#     yield 666
#     yield 555
#     yield 777
#
# g = func1()

# print(g)  # <generator object func1 at 0x0000000001197888>
# 第一：函数中只要有yield 那他就不是一个函数，而是一个生成器
# 第二：g称作生成器对象。
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# def func1():
#     for i in range(1,10001):
#         print('老男孩校服%d号' % i)
# func1()

# def func1():
#     for i in range(1,10001):
#         yield '老男孩校服%d号' % i
# g = func1()
#
# for i in range(50):
#     g.__next__()
#
# for j in range(150):
#     print(g.__next__())

# l1 = [i for i in range(1000)]

# send
# def generator():
#     print(123)
#     content = yield 1
#     print(content)
#     print(456)
#     yield 2
# g = generator()
# g.__next__()
# g.send('hello')

'''
next 和 send 功能一样，都是执行一次
send 可以给上一个yield赋值。

'''
