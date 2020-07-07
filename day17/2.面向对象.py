# 参加工作
# 游戏公司
# 人狗大战
# 角色 的属性固定下来
# 人 ：昵称、性别、血、攻击力
# 狗 ：名字、品种、血、攻击力
# def Person(name,sex,hp,ad):
#     # 人模子
#     self = {'name': name, 'sex':sex, 'hp': hp, 'ad': ad}
#     def attack(dog): # 闭包
#         # 人攻击狗
#         print('%s攻击%s' % (self['name'], dog['name']))
#         # 狗掉血，狗的血量-人的攻击力
#         dog['hp'] -= self['ad']
#     self['attack'] = attack
#     return self
#
# def Dog(name,kind,hp,ad):
#     # 狗模子
#     self = {'name': name, 'kind':kind, 'hp': hp, 'ad': ad}
#     def bite(person):
#         print('%s咬了%s' % (self['name'], person['name']))
#         # 人掉血，人的血量-狗的攻击力
#         person['hp'] -= self['ad']
#         if person['hp'] <= 0: print('game over,%s win' % self['name'])
#     def bite2():pass
#     self['bite'] = bite
#     self['bite2'] = bite2
#     return self
#
# # 人 规范了属性的个数 简化了创造人物的代码
# alex = Person('a_sb','不详',1,5)
# boss_jin =Person('金老板','女',2,50)
#
# # 狗
# chen = Dog('旺财','teddy',50,20)
# alex['attack'](chen)
# print(chen['hp'])

# 面向对象编程
# 类的概念 ： 具有相同属性和技能的一类事物
#  人类 抽象
# 对象 ： 就是对一个类的具体的描述
#  具体的人 具体

# 使用面向对象的好处：
    # 使得代码之间的角色关系更加明确
    # 增强了代码的可扩展性
    # 规范了对象的属性和技能
# 面向对象的特点：结局的不确定性

# 人类
# 狗类

# 购物
# 商品 ：名字 类别 价格 产地 保质期 编号
    # 苹果 生鲜类 5块钱  --- 对象
# 人 ：
# from math import pi
# class Person:
#     perimeterl = 1
#     area = 1
#     def __init__(self,radius):
#         self.radius = radius
#         # self.pi = pi
#     def perimeter(self):
#         return 2*pi*self.radius
#         # print(self.na)
# p = Person(1)
# print(p.perimeter())
