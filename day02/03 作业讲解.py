'''
1、使用while循环输入 1 2 3 4 5 6     8 9 10
2、求1-100的所有数的和
3、输出 1-100 内的所有奇数
4、输出 1-100 内的所有偶数
5、求1-2+3-4+5 ... 99的所有数的和
6、用户登陆（三次机会重试）
'''
#2、求1-100的所有数的和
# sum = 0
# count = 1
# while count < 101:
#     sum = sum + count
#     count += 1  # count = count + 1
# print(sum)

#5、求1-2+3-4+5 ... 99的所有数的和
# sum = 0
# count = 1
# while count < 100:
#     if count % 2 == 0:
#         sum -= count
#     else:
#         sum += count
#     count += 1
# print(sum)
#3、输出 1-100 内的所有奇数
# count = 1
# while count < 101:
#     print(count)
#     count += 2

# count = 1
# while count < 101:
#     if count % 2 == 1:
#         print(count)
#     count += 1

#6、用户登陆（三次机会重试）
# username = 'OldBoy'
# password = '123'
# i = 0
# while i < 3:
#     name = input('请输入用户名：')
#     pwd = input('请输入密码：')
#     if name == username and pwd == password:
#         print('登陆成功')
#         break
#     else:
#         print('用户名或密码错误')
#         i += 1