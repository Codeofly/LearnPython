'''s = 'k:1|k1:2|k2:3|k3:4'
di = {}


for i in s.split("|") :
    di[i.split(":")[0]]=int(i.split(":")[1])

print(di)'''

# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}

'''li = [11, 22, 33, 44, 55, 66, 77, 99, 90, 88]
dic = {'k1': [], 'k2': []}

for i in li:
    if i > 66:
        dic['k1'].append(i)
    elif i < 66:
        dic['k2'].append(i)
    else:
        print("i = 66")
print(dic)'''

li = [11, 22, 33, 44, 55, 66, 77, 99, 90, 88]
dic = {}

for i in range(len(li) - 1, -1, -1):
    ...