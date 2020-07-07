# import os
# os.makedirs('glance/api')
# os.makedirs('glance/cmd')
# os.makedirs('glance/db')
# l = []
# l.append(open('glance/__init__.py','w'))
# l.append(open('glance/api/__init__.py','w'))
# l.append(open('glance/api/policy.py','w'))
# l.append(open('glance/api/versions.py','w'))
# l.append(open('glance/cmd/__init__.py','w'))
# l.append(open('glance/cmd/manage.py','w'))
# l.append(open('glance/db/models.py','w'))
# map(lambda f:f.close() ,l)


# 模块是对外提供功能的

# 如果 我写的这个模块 足够大 能提供的功能足够多
# 多到一个文件写不下
# 把对外提供的功能 根据提供的内容不同，分成几个文件
# 把这些文件放在一个文件夹下，就形成了包

# django框架  包
# 操作数据库的 模块
# 和web页面交互的 模块
# 登录认证 模块
# 安全的中间件 模块

# 导入具体的文件
# from glance.api import policy
# policy.get()
#
# import glance.api.policy as policy
# # glance.api.policy.get()
# policy.get()

# 直接导入包
# import sys
# print(sys.path)


# import glance
# 使用绝对路径
# 导入一个包 相当于 执行了这个包下面的 __init__.py
# glance   #对象
# glance.api.policy.get()
# glance.cmd.manage.main()
# sys.path

# from new_pac import glance
#
# 绝对路径
    # 被直接执行的文件与包的关系必须是固定的，
        # 一旦发生改变，包内的所有关系都要重新指定
    # 跨包引用

#





# import sys
# print(sys.path)


