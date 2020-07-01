from functools import wraps
# def func1():
#     print('你有病呀，领导，测试我的执行效率干甚。')

# print(time.time())  # 时间戳
# start_time = time.time()
# func1()
# time.sleep(0.3)
# end_time = time.time()
# print('此函数的执行效率%s' % (end_time - start_time))

# def func1():
#     print('你有病呀，领导，测试我的执行效率干甚。')
#
# def func2():
#     print('你有病呀，领导2，测试我的执行效率干甚。')
# func1()

# def func1():
#     print('你有病呀，领导，测试我的执行效率干甚。')
# func1()
# def timmer(f):
#     start_time = time.time()
#     f()
#     time.sleep(0.3)
#     end_time = time.time()
#     print('此函数的执行效率%s' % (end_time - start_time))

# f1 = func1  # f1 = func1
# func1 = timmer  # 新变量func1 = timmer
# func1(f1)


# def func2():
#     print('你有病呀，领导，测试我的执行效率干甚。')
# def timmer(f):  # f = func1
#     def inner():
#         start_time = time.time()
#         f()  #  func1()
#         time.sleep(0.3)
#         end_time = time.time()
#         print('此函数的执行效率%s' % (end_time - start_time))
#     return inner
# # 语法糖@
#
# @timmer  # func1 = timmer(func1)
# def func1():
#     print('你有病呀，领导，测试我的执行效率干甚。')

# func1 = timmer(func1)  # inner
# func1()  # inner()


# def timmer(f):  # f = func1 函数名
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         f(*args,**kwargs)
#         time.sleep(0.3)
#         end_time = time.time()
#         print('此函数的执行效率%s' % (end_time - start_time))
#     return inner
#
# @timmer # func1 = timmer(func1) # inner
# def func1(a,b):
#     print(a,b)
#     print('你有病呀，领导，测试我的执行效率干甚。')
#
# @timmer
# def func2(a,b,c,d):
#     print(a,b,c,d)
#     print('你有病呀，领导，测试我的执行效率干甚。')
#
# func1(1,2)  # inner()
# func2(2,3,4,5)
# def timmer(f):  # f = func1 函数名
#     def inner(*args,**kwargs):
#         start_time = time.time()
#         ret = f(*args,**kwargs)
#         time.sleep(0.3)
#         end_time = time.time()
#         print('此函数的执行效率%s' % (end_time - start_time))
#         return ret
#     return inner
#
#
# @timmer # func1 = timmer(func1) # inner
# def func1(a,b):
#     print(a,b)
#     print('你有病呀，领导，测试我的执行效率干甚。')
#     return 666
#
# print('************',func1(1,2))



# def f1():
#     print(666)
# f = f1
# f()
# a = 5
# a = 4 +3
# print(a)
# def func2(a1,b1):
#     print(a1,b1)
#
# def func3(a,b):
#     func2(a,b)
# func3(1,2)


# def wrapper(func):
#     def inner(*args,**kwargs):
#         '''被装饰函数之前'''
#         ret = func(*args,**kwargs)
#         '''被装饰函数之后'''
#         return ret
#     return inner
#
# @wrapper
# def func(a,b):
#     pass
#     return 566