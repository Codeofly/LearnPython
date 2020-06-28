# li = [1, 3, 2, 'a', 4, 'b', 5, 'c']
# 5)通过对li操作l5 = [‘c’]
# print(li[3])
# print(li[0])
# print(li[:3])
# print(li[-1:])
# print(li[1:])
'''
3,写代码，有如下列表，按照要求实现每一个功能。
lis = [2,3,‘k’,[‘qwe’,20,[‘k1’,[‘tt’,3,’1’]],89],’ab’,’adv’]
1)将列表lis中的’tt’变成大写（用两种方式）。
2)将列表中的数字3变成字符串’100’（用两种方式）。
3)将列表中的字符串’1’变成数字101（用两种方式）。
'''
# lis = [2,3,'k',['qwe',20,['k1',['tt',3,'1']],89],'ab','adv']
# lis[3][2][1][0] = 'TT'
# print(lis)
# lis[3][2][1][0] = lis[3][2][1][0].upper()
# print(lis)
# lis[3][2][1][1] = '100'
# print(lis)
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
# print(lis)
# lis[3][2][1][2] = int(lis[3][2][1][2]) + 100
# print(lis)
# lis[3][2][1][2] = int(lis[3][2][1][2] + '01')
# print(lis)

'''
5,查找列表li中的元素，移除每个元素的空格， for  i.strip()
并找出以’A’或者’a’开头，
并以’c’结尾的所有元素，
并添加到一个新列表中,最后循环打印这个新列表。
li = [‘taibai ’,’alexC’,’AbC ’,’egon’,’ Ritian’,’ Wusir’,’  aqc’]
for 
'''
# li = ['taibai ','alexC','AbC ','egon',' Ritian',' Wusir','  aqc']
# l1 = []
# for i in li:
#     i = i.strip()
#     if i[0].upper() == 'A' and i[-1] == 'c':
#         l1.append(i)
# print(l1)
# l1 = []
# for i in li:
#     i = i.strip()
#     if (i.startswith('A') or i.startswith('a')) and i.endswith('c'):
#         l1.append(i)
# print(l1)
'''
开发敏感词语过滤程序，提示用户输入评论内容，
如果用户输入的内容中包含特殊的字符：
敏感词列表 li = ["苍老师","东京热",”武藤兰”,”波多野结衣”]
则将用户输入的内容中的敏感词汇替换成***，并添加到一个列表中；
如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中
'''

# li = ['苍老师','东京热','武藤兰','波多野结衣']
# ret = input('input:')  # ***东京热武藤兰波多野结衣小泽玛利亚松岛枫
# l1 = []
# for i in li:
#     ret = ret.replace(i,"*"*len(i))  # ******武藤兰波多野结衣小泽玛利亚松岛枫
# l1.append(ret)
# print(l1)
# lis = []
# for i in li:
#     ret = ret.replace(i,len(i) * '*')
# lis.append(ret)
# print(lis)