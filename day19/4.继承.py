# 面向对象的三大特性
    # 继承  1.8天
    # 多态  0.2天
    # 封装  1天

# 初识继承

# 游戏
# 人物 ： 名字 角色 性别 职业 技能
#     治疗 # 回血 增加属性
#         医生
#         护士
#     输出
#     防御

# class Person:
#     def __init__(self,name,hp,ad):
#         self.name = name     # 对象属性 属性
#         self.hp = hp         #血量
#         self.ad = ad         #攻击力
#
# class Dog:
#     def __init__(self,name,hp,ad):
#         self.name = name
#         self.hp = hp
#         self.ad = ad

# 类与类之间的关系： 什么是什么的关系
# 单继承
# class Parent:pass
# class Son(Parent):pass   # 继承关系
#     # Son继承了Parent
# print(Son.__bases__)  # 内置的属性           (<class '__main__.Parent'>,)
# print(Parent.__bases__)  # 内置的属性        默认的(<class 'object'>,)

# 在python3中，所有的类都会默认继承object类
# 继承了object类的所有类都是新式类
# 如果一个类没有继承任何父类，那么__bases__属性就会显示<class 'object'>

# 多继承
# class Parent1:pass
# class Parent2:pass
# class Parent3:pass
# class Son(Parent1,Parent2,Parent3):pass   # 继承关系
# print(Son.__bases__)

# 父类 ：基类 超类
# 子类 ：派生类
class Animal:
    role = 'Animal'
    def __init__(self,name,hp,ad):
        self.name = name     # 对象属性 属性
        self.hp = hp         #血量
        self.ad = ad         #攻击力

    def eat(self):
        print('%s吃药回血了'%self.name)

class Person(Animal):
    r = 'Person'
    def attack(self,dog):   # 派生方法
        print("%s攻击了%s"%(self.name,dog.name))

    def eat2(self):
        print('执行了Person类的eat方法')
        self.money = 100
        self.money -= 10
        self.hp += 10

class Dog(Animal):
    def bite(self,person):  # 派生方法
        print("%s咬了%s" % (self.name, person.name))

# 先有了人 狗两个类
# 发现两个类有相同的属性、方法
# 人和狗 都是游戏里的角色
# 抽象出一个animal类型
# 继承

# 继承中的init
# alex = Person('alex',10,5)
# print(Person.__dict__)   # role
# print(Person.role)
# print(alex.__dict__)
# dog = Dog('teddy',100,20)
# print(dog)
# print(dog.__dict__)

# 继承中的派生方法
# alex = Person('alex',10,5)
# dog = Dog('teddy',100,20)
# alex.attack(dog)
# dog.bite(alex)

# 继承父类的方法：自己没有同名方法
# alex = Person('alex',10,5)
# dog = Dog('teddy',100,20)
# alex.eat2()
# alex.eat()
# dog.eat()

# 对象使用名字的顺序: 先找对象自己内存空间中的，再找对象自己类中的，再找父类中的
# alex = Person('alex',10,5)
# alex.eat = 'aaa'
# print(alex.eat())  # 报错

# self.名字的时候，不要看self当前在哪个类里，要看这个self到底是谁的对象
class Parent:
    def func(self):
        print('in parent func')
    def __init__(self):
        self.func()

class Son(Parent):
    def func(self):
        print('in son func')

s = Son()



# 作业 ：
# 读博客
# 把实例全走一遍
# 默写 圆环类与圆类组合

