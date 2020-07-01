def wrapper1(func):  # func ==  f函数名
    def inner1():
        print('wrapper1 ,before func')  # 2
        func()
        print('wrapper1 ,after func')  # 4
    return inner1

def wrapper2(func):  # func == inner1
    def inner2():
        print('wrapper2 ,before func')  # 1
        func()
        print('wrapper2 ,after func')  # 5
    return inner2
@wrapper3
@wrapper2  #  f = wrapper2(f)  里面的f==inner1  外面的f == inner2
@wrapper1  # f = wrapper1(f)   里面的f==函数名f  外面的f == inner1
def f():  # 3
    print('in f')

f()  # inner2()

@wrapper2
@wrapper3  #  f = wrapper2(f)  里面的f==inner1  外面的f == inner2
@wrapper1  # f = wrapper1(f)   里面的f==函数名f  外面的f == inner1
def f():  # 3
    print('in f')

f()  #