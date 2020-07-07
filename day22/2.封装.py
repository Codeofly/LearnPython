# 面向对象的三大特性 ： 继承 多态 封装
# 封装 ：
    # 广义上的
    # 狭义上的 ：会对一种现象起一个专门属于它的名字

# 把一堆东西装在一个容器里

# 函数和属性装到了一个非全局的命名空间 —— 封装
# class A:
#     __N = 'aaa'  # 静态变量
#
# print(A.__N)

# python
# pulic 公有的
# private 私有的

# java完全面向对象的语言
# public 公有的
# protect 保护的
# private 私有的

# 定义一个私有的名字 ： 就是在私有的名气前面加两条下划线 __N = 'aaa'
# 所谓私有，就是不能在类的外面去引用它
# class A:
#     __N = 'aaa'  # 静态变量
#     def func(self):
#         print(A.__N)  # 在类的内部使用正常
#
# a = A()
# a.func()
# print(A.__N)   # 在类的外部直接使用 报错


# class A:
#     __N = 'aaa'  # 静态变量
#     def func(self):
#         print(A.__N)  # 在类的内部使用正常
#
# print(A.__dict__)
# print(A._A__N)   # python就是把__名字当成私有的语法

# 一个私有的名字 在存储的过程中仍然会出现在A.__dict__中，所以我们仍然可以调用到。
# python对其的名字进行了修改： _类名__名字
# 只不过在类的外部调用 ：需要“_类名__名字”去使用
# 在类的内部可以正常的使用名字

# _A__N
# 在类内 只要你的代码遇到__名字，就会被python解释器自动的转换成_类名__名字


# 私有的属性
# class B:
#     def __init__(self,name):
#         self.__name = name
#     def func(self):
#         print('in func : %s'%self.__name)
# b = B('alex')
# # print(b._B__name)
# b.func()

# 私有的方法
class C:
    def __wahaha(self):
        print('wahaha')
    def ADCa(self):
        self.__wahaha()
c = C()
# c._C__wahaha()
c.ADCa()

# 在类中，静态属性，方法，对象属性都可以变成私有的，只需要在这些名字之前加上__

class D:
    def __func(self):   #'_D__func'
        print('in func')

class E(D):
    def __init__(self):
        self.__func()      # '_E__func'
e = E()
# 私有的名字不能被子类继承


# class D:
#     def __init__(self):
#         self.__func()
#     def __func(self):
#         print('in D')
#
# class E(D):
#     def __func(self):
#         print('in E')
# e = E()
# 私有的名字，在类内使用的时候，就是会变形成_该类名__方法名
# 以此为例 ：没有双下换线会先找E中的func
# 但是有了双下划线，会在调用这个名字的类D中直接找_D__func

# class F:
#     pass
# F.__name = 'alex'  # 不是在创建私有属性
# print(F.__name)
# print(F.__dict__)
# 变形只在类的内部发生

# class F:
#     def ADCa(self):
#         self.__name = 'alex'   # _F__name
#
# f = F()
# f.ADCa()
# print(f._F__name)

# java中的对比
# public 公有的    在类的内部可以使用，子类可以使用，外部可以使用    python中所有正常的名字
# protect 保护的   在类的内部可以使用，子类可以使用，外部不可以使用  python中没有
# private 私有的   只能在类的内部使用，子类和外部都不可以使用        python中的__名字

# 私有的用法
# 当一个方法不想被子类继承的时候
# 有些属性或者方法不希望从外部被调用，只想提供给内部的方法使用

# 描述一个房子
    # 单价
    # 面积
    # 长宽高
# class Room:
#     def __init__(self,name,price,length,width,height):
#         self.name = name
#         self.price = price
#         self.__length = length
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         return self.__length*self.__width

# r = Room('鹏鹏',100,2,1,0.5)
# print(r.name)
# print(r.price)
# print(r.area())

# class Person:
#     def __init__(self,name,pwd):
#         self.name = name
#         self.__pwd(pwd)
#     def __pwd(self,pwd):
#         # '12345' ---> ascii ---> 2175981070935
#         self.my_secret_pwd = 2175981070935














