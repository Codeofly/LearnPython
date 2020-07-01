#day8
# 3. 文件a1.txt内容：每一行内容分别为商品名字，价钱，个数。
# 文件内容：
# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
#
# 通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3},
# {'name':'tesla','price':1000000,'amount':1}......]
# 并计算出总价钱。
# l1 = []
# with open('a1.txt',encoding='utf-8') as f1:
#     for i in f1:
#         li = i.strip().split()
#         dic = {}
#         for j in li:
#             l2 = j.strip().split(':')
#             dic[l2[0]] = l2[1]
#         l1.append(dic)
# print(l1)
# 4,文件a2.txt内容：每一行内容分别为商品名字，价钱，个数。
# 文件内容：
# 序号     部门      人数      平均年龄      备注
# 1       python    30         26         单身狗
# 2       Linux     26         30         没对象
# 3       运营部     20         24         女生多
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'},
# ......]
# 并计算出总价钱。
# l1 = []
# with open('a1.txt',encoding='utf-8') as f1:
#     list_name = f1.readline().strip().split()
#     for i in f1:
#         for j in li:
#             l2 = j.strip().split(':')
#             pass
#         l1.append(dic)
# print(l1)

#day10
# 3、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a = 10
# b = 20
#
# def test5(a,b):
#     print(a,b)
#
# c = test5(b,a)
# print(c)


# 4、读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#     a=3
#     b=5
#     print(a,b)
# c = test5(b,a)
# print(c)
#
#
#
#
# 相关面试题（先从纸上写好答案，然后在运行）：
# 1，有函数定义如下：
# def calc(a,b,c,d=1,e=2):
#     return a+b+c+d+e
# print(calc(1,2,3,4,5))  # 9 15
# print(calc(1,2))  error
# print(calc(e=4,c=5,a=2,b=3))  # 15
# print(calc(1,2,3))  # 9
# print(calc(1,2,3,e=4))  # 11
# print(calc(1,2,3,d=5,4))  # error
# 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1,2,3,4,5))_____ print(calc(1,2))____print(calc(e=4,c=5,a=2,b=3))___
# print(calc(1,2,3))_____ print(calc(1,2,3,e=4))____print(calc(1,2,3,d=5,4))_____
# 2，下面代码打印的结果分别是_________,________,________.


# def extendList(val,list=[]):
#     list.append(val)
#     return list

#默认参数为可变数据类型时，使用的是同一个。

# list1 = extendList(10)  # []
# # print('list1=%s'%list1) # [10,]
# # list2 = extendList(123,[])  # [123,]
# # print('list2=%s'%list2)
# # list3 = extendList('a') # [10,’a']
# # print('list3=%s'%list3)
# # print('list1=%s'%list1)
#
# # day9
# # 9、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（进阶）。
# import os
# # with open('log',encoding='utf-8') as f1,\
# #     open('log.bak',encoding='utf-8',mode='w') as f2:
# #     for i in f1:
# #         new_i = i.replace('SB','alex')
# #         f2.write(new_i)
# # os.remove('log')
# # os.rename('log.bak','log')
#
# def File_modification(path,old,new):
#     with open(path, encoding='utf-8') as f1, \
#             open(path+'.bak', encoding='utf-8', mode='w') as f2:
#         for i in f1:
#             new_i = i.replace(old, new)
#             f2.write(new_i)
#     os.remove(path)
#     os.rename(path+'.bak', path)
#     return True
# print(File_modification('log','alex','SB'))
#
#
# # 10、写一个函数完成三次登陆功能，再写一个函数完成注册功能(进阶)
#
# #注册
# #用户输入用户名，密码
# #检测用户名不相同
# #用户名正确，写入文件用户名密码
##先让用户选择，是登陆还是注册
#选择序号完毕之后，运行相应的程序，
#验证成功之后，可以让其继续选择，登陆还是注册，还可以选择退出。
def register(*args,**kwargs):
    flag = True
    while flag:
        username = input('请输入注册的用户名：').strip()
        with open('register_msg',encoding='utf-8') as f1:
            for i in f1:
                li = i.strip().split()  # [张三，123]
                if username == li[0] or username == '' :
                    print('用户名已存在，请重新注册')
                    break
            else:
                password = input('请输入您注册的密码：')
                with open('register_msg',encoding='utf-8',mode='a') as f2:
                    f2.write('\n{}\t{}'.format(username,password))
                    print('注册成功')
                    flag = False
def login(*args,**kwargs):
    while True:
        name = input('请输入登录用户名:q\Q退出').strip()
        if name.upper() == 'Q':
            return '感谢登录'
        mima = input('请输入登录密码:')
        with open('register_msg', encoding='utf-8') as f1:
                fi = f1.read()
                if name  in fi:
                    if mima in fi:
                        print('登录成功')
                else:
                    print('用户名或密码错误，请重新输入')

print('{}\t{}\n{}\t{}'.format('1', '登录', '2', '注册'))
b = input('请选在登录还是注册：1/2').strip()
b = int(b)
if b == 1:
    print(login())
elif b == 2:
    print(register())
else:
    print('输入有误，请重新输入。')

while True:
    print('{}\t{}\n{}\t{}'.format('1', '登录', '2', '注册'))
    c = input('请选在登录还是注册：1/2，q\Q退出').strip()
    if c.upper() == 'Q': break
    c = int(c)
    if c == 1:
        print(login())
    elif c == 2:
        print(register())
    else:
        print('输入有误，请重新输入。')

