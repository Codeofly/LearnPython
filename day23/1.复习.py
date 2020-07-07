# 进阶
# 常用模块
    # 序列化模块 hashlib模块
# 写作业
# 考试 下周三、周四

class A:
    def func1(self):pass   # 对象与方法之间的绑定
    def func4(self): pass  # 对象与方法之间的绑定
    @classmethod
    def func2(cls): pass    # 类与方法之间的绑定
    @staticmethod
    def func3(): pass


a = A()
b = A()
# 普通方法 对象和类绑定的过程
# print(A.func1)
# print(a.func1)   # func1(a)
# print(b.func1)

# 类方法 由于不适用对象内存空间中的属性，所以不会将对象和方法绑在一起
# 而是将类和方法绑在一起
# print(A.func2)
# print(a.func2)   # 对象能找到类 类里面绑着方法
# print(b.func2)

# 静态方法    不是绑定方法 没有和对象或者类发生任何绑定关系
# print(A.func3)
# print(a.func3)
# print(b.func3)


# class B:
#     pass
# b1 = B()
# b2 = b1
# print(b2)
# print(b1)
# def func(b):
#     print(b)
#     return b
# ret = func(b2)
# python处处皆对象
# 1
# 'a'
# [b1,b2]
# [1,2,3]

# class Foo:
#     def __init__(self,name):
#         self.name = name
#         self.age = 18
#
# class Son(Foo):
#     def __init__(self,name,money):
#         Foo.__init__(self,name)
#         self.age = 20
#         self.money = money
#
# son = Son('egon',500)
# print(son.__dict__)