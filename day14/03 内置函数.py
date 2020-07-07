"""
len()
count()
print()
max()
min()
dir()
list()
eval()
open()
str()
isinstance()
format()
type()
tuple()
iter()
input()
int()
set()
frozenset()
"""
#其他相关：
#***eval:执行字符串类型的代码，并返回最终结果
# print(eval('3 +4'))
# ret = eval('{"name":"老男孩"}')
# print(ret,type(ret))

#***exec:执行字符串类型的代码,流程语句。
ret1 = '''
# li = [1,2,3]
# for i in li:
#     print(i)
'''
# print(exec('3 +4'))
# print(exec(ret1))
#compile:将字符串类型的代码编译。代码对象能够通过exec语句来执行或者eval()进行求值。
# code1 = 'for i in range(0,10): print (i)'
# compile1 = compile(code1,'','exec')
# exec (compile1)

#***print()
#print(self, *args, sep=' ', end='\n', file=None)
# print(333,end='')
# print(666,)
# print(111,222,333,sep='|')
# with open('log',encoding='utf-8',mode='a') as f1:
#     print('5555',file=f1)

#*hash哈希
# print(hash(12322))  # 数字不变
# print(hash('123'))
# print(hash('arg'))
# print(hash('alex'))
print(hash(True))
print(hash(False))
# print(hash((1,2,3)))

#*help：函数用于查看函数或模块用途的详细说明。
# print(help(list))

#***callable：函数用于检查一个对象是否是可调用的。
# 如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。
# def func1():
#     print(555)
# a = 3
# f = func1
# print(callable(f))
# print(callable(a))

#***dir
# print(dir(list))

# *next
# 首先获得Iterator对象:
# it = iter([1, 2, 3, 4, 5])
# # 循环:
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break
#*iter()

# *int
# print(int())  # 0
#
# print(int('12'))  # 12
#
# print(int(3.6))  # 3
#
# print(int('0100',base=2))  # 将2进制的 0100 转化成十进制。结果为 4


# print(type(3.14))  # float

# print(float(3))

'''

complex：函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。
如果第一个参数为字符串，则不需要指定第二个参数。。
'''

'''
*bin：将十进制转换成二进制并返回。

*oct：将十进制转化成八进制字符串并返回。

*hex：将十进制转化成十六进制字符串并返回。
'''
# print(bin(5))  # 0b101
# print(oct(7))  # 0o7
# print(oct(9))  # 0o11
# print(hex(10))  # 0xa
# print(hex(15))  # 0xf
# print(hex(19))  # 0x13

#*abs：函数返回数字的绝对值。
# print(abs(-20))






# *divmod：计算除数与被除数的结果，返回一个包含商和余数的元组(a // b, a % b)。
# print(divmod(11,3))  # (3, 1)

#round：保留浮点数的小数位数，默认保留整数。
# print(round(3.1415))
# print(round(3.1415,3))

#pow：求x**y次幂。（三个参数为x**y的结果对z取余）
# print(pow(2,3))
# print(pow(2,3,5))

#***sum：对可迭代对象进行求和计算（可设置初始值）。
# print(sum([1,2,3]))
# print(sum([1,2,3],100))

#***max：返回可迭代对象的最大值（可加key，key为函数名，通过函数的规则，返回最大值）。
# print(max([1,2,3]))

# ret = max([1,2,-5,],key=abs)  # 按照绝对值的大小，返回此序列最大值
# print(ret)
#***min
# ret = min([1,2,-5,],key=abs)    #1          # 按照绝对值的大小，返回此序列最小值
# print(ret)

#***reversed：将一个序列翻转，并返回此翻转序列的迭代器。
# ite = reversed(['a',2,3,'c',4,2])
# print(ite)
# for i in ite:
#     print(i)
#slice：构造一个切片对象，用于列表的切片。

# li = ['a','b','c','d','e','f','g']
# l2 = ['a','b','c',1,2,3,4,54]
# sli_obj = slice(3)
# print(li[sli_obj])
# print(l2[sli_obj])

# sli_obj = slice(7,0,-2)
# print(li[sli_obj])

#*** format 用于格式化输出很重要
# s1 = format('test', '<30')
# print(format('test', '<30'))
# print(format('test', '>20'))
# print(format('test', '^20'))
# print(len(s1))

