# import time
# 时间
# 计算执行代码的时间   time.time()   # 1524536396.9483523
# 让程序停在这里一段时间 sleep

# 记录时间的格式：
    # 给人看的
    # 给机器看的
    # 计算用的

import time
# 时间戳时间
# print(time.time())   # 时间戳时间   # 计算时间差  精准的运算
#格式化时间
# print(time.strftime('%Y-%m-%d %H:%M:%S'))# 字符串格式化时间   # 记录下来给人看
# print(time.strftime('%y-%m-%d'))# 字符串格式化时间
# print(time.strftime('%x %X'))# 字符串格式化时间
# print(time.strftime('%c'))# 字符串格式化时间
#结构化时间
# print(time.localtime())# 本地结构化时间        # 时间戳时间转格式化时间的中间件
                                                # 对应项的简单计算
# print(time.gmtime())   # 英国的结构化时间

# 2015-8-8
# p = time.strptime('2015-8-8','%Y-%m-%d')
# print(p)
# print(time.mktime(p))
# print(time.time()-time.mktime(p))

# print(time.time())
#
# ret = time.localtime(1500000000)
# print(ret)
# print(time.strftime('%Y-%m-%d %H:%M:%S',ret))

# ret = time.localtime(2000000000)
# print(ret)
# print(time.strftime('%Y-%m-%d %H:%M:%S',ret))

# ret = time.localtime(3000000000)
# print(ret)
# print(time.strftime('%Y-%m-%d %H:%M:%S',ret))  #2033   2065    32

# ret = time.localtime(0)
# print(ret)
# print(time.strftime('%Y-%m-%d %H:%M:%S',ret))  #1970 1 1 8
#
# ret = time.gmtime(0)
# print(ret)
# print(time.strftime('%Y-%m-%d %H:%M:%S',ret))  #1970 1 1 0
#
#
# print(time.strftime('%c'))
# print(time.ctime(1500000000))

# ret = time.localtime(2000000000)
# print(ret)
# print(time.asctime())
# print(time.asctime(ret))

# 作业
# y-m-d h:M:S
# 从当前时间开始 比起y-m-d h:M:S过去了多少年 多少月 多少天 多少h，多少m，多少s

