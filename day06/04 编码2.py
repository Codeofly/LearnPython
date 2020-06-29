# s = 'fdsagsadfsad方式打开家乐福；按时fdsafdsa'
# ip地址 端口等等
# s1 = input('你好')
# s1
# s = 'laonanhai'
# s1 = b'laonanhai'
# print(type(s))
# print(type(s1))


# s = 'alex'  # str
# s1 = s.encode('utf-8')  # bytes
# encode 编码 ：str --- > bytes
# s = 'hello girl'
# s1 = s.encode('utf-8')
# print(s1)

# s = 'hello girl'
# s1 = s.encode('gbk')
# print(s1)
# s = '中国'
# s1 = s.encode('utf-8')
# print(s1)
s = '中国'
s1 = s.encode('utf-8')

print(s1)

#解码 一
s2 = str(s.encode('utf-8'), encoding='utf-8')
print(s2)

#解码 二
s3 = s1.decode('utf-8')
print(s3)
