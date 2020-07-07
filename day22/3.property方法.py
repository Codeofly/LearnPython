# 人体BMI指数
# 体质指数（BMI）=体重（kg）÷身高^2（m）
# 写一个类 描述人体BMI指数

class Person:
    def __init__(self,name,weight,height):
        self.name = name
        self.__height = height
        self.__weight = weight
        # self.bmi = self.__weight / self.__height ** 2
        # self.bmi = self.cal_BMI()

    def cal_BMI(self):
        return self.__weight / self.__height ** 2

    @property
    def bmi(self):
        return self.__weight / self.__height ** 2
p = Person('大表哥',92,1.85)
print(p.cal_BMI())
# p.cal_BMI()   # bmi是一个名词
# print(p.bmi)   # bmi是一个名词
# p._Person__weight = 90
# print(p.bmi)
# 将一个方法伪装成一个属性
    # 并不会让你的代码有什么逻辑上的提高
    # 只是从调用者的角度上换了一种方式，使之看起来更合理

# 单纯的在init中计算
# class Person:
#     def __init__(self,name,weight,height):
#         self.name = name
#         self.__height = height
#         self.__weight = weight
#         self.bmi = self.__weight / self.__height ** 2
#
# p = Person('大表哥',92,1.85)   #
# print(p.bmi)   # bmi是一个名词
# p._Person__weight = 90   # 3天
# print(p.bmi)

# class Person:
#     def __init__(self,name,weight,height):
#         self.name = name
#         self.__height = height
#         self.__weight = weight
#     @property
#     def bmi(self):
#         return self.__weight / self.__height ** 2
#
# p = Person('大表哥',92,1.85)
# print(p.bmi)
# p._Person__weight = 90
# print(p.bmi)

# @property 能够将一个方法伪装成一个属性
# 从原来的的对象名.方法名()，变成了对象名.方法名
# 只是让代码变的更美观

# 如果有重名的名字
# class Person:
#     def __init__(self,name,weight,height):
#         self.name = name
#         self.__height = height
#         self.__weight = weight
#     @property
#     def bmi(self):
#         return self.__weight / self.__height ** 2
# print(Person.__dict__)
# p = Person('大表哥',92,1.85)
# print(p.__dict__)
# print(p.bmi)   # 对这个属性 只能看了

# 被property装饰的bmi仍然是一个方法 存在Person.__dict__
# 对象的.__dict__中不会存储这个属性

# 在一个类加载的过程中，会先加载这个中的名字，包括被property装饰的
# 在实例化对象的时候，python解释器会先到类的空间里看看有没有这个被装饰的属性，
# 如果有就不能再在自己对象的空间中创建这个属性了

# 圆形类
# 半径 面积 周长
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def cal_area(self):
#         return self.r**2*pi
#     def cal_perimeter(self):
#         return 2*pi*self.r
# c = Circle(10)
# print(c.cal_area())
# print(c.cal_perimeter())

# 将方法伪装成属性，方法中一般涉及的都是一些计算过程
# from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     @property
#     def area(self):
#         return self.r**2*pi
#
#     @property
#     def perimeter(self):
#         return 2*pi*self.r
# c = Circle(10)
# print(c.area)
# print(c.perimeter)
# c.r = 15
# print(c.area)
# print(c.perimeter)

# __name setter deleter
# class Person0:
#     def __init__(self,name):
#         self.name = name
#
# p = Person0('alex')
# print(p.name)
# p.name = 'sb'
# p.name = 123

# class Person:
#     def __init__(self,name):
#         self.__name = name  # 私有的属性了
#     @property
#     def name(self):
#         return self.__name
#
#     def set_name(self,new_name):
#         if type(new_name) is str:
#             self.__name = new_name
#         else:
#             print('您提供的姓名数据类型不合法')
#
# p = Person('alex')
# print(p.name)
# # 和直接定义name属性有什么区别？？？
# p.set_name('alex_sb')
# print(p.name)
# p.set_name(123)
# print(p.name)


# 方法伪装成的属性的修改
# class Person:
#     def __init__(self,n):
#         self.__name = n  # 私有的属性了
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter        # 重要程度 ***
#     def name(self,new_name):
#         if type(new_name) is str:
#             self.__name = new_name
#         else:
#             print('您提供的姓名数据类型不合法')
#
# p = Person('alex')
# print(p.name)       #def name(self):
# p.name = 'alex_sb' #def name(self,new_name):
# print(p.name)       #def name(self):
# p.name = 123 #def name(self,new_name):
# print(p.name)       #def name(self):

# 方法伪装成的属性的删除
class Person:
    def __init__(self,n):
        self.__name = n  # 私有的属性了
    @property            # 重要程度 ****
    def name(self):
        return self.__name
    # @name.deleter
    # def name(self):
    #     print('name 被删除了')
    # @name.deleter         # 重要程度*
    # def name(self):
    #     del self.__name

# p = Person('alex')
# print(p.name)
# del p.name  # 只是执行了被@name.deleter装饰的函数
# print(p.name)

#@property --> func     将方法伪装成属性，只观看的事儿
#@func.setter --> func  对伪装的属性进行赋值的时候调用这个方法 一般情况下用来做修改
#@func.deleter --> func 在执行del 对象.func的时候调用这个方法 一般情况下用来做删除 基本不用

# 商品的 折扣
# 有一个商品 ： 原价 折扣
# 当我要查看价格的时候 我想看折后价
# class Goods:
#     def __init__(self,name,origin_price,discount):
#         self.name = name
#         self.__price = origin_price
#         self.__discount = discount
#
#     @property
#     def price(self):
#         return self.__price * self.__discount
#     @price.setter
#     def price(self,new_price):
#         if type(new_price) is int or type(new_price) is float:
#             self.__price = new_price
# apple = Goods('apple',5,0.8)
# print(apple.price)
# # 修改苹果的原价
# apple.price = 8
# print(apple.price)


# 将一些需要随着一部分属性的变化而变化的值的计算过程 从方法 伪装成属性
# 将私有的属性保护起来，让修改的部分增加一些约束，来提高程序的稳定性和数据的安全性

















