# class A:
#     def __init__(self,name,age,sex,cls):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.cls = cls
#     def __len__(self):
#         return len(self.__dict__)
#
# # 有一个内置函数 和内置方法len()是唯一对应的关系
# a1 = A('alex',81,'不详',2)
# a1.hobby = '烫头'
# a2 = A('egon',20,'不详',3)
# a3 = A('yuan',21,'不详',4)
# print(len(a1))
# print(len(a2))
# print(len(a3))

# l = list([1,2,3,4,5])
# print(l)
# print(len(l))

# 内置的东西
# 都和内置的方法有着千丝万缕的联系

# 字典的存储
# hash

# class A:
#     def __init__(self,name,age,sex,cls):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.cls = cls
#     def __hash__(self):
#         return 0
# a1 = A('alex',81,'不详',2)
# print(hash(a1))























