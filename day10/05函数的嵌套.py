# 函数什么时候执行？ 函数调用的时候执行。
# 代码从上至下依次执行， 调用函数：函数里面从上至下依次执行。
# print(111)
# def func1():
#     print(333)
#
# def func2():
#     print(444)
#
# def func3():
#     print(555)
#     func2()
#
# func1()
# print(222)
# 111 333 222

# print(111)
# def func1():
#     print(333)
#     func2()
#     print(666)
#
# def func2():
#     print(444)
#
# def func3():
#     print(555)
#
# func1()
# print(222)
# 111 333 444 666 222


# print(111)
# def func1():
#     print(333)
#     func2()
#     print(666)
#
# def func2():
#     print(444)
#     func3()
#
# def func3():
#     print(555)
#
# func1()
# print(222)
# 111 333 444 555 666 222

# a = 2
# b = 3
# def func1():
#     c = 5
#     d = 6
#     print(globals())  # 全局变量放在一个字典中
#     return locals()  # {'c': 5, 'd': 6}
# print(func1())

# print(globals())  # 全局名称空间：所有变量
# print(locals())  # 局部名称空间：所有变量


