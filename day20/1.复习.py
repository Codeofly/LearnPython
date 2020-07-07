# 关于作业
    # 1.以后都是大作业 ：
        # 找到多有的类
        # 给所有的类设计属性
        # 组合关系
        # 登陆怎么做？程序的流程？
    # 2.面试题 概念 课上都会说
    # 3.考试

# 组合 什么有什么的关系
# class Birthday:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def fmt(self):
#         return '%s-%s-%s'%(self.year,self.month,self.day)
# class Teacher:
#     def __init__(self,name,birth):
#         self.name = name
#         self.birthday = birth
#     def birth_month(self):
#         self.birthday.fmt()  # 引用组合对象的方法
#         return self.birthday.month  # 引用组合对象的属性
# class Teacher2:
#     def __init__(self,name,birth):
#         self.name = name
#         self.birthday_year = 1968
#         self.birthday_month = 4
#         self.birthday_day = 13
#
# # 老师有生日
# birth = Birthday(1968, 4, 13)
# alex = Teacher('alex',birth)
# birth.year
# alex.birthday.year   # 调用组合对象中的属性
# print(birth.fmt())
# print(alex.birthday.fmt())  #调用组合对象中的方法


# 继承
# 猫
    # 属性 性别 品种
    # 方法 吃 喝 爬树
# 狗
    # 属性 性别 品种
    # 方法 吃 喝 看门
class Animal:
    def __init__(self,name,sex,kind):
        self.name = name
        self.sex = sex
        self.kind = kind
    def eat(self):
        print('%s is eating'%self.name)

    def drink(self):
        print('%s is drinking'%self.name)

class Cat(Animal):
    def climb(self):
        print('%s is climbing'%self.name)

class Dog(Animal):
    def watch_door(self):
        print('%s is watching door'%self.name)

# 1.确认自己没有init方法
# 2.看看有没有父类
# 3.发现父类Animal有init
# 4.看着父类的init方法来传参数
tom = Cat('tom','公','招财猫')   # 实例化对象
# tom.eat = '猫粮'
print(Cat.__dict__)   # Cat.__dict__ Cat类的命名空间中的所有名字
print(tom.__dict__)   # tom.__dict__ 对象的命名空间中的所有名字
tom.eat()   # 先找自己对象的内存空间 再找类的空间 再找父类的空间
tom.climb()   # 先找自己的内存空间 再找类的空间

