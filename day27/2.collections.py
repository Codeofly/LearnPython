# from collections import OrderedDict
# d = OrderedDict()
# d['a'] = 1
# d['z'] = 2
# d['b'] = 3
# print(d)
#
# d['z'] = 0
# print(d)

# {'apple':100,'computer':10000}

# 默认字典
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，
# 将所有大于 66 的值保存至字典的第一个key中，
# 将小于 66 的值保存至第二个key的值中。
# dic = {}
# l = [11,22,33,44,55,66,77,88,99,90]
# for i in l:
#     if i>66:
#         if dic.get('k1'):
#             dic['k1'].append(i)
#         else:
#             dic['k1'] = [i]
#     elif i<66:
#         if dic.get('k2'):
#             dic['k2'].append(i)
#         else:
#             dic['k2'] = [i]
# print(dic)

# from collections import defaultdict

# d = defaultdict(set)
# print(d)
# print(d['a'])
# d['b'] = 10
# print(d)


# defaultdict(list)  # callable
# l = []
# dic = {'k1':l,'k2':l}

# d = defaultdict(list)   #{1:''}
# print(d)
# print(d[1])
# print(d)

# {} 默认的value是5
# from collections import defaultdict
# d = defaultdict(lambda : 5)
# print(d[1])
# print(d)

# from collections import defaultdict
# d = defaultdict(list)
# l = [11,22,33,44,55,66,77,88,99,90]
# for i in l:
#     if i>66:
#         d['k1'].append(i)
#     elif i<66:
#         d['k2'].append(i)
#
# print(d)

# 默认字典最大的好处就是 永远不会在你使用key获取值的时候报错
# 默认字典 是给 字典中的value设置默认值

# from collections import Counter
# c = Counter('abcdeabcdabcaba')
# print(c)

# class Configparser:
#     def __init__(self,section,option):
#         self.section = section
#         self.option = option
#     def write(self,f):
#         f.write(self.section,self.option)
#
#
# f = open('test','w')
# config = Configparser('a','b')
# config.write(f)
#
#
# import configparser
# configparser.ConfigParser.write()
