# 店庆 全场八折
class Goods:
    __discount = 0.8
    def __init__(self,name,origin_price):
        self.name = name
        self.__price = origin_price

    @property
    def price(self):
        return self.__price * Goods.__discount

    @classmethod
    def change_discount(cls,new_discount):     # 类方法 可以直接被类调用 不需要默认传对象参数 只需要传一个类参数就可以了
        cls.__discount = new_discount

Goods.change_discount(1)  # 不依赖对象的方法 就应该定义成类方法 类方法可以任意的操作类中的静态变量
apple = Goods('apple',5)
banana = Goods('banana',8)
print(apple.price)
print(banana.price)

# 折扣变了 店庆结束 恢复折扣
# apple.change_discount(1)   # 如果要改变折扣 是全场的事情 不牵扯到一个具体的物品 所以不应该使用对象来调用这个方法
# print(apple.price)
# print(banana.price)


# staticmethod
# 当一个方法要使用对象的属性时 就是用普通的方法
# 当一个方法要使用类中的静态属性时 就是用类方法
# 当一个方法要既不使用对象的属性也不使用类中的静态属性时，就可以使用staticmethod静态方法

# def login():
#     user= input('user :')
#     if user == 'alex':print('success')
#     else :print('faild')
#
# login()
class Student:
    def __init__(self,name):pass

    @staticmethod
    def login(a):                   # login就是一个类中的静态方法 静态方法没有默认参数 就当成普通的函数使用即可
        user = input('user :')
        if user == 'alex':
            print('success')
        else:
            print('faild')

Student.login(1)

# 完全面向对象编程
# 先登录 后 实例化
# 还没有一个具体的对象的时候 就要执行login方法

# 使用什么样的方法要看具体用到了哪些名称空间中的变量
    # 当一个方法要使用对象的属性时 就是用普通的方法
    # 当一个方法要使用类中的静态属性时 就是用类方法
    # 当一个方法要既不使用对象的属性也不使用类中的静态属性时，就可以使用staticmethod静态方法a
