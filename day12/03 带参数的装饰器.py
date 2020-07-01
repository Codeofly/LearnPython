import time
def timmer(*args,**kwargs):
    def wrapper(f):
        def inner(*args,**kwargs):
            if flag:
                start_time = time.time()
                ret = f(*args,**kwargs)
                time.sleep(0.3)
                end_time = time.time()
                print('此函数的执行效率%f' % (end_time-start_time))
            else:
                ret = f(*args, **kwargs)
            return ret
        return inner
    return wrapper

flag = True
@timmer(flag,2,3)  # 两步：1，timmer(flag) --> wrapper 2,@wrapper 装饰器
def func1():
    print(666)


@timmer(flag)
def func2():
    print(777)
func1()
func2()

# import time
# flag = True
# def wrapper(f):
#     def inner(*args,**kwargs):
#         if flag:
#             start_time = time.time()
#             ret = f(*args,**kwargs)
#             time.sleep(0.3)
#             end_time = time.time()
#             print('此函数的执行效率%f' % (end_time-start_time))
#         else:
#             ret = f(*args, **kwargs)
#         return ret
#     return inner
