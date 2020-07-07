# __call__
# __eq__
# __del__
# __new__
# item  对象使用中括号的形式去操作

# __call__
# class Teacher():
#     def __call__(self):
#         print(123)
#     def call(self):print(123)
# t = Teacher()
# t.call()
# t()   # 对象名() 相当于调用类内置的__call__
# 一个对象是否可调用 完全取决于这个对象对应的类是否实现了__call__
# callable
# print(callable(Teacher))
# print(callable(t))

# class A:
#     def __eq__(self, other):
#         # if self.__dict__ == other.__dict__:
#             return True
# # __eq__()
# a = A()
# a.name = 'alex'
# b = A()
# b.name = 'egon'
# print(a)
# print(b)
# print(a == b)

# == 是由__eq__的返回值来决定的

# __del__ 析构方法:  在删除一个对象的时候做一些首尾工作
# class A:
#     def __init__(self):
#         pass
#         # self.f = open('文件','w')
#     def __del__(self):
#         print('执行我啦')
# a = A()
# del a
# print('aaa')
# 会报错，已经删除了对象a，再查询就查询不到了，但是‘执行我了’正常执行了
class A:
    def __init__(self):
        self.f = open('文件','w')
    def __del__(self):
        self.f.close()
        print('执行我啦')
a = A()
del a
print(a)
print('aaa')

# __new__ 构造方法
# 实例化的时候
# 创造对象的过程  __new__
# __init__ 初始化

# 设计模式 —— 单例模式
# 单例模式 就是 一个类 只能有一个实例
# class A:pass
# a = A()
# b = A()
# print(a)
# print(b)

class B:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            obj = object.__new__( cls)
            cls.__instance = obj
        return cls.__instance
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def func(self):
        print(self.name)
a = B('alex',80)
b = B('egon',20)
print(a)
print(b)
print(a.name)
print(b.name)

# item
# dic = {'k':'v'}
# print(dic['k'])

#
# class Foo:
#     def __init__(self,name):
#         self.name=name
#
#     def __getitem__(self,item):
#         return  self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#
# f = Foo('alex')
# # f.name = ...
# print(f['name'])    # f.__getitem__('name')
# f['age']  = 18      # 赋值
# print(f.age)         # 自带的语法
# print(f['age'])     # 修改
# f['age']  = 80
# print(f['age'])     # 通过实现__getitem__得到的
# del f['age']
# print(f.age)         # 删除

# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
# f = Foo('alex')
# del f.name     #相当于执行了__delattr__
# # delattr(f,'name')

# 100个同一个类的对象
# Person name age sex
# 100 name sex
# class A:
#     pass












