# l1 = [1,2,3]
# l2 = l1
# l2.append(111)
# # print(l1,l2)
# print(id(l1))
# print(id(l2))
# # 对于赋值运算，指向的是同一个内存地址。字典，列表，集合都一样。
# s = 1000
# s1 = s
# print(id(s))
# print(id(s1))

    #copy 不是指向一个，在内存中开辟了一个内存空间
    #对于浅copy来说，第一层创建的是新的内存地址，
    # 而从第二层开始，指向的都是同一个内存地址，
    # 所以，对于第二层以及更深的层数来说，保持一致性。
# l1 = [1,2,3]
# l2 = l1.copy()
# l1.append(111)
# print(id(l1),id(l2))
# l1 = [1,2,[1,2,3,[22,33,44]],4]
# l2 = l1.copy()
# l1[2].append(666)
# print(l1)
# print(l2)
# print(id(l1))
# print(id(l2))

#deep.copy
# 对于深copy来说，两个是完全独立的，
# 改变任意一个的任何元素（无论多少层），另一个绝对不改变.
# import copy
# l1 = [1, 2, [1, 2, 3], 4]
# l2 = copy.deepcopy(l1)
# l1[2].append(666)
# print(l1,l2)
# print(id(l1[2]),id(l2[2]))

# l1 = [1,2,3]
# l2 = l1
# l2.append(111)
# print(l1,l2)

# l1 = [1,2,3,[22,33]]
# l2 = l1[:]           # 切片 为 浅copy
# l1[3].append(666)
# print(l2)  # [1, 2, 3, [22, 33, 666]]

# l1 = [1,2,3,]
# l2 = l1[:]
# l1.append(666)
# print(l2)