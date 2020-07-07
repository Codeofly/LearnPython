# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0),错误退出sys.exit(1)
# sys.version        获取Python解释程序的版本信息
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称

# import sys
# print('*'*6)
# sys.exit()      #退出程序，正常退出时exit(0),错误退出sys.exit(1)
# print('-'*6)

# import sys
# print(sys.version)

# import sys
# print(sys.platform)

# import sys    # *****
# print(sys.path)

# 内存
# 程序在运行起来的时候
#  启动解释器 加载一些基础的内容  内置函数 内置模块  -->内存里
#  sys.path 系统的路径   import
# import os,sys

# import sys
# print(sys.argv)   # 列表 列表的第一项是当前文件所在的路径
# if sys.argv[1] == 'alex' and sys.argv[2] == '3714':
#     print('登陆成功')
# else:
#     sys.exit()
# user = input('>>>')
# pwd = input('>>>')
# if user == 'alex' and pwd == '3714':
#     print('登陆成功')
# else:
#     sys.exit()
# print('我能完成的功能')


# 执行一个程序
# debug
# 直接执行
import sys
import logging
inp = sys.argv[1] if len(sys.argv)>1 else 'WARNING'
logging.basicConfig(level=getattr(logging,inp))  # DEBUG
num = int(input('>>>'))
logging.debug(num)
a = num * 100
logging.debug(a)
b = a - 10
logging.debug(b)
c = b + 5
print(c)  #   3000

