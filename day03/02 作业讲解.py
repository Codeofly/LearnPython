# if 3 > 2 :
#     print(555)
# if 2 > 1:
#     print(333)
# elif 4 > 2:
#     print(222)
# else:
#     print(666)
# 写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
# sum = 0
# count = 1
# while count < 100:
#     if count == 88:
#         count += 1
#     if count % 2 == 0:
#         sum -= count
#     else:
#         sum += count
#     count += 1
# print(sum)

sum = 0
count = 0
while count < 99:
    count += 1
    if count == 88:
        continue
    if count % 2 == 0:
        sum -= count
    else:
        sum += count
print(sum)
'''
9. ⽤用户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使字符串格式化）
'''

username = '老男孩'
password = '123'
i = 0
while i < 3:
    name = input('请输入用户名：')
    pwd = input('请输入密码：')
    if name == username and pwd == password:
        print('登陆成功')
        break
    else:
        print('用户名或密码错误，还剩%s机会' % (2-i))
        i += 1
        if i == 3:
            choice = input('是否还想在试试？Y')
            if choice == 'Y':
                i = 0
else:
    print('还要不要脸了....')