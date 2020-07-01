# def func(*args):
#     print(args)
# func(1,2,3,4,5,7,8,9,1,2,3,4,5,6,7,8)

# *args 动态参数，万能参数

# args接受的就是实参对应的 所有位置参数，并将其放在元组中。

# 形参对应顺序：
# 位置参数，*args，默认参数


# def func(a,b,c,d,*args,e='男'):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)return
#     print(e)
# func(1,2,3,4,5,6,7,e='女')
# **kwargs 动态传参，他将所有的关键字参数(无意义的)放到一个字典中。

def func(a, b, c, **kwargs):
    print(kwargs)


func(1, 2, r=4, b1=5, c1=6, c=7, )


def func(a, b, c, d, *args, e='男', **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(e)
    print(kwargs)


func(1, 2, 3, 4, 5, 6, 7, v=3, m=7, h=9, e='女')

# 最终顺序：位置参数，*args，默认参数，**kwargs

# def func1(*args,**kwargs):
#     pass
# func1()

# * 魔法运用

# def func(*args):
#     print(args) #(1,2,30,1,2,33.。。。。。)
# l1 = [1,2,30]
# l2 = [1,2,33,21,45,66]
# tu = (1,2,3)
# func(1,2,30,1,2,33,21,45,66)
# func(*'qweqrfdsaf')
# func(*{'name':'alex',"age":12})
# func(*l1,*l2)
# def func(*args):
#     print(args)
# func(1,2,3,10,20,80)

# def func(**kwargs):
#     print(kwargs)
#
# dic1 = {'name1':'alex','age1':46}
# dic2 = {'name':'老男孩','age':56}
# func(**dic1,**dic2)

# 在函数的调用执行时，
#   *可迭代对象，代表打散(list,tuple,str,dict(键))将元素一一添加到args。
#  **字典，代表打散，将所有键值对放到一个kwargs字典里。

# 在函数定义时， *args，**kwargs代表的是聚合。
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# dic1 = {'name1':'xiao','age1':46}
# dic2 = {'name':'fei','age':56}
# func(*[1,2,3,4],*'asdfsad',**dic1,**dic2)

# def func(*args,**kwargs):
#     # args = (1,2,3,4)
#     # kwargs = {'age': 56, 'name': '老男孩'}
#     print(*args)
#     print(**kwargs) #(age = 56 ,name = 老男孩)
# dic1 = {'name1':'alex','age1':46}
# dic2 = {'name':'老男孩','age':56}
# # func(*[1,2,3,4],*'asdfsad',**dic1,**dic2)
# func(**dic2)
