#range 当成一个数字列表，范围
for i in range(100): # [0,1,2,。。。99]
    print(i,end=",")
print("")

for i in range(0,10):  # [0,1,2,。。。9]
    print(i,end=",")
print("")

for i in range(0,10,2):  # [0,1,2,。。。9]
    print(i,end=",")
print("")

for i in range(10,0,-1):  # [10,9,8,...1]
    print(i,end="\t")
print("")

li = [2,3,'alex',4,5]
for i in li:
    print(li.index(i),end="\t")
print("")

for i in range(0,len(li)):
    print(i,end="\t")
li = [1,2,3,['alex','wusir','老男孩'],4]
'''
# for i in li:
#     print(i)
#     for ....
'''
