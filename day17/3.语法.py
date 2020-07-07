# class Person:
#     role = 'person'   # 静态属性
#     def f1(self):     # 动态属性 方法（函数）  默认带一个参数self
#         print(1234567)
# 查看静态变量的第一种方式
# print(Person.__dict__)   # 内置的双下方法
# print(Person.__dict__['静态变量'])
# Person.__dict__['静态变量'] = 456  # 报错
# print(Person.__dict__['静态变量'])

# 查看静态变量的第二种方式
# print(Person.静态变量)   # 123 值
# print(Person.role)
# Person.静态变量 = 456
# print(Person.静态变量)
# del Person.静态变量
# print(Person.__dict__)
# 类名
    # 引用静态变量
        # 1.类名.__dict__['静态变量名'] 可以查看，但是不能删改
        # 2.类名.静态变量名 直接就可以访问,可以删改
                # 删除一个静态变量 del 类名.静态变量名
    # 引用动态变量
        # 1.类名.方法名  查看这个方法的内存地址
        # 1.类名.方法名(实参)  调用了这个方法，必须传一个实参，这个实参传给了self
    # 创造一个对象 - 实例化
        # 产生一个实例（对象）的过程
        # 对象 = 类名()
# alex = Person()   # 创造一个对象
# alex 是对象、实例
# Person是类
# 对象 = 类名()

# class Person:
#     role = 'person'   # 静态属性
#     def __init__(self,name,sex,hp,ad):
#         self.name = name     # 对象属性 属性
#         self.sex = sex
#         self.hp = hp
#         self.ad = ad
#     def attack(self):
#         print('%s发起了一次攻击'%self.name)
#
# alex = Person('a_sb','不详',1,5)
# boss_jin = Person('金老板','女',20,50)
#
# alex.attack()      # Person.attack(alex)
# boss_jin.attack()  # Person.attack(boss_jin)
class Person:
    def __init__(self,name,sex,hp,ad):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.ad = ad
    def attack(self,ppp):
        print('%s对%s发起了攻击,%s掉了%s血' % (self.name,ppp.name,ppp.name,self.ad))
        ppp.hp -= self.ad
        if ppp.hp <= 0:
            print('%s win' % self.name)
class Person2:
    # ret = 'nihao'
    def __init__(self,name,sex,hp,ad):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.ad = ad
    def dog(self,people):
        print('%s咬了%s一口,%s掉了%s血' % (self.name,people.name,people.name,self.ad))
        people.hp -= self.ad
        if people.hp <= 0:
            print('%s win' % self.name)
moumou = Person('策哥','男',10,50)
gou = Person2('旺财','tebby',10,20)
# moumou.attack(gou)
# print(gou.hp)
gou.dog(moumou)
print(moumou.hp)
# gou.dog(moumou)
# print(moumou.hp)
# moumou.attack(gou)
# print(gou.hp)
# alex['anme']()


# alex = Person('a_sb','不详',1,5)
# alex.__dict__['name'] = 'alex'
# print(alex.name)
# alex.name = 'a_sb'
# print(alex.name)
# boss_jin = Person('金老板','女',20,50)
# print(boss_jin.name)
# 实例化的过程：
    # 1.创造一个实例,将会作为一个实际参数  # python
    # 2.自动触发一个__init__的方法，并且把实例以参数的形式传递给__init__方法中的self形参
    # 3.执行完__init__方法之后，会将self自动返回给alex
# __init__方法 ：初始化方法，给一个对象添加一些基础属性的方法，一般情况下是针对self的赋值
# 对象
    # 在类的内部 self是本类的一个对象
    # 在类的外部，每一个对象都对应着一个名字，这个对象指向一个对象的内存空间
    # 属性的调用：
        # 对象名.属性名               第一种调用方法
        # 对象名.__dict__['属性名']   第二种调用方法
    # 方法的调用 ：
        # 类名.方法名(对象名)  # 那么方法中的self参数就指向这个对象
        # 对象名.方法名()      # 这样写 相当于  方法中的self参数直接指向这个对象
