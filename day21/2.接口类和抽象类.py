# 抽象类和接口类
# java 编程原则和设计模式
# 设计模式  程序设计 具有里程碑意义的设计方式 从java中演变出来的
    # 单例模式
        # 一个类只有一个实例
## 算法导论  计算的方法 时间和空间的问题 权威通用

# java
    # 面向对象
    # java不能多继承
# 编程原则
    # python
    # 开放封闭原则
        # 开放 对扩展是开放的
        # 封闭 对修改是封闭的
    # 依赖倒置原则
    # 接口隔离原则
# 已经写完的程序代码是不允许修改的

# 支付功能的例子
    # 支付宝支付
    # qq支付
    # apply_pay
    # 微信支付

# 创建一个规范
# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):    # 抽象类 接口类  规范和约束  metaclass指定的是一个元类
#     @abstractmethod
#     def pay(self):pass  # 抽象方法
#
# class Alipay(Payment):
#     def pay(self,money):
#         print('使用支付宝支付了%s元'%money)
#
# class QQpay(Payment):
#     def pay(self,money):
#         print('使用qq支付了%s元'%money)
#
# class Wechatpay(Payment):
#     def pay(self,money):
#         print('使用微信支付了%s元'%money)
#     def recharge(self):pass
#
# def pay(a,money):
#     a.pay(money)
#
# a = Alipay()
# a.pay(100)
# pay(a,100)    # 归一化设计：不管是哪一个类的对象，都调用同一个函数去完成相似的功能
# q = QQpay()
# # q.pay(100)
# pay(q,100)
# w = Wechatpay()
# pay(w,100)   # 到用的时候才会报错



# 抽象类和接口类做的事情 ：建立规范
# 制定一个类的metaclass是ABCMeta，
# 那么这个类就变成了一个抽象类(接口类)
# 这个类的主要功能就是建立一个规范

# 抽象类中所有被abstractmethod装饰的方法都必须被继承的子类实现
# 如果不实现，那么在实例化阶段将会报错

# 无论是抽象类还是接口类metaclass=ABCMeta 都不可以被实例化
# p = Payment()  # 报错
