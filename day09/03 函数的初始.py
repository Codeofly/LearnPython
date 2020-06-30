# s = 'fdsfdsagdfas'
# count = 0
# for i in s:
#     count += 1
# # print(count)
#
l1 = [1, 2, 3, 4, 5, 'a', 'b', 'dfsa', 3]


# count = 0
# for j in l1:
#     count += 1
# print(count)
# 重复代码多
# 可读性差
# 函数的产生：
# 函数就是封装一个功能。
# def my_len():
#     # def 关键字 定义一个函数
#     # my_len 函数名书写规则与变量一样。
#     # def 与函数名中间一个空格。
#     # 函数名():加上冒号
#     # 函数体
#     count = 0
#     for j in l1:
#         count += 1
#     print(count)
#
#
# my_len()
# 函数的执行：函数名 + （）
#
# while True:
#     print(222)
#     print(666)
# print(len([1,23,4]))

# 函数的返回值
# 写函数，不要再函数中写print（）
# return
# 1,在函数中，遇到return结束函数。
# 2,将值返回给函数的调用者。
#     无 return
#     return None
#     return 1个值  该值是什么，就直接返回给函数的调用者，函数名（）
#     return 多个值 将多个值放到一个元组里，返回给函数的调用者。
# def fun():
#     print(111)
#     print(222)
#     print(333)
#     return 2,3,4
# a,b,c = fun()
# print(a,b,c)

# def my_len():
#     count = 0
#     for j in l1:
#         count += 1
#     # return count
#     # return 777
#     # return [1,2,3]
#     return 1,2,3,[22,33],'alexsb'
# # ret = my_len()
# # print(ret)
# print(my_len())

print(len('3243243'))

# 函数的传参

# def my_len(l):  # l 形式参数 形参
#     count = 0
#     for j in l:
#         count += 1
#     return count
# a = 'fdsafds    afdsagfsadf'
# print(my_len(a))  # 实际参数 ，实参
# print(my_len([1,2,3]))
# 实参角度：
# 1，位置传参。按顺序，一一对应。
# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# func('fdsafdas',3,4)
# 写一个函数，功能比大小，
# def max_min(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num1 = int(input('请输入一个数：'))
# num2 = int(input('请输入另一个数：'))
# print(max_min(num1,num2))
# ps: 三元运算
# def max_min(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(max_min(100,200))
# def max_min(a,b):
#     return   a if a > b else b
# print(max_min(300,200))
# 2，关键字传参,不按顺序,一一对应。
# def max_min(a,b):
#     return a if a > b else b
# print(max_min(b = 300,a = 200))
# 3，混合传参,关键字参数永远在最后面。
# def func1(a,b,c,d,e):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)
# func1(1,2,d=4,c=3,e=5)
# func1(1,4,d=2,c=3,e=5)
# 按照形参角度。
# 1，位置传参。按顺序，一一对应。
# def func(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# func('fdsafdas',3,4)
# #2，默认参数。
# def func(a,b=666):  #
#     print(a,b)
# # func(1,2)
# # func(1,777)
# func(1,2)
# s = 'alex'.center(30,'*')
# print(s)
# def Infor_entry(username,sex='男'):
#     with open('name_list',encoding='utf-8',mode='a') as f1:
#         f1.write('{}\t{}\n'.format(username,sex))
#
# while True:
#     username = input('请输入姓名（男生以1开头）').strip()
#     if '1' in username:
#         username = username[1:]
#         Infor_entry(username)
#     else:
#         Infor_entry(username,'女')
