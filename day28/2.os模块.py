import os
'''
print(os.getcwd())   # 获取当前文件所在的路径
# os.chdir("D:\\")
# print(os.getcwd())
# print(os.curdir)
# os.pardir


os.makedirs('dirname1/dirname2')  # 创建多级
os.mkdir('dirname/son_dir')      # 创建单级
# os.rmdir('dirname1/dirname2')
# os.removedirs('d1/d2')

print(os.listdir('D:\python11'))

print(os.name)
# print(os.stat(r'D:\python11\day28\2.os模块.py'))
# if os.name == 'nt':
#     path = 'python\\2.mok.py'
# elif os.name == 'posix':
#     path = 'python/2.mok.py'

path = 'python%s2.mok.py'%os.sep
print(path)

os.system("dir")    # exec
ret = os.popen("dir").read()  # eval
print(ret)

# print(os.environ)

'''
# path系列
# print(os.path.abspath('userinfo'))
# print(os.path.split(os.path.abspath('userinfo')))
# print(os.path.dirname(os.path.abspath('userinfo')))
# print(os.path.basename(os.path.abspath('userinfo')))
# print(os.path.exists(r'D:\python11\day28\userinfo2'))
# print(os.path.isabs(r'userinfo2'))
# print(os.path.isfile(r'userinfo'))
# print(os.path.isdir(r'dirname1'))
# print(os.path.join('D:\\python11\\day28','userinfo'))
print(os.path.getsize('D:\pycharm项目\day  25   模块'))
# print(os.path.getsize(r'D:\python11期视频笔记\录制_2018_04_08_15_46_07_104.mp4'))

# 计算文件夹中所所有文件的大小

# '\\nex\\table'
# r'\nex\table'


# import os
# #获取当前目录
# print (os.getcwd())
# 获取上级目录 ret
# ret = os.pardir
# #切换到上级目录
# os.chdir(ret)
# print (os.getcwd())

# print (os.getcwd())
# os.chdir('..')
# print (os.getcwd())