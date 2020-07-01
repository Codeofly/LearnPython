# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func(1,2,3,name='老男孩',age=12)

'''
在函数的执行（调用）时：打散。
    *可迭代对象（str，tuple，list，dict（key））每一个元素添加到args元组中。
    **dict 将字典的键值对添加到kwargs字典中。

在函数的定义时： 聚合。
    *args将所有的位置参数聚合到一个元组中。
    **kwargs 将所有的关键字参数聚合到一个字典中。
'''
# def func(*args,**kwargs):
#     #args(1,2,3,4)
#     #kwargs{'name':'alex','name1':'老男孩'}
#     # print(*args)
#     print(**kwargs)
# func(1,2,3,4,**{'name':'alex','name1':'老男孩'})

# def func():
#     global a
#     a = 3
# func()
# print(a)

# count = 1
# def search():
#     global count
#     count = 2
# search()
# print(count)
# li = [1,2,3]
# dic = {'a':'b'}
#
# def change():
#     li.append('a')
#     dic['q'] = 'g'
#     # print(dic)
#     # print(li)
# change()
# print(li)
# print(dic)
#python2 没有nonlocal
# def add_b():
#     b = 42
#     def do_global():
#         b = 10
#         print(b) # 1.10
#         def dd_nonlocal():
#             nonlocal b
#             b = b + 20
#             print(b)  # 2.30
#         dd_nonlocal()
#         print(b)  # 3.30
#     do_global()
#     print(b) # 4.42
# add_b()