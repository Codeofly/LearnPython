# 写一个类 定义100个对象
# 拥有三个属性 name age sex
# 如果两个对象的name 和 sex完全相同
# 我们就认为这是一个对象
# 忽略age属性
# 做这100个对象的去重工作
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __hash__(self):
        # hash算法本身就存在了 且直接在python中就能调用
        # 姓名相同 性别相同的对象的hash值应该相等才行
        # 姓名性别都是字符串
        return hash(self.name+self.sex)
    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True
# python2.7
# 去重 set
# hash方法
# set([obj,obj])   unhashable
# hash算法  一个值 进行一系列的计算得出一个数字在一次程序执行中总是不变
            #来让每一个不同的值计算出的数字都不相等
obj_lst = []
obj_lst.append(Person('alex',80,'male'))
obj_lst.append(Person('alex',70,'male'))
obj_lst.append(Person('alex',60,'male'))
obj_lst.append(Person('boss_jin',50,'male'))
obj_lst.append(Person('boss_jin',40,'male'))
obj_lst.append(Person('boss_jin',30,'male'))
obj_lst.append(Person('nezha',20,'male'))
obj_lst.append(Person('nezha',10,'male'))
obj_lst = set(obj_lst)
for obj in obj_lst:print(obj.name)
# set对一个对象序列的去重 依赖于这个对象的两个方法 hash eq


# 可hash顺带着写的
# eq来做判断

# key hash 数字 --》 内存地址 --》 value
# set hash 数字 --》 内存地址 --》 set中的元素
# 'aaa' hash

# java
# set去重 一个容器中 有相同值的内容  __eq__
# 当你这个容器中有10000个元素的时候 我判断第10000个元素
# hash算法
    # 'abc'
    # 'bca'
# set对一个对象序列的去重 如何判断这两个值是否相等
# 值a进行hash --> 存值
# 值b进行hash --> 判断值是否相等 -相等-> 说明是一样的
                                #-不相等-> 在开辟一个空间 来存放b



