# a = 4
# b = 3
# c = [1,2,3,4]
# c1 = {'name':'alex'}
#
# def func1():
#     name = '老男孩'
#     print(name)
# func1()
#当执行函数的时候，他会在内存中开辟一个临时名称空间，存放函数体内的所有变量与值的关系，
# 随着函数的执行完毕，临时空间自动关闭。
#input(),print(),len 内置函数

# name = '老男孩'
# def func1():
#     name = 'taibai'
#     print(name)
# func1()
# def my_len(argv):
#     return 666
# print(len([12,3,]))
a = 2
print(a)
def func1():
    age = 11
    print(age)
func1()