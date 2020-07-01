# from functools import wraps
# def wrapper(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         """执行函数前的操作"""
#         ret = func(*args, **kwargs)
#         """执行函数后的操作"""
#         return ret
#     return inner
#
# @wrapper  # func = wrapper
# def func():
#     '''
#     此函数是登录认证用。
#     :return: True or False
#     '''
#     print(666)
#     return True
#
# print(func.__name__)
# print(func.__doc__)

# def timmer(argv):
#
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             """执行函数前的操作"""
#             ret = func(*args, **kwargs)
#             """执行函数后的操作"""
#             return ret
#         return inner
#     return wrapper
#
# @timmer('京东')  # --> wrapper  @wrapper
# def func():
#     '''
#     此函数是登录认证用。
#     :return: True or False
#     '''
#     print(666)
#     return True
#
# @timmer('淘宝')
# def func():
#     '''
#     此函数是登录认证用。
#     :return: True or False
#     '''
#     print(666)
#     return True

