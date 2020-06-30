# f = open('D:\护士老师主妇空姐联系方式.txt',encoding='utf-8',mode='r')
# content = f.read()
# print(content)
# f.close()
'''
f：变量，f_obj,file,f_handler,...文件句柄。
open windows的系统功能，
windows默认编码方式：gbk，linux默认编码方式utf-8。
f.close()

流程：打开一个文件，产生一个文件句柄，
      对文件句柄进行操作，关闭文件。
'''

# f = open('D:\护士老师主妇空姐联系方式.txt',encoding='gb2312')
# 1:全部读出来f.read()
# f = open('log',encoding='utf-8')
# content = f.read()
# print(content,type(content))
# f.close()

#2:一行一行的读
# f = open('log',encoding='utf-8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

#3:将原文件的每一行作为一个列表的元素。
# f = open('log',encoding='utf-8')
# print(f.readlines())
# f.close()

#4:读取一部分read（n）。
# 在r模式下，read（n）按照字符去读取。
# 在rb模式下，read（n）按照字节去读取。
# f = open('log',encoding='utf-8')
# print(f.read(3))
# f.close()
# f = open('log',mode='rb')
# content = f.read(4)
# print(content)
# f.close()

#5:循环读取。

# f = open('log',encoding='utf-8')
# for i in f:
#     print(i.strip())
# f.close()



#非文字类的文件时，用rb
# f = open('D:\护士老师主妇空姐联系方式.txt',mode='rb')
# content = f.read()
# print(content)
# f.close()

# w
#没有文件，创建一个文件写入内容
# f = open('log1',encoding='utf-8',mode='w')
# f.write('儿科王金发；剪短发了肯定撒就废了；就')
# f.close()
#有文件，将原文件内容清空，在写入内容。
# f = open('log1',encoding='utf-8',mode='w')
# f.write('666')
# f.close()

# wb
# f = open('log',mode='wb')
# f.write('老男孩教育'.encode('utf-8'))
# f.close()

# a
#没有文件，创建一个文件追加内容
# f = open('log2',encoding='utf-8',mode='a')
# f.write('666')
# f.close()
# 有文件，直接追加内容。
# f = open('log2',encoding='utf-8',mode='a')
# f.write('666')
# f.close()

# r+ 先读，后追加 一定要先读后写
# # f = open('log',encoding='utf-8',mode='r+')
# # content = f.read()
# # print(content)
# # f.write('aaa')
# # f.close()
#
# #错误的
# # f = open('log',encoding='utf-8',mode='r+')
# # f.write('BBB')
# # content = f.read()
# # print(content)
# # f.close()
#
# # w+ 先写后读。
# # f = open('log',encoding='utf-8',mode='w+')
# # f.write('中国')
# # #print(f.tell())  # 按字节去读光标位置
# # f.seek(3)  # 按照字节调整光标位置
# # print(f.read())
# # f.close()
# #w+b
#
#
# #a+ 追加读
# # f = open('log',encoding='utf-8',mode='a+')
# # f.write('BBB')
# # content = f.read()
# # print(content)
# # f.close()
# #a+b
#
# #其他方法
# # f = open('log',encoding='utf-8')
# # print(f.read())
# # print(f.writable())
# # f.close()
#
# # f = open('log',encoding='utf-8',mode='a')
# # f.truncate(7) # 按字节对原文件截取
# # f.close()
# #功能一：自动关闭文件句柄。
# #功能二：一次性操作多个文件句柄。
# # with open('log',encoding='utf-8') as f:
# #     print(f.read())
# # with open('log1',encoding='utf-8') as f1:
# #     print(f1.read())
#
# # with open('log',encoding='utf-8') as f1,\
# #     open('log1',encoding='utf-8') as f2:
# #     print(f1.read())
# #     print(f2.read())44
#
# # 1，将原文件读取到内存。
# # 2，在内存中进行修改，形成新的内容。
# # 3，将新的字符串写入新文件。
# # 4，将原文件删除。
# # 5，将新文件重命名成原文件。
# import os
# with open('log',encoding='utf-8') as f1,\
#     open('log.bak',encoding='utf-8',mode='w') as f2:
#     content = f1.read()
#     new_content = content.replace('alex','SB')
#     f2.write(new_content)
# os.remove('log')
# os.rename('log.bak','log')
#
# # import os
# # with open('log',encoding='utf-8') as f1,\
# #     open('log.bak',encoding='utf-8',mode='w') as f2:
# #     for i in f1:
# #         new_i = i.replace('SB','alex')
# #         f2.write(new_i)
# # os.remove('log')
# # os.rename('log.bak','log')
# import os
# with open('log',encoding='utf-8',mode='r') as y, \
#     open('log_bak',encoding='utf-8',mode='w') as y1:
#     content = y.read()
#     new_content = content.replace('alex','SB')
#     y1.write(new_content)
# os.remove('log')
# os.rename('log.bak','log')
#
#
# import os
# with open('log',encoding='utf-8',mode='r') as y,\
#     open('log.bak',encoding='utf-8',mode='w') as y1:
#     c = y.read()
#     z = c.replace('alex','SB')
#







































































