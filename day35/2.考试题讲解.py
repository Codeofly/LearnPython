# 一 基础知识：（70分）
# 1.文件操作有哪些模式？请简述各模式的作用（2分）

# 2.详细说明tuple、list、dict的用法，以及它们的特点（3分）
# list用于存储一组数据，例如 一组名字 一组数字 类似容器，可以表示多种数据的有序的序列
# tuple就是不可变的列表，用来描述不能改变的数据 类似 动态传入参数 函数多个返回值 一些有特定个数的 不该被改变的例如 表示星期 点的坐标等
# dict 是用于存储有关系的一组一组数据的，方便快速根据key查找value的 无序的 key不能重复的 一组数据

# 3.解释生成器函数（generator）与普通函数的不同，并实现且使用简单generator（3分）
# 生成器 和 函数有关系么？
# 生成器函数 本质是函数
# 生成器函数调用之后这个函数不执行，返回的结果是一个生成器，生成器也是迭代器
# 函数调用之后，内部的代码立即执行，返回一个函数的返回值
def func(): yield 1

# 4.如何理解lambda函数/表达式（2分）
# 能够实现一些简单的功能的函数、可以和内置函数配合着使用
def func(a,b): return a if a>b else b


# 5.a=10
#   b=20
#   def test5(a,b):
#      print(a,b)
#   c = test(b,a)
#   print(c)
#   上述代码中,打印出来的值a,b,c分别是什么？为什么？（4分）

# 6. 描述一下@property是做什么用的，简单写一个实例并执行（4分）
# 将一个方法伪装成一个属性
class A:
    @property
    def name(self):
        return 'alex'
a = A()
print(a.name)

# 7.d={'k1':'v1','k2’:[1,2,3],(‘k’,’3’):{1，2，3}}（4分）
#   请用程序实现：
#   1）输出上述字典中value为列表的key（2分）
#   2）如果字典中的key是一个元祖，请输出对应的value值。（2分）
#   3）d[('k','3')]对应的value是一个什么数据类型（1分）
# d={'k1':'v1','k2':[1,2,3],('k','3'):{1,2,3}}
# for item in d:
#     if type(d[item]) is list:print(item)
# for item in d:
#     if type(item) is tuple:print(d[item])


# 8.如果不使用@wrapper装饰器，请在a()之前加入一句代码，达到相同的效果（2分）
# def wrapper(func):
#     def inner(*arg, **kwargs):
#         func(*arg, **kwargs)
#     return inner
#
# # @wrapper
# def a(arg):
#     print(arg)
# # a = wrapper(a)
# a()

# 9.请处理文件7th_questions,输出所有以'T'开头的行（5分）
# startswith

# 10.读登陆文件夹中的代码，请为这段代码画流程图（8分）

# 11 默写10个字符串对象的方法，描述它的作用（5分）

# 12.有如下代码，写出调用的顺序以及结果（5分）
# def f1():
#     print('funcname is f1')
#
# def f2():
#     print('funcname is f2')
#     return 1
#
# def f3(func1):
#     ll = func1()
#     print('funcname is f3')
#     return ll
# #
# print(f3(f2))
# 
# 13. 创建一个闭包函数需要满足哪几点？（2分）
# 内部函数 使用 外部函数的变量

# 14.将时间打印出成一个2017/10/01 18:08:15的格式（3）
import time
time.strftime('%Y/%m/%d %H:%M:%S')
#   将 "2017-11-18" 17:43:43" 转换为结构化时间
time.strptime("2017-11-18 17:43:43",'%Y-%m-%d %H:%M:%S')

# 15.用什么模块能知道文件夹存不存在？(1)   os.path.isdir
#     怎么获取这个文件夹的大小？(2)
    # 遍历这个文件夹 对这个文件夹下的文件进行累加计算
    # os.path.getsize

# 16 简单解释Python中static method（静态方法）和class method（类方法）(2)
#  两个都不需要实例化就可以直接用类名调用
#  静态方法不应该引用实例或者类中的属性，类方法应该引用类中的变量但不能引用实例的属性
#  类方法需要有一个cls默认参数，静态方法没有默认参数

# 17．请描述一下__new__方法和__init__的区别以及是做什么的（2）
# __new__方法 创建一个对象
# __init__方法 给一个对象添加一些初始化属性

# 18. 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？（编程题）(5)
# l = [1,2,3,4]
# new_l = []
# for i in l:
#     for j in l:
#         for k in l:
#             if i!=j and j!=k and i!=k:
#                 new_l.append('%s%s%s'%(i,j,k))
# print(len(new_l),new_l)

# 19.有这个一个test2文件，文件中模拟一个网站的页面定义了多个函数，现在有个需求是不使用if，else条件语句，进行判断我想访问那个页面
# 例如：
# 请输入你要访问的url>>>：login
# 他就提示我们   ----  这是一个登陆页面！说明登陆成功了
# 反射
# import test2
# fun_name = input('url>>>：')
# if hasattr(test2,fun_name):
#     getattr(test2,fun_name)()


# 20.实现一个发红包的编程题（使用random）编程题
import random
# def hongbao():
#     try:
#         money = int(input('请输入红包的钱数'))
#         num = int(input('请输入红包个数'))
#     except Exception:
#         return '请正确输入'
#     p=0
#     l=[]
#     for i in range(num-1):   #20
#         p=random.uniform(0,money-p)   # 0-200
#         l.append(p)
#     p=money-sum(i for i in l)
#     l.append(p)
#     random.shuffle(l)
#     return l
# print(hongbao())

