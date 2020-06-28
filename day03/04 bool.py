# bool True False
#数据类型转换：
'''
int  str

int bool

str bool
    空字符串 False
    其他都是True
'''
s1 = ''
if s1:
    print(666)
else:
    print(111)
s = str(True)
print(s,type(s))