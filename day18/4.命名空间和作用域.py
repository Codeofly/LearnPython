# class Person:
#     role = 'person'   # 静态属性
#     def __init__(self,name,sex,hp,ad):
#         self.name = name     # 对象属性 属性
#         self.sex = sex
#         self.hp = hp
#         self.ad = ad
#     def attack(self):
#         self.hobby = 'girl'
#         print('%s发起了一次攻击'%self.name)
#
# alex = Person('a_sb','不详',1,5)
# alex.attack()   # Person.attack(alex)
# alex.age = 81
# # alex --> Person
# # Person实例化了alex
# print(alex.__dict__)

# alex.name   #alex 指向我自己的内存空间 在自己的内存空间里找到name
# alex.attack #alex 先找自己的内存空间 再找到类对象指针 再根据类对象指针找到类 再通过类找到attack
# 对象的内存空间里: 只存储对象的属性，而不存储方法和静态属性
# 方法和静态属性都存储在类的内存空间中
# 为了节省内存，让多 个对象去共享类中的资源


# class Person:
#     role = 'person'   # 静态属性
#     def __init__(self,name,sex,hp,ad):
#         self.name = name     # 对象属性 属性
#         self.sex = sex
#         self.hp = hp
#         self.ad = ad
#         self.attack = 'hahaha'
#     def attack(self):
#         print('%s发起了一次攻击'%self.name)
#
# alex = Person('a_sb','不详',1,5)
# boss_jin = Person('金老板','女',50,20)
# print(alex.role)
# print(boss_jin.role)
# alex.role = 'dog'
# print(alex.role)
# print(boss_jin.role)    # dog or ? person



# class Person:
#     role = 'person'   # 静态属性
#     def __init__(self,name,sex,hp,ad):
#         self.name = name     # 对象属性 属性
#         self.sex = sex
#         self.hp = hp
#         self.ad = ad
#         self.attack = 'hahaha'
#     def attack(self):
#         print('%s发起了一次攻击'%self.name)
#
# alex = Person('a_sb','不详',1,5)
# boss_jin = Person('金老板','女',50,20)
# print(alex.role)
# print(boss_jin.role)
# alex.role = 'dog'
# print(alex.role)
# 模拟人生
# class Person:
#     money = 0
#     def __init__(self,name):
#         self.name = name
#     def work(self):
#         print(self.name,'工作,赚了1000块钱')
#         Person.money += 1000
#
# father = Person('father')
# mother = Person('mother')
# mother.work()
# father.work()
# print(Person.money)


# 写一个类 完成一个功能 ： 可以统计这个类有几个对象
# class Foo:
#     count = 0
#     def __init__(self):
#         Foo.count += 1
# f1 = Foo()
# f2 = Foo()
# f3 = Foo()
# f4 = Foo()
# f5 = Foo()
# print(Foo.count)  #



class Person:
    money = 0
    def __init__(self,name):
        self.name = name
    def work(self):
        print(self.name,'工作,赚了1000块钱')
        self.money += 1000

father = Person('father')
mother = Person('mother')
mother.work()
father.work()
print(Person.money)   # 2000 or 0?

# class Person:
#     money = [0]
#     def __init__(self,name):
#         self.name = name
#     def work(self):
#         print(self.name,'工作,赚了1000块钱')
#         Person.money =  [Person.money[0] + 1000]
#
# father = Person('father')
# mother = Person('mother')
# mother.work()
# father.work()
# print(Person.money)

# 对象属性是独有的，静态属性和方法是共享的
# 对象使用名字：先找自己内存空间中的，再找类的内存空间中的
# 类名.静态变量名 ：对于静态属性的修改，应该使用类名直接修改










