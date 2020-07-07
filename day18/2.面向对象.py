class Person:
    role = 'person'   # 静态属性
    def __init__(self,name,sex,hp,ad):
        self.name = name     # 对象属性 属性
        self.sex = sex
        self.hp = hp         #血量
        self.ad = ad         #攻击力
    def attack(self,d):
        d.hp -= self.ad
        print('%s攻击了%s，%s掉了%s点血'%(self.name,d.name,d.name,self.ad))

class Dog:
    def __init__(self,name,kind,hp,ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad
    def bite(self,p):
        p.hp -= self.ad
        print('%s咬了%s一口,%s掉了%s点血' % (self.name, p.name, p.name, self.ad))

alex = Person('a_sb','不详',1,5)
boss_jin = Person('金老板','女',20,50)
teddy = Dog('笨笨','teddy',50,10)
teddy.bite(alex)
print(alex.hp)
boss_jin.attack(teddy)
print(teddy.hp)

# alex.attack()      # Person.attack(alex)
# boss_jin.attack()  # Person.attack(boss_jin)

# 人和狗
# 4个技能 玩家可以选择技能
