# str
# s = 'alex'
# s1 = ' '
# ret = s1.isspace()
# print(ret)
# tuple

# 对于元组：如果只有一个元素，并且没有逗号，
# 此元素是什么数据类型，该表达式就是什么数据类型。
# tu = (1)
# tu1 = (1,)
# print(tu,type(tu))
# print(tu1,type(tu1))

# tu = ('老男孩')
# tu1 = ('老男孩',)
# print(tu,type(tu))
# print(tu1,type(tu1))

# tu = ([1,2,3])
# tu1 = ([1,2,3],)
# print(tu,type(tu))
# print(tu1,type(tu1))

# 对于list
# 在循环一个列表时，最好不要进行删除的动作（一旦删除，索引会随之改变），容易出错。
# li = [11,22,33,44,55]
# 将索引为奇数的元素删除。
# del li[1::2]
# print(li)
# l1 = []
# for i in range(len(li)):
#     if i % 2 == 0:
#         l1.append(li[i])
# li = l1
# print(li)

# l1 = []
# for i in li:
#     if li.index(i) % 2 == 0:  # 有重复会报错
#         l1.append(i)
# li = l1
# print(li)
# for i in range(len(li)):
#     print(li)  # [11, 22, 33, 44, 55]    [11, 22, 33, 44, 55]  [11, 33, 44, 55] [11, 33, 44, 55]  [11, 33, 44]
#     print(i)  # 0  1 2 3 4
#     if i % 2 == 1:
#         del li[i]
#     print(li)  # [11, 22, 33, 44, 55]  [11, 33, 44, 55]  [11, 33, 44, 55]  [11, 33, 44]  [11, 33, 44]
#     print(i)  # 0  1  2  3 4
# print(li)  # list assignment index out of range
# del li[100]  # list assignment index out of range
# for i in li:
#     print(li)
#     li.remove(i)
#     print(li)
# print(li)
# for i in range(len(li)-1,-1,-1):
#     if i % 2 == 1:
#         del li[i]
# print(li)

# dict
# dic = dict.fromkeys('abc','alex')
# print(dic)         {'a': 'alex', 'b': 'alex', 'c': 'alex'}
# dic = dict.fromkeys([1,2,3],[])
# print(dic)           {1: [], 2: [], 3: []}
# dic[1].append('老男孩')
# print(dic)          {1: ['老男孩'], 2: ['老男孩'], 3: ['老男孩']}


dic = {'k1': 'value1', 'k2': 'value2', 'name': 'wusir'}
# 将字典中含有k元素的键，对应的键值对删除。


# 在循环字典中，不能增加或者删除此字典的键值对。
# dictionary changed size during iteration

# for i in dic:
#     if 'k' in i:
#         del dic[i]
# count = 0
# for i in dic:
#     dic[i+str(count)] = dic[i]
#     count += 1
'''
l1 = []
for i in dic:
    if 'k' in i:
        l1.append(i)

for i in l1:
    del dic[i]
print(dic)
'''
# 数据转换：
# int str bool
# str list  split  join
# 无意义
# li = ['wusir','alex']
# s = str(li) # '['wusir','alex']'
# print(s,type(s))

# tuple list
# tu = (1,2,3)
# li = list(tu)
# print(li)

# l1 = [1,2,3]
# tu1 = tuple(l1)
# print(tu1)

# 数据类型转化成bool 为False
# 0 "  [] () {}

# tuple >> str
# tu = ('wusir','老男孩','老男')
# s = " ".join(tu)
# print(s)


# str1 =  'wusir'
# li = list(str1)
# print(li)
# tu = tuple(li)
# print(tu)