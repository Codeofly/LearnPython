a = 1000
b = 1000
print(a == b)
# == 比较的是数值
#is  比较的是内存地址。
# print(a is b)
#查看内存地址id（）
# print(id(a))
# print(id(b))

#小数据池：

#数字： -5 ~ 256 节省空间。

#字符串： 1，如果含有特殊字符，不存在小数据池。
#         2，str（单个） * int  int > 20 不存在小数据池。

#其他都不存在小数据池。