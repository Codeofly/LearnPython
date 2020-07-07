# from my_module import func1
# print(money)
# money = 20
# print(money)

# def func():
#     print('in demo2')
#
# func()
# func1()
# import sys
# print(sys.modules)
# from my_module import func1

# 导入模块的时候 sys.modules  import
# 使用变量的时候看的是命名空间 globals()

# from my_module import func1,func2
# money = 999
# func1()
# func2()
# 尽管导入的func1,func2都属于全局的变量了，
# 但是使用func2的时候要用到的变量仍然是局部的

# from my_module import func1,func2
# if inp ==  'sha':
#     from my_module import func1 as func
# elif inp ==  'sha2':
#     from my_module import func2 as func
# elif inp ==  'md5':
#     from my_module import func3 as func
#
# func()
# from time import time as t,sleep as s
# import my_module
# my_module.a
# from my_module import *
# print(a)
# print(A)
# print(func1)

# from my_module import *
# print(a)
# print(func1)
# print(func2)

import my_module
my_module.func2()

# from ... import ...
# from 模块名 import 名字
    # 导入的名字直接属于全局，但是指向模块的名字所在的内存空间
# 导入的名字如果是函数或者方法，引用了全局的变量，
# 仍然使用模块中的变量
# 导入的名字和全局的名字是一样的，谁最后抢占到就是谁的
# 可以导入多个名字，用逗号分割
# 还可以起别名 as
# from 模块 import *   那么默认会把模块中所有名字都导入到全局
# * 和 __all__

# 作业1：计算文件夹中所所有文件的大小
# 作业2
# 思考：假如有两个模块a，b。
# 我可不可以在a模块中import b ，再在b模块中import a？
