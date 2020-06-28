#1
name = "aleX leNb"
# print(name.strip('ab'))

# index1 = name.find('e')
# print(index1)
# index2 = name.find('e', 3)
# print(index2)
'''
4，实现一个整数加法计算器(两个数相加)：
如：content = input(‘请输入内容:’) 
 # 如用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

'''
content = input("请输入内容：").strip().split('+')
x = 0
z = 0
# s = 0
# z = 0
# x = 0
# a = 0
# while s < len(content):
#     x = int(content[s])
#     z = z + x
#     a = z + int(content[0])
# print(a)
#
#
#
for i in content:
 x = int(i)
 z = z  + x
print(z)
# print(len(content))
# print(content[n])

# 5，计算用户输入的内容中有几个整数。
# 如：content = input(‘请输入内容：’)   # 如fhdal234slfh98769fjdla231
# content = input('请输入内容：')
# count = 0
# for i in content:
#     if i.isdigit():
#         count += 1
#
# print(count)
,.


# content = input("input:")
# n = len(content)
# m = 0
# ls = []
# s = ''
# while m < n:
#     if content[m].isdigit():
#         s = s+content[m]
#         if not content[m+1].isdigit():
#             ls.append(int(s))
#             m+=1
#             s = ''
#     else:
#         m+=1
#
# for x in ls:
#     print(ls)

# content = input("请输入你想输入的内容:")
# s = ''
# ls = []
# n = len(content)
# m = 0
# num = 0
# while m<n:
#     if content[m].isdigit():
#         s = s + content[m]
#         if not content[m+1].isdigit():
#             ls.append( int(s))
#             s = ''
#         m+=1
#     else:
#         m+=1
#
# print(len(ls))
# for x in ls:
#     print(type(x))
#     print(x)
# s = 'fdsafdsa'
# for i in s:
#     print(i)
# else:
#     print(666)

li = ["苍老师","东京热","武藤兰","波多野结衣"]
l1 = []
comment = input('请输入评论>>>')
for i in li:
    if i in comment:
        comment = comment.replace(i,'*'*len(i))
l1.append(comment)
print(l1)