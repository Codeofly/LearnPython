# ******
# 类
# role = 123
# print(eval('role'))
# class A:
#     role = 'Person'
#     def func(self):
#         print('*'*self)
# # ret = input('>>>')
# # print(A.__dict__[ret])
# # getattr
# print(getattr(A,'role'))     # 从A的命名空间里找一个属性 ，直接就可以找到这个属性的值
# f = getattr(A,'func');f(1)   # 从A的命名空间里找一个方法 ，找到的是这个方法的内存地址
# getattr(A,'func')(1)
# A.func(1)
# 反射
# 正常情况下如果可以拿到这个变量 那么如有有这个变量的字符串形式 就是用反射可以获取到这个值
# 使用字符串数据类型的变量名 访问一个命名空间中的名字
# 找一个属性 ，直接就可以找到这个属性的值
# 找一个方法 ，找到的是这个方法的内存地址
# hasattr() 判断一个命名空间中有没有这个名字
# getattr() 从命名空间中获取这个名字对应的值

# 类中的反射
    # 类可以获取类中的属性和方法

# class A:
#     role = 'Person'
#     def func(self):
#         print('*'*self)


# print(hasattr(A,'r'))
# print(hasattr(A,'role'))
# print(hasattr(A,'func'))
# ret = input('>>>')
# if hasattr(A,ret):
#     print(getattr(A,ret))     # getattr从A的命名空间里找一个属性 ，属性不存在会报错
# if hasattr(A,ret):
#     func = getattr(A,ret)
#     func(1)

# hasattr getattr
# class A:
#     role = 'Person'
#     def __init__(self):
#         self.money = 500
#     def func(self):
#         print('*'*10)
#
# a = A()
# print(a.func)
# getattr(a,'func')()
# print(getattr(a,'money'))

# 类使用类命名空间中的名字
# 对象使用对象能用的方法和属性
# 模块使用模块中的名字
    # import os ; getattr(os,'rename')('user','user_info')
# 从自己所在的模块中使用自己名字

# 什么.什么
# import time   # 一个py文件就是一个模块
# time.time()
# print(time.time())
# print(getattr(time,'time')())

# import os
# os.rename('userinfo','user')
# getattr(os,'rename')('user','user_info')

# 'Teacher'   -- Teacher
# import teacher
# alex = teacher.Teacher('alex')
# print(alex.__dict__)

# import teacher
# t = 'Teacher'
# Teach_class = getattr(teacher,t)
# alex = Teach_class('alex')
# print(teacher.Teacher('alex'))

# a = 1
# b = 2
# def login():
#     print('执行login功能')
#
# def register():
#     print('执行register功能')
#
# import sys  # 和python解释器相关的内容都在sys里
# print(sys.modules['__main__'])
# func = input('>>>')
# if hasattr(sys.modules['__main__'],func):
#     getattr(sys.modules['__main__'],func)()


# 类使用类命名空间中的名字
#     getattr(类名,'名字')
# 对象使用对象能用的方法和属性
#     getattr(对象名,'名字')
# 模块使用模块中的名字
#     导入模块
#     getattr(模块名,'名字')
    # import os ; getattr(os,'rename')('user','user_info')
# 从自己所在的模块中使用自己名字
#     import sys
#     getattr(sys.modules['__main__'],名字)

# getattr一定要和hasattr配合使用

# 反射 4个内置函数
# getattr                   ******
# hasattr                   ******
# setattr  # 修改和新建      **
# delattr  # 删除一个属性    *

# 增删改 对象属性
# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def wahaha(self):
#         print('wahahahahaha')
#
# a = A('alex')
# a.name
# a.wahaha()
# getattr(a,'name')
# # a 'age' = 18
# # a.age = 18
# print(a.__dict__)
# setattr(a,'age',18)   # 给a对象新增一个属性
# print(a.__dict__)
# setattr(a,'name','egon')
# print(a.__dict__)
#
# # del a.age
# delattr(a,'age')
# print(a.__dict__)


# 增删改 方法
# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def wahaha(self):
#         print('wahahahahaha')
#
# def qqxing(self):
#     print('qqqqqxing')
#
# a = A('alex')
# setattr(A,'qqxing',qqxing)
# setattr(a, 'qqxing', qqxing)
# print(a.__dict__)       #将qqxing存到对象中了
# a.qqxing(a)
class A:
    def __init__(self,name):
        self.name = name
