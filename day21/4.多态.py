# 多态
# java c++ c# —— 强类型语言
# 相同数据类型之间做运算
# def func(int a):pass
# func('a')

# shell语言 —— 弱类型语言
# 1+'1'
# def func(a):pass
# 1 'a' [1,2,3] ()

# 介于 强类型 与 弱类型之间 —— python 动态强类型语言
# 相同数据类型之间做运算
# def func(a):pass
class Payment:
    def pay(self):pass

class QQpay(Payment):
    def pay(self,money):
        print('使用qq支付了%s元'%money)

class Wechatpay(Payment):
    def pay(self,money):
        print('使用微信支付了%s元'%money)
    def recharge(self):pass

# def pay(Payment pay_obj,int money):   #  java 多态 在一个类之下发展出来的多个类的对象都可以作为参数传入这里
#     pay_obj.pay(money)

# 无论是python的2.*还是3.* ： 天生自带多态效果

# qq_obj = QQpay()
# print(type(qq_obj))  # 一个对象的数据类型就是它所在的类
# # # qq_obj.pay(100)
# pay(qq_obj,100)
# we_obj = Wechatpay()
# # # we_obj.pay(200)
# pay(we_obj,200)
# def len(object obj):pass
# class len_class:pass
# class tuple(len_pass):pass
# class list(len_pass):pass
# class str(len_pass):pass
# tuple list str dict set

# 鸭子类型
# class QQpay():
#     def pay(self,money):
#         print('使用qq支付了%s元'%money)
#
# class Wechatpay():
#     def pay(self,money):
#         print('使用微信支付了%s元'%money)
#
# def pay(pay_obj,money):
#     pay_obj.pay(money)

# 索引
class list:
    def index(self):pass
class str:
    def index(self):pass
class tuple:
    def index(self):pass
# [].index()
# ''.index()
# ().index()


# 多态和鸭子类型
# 多态 通过继承实现
    # java 在一个类之下发展出来的多个类的对象都可以作为参数传入一个函数或者方法
    # 在python中不需要刻意实现多态，因为python本身自带多态效果
# 鸭子类型
    # 不是通过具体的继承关系来约束某些类中必须有哪些方法名
    # 是通过一种约定俗成的概念来保证在多个类中相似的功能叫相同的名字


# 复习课上的例子 重点记概念
# 面向对象的思维导图