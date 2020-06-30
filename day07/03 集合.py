# 去重
# li = [11,11,22,22,33,33,33,44]
# set1 = set(li)
# print(set1)

# li = list(set(li))
# print(li)
# set = {11,22,33,11,22,33,44}
# print(set)

# set1 = {'alex', 'wusir', 'ritian', 'egon', 'barry'}
# 增
# set1.add('女神')
# print(set1)
# set1.update('abc')     # 迭代增加
#                           {'wusir', 'ritian', 'egon', 'alex', 'a', 'c', 'b', 'barry'}
# set1.update([1,2,3])
# print(set1)

# 删
# set1.remove('alex')    # 按照 元素 删除
# print(set1)

# ret = set1.pop()       # 随机删除
# print(ret)
# print(set1)

# set1.clear()           # 清空集合 set()
# print(set1)  # set()

# del set1               # 从内存中删除集合
# print(set1)

#
# for i in set1:
#     print(i)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# # 交集   &   intersection
# print(set1 & set2)  # {4, 5}
# print(set1.intersection(set2))  # {4, 5}

# 反交集 ^ symmetric_difference
# print(set1 ^ set2)                # {1, 2, 3, 6, 7, 8}
# print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}

# 并集 | union
# print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}

# 差集 -
# print(set1 - set2)  # {1, 2, 3}
# print(set2 - set1)  # {6, 7, 8}

# set1 = {1,2,3}
# set2 = {1,2,4,5,6}
# print(set1.issubset(set2))  # 子集   set1 是set2的子集
# print(set2.issuperset(set1))  # 超集 set2 是set1的超集

# set1 = {'xiao',"xiaofei"}
# set2 = frozenset(set1)    # 变成不可变的set   frozenset({'xiao', 'xiaofei'})
#                                             <class 'frozenset'>
# print(set2,type(set2))


# s = {1,2,3,4}
# s2 = {1,2,3,4,5,6,7}
# print(s.issubset(s2))
# f = open('D:\联系.txt',encoding='utf-8',mode='w')
# f1 = f.write('xiaoxiaofeifei')
# f.close()
# f = open('测试练习',encoding='utf-8')
# f1 = f.read()
# print(f1)
# f.close()
