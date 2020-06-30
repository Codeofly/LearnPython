#global
# 1,在局部空间内，声明一个全局变量
# def func1():
#     global name
#     name = '老男孩'
#     print(name)
# func1()
# print(name)
# 2,在局部空间内改变一个全局变量
a = 4
def func1():
    global a
    a = 5
    # print(name)
func1()
# print(a)

#nonlocal
# 1,不能修改全局变量。

a = 4
def func1():
    nonlocal a
    a = 5
    # print(name)
func1()
print(a)
#在局部作用域中，对父级作用域（或者更外层作用域非全局作用域）的变量进行引用和修改，
# 并且引用的哪层，从那层及以下此变量全部发生改变。
# a = 4
# def func1():
#     b = 6
#     def func2():
#         b = 666
#         print(b) #666
#     func2()
#     print(b) # 6
#
# func1()

# b = 4
# def func1():
#     global b
#     b = 6
#     def func2():
#         nonlocal b
#         b = 666
#         print(b) #
#     func2()
#     print(b) #
# print(b)
# func1()