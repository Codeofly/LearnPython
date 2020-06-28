# and or not
# 第一种：前后都是比较运算。
#优先级：（）> not > and > or 同一个优先级，从左至右依次计算。
# print(1 > 2 and 3 < 4 and 3 > 2 or 2 < 3)
# print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# 第二种：前后都是数值运算。
'''
x or y if x True,则 return x,否则 return y
'''
# print(1 or 3)
# print(1 or 3)
# print(2 or 3)
# print(0 or 3)
# print(-1 or 3)
# print(1 and 2)
# print(0 and 2)

# 第三种：混合。
# print(1 > 2 or 3 and 4)
# print(2 or 2 > 3 and 4)
# print(0 or 2 > 3 and 4)

#数据类型转换：
'''
int ---> bool  非0即True，0为False
bool---> int  True  1  False 0
print(int(True))
print(int(False))
print(bool(100))
print(bool(0))
'''
# print(3 > 2 or 1 > 2)
#  and
# or
print( True and False)
print( False and False)
print( False and True)
print( True and True)
print( '~~~~~~~~~~~~~~')
print( True or False)
print( False or False)
print( False or True)
print( True or True)
print( '~~~~~~~~~~~~~~')
print( 0 or 1)
print( 1 or 0)
print( 1 or 1)
print( 0 or 0)
print( '~~~~~~~~~~~~~~')
print( 0 or 2)
print( 2 or 0)
print( 2 or 2)
print( 0 or 0)
print( '~~~~~~~~~~~~~~')
print( 0 and 1)
print( 1 and 0)
print( 1 and 1)
print( 0 and 0)
print( '~~~~~~~~~~~~~~')
print( 0 and 2)
print( 2 and 0)
print( 2 and 2)
print( 0 and 0)

print( True and False)
print( False and False)
print( False and True)
print( True and True)