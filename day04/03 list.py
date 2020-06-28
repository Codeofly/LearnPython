#
li = ['alex', 123, True, (1, 2, 3, 'wusir'), [1, 2, 3, '小明',], {'name':'alex'}]
#索引，切片，步长
print(li[0])
print(li[2])
print(li[1:4])
print(li[:5:2])
print(li[-1:-3:-1])
li = [1,'a','b','a',2,3,'老男孩']
# 增
#append
li.append('alex')
print(li.append('alex'))
li.append([1,2,3])

# name_list = ['杰哥' ,'民歌','花心哥','狗友','芳芳']
# while True:
#     name = input('请输入新员工姓名：Q/q')
#     if name.upper() == 'Q':break
#     else:
#         name_list.append(name)
#         print('已成功添加新员工%s' % name)
# print(name_list)
# print(li)
#insert 插入
x
#extend 迭代添加,到最后
# li.extend('ABC')
# li.extend([1,2,3])
# print(li)

#删
#pop 按索引删除
li.pop()  # 默认删除最后一个
li.pop(1)  # 默认删除最后一个
s = li.pop(1)
print(s)
print(li)

#remove
li.remove('a')
print(li)

#clear 清空内容
li.clear()
print(li)

# del #删除列表
del li
print(li)
#切片删除
del li[:3]
del li[:3:2]
print(li)
# 改 按照索引改
print(li[1])
li[1] = 'A'
print(li[1])
li[1] = [11,22,33,44]
print(li)
#按照切片去改
li[:3] = 'Q'
print(li)
li[:3] = 'alexsb'
print(li)
li[:3] = [11,22,33,44]
print(li)


# 查
#索引，切片步长，查看
for 循环
print(li[:3])
for i in li:
    print(i)
l1 = [1, 2, 1, 7, 5, 4, 9, 8, 3]
#其他操作方法
#sort 从小到大，正向排序
l1.sort()
print(l1)
#从大到小，反向排序
l1.sort(reverse=True)
print(l1)
#翻转
l1.reverse()
print(l1)

#len 长度
print(len(l1))

#count
print(l1.count(1))

#index 通过元素找索引
print(li.index('a'))
