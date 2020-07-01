# from functools import wraps
# def wrapper(f):  # f = func1
#     @wraps(f)
#     def inner(*args,**kwargs): #聚合
#         #args （1,2,3）
#         '''执行函数之前的相关操作'''
#         ret = f(*args,**kwargs)  # 打散 1,2,3
#         '''执行函数之后的相关操作'''
#         return ret
#     return inner
# #
# # # 函数的执行时，*打散。
# # # 函数的定义时，*聚合。
@wrapper  # func1 = wrapper(func1)  func1 = inner
def func1(*args): #args (1,2,3)
    print(666)
    return args
print(func1(*[1,2,3]))  # inner(3,5) 打散
#
#
# def func1():
#     """
#     此函数是完成登陆的功能，参数分别是...作用。
#     :return: 返回值是登陆成功与否（True，False）
#     """
#     print(666)
#     # print(func1.__name__)
#     # print(func1.__doc__)
#     return True
# func1()
# print(func1.__name__)
# print(func1.__doc__)
@wrapper
def func1():
    """
    此函数是完成登陆的功能，参数分别是...作用。
    :return: 返回值是登陆成功与否（True，False）
    """
    print(666)
    return True
func1()
print(func1.__name__)
print(func1.__doc__)