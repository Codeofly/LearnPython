# 归一化设计
# l = [1,2,2]
# l2 = {1,2,3,4}
# l3 = (1,2)
# a = '1234567'
# print(len(l))
# print(l3.__len__())
# len()  和 __len__()
# 只有一个类中实现了__len__()方法，才能使用len()函数
# def len2(obj):  # 归一化设计
#     return obj.__len__()

# print(len(l))
# print(len(l2))
# print(len(l3))
l = [1,2,3]
l1 = {1,2,3,4,5}
l3 = 'sahfjsdfhkj'
def len2(obj):
    return obj.__len__()
print(len(l))               #3
print(len(l1))              #5s
print(len(l3))              #11