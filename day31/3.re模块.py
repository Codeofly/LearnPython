# import re
# ret = re.findall('a', 'eva egon yuan')
# print(ret)
# # findall接收两个参数 ： 正则表达式 要匹配的字符串
# # 一个列表数据类型的返回值：所有和这条正则匹配的结果
# ret = re.findall('\d+', 'dsaglhlkdfh1892494kashdgkjh127839')
# print(ret)

# 从a文件中找出所有的手机号码 —— 正则
# 13|14|15|16|17|18|19
# 1[3-9]\d{9}
# import re
# ret = re.search('b', 'eva egon yuan')
# search和findall的区别：
    #1.search找到一个就返回，findall是找所有
    #2.findall是直接返回一个结果的列表，search返回一个对象
# 如果匹配到了，返回一个结果对象
# 如果没匹配到，返回一个None
# if ret:
#     print(ret.group())  # 从结果对象中获取结果

# import re
# ret = re.match('a', 'eva egon yuan')
# if ret:
#     print(ret.group())
# match
    # ·1 意味着在正则表达式中添加了一个^
    # ·2 和search一样 匹配返回结果对象 没匹配到返回None
    # ·3 和search一样 从结果中获取值 仍然用group
    #
# 'a'   --->  '^a'

# import re
# ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
# print(ret)

# import re
# obj = re.compile('\d{3}')  # 编译 在多次执行同一条正则规则的时候才适用
# ret1 = obj.search('abc123eeee')
# ret2 = obj.findall('abc123eeee')
# print(ret1.group())
# print(ret2)

# 正则表达式 -->根据规则匹配字符串
# 从一个字符串中找到符合规则的字符串 --> python
# 正则规则 -编译-> python能理解的语言
# 多次执行，就需要多次编译 浪费时间 re.findall('1[3-9]\d{9}',line)
# 编译 re.compile('\d{3}')

# import re
# ret = re.finditer('\d', 'ds3sy4784a')   #finditer适用于结果比较多的情况下，能够有效的节省内存
# print(ret)  # <callable_iterator object at 0x10195f940>
# print(ret.__next__().group())
# for i in ret:
#     print(i.group())

# print(next(ret).group())  #查看第一个结果
# print(next(ret).group())  #查看第二个结果
# print([i.group() for i in ret])  #查看剩余的左右结果

# 当分组遇到re模块
# import re
# ret1 = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
# ret2 = re.findall('www.(?:baidu|oldboy).com', 'www.baidu.com')
# print(ret1)
# print(ret2)
# findall会优先显示组内匹配到的内容，如果想取消分组优先效果，在组内开始的时候加上?:

# import re
# ret=re.split("\d+","eva3egon4yuan")
# print(ret) #结果 ： ['eva', 'egon', 'yuan']
# ret=re.split("(\d+)","eva162784673egon44yuan")
# print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']
# split分割一个字符串，默认被匹配到的分隔符不会出现在结果列表中，
# 如果将匹配的正则放到组内，就会将分隔符放到结果列表里

# 分组命名 和 search遇到分组
# 标签 .html 网页文件 标签文件
import re
#分组的意义
    # 1.对一组正则规则进行量词约束
    # 2.从一整条正则规则匹配的结果中优先显示组内的内容
#"<h1>hello</h1>"
# ret = re.findall('<\w+>(\w+)</\w+>',"<h1>hello</h1>")
# print(ret)

# 分组命名
# ret = re.search("<(?P<tag>\w+)>(?P<content>\w+)</(?P=tag)>","<h1>hello</h1>")
# print(ret)
# print(ret.group())   # search中没有分组优先的概念
# print(ret.group('tag'))
# print(ret.group('content'))

# ret = re.search(r"<(\w+)>(\w+)</\1>","<h1>hello</h1>")
# #如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
# #获取的匹配结果可以直接用group(序号)拿到对应的值
# print(ret.group())
# print(ret.group(0))  #结果 ：<h1>hello</h1>
# print(ret.group(1))  #结果 ：h1
# print(ret.group(2))  #结果 ：hello

# 1 - 2 * ( (60-30 +(-40/5) * 20) - (-4*3)/ (16-3*2) )
# 计算一个字符串数据类型的表达式 ： 整数 小数 加减乘除 小括号
# 不准eval1
# 将字符串中所有的空格都去掉
# 使用正则表达式 先匹配最内层的小括号
# 使用正则表达式 匹配最内层括号中最先出现的第一个乘法或者除法的（原子）表达式
# 计算这个原子表达式 '2*3' / '4/50'
# 将乘除法的结果填回表达式中
# 再计算下一个出现的乘除法，直到这个小括号中再也没有乘除
# 计算加减法，替换
# 这个小括号中的所有内容都计算成一个结果

# 从小的功能开始
    # 先最简单的 a+b c*d
    # 再计算没有括号的表达式   a+c*b
    # 再算 a-b+c*d/e
    # 再算有一个括号的
    # 再算有两个括号并排的
    # 再算有两个括号嵌套的
    # 。。。

import re

# ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']
# ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
# print(ret) #['1', '-2', '60', '', '5', '-4', '3']
# ret.remove("")
# print(ret) #['1', '-2', '60', '5', '-4', '3']

st = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
import re
y = 0
ret = re.findall('\d+','1+ 2')
ret1 = re.findall('[\d]\*[\d]','1*2')
obj = re.compile('[\d\s].[\s\d]')
ret2 = obj.findall('1 + 2* 3 -5 * 6')
print(ret2)
# print(ret1)
# for i in ret:
#     y += int(i)
# print(y)





