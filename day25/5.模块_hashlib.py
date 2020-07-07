# # hash      哈希算法 可hash数据类型——>数字的过程
#
# # hashlib  —— 摘要算法
#     # 也是一些算法的集合，有好多算法
#     # 字符串 --> 数字
#     # 不同的字符串 -->  数字一定不同
#     # 无论在哪台机器上，在什么时候计算，对相同的字符串结果总是一样的
#     # 摘要过程不可逆
#
# # 用法
# # 文件的一致性校验
# # 密文验证的时候加密
#
# # 密文验证的时候加密
# import hashlib
# # md5算法 通用的算法
# # sha算法 安全系数更高,sha算法有很多种，后面的数字越大安全系数越高，
#         # 得到的数字结果越长，计算的时间越长
# m = hashlib.md5()
# m.update('alex3714'.encode('utf-8'))
# print(m.hexdigest())
#
# m = hashlib.md5()
# m.update('dazhizi sha'.encode('utf-8'))
# print(m.hexdigest())
#
# m = hashlib.md5()
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())
#
#
# # 将所有常见的密码  md5摘要
# # 密码 摘要结果
# # 暴力破解 和 撞库
#
# # 加盐
# m = hashlib.md5('wahaha'.encode('utf-8'))
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())                             # d1c59b7f2928f9b1d63898133294ad2c
#
# # 123456
# m = hashlib.md5('wahaha'.encode('utf-8'))
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())
#
# # 动态加盐
# # 500    用户名 和 密码
# # 123456
# # 111111   d1c59b7f2928f9b1d63898133294ad2c
# # pwd username
# username = 'alex'
# m = hashlib.md5(username[:2:2].encode('utf-8'))
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())                             # d1c59b7f2928f9b1d63898133294ad2c
import hashlib
m = hashlib.md5()
m.update('root'.encode('utf-8'))
print(m.hexdigest())


# 文件的一致性校验 周一讲