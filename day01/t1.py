# -*- encoding:utf-8 -*-
#print('我爱你，中国') 
#print(1+2+3+4)
#print((1+2+3+4)*3 + 5)
#print((((1+2+3+4)*3 + 5) + 100) / 3)
#print((((1+2+3+4)*3 + 5) + 100) / 3＋．．．)
x = 1+2+3+4
y = x * 3 + 5
z = (y +100) / 3
#变量：将程序的中间结果暂时储存起来，以便后续程序调用。
#变量：
'''
w__ = 22
e_a_ = '太白'
e$ = 'fdsa'
-_ = '15'
2g = 33
__ = '老男孩'



age1 = 12
age2 = age1
age3 = age2
age2 = 6
age1 = 33
print(age1,age2,age3)  # 12 12 12  12 6 12
'''
# 数字类型
i = 100
#print(i * 3)

#字符串类型
#在python中被引号引起来的数据就是字符串。
name = '老男孩'
name2 = "路飞学院"
#print(name,name2)
#配合使用
#msg = "My name is Alex , I'm 22 years old!"
#name3 = '''太白'''
msg = '''
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
'''
#print(msg)

#字符串：+与字符串+     * 与数字乘
#字符串的拼接 + 
n1 = '老男孩'
n2 = '     是最好的培训机构'
n3 = n1 + n2
#print(n3)
#字符串的相乘*
i = '坚强'
#print(i*8)

#bool值 True  False
#print(1 > 2 and 3 < 4 or 4 > 5)
#print(1,type(1))
'''
print('老男孩',type('老男孩'))
print(False,type(False))
print('False',type('False'))
'''
# input 数据类型全部是字符串类型
'''
name = input('请输入你的名字：')
age = input('请输入你的年龄：')
hobby = input('请输入你的爱好：')
s = '我的名字是'+ name + '我的年龄' + age + '我的爱好' + hobby
print(s)


print(111)
if 3 > 2:
	print(666)
print(222)

if 1 > 2:
	print(666)
else:
	print(333)


choice = input('请输入你的猜的数字：')
if choice == '2':
	print('我请你吃饭')
elif choice == '6':
	print('免一周作业')
elif choice == '3':
	print('一起去大保健')
else:
	print('选择错误.....')


age = int(input('请猜我的年龄:'))
if True:
	if age <= 18:
		print('恭喜你猜对了')
	else:
		print('这都看出来...')
else:
	print(666)


while True:
	print('痒')
	print('凉凉')
	print('体面')
	print('社会摇')


print(222)
while True:
	print(111)
	print(333)
print(444)

#标志位ｆｌａｇ

flag = True
while flag:
	print('痒')
	print('凉凉')
	print('体面')
	print('社会摇')
	flag = False


flag = True
count = 1
while flag:
	print(count)
	count = count + 1
	if count == 101:
		flag = False

count = 1
while count < 101:
	print(count)
	count = count + 1


while True:
	print(111)
	print(222)
	break
	print(333)
	print(333)

count = 1
while True:
	print(count)
	count = count + 1
	if count == 101:
		break

while True:
	print(111)
	print(222)
	continue
	print(333)

count = 0
while count < 10:
	count = count + 1
	if count == 7:
		continue
	print(count)

count 
sum = 0
#%

while:
	username = input()
	password = input()
	if unsername == '小明' and password == '123':
	print('登陆成功')
	else:
		pass

'''
