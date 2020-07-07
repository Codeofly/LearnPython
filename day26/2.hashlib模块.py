# import hashlib
# 密文验证
# m = hashlib.md5() # 创建了一个md5算法的对象
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())
# 永远不会变
# m = hashlib.md5(b'bilibili') # 创建了一个md5算法的对象
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())
# 固定的盐 自己注册你的用户 500
# 数据库
# 动态加盐
# user = b'bilibili'
# m = hashlib.md5(user[::-1]) # 创建了一个md5算法的对象
# m.update('123456'.encode('utf-8'))
# print(m.hexdigest())

# 文件的一致性校验
# md5obj = hashlib.md5()
# md5obj.update(b'hello,')
# md5obj.update(b'alex,')
# md5obj.update(b'I know your ')
# md5obj.update(b'password is alex3714')
#882744b4dca21988e5716a235584a67b
#882744b4dca21988e5716a235584a67b
# print(md5obj.hexdigest())
# 一段字符串直接进行摘要和分成几段摘要的结果是相同的
# import hashlib
# def check(filename):
#     md5obj = hashlib.md5()
#     with open(filename,'rb') as f:
#             content = f.read()
#             md5obj.update(content)
#     return md5obj.hexdigest()
#
# def check(filename):
#     md5obj = hashlib.md5()
#     with open(filename,'rb') as f:
#         while True:
#             content = f.read(4096)
#             if content:
#                 md5obj.update(content)
#             else:
#                 break
#     return md5obj.hexdigest()
#
# ret1 = check('file1')
# ret2 = check('file2')
# print(ret1)
# print(ret2)


# 作业
# 写一个函数
# 参数是两个文件的路径
# 返回的结果是T/F

# 序列化  把数据类型变成字符串
# 为什么要有序列化 因为在网络上和文件中能存在的只有字节
# json   在所有语言中通用 只对有限的数据类型进行序列化 字典 列表 字符串 数字 元组
#        在多次写入dump数据进入文件的时候，不能通过load来取。
# pickle 只能在python中使用 对绝大多数数据类型都可以进行序列化
#        在load的时候，必须拥有被load数据类型对应的类在内存里
# dumps   序列化
# loads   反序列化
# dump    直接向文件中序列化
# load    直接对文件反序列化

# shelve
# f = open()

