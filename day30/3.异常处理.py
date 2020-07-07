# 错误 ：语法错误 应该在开发的过程中就杜绝
# 异常
# num = 0
# 100/num



# 程序中的异常 ： 报错之后程序终止
# try:
#     # name   # NameError
#     int(input('num : '))  # ValueError
#     dic = {}
#     dic['k']  # KeyError
#     class A:pass
#     a = A()
#     a.name   # AttributeError
#     l = []
#     l[5]       # IndexError
#     import ab   # ImportError
# except ValueError:
#     print('遇到Value error了')
# except NameError:
#     print('遇到name error了')
# except KeyError:
#     print('key Error')

# try:
#     # name   # NameError
#     int(input('num : '))  # ValueError
#     dic = {}
#     dic['k']  # KeyError
#     class A:pass
#     a = A()
#     a.name   # AttributeError
#     l = []
#     l[5]       # IndexError
#     import ab   # ImportError
# except Exception as e :
#     print('exception',e)

# l = ['创建老师','创建学校']
# while True:
#     try:
#         for num,item in enumerate(l,1):
#             print(num,item)
#         index = int(input('num : '))
#         print(l[index-1])
#         break
#     except ValueError:
#         print('请输入一个数字。')
#     except IndexError:
#         print('您输入的数字不在选择范围内')
#     except Exception as e:
#         print(e)


# try:
#     name = 10
# except NameError:
#     print('触发了 name error')
# else:
#     print('执行else里的语句了')

# try:
#     print('发短信')
# except NameError:
#     print('触发了 name error')
# else:
#     print('转账成功')

# try:
#     name
# except NameError:
#     print('name error')
# else:
#     print('success')
# # finally:                      # finally 执行try中的代码 不管是否触发了错误 都会执行finally中的代码
# print('finally')

# try except        try中的代码遇到异常 就执行except中的代码
# try except else   try中的代码遇到异常 就执行except中的代码 没遇到异常就执行else中的代码
# trt except else finally  try中的代码遇到异常 就执行except中的代码 没遇到异常就执行else中的代码 无论如何都执行finally中的代码
# try finally       不能处理异常了，但是无论是否发生异常，都会执行finally中的代码

# f = open('file')
# try:
#     print('操作f')
# finally:
#     f.close()

# def func():
#     try:
#         return 1
#     finally:
#         print('finally')
#
# func()

# import time
# def wrapper(func):
#     def inner(*args,**kwargs):
#         try:
#             start = time.time()
#             return func(*args,**kwargs)
#         finally:
#             end = time.time()
#             print(end - start)
#     return inner
#
# @wrapper
# def func():
#     time.sleep(1)
#
# func()

#  主动触发异常
# raise TypeError
# class Payment:
#     def pay(self,money):
#         raise NotImplementedError('没有实现pay方法')
# class Alipay(Payment):
#     def pay(self,money):
#         print('支付宝支付%s元'%money)
#
# class WechatPay(Payment):
#     def pay(self,money):
#         print('微信支付%s元' % money)
#
# def pay(obj,money):
#     obj.pay(money)
#
# we = WechatPay()
# pay(we,10)


# try:
#     raise TypeError
# except TypeError:
#     print()

# class EvaException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return self.msg
#
# raise EvaException('错误的内容')
# try:
#     raise EvaException('错误的内容')
# except EvaException as e:
#     print(e)

# 断言
# assert 1==2
def func():
    a

def main():
    func()

try:
    main()
except:
    pass
