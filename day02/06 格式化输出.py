# % 占位符 s str 字符串 d digit 数字
#第一种：
# name = input('请输入你的姓名：')
# age = input('请输入你的年龄：')
# hobby = input('请输入你的爱好：')
# msg = '我叫%s，今年%d岁，爱好%s' % (name,int(age),hobby)
# print(msg)
#第二种
# dic = {'name':'老男孩','age':51,'hobby':'无所谓'}
# msg = '我叫%(name)s，今年%(age)d岁，爱好%(hobby)s' % dic
# print(msg)

# 在格式化输出中单纯的显示%  用%% 解决。
# name = input('请输入你的姓名：')
# age = input('请输入你的年龄：')
# msg = '我叫%s，今年%d岁，学习进度为1%%' % (name,int(age))
# print(msg)


