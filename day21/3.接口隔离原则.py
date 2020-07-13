# 什么叫接口
# python里没有接口的概念
# 那接口是哪儿来的概念呢？# java类没有多继承 接口可以实现多继承
# 描述动物园
# 会游泳的 会走路的 会爬树的 会飞的
# 老虎
# 青蛙
# 天鹅
# 猴子
from abc import ABCMeta,abstractmethod
class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):pass
    @abstractmethod
    def cal_flying_speed(self):pass
    @abstractmethod
    def cal_flying_height(self):pass
class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):pass
class SwimAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):pass
class Tiger(WalkAnimal,SwimAnimal):
    def walk(self):pass
    def swim(self):pass
class Monkey:
    def walk(self):pass
    def climb(self):pass
class Swan(FlyAnimal,WalkAnimal,SwimAnimal):
    def swim(self):pass
    def walk(self):pass
    def fly(self):pass
    def cal_flying_speed(self):pass
    def cal_flying_height(self):pass
class Parrot(FlyAnimal):
    def fly(self):pass
    def cal_flying_speed(self):pass
    def cal_flying_height(self): pass
# 所有会飞的动物 具有一些会飞的动物的特性
# 所有会走的动物 具有一些会走的动物的特性

# 接口类的作用：
    # 在java中，能够满足接口隔离原则，且完成多继承的约束
    # 而在python中，满足接口隔离原则，由于python本身支持多继承，所以就不需要接口的概念了

# 抽象类和接口类
# 在python中
    #并没有什么不同，都是用来约束子类中的方法的
    #只要是抽象类和接口类中被abstractmethod装饰的方法，都需要被子类实现
    #需要注意的是，当多个类之间有相同的功能也有不同的功能的时候，应该采用多个接口类来进行分别的约束

# 在java中
    # 抽象类和接口截然不同
    # 抽象类的本质还是一个类 是类就必须遵循单继承的规则，所以一个子类如果被抽象类约束，那么它只能被一个父类控制
    # 当多个类之间有相同的功能也有不同的功能的时候 java只能用接口来解决问题

# 面试的时候
    # 抽象类 是python中定义类的一种规范
    # 接口
# 在公司类写代码的时候
    # 如果遇到抽象类 记得按照抽象类中的规范一一实现对应的方法，