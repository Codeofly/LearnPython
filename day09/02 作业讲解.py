'''
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3
通过代码，将其构建成这种数据类型：
[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
'''
# l1 = []
# with open('a.txt',encoding='utf-8') as f1:
#     for i in f1:
#         l2 = i.strip().split()
#         dic = {'name':l2[0],'price':l2[1],'amount':l2[2],'year':l2[3]}
#         l1.append(dic)
# print(l1)
# sum = 0
# for i in l1:
#     sum1 = int(i['price']) * int(i['amount'])
#     sum += sum1
# print(sum)


# l1 = []
# dic = {}
# with open('a.txt',encoding='utf-8') as f1:
#     for i in f1:
#         l2 = i.strip().split()
#         dic['name'] = l2[0]
#         dic['price'] = l2[1]
#         dic['amount'] = l2[2]
#         print(dic)
#         l1.append(dic)
#         print(l1)
# print(l1)

# l1 = []
# name_list = ['name','price','amount','year',]
# with open('a.txt',encoding='utf-8') as f1:
#     for i in f1:
#         l2 = i.strip().split()
#         #l2 = [apple,10,3,2004]
#         dic = {}
#         for j in range(len(l2)):
#             dic[name_list[j]] = l2[j] # dic[name] = apple dic[price] = 10
#         l1.append(dic)
# print(l1)