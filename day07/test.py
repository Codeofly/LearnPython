import copy

# for i in range(10):
#     print(i)
#
# dic = dict.fromkeys('abc','alex')
# print(dic)
# dic = dict.fromkeys([1,2,3],[])
# print(dic)
# dic[1].append('老男孩')
# print(dic)
#
# l1 = [1, 2, 3, 4, ['alex']]
# l2 = l1[::]
# l1[-1].append(666)
# print(l2)
#
# print(id(l1))
# print(id(l1[-1]))
# print(id(l2))
# print(id(l2[-1]))
#
# l1 = [1, 2, 3, 4, ['alex']]
# l2 = l1[::]
# l1.append(666)
# print(l2)

l1 = [1, 2, 3, 4, ['alex']]
l2 = copy.deepcopy(l1)
l1[-1].append(666)
print(l2)


dict