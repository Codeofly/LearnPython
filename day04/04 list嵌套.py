li = [1,2,'alex',['100','wusir',99,[]],22]
# 1，将alex 变成首字母大写的Alex
#capitalize()
li[2] = 'Alex'
print(li)
print(li[2].capitalize())
li[2] = li[2].capitalize()
print(li)
# 2，将wusir变成全部大写的wusir 放到原处
print(li[3])
l2 = li[3]
print(l2[1].upper())
li[3][1] = l2[1].upper()
print(li)
li[3][1] = li[3][1].upper()
print(li)
# 3，将99加1变成100，放回原处
li[3][2] = li[3][2] + 1
print(li)