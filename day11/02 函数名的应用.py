# 函数名是什么？
# 函数名是函数的名字，本质：变量，特殊的变量。
# 函数名() 执行此函数。

# 1,单独打印函数名  <function func1 at 0x0000000000872378>
# def func1():
#     print(666)
# print(func1)  # <function func1 at 0x0000000000872378>
# a = 6
# print(a)

# 2，函数名的赋值。


# def func2():
#     print(666)
#
# f = func2
# print(f())

# 3,函数名可以作为容器类数据的元素。
# def f1():
#     print(1211)
#
#
# def f2():
#     print(1222)
#
#
# def f3():
#     print(1233)
#
#
# def f4():
#     print(1233)

'''
f1()
f2()
f3()
f4()
'''

# l1 = [f1, f2, f3, f4]
# for i in l1:
#     i()

# l1 = []
# for i in range(1,5):
#     l1.append('f'+str(i))
# # print(l1)

# for i in l1:
#     eval(i)()

# 4 函数名可以作为参数。
# a = 1
# def f1(x):
#     print(x)
# f1(a)


# def f1():
#     print(666)
#
#
# def f2(x):  # x = f1
#     x()  # f1()
#
# f2(f1)

# 5,函数名可以作为函数的返回值。

# def f11(x):
#     return x
#
# ret = f11(5)  # 5
# print(ret)



# def f1():
#     print(666)
#
#
# def f2(x):  # x = f1
#     return x
#
#
# ret = f2(f1)  # f1
# ret()


# def wraaper():
#     def inner():
#         print(666)
#     inner()
# wraaper()


def wraaper():
    def inner():
        print(666)
    return inner

ret = wraaper()  # inner
ret()  # inner()

# 闭包：就是内层函数对外层函数（非全局）变量的引用。
# 如何判断  内层函数名.__closure__  cell 就是=闭包

# def wraaper1():
#     name = '老男孩'
#     def inner():
#         print(name)
#     inner()
#     print(inner.__closure__)  # cell

# wraaper1()


# name = '老男孩'
# def wraaper2():
#     name1 = 'alex'
#     def inner():
#         print(name)
#         print(name1)
#     inner()
#     print(inner.__closure__)  #  None
# wraaper2()

#面试题 闭包
# name = '老男孩'
# def wraaper2(n):
#     #  n = '老男孩' 相当于
#     def inner():
#         print(n)
#     inner()
#     print(inner.__closure__)  #  None
# wraaper2(name)

# 闭包：当函数开始执行时，如果遇到了闭包，他有一个机制，
# 他会永远开辟一个内存空间，将闭包中的变量等值放入其中，不会随着函数的执行完毕而消失。

from urllib.request import urlopen
# content1 = urlopen('http://www.cnblogs.com/jin-xin/articles/8259929.html').read().decode('utf-8')
# content2 = urlopen('http://www.cnblogs.com/jin-xin/articles/8259929.html').read().decode('utf-8')
# content3 = urlopen('http://www.cnblogs.com/jin-xin/articles/8259929.html').read().decode('utf-8')
# print(content)


def index():
    url = "http://www.xiaohua100.cn/index.html"
    def get():
        def fun():
            pass
        return urlopen(url).read()
    a = 3
    return get



print(index()())
print(index()())
print(index()())
print(index()())
print(index()())
print(index()())
