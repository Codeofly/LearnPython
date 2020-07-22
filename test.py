
import sys,os

print(sys.version)
print(sys.platform)
print(sys.path)

print(os.name)


# import time
# 
# 计算时间差
# 
# 变成 time.struct_time
# start_time = time.strptime('2017-09-11 08:30:00', '%Y-%m-%d %H:%M:%S')
# 变成时间戳
# true_time = time.mktime(start_time)
# end_time = time.localtime()
# time_now = time.mktime(end_time)
# 求时间戳差值
# dif_time = time_now - true_time
# 格式化 时间戳
# struct_time = time.gmtime(dif_time)
# time.struct_time  -  1970/1/1 0：0：0  为时间差
# print('过去了%d年%d月%d天%d小时%d分钟%d秒' \
#       % (struct_time.tm_year - 1970,
#          struct_time.tm_mon - 1,
#          struct_time.tm_mday - 1,
#          struct_time.tm_hour,
#          struct_time.tm_min,
#          struct_time.tm_sec))
# 
# t = time.time()
# print(t)
# g = time.gmtime()
# print(g)
# s = time.mktime(g)
# print(s)
# 
# print(time.localtime(10000000))
# print(time.mktime(time.localtime(10000000)))
# print(time.strptime(time.localtime(10000000)))
# 
# 简单配置
# import logging
# 默认情况下 只显示 警告 及警告级别以上信息
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %y %H:%M:%S',
#                     filename = 'day26/userinfo2.log'
# 
#                     )
# logging.debug('debug message')       # debug 调试模式 级别最低
# logging.info('info message')         # info  显示正常信息
# logging.warning('warning message')   # warning 显示警告信息
# logging.error('error message')       # error 显示错误信息
# logging.critical('critical message') # critical 显示严重错误信息
# 
# 
# 
# import configparser
# 
# config = configparser.ConfigParser()
# config.read('day26/example.ini')
# config.add_section('yuan')
# config.remove_section('bitbucket.org')
# config.remove_option('topsecret.server.com', "forwardx11")
# config.set('topsecret.server.com', 'k1', '11111')
# config.set('yuan', 'k2', '22222')
# config.set('DEFAULT','1234','1234')
# config.write(open('day26/new2.ini', "w"))
# 
# import configparser
# 
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'a': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11': 'yes'
#                      }
# 
# config['bitbucket.org'] = {'User': 'hg'}
# config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}
# with open('day26/example2.ini', 'w') as f:
#     config.write(f)
# 
# dic = {"大表哥": (190, 90)}  # python
# 
# print(dic)
# print(type(dic))
# print(str(dic))
# 
# import json
# import pickle
# import shelve
# 
# ret = json.dumps(dic, ensure_ascii=False)
# print(type(ret),ret)
# 
# res = json.loads(ret)
# print(type(res),res)
# str1 = res["大表哥"]
# print(type(str1),str1)
# 
# 
# 
# print(type(dic),dic)
# str2 = dic["大表哥"]
# print(type(str2),str2)
# 
# f = shelve.open('day25/shelve_file')
# print(type(f['key']),f['key'])
# for i in f :
#     print(i+":"+str(f[i]))
#     # print(type(i),i)
# f.close()
# 
# 
# 
# 
# 
# 
# class B:
#     def __str__(self):
#         return " b str"
# 
#     def __repr__(self):
#         return "----- b repr"
# 
# 
# class A(B):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # return self.name
# 
#     def __str__(self):
#         return " a str"
# 
#     def __repr__(self):
#         return "------- a repr"
# 
# 
# a = A("a", "1234")
# print("a.name: %s" % a.name)
# print("str(a) %s" % str(a))
# print("a.__str__() %s" % a.__str__())
# print("str(a.name) %s" % str(a.name))
# 
# a = 1
# b = 2
# a == b
# 
# print(a.__eq__(b))
