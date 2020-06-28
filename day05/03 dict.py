# dic = {"name":"jin",
#        "age":18,
#        "sex":"male",
#        }
# # print(dic)
# #哈希表：
# # print(hash('name'))
# # print(hash('fsagffsadgsdafgfdsagsadfgfag'))
# # print(hash('age'))
# # 增
# #第一种： 有则覆盖，无则添加
# # dic['hobby'] = 'girl'
# # print(dic)
# # dic['name'] = 'wusir'
# # print(dic)
# #第二种 setdeafult 无则添加，有则不变。
# # dic.setdefault('hobby')
# # dic.setdefault('hobby','girl')
# # dic.setdefault('name','ritian')
# # print(dic)
#
# # 删
# #pop  有返回值
# # print(dic.pop('age'))
# # print(dic)
# # dic.pop('hobby')  # 报错
# # print(dic.pop('hobby', None))  # 返回你设定的值
# #clear 清空
# # dic.clear()
# # print(dic)
# #del
# # del dic
# # print(dic)
# # del dic['name']
# # print(dic)
# # dic.popitem()  # 随机删除 有返回值
# # print(dic.popitem())
# # print(dic)
#
#
# # 改
# dic['name'] = '太白'
# print(dic)
#两个字典的改
# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic2.update(dic)  # 将dic键值对，覆盖并添加到dic2
# # print(dic)
# print(dic2)

# 查
# print(dic['name'])
# print(dic['name1']) # 报错
# print(dic.get('name'))
# print(dic.get('name1'))  # 默认返回None
# print(dic.get('name1','咩有此键值对'))  # 默认返回None

# 其他方法：
#keys() values() items()
# print(dic.keys(),type(dic.keys()))
# print(dic.keys())
# for i in dic.keys():
#     print(i)
# for i in dic:
#     print(i)
# li = list(dic.keys())
# print(li)
# print(dic.values())
# for i in dic.values():
#     print(i)
# print(dic.items())
# for i in dic.items():
#     print(i)
#特殊类型 dict 转化 成list
# print(list(dic.keys()))

#概念：分别赋值
# a,b = 2,3
# print(a,b)
# a,b = (2,3)
# print(a,b)
# a,b = [2,3]
# print(a,b)
# a = 4 ,b = 5
# a = 4
# b = 5
# a,b = b,a
# print(a,b)
# print(dic.items())
# for k,v in dic.items():
#     print(k,v)
# print(dic.items())

dic = {'1':2,'3':3}
dic.setdefault( '2',[1,2,3])
print(dic)