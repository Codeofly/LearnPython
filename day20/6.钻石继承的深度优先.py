# coding:utf-8
class A(object):
    pass
    # def func(self):
    #     print('A')
class B(A):
    pass
    # def func(self):
    #     print('B')
class C(A):
    def func(self):
        print('C')
class D(B,C):
    def func(self):
        super(D,self).func()
        print('D')

D.mro()
# 经典类 :在python2.*版本才存在,且必须不继承object
    # 遍历的时候遵循深度优先算法
    # 没有mro方法
    # 没有super()方法
# 新式类 :在python2.X的版本中，需要继承object才是新式类
    # 遍历的时候遵循广度优先算法
    # 在新式类中，有mro方法
    # 有super方法,但是在2.X版本的解释器中，必须传参数(子类名，子类对象)
d = D()
d.func()