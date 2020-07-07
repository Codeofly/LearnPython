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

from new_pec2 import glance
# glance.api.policy.get()

# 在一个py文件中使用了相对路径引入一个模块
# 那么这个文件就不能被当成脚本运行了

