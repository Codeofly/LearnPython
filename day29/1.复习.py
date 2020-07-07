# os模块
    # 和操作系统交互
    # 工作目录 文件夹 文件 操作系统命令 路径相关的
# 2.模块
    # 最本质的区别 import会创建一个专属于模块的名字，
        # 所有导入模块中的都会在这个空间中
    # import
    # from import
    # as 起别名
    # * 和 __all__

# import os
# def get_size(dir):
#     sum_size = 0
#     for item in os.listdir(dir):
#         path = os.path.join(dir,item)
#         if os.path.isfile(path):
#             sum_size += os.path.getsize(path)
#         else:
#             sum_size += get_size(path)
#     return sum_size
# ret = get_size('D:\python11')
# print(ret)

# 栈
import os
def get_size(path):
    l = [path]
    sum_size = 0
    while l:
        path = l.pop()    # l = ['D:\python11\day2','D:\python11\day3'...]
        for item in os.listdir(path):    #path = 'D:\python11'
            path2 = os.path.join(path, item)   # path2 = 'D:\python11\day2'
            if os.path.isfile(path2):
                sum_size += os.path.getsize(path2)   # sum = 文件的大小 + 0
            else:                             # l = ['D:\python11\day2','D:\python11\day3'...'D:\python11\venv1\Include']
                l.append(path2)
    return sum_size
print(get_size('D:\python11'))

# import os
# def cal_size(f):
#     count = 0
#     file_list = os.listdir(f)
#     while file_list:
#         try:
#             ret = os.path.join(f,file_list.pop())
#             # if os.stat(ret)[0] == 16895:
#             if os.path.isdir(ret):
#                 count = count + cal_size(ret)
#             else:
#                 count = count + os.path.getsize(ret)
#         except:
#             continue
#
#     return count
#
# f = 'D:\python11'
# print(cal_size(f))


# import os
# def get_size(path):
#     l = [path]
#     sum_size = 0
#     while l:
#         path = l.pop()
#         for item in os.listdir(path):
#             path2 = os.path.join(path, item)
#             if os.stat(path2)[0] == 16895:
#                 l.append(path2)
#             else:
#                 sum_size += os.path.getsize(path2)
#     return sum_size
# print(get_size('D:\python11'))


# 三级菜单（栈）
