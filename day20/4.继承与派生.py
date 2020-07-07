class Animal:
    def __init__(self,name,hp,ad):
        self.name = name     # 对象属性 属性
        self.hp = hp         #血量
        self.ad = ad         #攻击力
    def eat(self):
        print('eating in Animal')
        self.hp += 20

class Person(Animal):
    def __init__(self,name,hp,ad,sex):        # 重写
        # Animal.__init__(self,name,hp,ad)
        # super(Person,self).__init__(name,hp,ad)   # 在单继承中，super负责找到当前类所在的父类，在这个时候不需要再手动传self
        super().__init__(name,hp,ad)   # 在单继承中，super负责找到当前类所在的父类，在这个时候不需要再手动传self
        self.sex = sex      # 派生属性
        self.money = 100
    def attack(self,dog):   # 派生方法
        print("%s攻击了%s"%(self.name,dog.name))
    def eat(self):                         # 重写
        super().eat()  # 在类内 使用 super()方法找父类的方法
        print('eating in Person')
        self.money -= 50

class Dog(Animal):
    def __init__(self,name,hp,ad,kind):
        Animal.__init__(self,name,hp,ad)
        self.kind = kind    # 派生属性
    def bite(self,person):  # 派生方法
        print("%s咬了%s" % (self.name, person.name))

# 人 sex
alex = Person('alex',100,10,'female')   # 实例化
print(alex.__dict__)

# 父类有eat 子类没有
# alex.eat() # 找父类的
# 子类有eat 不管父类中有没有
# alex.eat() # 找子类的
# 当子类中有，但是我想要调父类的
# Animal.eat(alex)          #指名道姓
# super(Person,alex).eat()  # super(子类名,子类对象)方法   —— 一般不用
# 子类父类都有eat方法，我想执行父类的eat和子类的eat
alex.eat()  # 执行子类的eat
print(alex.__dict__)
#
# 对象
# Person.attack(alex)   # alex.attack()

# 狗 kind
# tg = Dog('到哥',100,50,'藏獒')
# print(tg.__dict__)