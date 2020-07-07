# import shelve   # python 专有的序列化模块 只针对文件
# f = shelve.open('shelve_file')     # 打开文件
# f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
# f.close()

# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)

# 设置只读方式
# import shelve
# f = shelve.open('shelve_file', flag='r')
# existing = f['key']
# f.close()
# print(existing)

# import shelve
# f = shelve.open('shelve_file', flag='r')
# # f['key']['int'] = 50    # 不能修改已有结构中的值
# # f['key']['new'] = 'new' # 不能在已有的结构中添加新的项
# f['key'] = 'new'         # 但是可以覆盖原来的结构
# f.close()
# #
# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)

# import shelve
# f1 = shelve.open('shelve_file')
# print(f1['key'])
# f1['key']['new_value'] = 'this was not here before'
# f1.close()

# import shelve
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)

# import shelve
# f2 = shelve.open('shelve_file', writeback=True)
# print(f2['key'])
# f2['key']['new_value'] = 'this was not here before'
# f2.close()
#
# f1 = shelve.open('shelve_file')
# existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
# f1.close()
# print(existing)