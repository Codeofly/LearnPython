# 组合 一个类的对象作为另一个类对象的属性
# 表示的 一种 什么有什么的关系

# 人狗大战
class Person:
    def __init__(self,name,sex,hp,ad,age):
        self.name = name     # 对象属性 属性
        self.sex = sex
        self.hp = hp         #血量
        self.ad = ad         #攻击力
        self.money = 0


    def attack(self,d):
        d.hp -= self.ad
        print('%s攻击了%s，%s掉了%s点血'%(self.name,d.name,d.name,self.ad))
    def pay(self):
        money = int(input('请输入您要充值的金额: '))
        self.money += money
        print('您的余额是：%s'%self.money)
    def wear(self,weapon):
        # 武器
        if self.money >= weapon.price:
            # 武器类的对象作为人类对象的一个属性
            self.weapon = weapon   # 组合 给人装备了武器
            self.money -= weapon.price
            print('购买成功，您已经顺利装备了%s'%weapon.name)
        else:
            print('余额不足，请充值。')
    def attack_with_weapon(self,dog):
        if 'weapon' in self.__dict__:
            self.weapon.skill(dog)
        else:
            print('请先装备武器')

class Dog:
    def __init__(self,name,kind,hp,ad):
        self.name = name
        self.kind = kind
        self.hp = hp
        self.ad = ad
    def bite(self,p):
        p.hp -= self.ad
        print('%s咬了%s一口,%s掉了%s点血' % (self.name, p.name, p.name, self.ad))

class Weapon:
    def __init__(self,name,price,ad,level):
        self.name = name
        self.price = price
        self.level = level
        self.ad = ad * self.level

    def skill(self,dog):
        dog.hp -= self.ad
        print('%s受到了%s的伤害，%s掉了%s点血'%(dog.name,self.name,dog.name,self.ad))

# 武器 是人的一个属性
# 武器也是一个类
    # 攻击力 价格 名字 品级
    # 技能 : 方法

# alex = Person('a_sb','不详',1,5)
# boss_jin = Person('金老板','女',20,50)
# teddy = Dog('笨笨','teddy',150,50)
# futou = Weapon('斧头',1000,100,1)
# nife = Weapon('刀',1000,100,1)
#
# alex.weapon = '123'
# alex.b1 = nife
# alex.b2 = futou
# print(alex.__dict__)
# alex.b.skill()
# 为什么会用组合 ：独立的对象不能发挥他的作用，必须依赖一个对象

# alex.pay()
# alex.wear(futou)
# print(alex.__dict__)
# print(alex.weapon)
# print(futou)
# # print(alex.weapon is futou)
# futou.skill(teddy)
# alex.weapon.skill(teddy)

# 武器 装备
# lst = ['攻击','充值','装备武器','使用武器攻击']
# while True:
#     for index, value in enumerate(lst, 1):
#         print(index, value)
#     num = int(input('请选择操作序号 >>>'))
#     if num == 1:
#         alex.attack(teddy)
#     elif num == 2:
#         alex.pay()
#     elif num == 3:
#         print('装备前余额 %s'%alex.money)
#         alex.wear(futou)
#         print('装备后余额 %s' % alex.money)
#     elif num == 4:
#         alex.attack_with_weapon()
#     else:
#         print('无效的序号')





