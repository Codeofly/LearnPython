
import configparser

config = configparser.ConfigParser()
config.read('day26/example.ini')
config.add_section('yuan')
config.remove_section('bitbucket.org')
config.remove_option('topsecret.server.com', "forwardx11")
config.set('topsecret.server.com', 'k1', '11111')
config.set('yuan', 'k2', '22222')
config.set('DEFAULT','1234','1234')
config.write(open('day26/new2.ini', "w"))

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

# # dic = {"大表哥": (190, 90)}  # python
# #
# # print(dic)
# # print(type(dic))
# # print(str(dic))
#
# # import json
# # import pickle
# import shelve
#
# # ret = json.dumps(dic, ensure_ascii=False)
# # print(type(ret),ret)
# #
# # res = json.loads(ret)
# # print(type(res),res)
# # str1 = res["大表哥"]
# # print(type(str1),str1)
# #
# #
# #
# # print(type(dic),dic)
# # str2 = dic["大表哥"]
# # print(type(str2),str2)
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
# # class B:
# #     def __str__(self):
# #         return " b str"
# #
# #     def __repr__(self):
# #         return "----- b repr"
# #
# #
# # class A(B):
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #         # return self.name
# #
# #     def __str__(self):
# #         return " a str"
# #
# #     def __repr__(self):
# #         return "------- a repr"
# #
# #
# # # a = A("a", "1234")
# # # print("a.name: %s" % a.name)
# # # print("str(a) %s" % str(a))
# # # print("a.__str__() %s" % a.__str__())
# # # print("str(a.name) %s" % str(a.name))
# #
# # a = 1
# # b = 2
# # a == b
# #
# # print(a.__eq__(b))
