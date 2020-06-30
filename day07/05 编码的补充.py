s = 'alex'
s1 = s.encode('utf-8')  # unicode ---> utf-8 编码
s3 = s1.decode('utf-8')  # utf-8 ---> unicode 解码
print(s3)

# s = 'alex'
# s1 = s.encode('gbk')  # unicode ---> gbk 编码
# s3 = s1.decode('gbk')  # gbk ---> unicode 解码
# print(s3)

# gbk ---> utf-8
# s = 'alex'
# s1 = s.encode('gbk')
# print(s1)
#
# s2 = s1.decode('gbk').encode('utf-8')
# print(s2)

s = '老男孩'
s1 = s.encode('gbk')
print(s1)

s2 = s1.decode('gbk').encode('utf-8')
print(s2)
