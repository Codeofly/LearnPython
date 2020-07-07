# py文件就是模块
# python之所以好用 模块多
# 三种
    # 内置模块   python安装的时候自带的
    # 扩展模块   itchat                         # 别人写好的 需要安装之后可以直接使用
               # beautiful soap
               # selenium  网页自动化测试工具
               # django tornado
    # 自定义模块 自己写的模块

# 内置模块
# 序列化模块
# hashlib模块

# 序列化模块
# 能存储在文件中的一定是字符串 或者是 字节
# 能在网络上传输的 只有字节
# dic = {"大表哥":(190,90)} #  python
# print(str(dic))
# print(str(dic).encode(encoding='utf-8'))
# b"{'\xe5\xa4\xa7\xe8\xa1\xa8\xe5\x93\xa5': (190, 90)}"
# s = b"{'\xe5\xa4\xa7\xe8\xa1\xa8\xe5\x93\xa5': (190, 90)}"
# ret = s.decode(encoding='utf-8')
# print(ret)
# print(eval(ret))

# dic = {"大表哥":(190,90)}
# dic --> 字符串  # 序列化
# 字符串 --> dic  # 反序列化
# 序列化 == 创造一个序列 ==》创造一个字符串
# 实例化 == 创造一个实例

# python中的序列化模块
    # json     所有的编程语言都通用的序列化格式
            #  它支持的数据类型非常有限 数字 字符串 列表 字典
    # pickle   只能在python语言的程序之间传递数据用的
            #  pickle支持python中所有的数据类型
    # shelve   python3.* 之后才有的

import json
# dic = {"大表哥":(190,90,'捏脚')}
# 序列化
# ret = json.dumps(dic,ensure_ascii=False)
# print(type(dic),dic)
# print(type(ret),ret)
# print('*',str(dic))   # 土办法
# 反序列化
# res = json.loads(ret)
# print(type(res),res)

# dump和load 是直接将对象序列化之后写入文件
# 依赖一个文件句柄
# dic = {"大表哥":(190,90,'捏脚')}
# f = open('大表哥','w',encoding='utf-8')
# json.dump(dic,f,ensure_ascii=False)  # 先接收要序列化的对象 再接受文件句柄
# f.close()

# f = open('大表哥','r',encoding='utf-8')
# ret = json.load(f)
# print(type(ret),ret)

# data = {'username':['李华','二愣子'],'sex':'male','age':16}
# json_dic2 = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'),ensure_ascii=False)
# print(json_dic2)

# 3个字典
# dic1 = {"大表哥":(190,90,'捏脚')}
# dic2 = {"2表哥":(190,90,'捏脚')}
# dic3 = {"3表哥":(190,90,'捏脚')}
# str1 = json.dumps(dic1)
# f = open('大表哥','a',encoding='utf-8')
# str1 = json.dumps(dic1)
# f.write(str1+'\n')
# str2 = json.dumps(dic2)
# f.write(str2+'\n')
# str3 = json.dumps(dic3)
# f.write(str3+'\n')
# f.close()

# f = open('大表哥','r',encoding='utf-8')
# for line in f:
#     print(json.loads(line.strip()))
# f.close()

# dumps序列化 loads反序列化  只在内存中操作数据 主要用于网络传输 和多个数据与文件打交道
# dump序列化  load反序列化   主要用于一个数据直接存在文件里—— 直接和文件打交道
# 参数

# import json
# dic = {(190,90,'捏脚'):"大表哥"}    # json不支持元组 不支持除了str数据类型之外的key
# print(json.dumps(dic))

import pickle
# dic = {(190,90,'捏脚'):"大表哥"}
# ret = pickle.dumps(dic)   # 序列化结果 不是一个可读的字符串 而是一个bytes类型
# print(ret)
# print(pickle.loads(ret))

# dic = {(190,90,'捏脚'):"大表哥"}
# f = open('大表哥2','wb')  # 使用pickle dump必须以+b的形式打开文件
# pickle.dump(dic,f)
# f.close()

# f = open('大表哥2','rb')
# print(pickle.load(f))
# f.close()

import pickle
# 关于写多行
# dic1 = {"大表哥":(190,90,'捏脚')}
# dic2 = {"2表哥":(190,90,'捏脚')}
# dic3 = {"3表哥":(190,90,'捏脚')}
# f = open('大表哥3','wb')
# pickle.dump(dic1,f)
# pickle.dump(dic2,f)
# pickle.dump(dic3,f)
# f.close()

# 读写入的多行
# f = open('大表哥3','rb')
# while True:
#     try:
#         print(pickle.load(f))
#     except EOFError:
#         break

# json 在写入多次dump的时候 不能对应执行多次load来取出数据，pickle可以
# json 如果要写入多个元素 可以先将元素dumps序列化，f.write(序列化+'\n')写入文件
        #    读出元素的时候，应该先按行读文件，在使用loads将读出来的字符串转换成对应的数据类型

# 关于序列化自定义类的对象
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# a = A('alex',80)
# import json
# json.dumps(a)
# import pickle
# ret = pickle.dumps(a)
# print(ret)
# obj = pickle.loads(ret)
# print(obj.__dict__)

# import pickle
# f = open('大侄子1','wb')
# pickle.dump(a,f)
# f.close()
# f = open('大侄子1','rb')
# obj = pickle.load(f)
# print(obj.__dict__)









