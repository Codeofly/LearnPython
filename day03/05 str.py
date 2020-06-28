# #索引与切片 s[起始索引:截止索引:步长]
# # s = '老男孩是最好的培训机构'
# #索引
# # s1 = s[0]
# # print(s1)
# # s2 = s[2]
# # print(s2)
# # s3 = s[-1]
# # print(s3)
# #切片  顾头不顾腚
# # s4 = s[0:3]
# # print(s4)
# # s41 = s[:3]
# # print(s41)
# # s5 = s[3:7]
# # print(s5)
# # s6 = s[:]
# # print(s6)
# #步长
# # s7 = s[:5:2]
# # print(s7)
# # s8 = s[:7:3]
# # print(s8)
# # 反向步长
# # s7 = s[-1:-5:-1]
# # print(s7)
#
# #
# # #常用操作方法
# # s = 'laonanHai'
# # #*** 首字母大写，其他字母小写
# # # s1 = s.capitalize()
# # # print(s1)
# #
# # #***全部大写，全部小写
# # # s2 = s.upper()
# # # s3 = s.lower()
# # # print(s2,s3)
# # # code = 'aeQu'.upper()
# # # your_code = input('请输入验证码').upper()
# # # if your_code == code:
# # #     print('验证码输入成功')
# # s = 'laonanHai'
# # # * 居中center
# # # s4 = s.center(30)
# # print(s4)
# # s4 = s.center(30,'*')
# # print(s4)
#
# #**大小写翻转
# # s5 = s.swapcase()
# # print(s5)
# # s = 'alex wusir*laonanhai2taibai'
# # #每个单词的首字母大写(非字母隔开)
# # # s6 =s.title()
# # # print(s6)
# #
# # s = 'alexlaonanhai'
# # #***判断以什么为开头，以什么为结尾。
# # # startswith endswith()
# # # s7 = s.startswith('a')
# # # s71 = s.startswith('al')
# # # s72 = s.startswith('alex')
# # # s73 = s.startswith('alex')
# # # s74 = s.startswith('l', 4)
# # # print(s74)
# # # print(s7,s71,s72,s74)
# # # s = '  laonanhai '
# # s = '\nlaonanhai\t'
# # ***去除首尾的空格，换行符，tab
# # 去除左边的空格，换行符，tab   lstrip()
# # 去除右边的空格，换行符，tab   rstrip()
# #strip（）
# # print(s)
# # print(s.strip())
# # print(s.lstrip())
# # print(s.rstrip())
# # # name = input('请输入用户名：').strip()
# # # if name == 'alex':
# # #     print(666)
# # s = ',laoxnanhaialexl'
# # # print(s.strip(',lax'))
# # s = 'alexex'
# # # *** find  index 通过元素找索引
# # # print(s.find('e'))
# # # print(s.find('e',3))
# # # print(s.find('A'))
# # print(s.index('A'))
# # # s = 'alexex'
# # #*** count 寻找元素出现的个数 可切片
# # print(s.count('e'))
# # print(s.count('ex'))
#
# #***replace 替换
# # s = '将发生多了范德萨发范德萨回复'
# # s1 = s.replace('范德萨', '小粉嫩')
# # print(s1)
# # s2 = s.replace('范德萨', '小粉嫩',1)
# # print(s2)
# # s3 = s.replace('范德萨', 'sb')
# # print(s3)
#
# # ***** split 分割  str ---> list
# # s = 'alex wusir taibai'
# # print(s.split())
# # s1 = 'alex,wusir,taibai'
# # print(s1.split(','))
# # s2 = 'alexawusirataibai'
# # print(s2.split('a'))
# # s3 = 'alexawusirataibai'
# # print(s3.split('a',1))  # 分割次数
#
#
# #***** format 格式化输出
# #三种用法
# #第一种用法：
# # s = '我叫{}，今年{}，爱好{}'.format('MT',18,'母牛')
# # print(s)
# # #第二种用法
# # s = '我叫{0}，今年{1}，爱好{2}，我依然叫{0},今年还是{1}'\
# #     .format('MT',18,'母牛')
# # print(s)
# # #第三种 键值对
# # s = '我叫{name}，今年{age}，爱好{hobby}'.format(age=18, name='MT', hobby='闷儿')
# # print(s)
# # name='123a'
# # # print(name.isalnum()) #字符串由字母或数字组成
# # # print(name.isalpha()) #字符串只由字母组成
# # # print(name.isdigit()) #字符串只由数字组成
# # if name.isdigit():
# #     name = int(name)
# #     print(name,type(name))
# # else:
# #     print('您输入的由非数字元素')
#*****len
s = 'fdsafdsaf'
print(s)
print(len(s))

print(s.count("a",0,len(s)))
# count = 0
# s = 'fdsafdsag'
# # print(s[0])
# # print(s[1])
# # print(s[2])
# # while count < len(s):
# #     print(s[count])
# #     count += 1
# # for i in s:
# #     print(i)