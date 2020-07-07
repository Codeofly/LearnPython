# def func1():
#     print(666)
#
# while True:
#     func1()
import sys
sys.setrecursionlimit(10000)
def func1(n):
    n += 1
    print(n)
    func1(n)

func1(0)

# 执行一次开辟一个空间，python对你内存一个保护机制，默认只能递归到998层。

def age(n):
    if n == 1:
        return 18
    else:
        return age(n-1) + 2

print(age(4))  # age(3) + 2  age(2) + 2 + 2  18 + 2 + 2 + 2
'''
def age(4):
    if n == 1:
        return 18
    else:
        return age(3) + 2  18 + 2 + 2 + 2
        
def age(3):
    if n == 1:
        return 18
    else:
        return age(2) + 2  18 + 2 + 2

def age(2):
    if n == 1:
        return 18
    else:
        return age(1) + 2    18 +2
        
def age(1):
    if n == 1:
        return 18
    else:
        return age(0) + 2
'''