# import random
# def Money(money, num):
#     n = 1
#     if num == 1:
#         print('获得了%s' % money)
#     while num > n:
#         my_money = round(random.uniform(0.01, money),2)
#         money = money - my_money
#         print('获得了%s' % my_money)
#         if n == num - 1:
#             print('获得了%s' % money)
#         if money < 0:
#             break
#         n += 1
# Money(200,20)

# def redbag(money,count):
#     d = []
#     for x in range(count):
#         d.append(random.randint(0, 100))
#     print(d)
#     rand_sum = sum(d)
#     print(rand_sum)
#     new_l = []
#     for x in d:
#         new_l.append(round(x/rand_sum*money,2))
#     new_l[-1] = round(money - sum(new_l[:-1]),2)
#     return new_l
# print(redbag(200,20))

# import random
# inp_money = float(input('红包金额：'))
# inp_count = int(input('红包个数：'))
# def red_packet(money, count):
#     li = []
#     money = int(money*100)         # 以分为单位的钱的总数   2000 10
#     money_site = random.sample(range(1, money), count-1)   #[1,2,3,4,5,6,7,8,9]
#     money_site.extend([0, money])  # [1,2,3,4,5,6,7,8,9,0,2000]
#     money_site = sorted(money_site)  # 排了个序
#     for i in range(count):  # 0-9  [0,1,2,3,4,5,6,7,8,9,2000] 19.91
#         li.append(round((money_site[i+1]-money_site[i])*0.01, 2))
#     print(sum(li))
#     return li
# ret = red_packet(inp_money, inp_count)
# print(ret)

# import random
# def redpacket(money, person):
#     '''
#     发红包函数
#     :param money: 红包总额
#     :param person: 抢红包人数
#     :return: 其实只返回了最后一次的红包金额，之前的都print打印输出了
#     '''
#     while person > 0:
#         if person == 1:
#             # 当人数为1时，他拿走余下的所有钱
#             return round(money, 2)
#             # 反之，当钱不为0和人数不为1时，随机发红包
#         elif money > 0 and person != 1:
#             # 红包最大金额应为红包总金额减去最小值(0.01)乘以人数，这样才能保证大家都有得抢
#             max_money = round(random.uniform(0.01, money - (0.01*person)), 2)
#             print(max_money)
#             # 人数递减
#             person -= 1
#             # 金额递减
#             money -= max_money
#             # 递归再去实现随机发红包
#             return redpacket(money, person)
#
# print(redpacket(100,6))

# 二 面向对象（30分）
# 
# 1.请简述类、对象、实例化、实例这些名词的含义（2分）
# 2.面向对象的三大特性是什么？（3分）
# 3.有一个类定义：（5分）
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

#     1）初始化10个不同的对象（2）
obj_l = []
for i in range(10,20):
    obj_l.append(Person('egg%s'%i,i))
#     2）求最高age的对象的name（3）
ret = max(*obj_l,key=lambda obj: obj.age)
print(ret.name)

# 4. 模拟cs游戏（15分）
# 	1）人物角色分为警察和匪徒两种，定义成两个类（10分）
# 
# 		所有的警察的角色都是police
# 		每个警察都有自己独有名字，生命值，武器，性别
# 		每个都可以开枪攻击敌人，切攻击目标不能是police
# 
# 
# 		所有的警察的角色都是terrorist
# 		每个匪徒都有自己独有名字，生命值，武器，性别
# 		每个都可以开枪攻击敌人，切攻击目标不能是terrorist
# 
# 	2）实例化一个警察，一个匪徒，警察攻击匪徒，匪徒掉血（2分）
# 
# 	3）提取警察类和匪徒类相似之处定义成一个父类，使用继承的方式减少代码重复（3分）
# 
# 5 读代码（10分）
# 
# 5（1）
class Base:
    def f1(self):
        self.f2()

    def f2(self):
        print('...')

class Foo(Base):
    def f2(self):
        print('9999')

obj = Foo()
obj.f1()
# 
# 问题1:面向对象中的self指的什么？（2分）  self --> Foo
# 问题2:运行结果并简述原因（3分） 9999
# 
# 
# 5（2）
# class JustCounter:
#    __secretCount = 0
#
#    def count(self):
#        self.__secretCount += 1
#        print(self.__secretCount)
#
# class Bars(JustCounter):
#
#     def count(self):
#         print(self.__secretCount)
#
#
# counter1 = JustCounter()
# counter2 = Bars()
# #
# counter1.count()
# counter2.count()
# print (counter1._JustCounter__secretCount)
# print (JustCounter._JustCounter__secretCount)

# 问题1:简述counter1.count()执行流程？（2分）
# 问题2:运行结果并简述原因（3分）


# 附加思考题（20分）：
#     有一个类的init方法如下：
#     class Person：
#         def __init__(self,name,age,sex,weight):
#             self.name = name
#             self.sex = sex
#             self.age = age
#             self.weight = weight
#     假设有100个person的对象，
#     若两个对象的obj1,obj2的name和sex属性相同
#     即obj1.name==obj2.name and obj1.sex==obj2.sex
#     我们认为两个对象为同一个对象，已知一个列表中的100个对象，对这100个对象进行去重。
#     提示：
#         重写Person类重的两个内置方法
