# import sys
# print(sys.modules)  # python解释器启动的时候
# import my_module

# 导入一个模块，
# 相当于这个模块从上到下依次被执行了
# 同一个模块不会被多次导入

# 如何使用my_module中的名字
# my_module.func1()
# import 的 过程
# import一个模块的时候，首先创建一个属于my_module的内存空间
# 加载my_module模块中所有的代码
    # 将my_module模块中的名字方法放在my_module的命名空间里
# my_module.func2()
# print(my_module.money)
#
# money = 200
# def func1():
#     print('in my func1')
# my_module.func2()
# func1()
#
# print(sys.modules)

# 50个人  ：25 json    25 pickle
# inp = input('json or pickle>>>')
# if inp == 'json':
#     import json as m
# elif inp == 'pickle':
#     import pickle as m
#
# m.dumps({'k':'v'})
# m.loads()

# 数据库
# mysql oracle
# 框架  oracle mysql
# if oracle:
#     import oracle as db
# else:
#     import mysql as db
# # db.open
# # db.write
# # db.close

import os
import sys
import time
import my_module
# PEP8
# 每一行import 应该导入一个模块
# 如果不是必要的需求，所有的模块都应该在文件的顶端导入
# 关于导入模块的顺序 先导入内置的 再导入扩展 最后导入自定义

# import
# 导入模块： 模块的名字要符合变量的定义规范
#            不要起你知道的内置的名字的模块
# 模块不会被多次导入
# 导入模块相当于
    # 开辟了一个新的空间
    # 执行被导入模块中的代码
    # 创建一个模块名作为这块空间的引用
# 导入的模块中的名字和全局文件中的名字不会冲突
# import 。。。 as 。。。
# 导入多个模块 import a,b,c

# PEP8规范
# 每一行import 应该导入一个模块
# 如果不是必要的需求，所有的模块都应该在文件的顶端导入
# 关于导入模块的顺序 先导入内置的 再导入扩展 最后导入自定义

# import sys
# print(sys.modules)

