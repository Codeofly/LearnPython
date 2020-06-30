'''

5、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数，并返回结果。
7、写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
	PS:字典中的value只能是字符串或列表
8、写函数，接收两个数字参数，返回比较大的那个数字。
9、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（进阶）。
def func8(path,old,new):
    pass
func8(log,alex,sb)


10、写一个函数完成三次登陆功能，再写一个函数完成注册功能(进阶)


'''
#2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

# def func1(argv):
#     l1 = []
#     for i in range(len(argv)):
#         if i % 2 == 1:
#             l1.append(argv[i])
#     return l1
# print(func1([1,2,3,4]))

# def func1(argv):return argv[1::2]
# print(func1([1,2,3,4]))
#  3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

# def func2(argv):
#     if len(argv) > 5:
#         return True
#     else:return False
# print(func2('fdsafsdagfdsa'))

# def func2(argv):
#     return True if len(argv) > 5 else False
# print(func2('fdsafsdagfdsa'))

# def func2(argv):
#     return len(argv) > 5
# print(func2('1'))

# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func3(argv):
#     l1 = []
#     if len(argv) > 2:
#         l1 = argv[:2]
#     else:
#         l1 = argv
#     return l1
# func3([1,2,3,4])

# def func3(argv):
#     return argv[:2] if len(argv) > 2 else argv
# func3([1,2,3,4])

# def func3(argv):
#     return argv[:2]
# # func3([1,2,3,4])
# l1 = [1]
# print(l1[:2])

# 5、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数，并返回结果。
# def func4(argv):
#     dic = {'digit':0,'alpha':0,'space':0,'other':0}
#     for i in argv:
#         if i.isdigit():
#             dic['digit'] += 1
#         elif i.isalpha():
#             dic['alpha'] += 1
#         elif i.isspace():
#             dic['space'] += 1
#         else:
#             dic['other'] += 1
#     return '数字%d,字母%d,空格%d,其他%d' % (dic['digit'],dic['alpha'],dic['space'],dic['other'])
#
# print(func4('fdsafd  1232432@#$%^fdf123   哈佛撒旦'))
# 6、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容，并返回结果。

# 7、写函数，检查传入字典的每一个value的长度(列表，字符串),如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func6(argv):
#     for i in argv:
#         if len(argv[i]) > 2:
#             argv[i] = argv[i][:2]
#     return argv
# 
# print(func6({"k1": "vv11", "k2": [11,22,33,44]}))
# 
# def func6(argv):
#     for i in argv:
#         argv[i] = argv[i][:2]
#     return argv
# 
# print(func6({"k1": "vv11", "k2": [11,22,33,44]}))