#bytes：只能编码，将unicode ---> 非unicode  bytes(s1,encoding='utf-8')。
# s1 = '老男孩'
# s2 = s1.encode('utf-8')
# s22 = bytes(s1,encoding='utf-8')
# print(s2)
# print(s2.decode('utf-8'))

#bytearry：返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
# ret = bytearray('alex',encoding='utf-8')  # [65,108,101,120]
# print(id(ret))
# print(ret)
# print(ret[0])  # 97
# ret[0] = 65
# print(ret)
# ret = memoryview(bytes('你好',encoding='utf-8'))
# print(len(ret))  # 6 utf-8的bytes类型，放在一个list中 [\xe4,\xbd,\xa0,\xe5,\xa5,\xbd]
# print(ret)
# print(bytes(ret[:3]).decode('utf-8'))
# print(bytes(ret[3:]).decode('utf-8'))
# print('你好'.encode('utf-8'))
'''
*ord:输入字符找该字符编码的位置 unicode
*chr:输入位置数字找出其对应的字符 unicode
ascii:是ascii码中的返回该值，不是就返回
'''
# print(ord('a'))
# print(ord('中'))
# print(chr(98))
# print(chr(20013))

# print(ascii('a'))
# print(ascii('中'))  # '\u4e2d'

# %r  原封不动的写出来
# name = 'taibai'
# print('我叫%r' % name)

#*** repr 原形毕露
# print(repr('{"name":"alex"}'))
# print('{"name":"alex"}')

# *** sorted  key
# li = [1,-2,-7,8,5,-4,3]
# print(sorted(li,reverse=True,key=abs))

# L = [('a', 1), ('c', 3), ('d', 4),('b', 2), ]
# sorted(L, key=lambda x:x[1])               # 利用key

# *** enumerate:枚举，返回一个枚举对象。 (0, seq[0]), (1, seq[1]), (2, seq[2]),
# li = ['老男孩', 'alex', 'wusir', '嫂子', 'taibai']
# print(enumerate(li))
# print('__iter__' in dir(enumerate(li)))
# print('__next__' in dir(enumerate(li)))

# for k,v in enumerate(li):
#     print(k,v)
# for k,v in enumerate(li,1):
#     print(k,v)

# * all  可迭代对象中，全都是True才是True
# * any  可迭代对象中，有一个True 就是True
# print(all([1,2,True,0]))
# print(any([1,'',0]))

# *** zip 拉链方法 形成元组的个数与最短的可迭代对象的长度一样，然后......
# l1 = [1, 2, 3, 4]
# l2 = ['a', 'b', 'c', 5]
# l3 = ('*', '**', (1,2,3), 777)
# l4= ('0', '99', (1,2,3), 777)
# print('__iter__' in dir(zip(l1,l2,l3,l4)))
# print('__next__' in dir(zip(l1,l2,l3,l4)))
# for i in zip(l1,l2,l3,l4):
#     print(i)

#filter 过滤 通过你的函数，过滤一个可迭代对象，返回的是True
# 类似于[i for i in range(10) if i > 3]

# def func(x):
#     return x % 2 == 0
# ret = filter(func,[1,2,3,4,5,6,7])
# print(ret)
# for i in ret:
#     print(i)

# li = [i for i in [1,2,3,4,5,6,7] if i % 2 == 0]
# print(li)

# def square(x) :            # 计算平方数
#     return x ** 2
# print(map(square,[1,2,3,4,5]))
# for i in map(square,[1,2,3,4,5]):
#     print(i)
# lambda
# def func1(x):
#     return x**2

# func = lambda x:x**2
# print(func(5))

# def func2(x,y):
#     return x + y

# func3 = lambda x,y:x+y
# print(func3(2,3))

#lambda 函数与内置函数的结合。
# sorted，map，fiter，max，min，reversed




# dic={'k1': 10, 'k2': 100, 'k3': 30}
# print(max(dic))
# print(max(dic, key=lambda x: dic[x]))  # k2
# print(dic[max(dic, key=lambda x: dic[x])])  # k2

# def func(x):
    # return x**2

# res = map(lambda x:x**2,[1,5,7,4,8])
# for i in res:
#     print(i)

l1 = [1,2,3,11,12,40,20,50,79]

# l2 = [i for i in l1 if i > 10]
# print(l2)

# def func2(x):
#     return x > 10
# ret = filter(lambda x: x > 10,l1)
# for i in ret:
#     print(i)
# func = lambda x,y: x if x > y else y