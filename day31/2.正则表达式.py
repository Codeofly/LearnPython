# time
# 时间 - python

# regex
# 正则表达式
# re模块 可以读懂 你写的正则表达式
# 根据你写的表达式去执行任务

# 正则表达式是做什么的？

# number = input('please input your phone number ： ')
# if number.isdigit() and number.startswith('13')\
#     or number.startswith('14')\
#     or number.startswith('15')\
#     or number.startswith('16')\
#     or number.startswith('17')\
#     or number.startswith('18')\
#     or number.startswith('19'):
#     print('通过初检查')
# else:
#     print('格式错误')

# import re
# number = input('please input your phone number ： ')
# ret = re.match('(13|14|15|17|18|19)[0-9]{9}',number)
# if ret:print('通过初检查')

# 正则表达式 字符串的操作
# 使用一些规则来检测字符串是否符合我的要求  —— 表单验证
# 从一段字符串中找到符合我要求的内容 —— 爬虫

# 完全相等的字符串都可以匹配上 ==

# 字符组  字符组代表一个字符位置上可以出现的所有内容
# 范围 ：
    # 根据asc码来的，范围必须是从小到大的指向
    # 一个字符组中可以有多个范围

# 身份证号码是一个长度为15或18个字符的字符串，首位不能为0
# 如果是15位则全部由数字组成；
# 如果是18位，则前17位全部是数字，末位可能是数字或x，
# 下面我们尝试用正则来表示：
# 15 位
a = '[1-9]\d{14}'
# 18 位
b = '[1-9]\d{16}[\dx]'

# [1-9]\d{13,16}[\dx]
# [1-9]\d{16}[\dx]|[1-9]\d{14}
# a|b [ab]

#[1-9]\d{16}[\dx]|[1-9]\d{14}  或
# 如果两个正则表达式之间用"或"连接，且有一部分正则规则相同，
# 那么一定要把规则长的放在前面

# [1-9]\d{13,16}[\dx]
# [1-9]\d{14}(\d{2}[\dx]){0,1}

# [1-9]\d{14}(\d{2}[\dx])? 分组
# 如果对一组正则表达式整体有一个量词约束，就将这一组表达式分成一个组
# 在组外进行量词约束

# r'\\n',r'\n'

# 贪婪匹配
a = 9-2*5/3+7/3*99/4*2998+10*568/14
print(a)