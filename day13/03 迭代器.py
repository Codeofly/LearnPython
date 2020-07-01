# s = 'laonanhai'
# print(dir(s))   # __iter__
# l1 = [1, 2, 3, 4]
# print(dir(l1))  # __iter__
# dic = {'1': 'alex', "2": "老男孩"}
# print(dir(dic))  # __iter__

# 什么是可迭代对象：内部含有__iter__方法的对象就叫做可迭代对象
# 可迭代对象就遵循可迭代协议。
# 如何判断 两种方式
# print('__iter__' in dir(s))
# from collections import Iterable
# l = [1, 2, 3, 4]
# print(isinstance(l, Iterable)) # True
# print(type(l))
# print(isinstance(l,list))

# 迭代器
# l1 = [1,2,3]
# 可迭代对象转化成迭代器：可迭代对象.__iter__()  --->迭代器
#迭代器不仅含有__iter__,还含有__next__。遵循迭代器协议。
# l1_obj = l1.__iter__()  # 迭代器
# print('__iter__' in  dir(l1_obj))
# print('__next__' in  dir(l1))
# print('__next__' in  dir(l1_obj))
# print(l1_obj.__next__())
# print(l1_obj.__next__())
# print(l1_obj.__next__())
# print(l1_obj.__next__())
# for i in l1_obj:
#     print(i)
#判断迭代器：
# print('__iter__' in  dir(l1_obj))
# print('__next__' in  dir(l1_obj))
# from collections import Iterator
# print(isinstance(l1_obj, Iterator))
# 迭代器的好处：
# 1，节省内存空间。
# 2，满足惰性机制。
# 3，不能反复取值，不可逆。
l2 = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in l2:
#     print(i)
'''
1,将可迭代对象转化成迭代器
2，内部使用__next__方法取值
3，运用了异常处理去处理报错。
'''
# l2 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2_obj = l2.__iter__()
# while True:
#     try:
#         i = l2_obj.__next__()
#         print(i)
#     except Exception:
#         break