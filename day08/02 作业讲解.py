# 2)有列表li = [‘alex’,’wusir’,’rain’]通过操作该列表构造一个字符串s=’alex*wusir*rain’
# li = ['alex','wusir','rain']
# s = '*'.join(li)
# print(s)

# 1-2+3-4+5.......+99
# count = 0
# sum = 0
# while count < 100:
#     if count % 2 == 1:
#         sum += count
#     else:
#         sum -= count
#     count += 1
# print(sum)
# sum = 0
# for i in range(1,100):
#     if i % 2 == 1:
#         sum += i
#     else:
#         sum -= i
# print(sum)
'''
13，计算用户输入内容中,索引为奇数,并且 对应的元素为数字 的 个数（没有则个数为零）（6分）
'''
# count = 0
# content = input('>>>')
# for i in range(1,len(content),2):
#     if content[i].isdigit():
#         count += 1
# print(count)
'''
16，实现一个整数加法计算器：（3分）
如：content = input(‘请输入内容:’) 
 # 如用户输入：5+8+7....(最少输入两个数相加)，
 然后进行分割再进行计算，将最后的计算结果添加到此字典中(替换None)：
dic={‘最终计算结果’:None}。
'''
# content = input("请输入内容:").strip()
# digit_list = content.split("+")
# dic={"最终计算结果":None}
# sum = 0
# for i in digit_list:
#     i = int(i)
#     sum += i
# dic["最终计算结果"] = sum
# print(dic)

"""
18,写程序：模拟公司hr录入员工账号密码的程序。（10分）
1)，员工的账号密码存储在这种数据类型中：
user_list = [
    {'username':'barry','password':'1234'},
    {'username':'alex','password':'asdf'},
	.........
             ]
2)非法字符模板：board = ['张三','李小四','王二麻子']
3)Hr输入用户名，密码 input（可持续输入 while ，如果想终止程序，那就在输入用户名时输入Q或者q退出程序break），
在Hr输入用户名时，检测此用户名是否有board里面的非法字符，如果有非法字符，
则将非法字符替换成同数量的*（如王二麻子替换成****），然后添加到user_list中，
如果没有非法字符，则直接添加到user_list中，每次添加成功后，打印出刚添加的用户名，密码。
"""
# user_list = [
#     {'username':'barry','password':'1234'},
#     {'username':'alex','password':'asdf'},
#              ]
# board = ['张三','李小四','王二麻子']
# while True:
#     username = input('请输入用户名：/输入Q或q退出程序：').strip()
#     if username.upper() == 'Q':break
#     password = input('请输入密码：').strip()
#     for i in board:
#         username = username.replace(i,'*'*len(i))
#     user_list.append({'username':username,'password':password})
#     print('您已成功添加%s,密码为%s' % (username,password))
# print(user_list)

'''
14，补充代码(从已有的代码下面继续写)：（6分）
有如下值li= [11,22,33,44,55,77,88,99,90]，
将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
li = [11,22,33,44,55,77,88,99,90]
result = {}
for row in li:
......
'''
# li = [11,22,33,44,55,77,88,99,90]
# result = {}
# for row in li:
#     if row > 66:
#         if 'key1' not in result:
#             result['key1'] = []
#         result['key1'].append(row)
#     if row < 66:
#         if 'key2' not in result:
#             result['key2'] = []
#         result['key2'].append(row)
# print(result)

# 17，按要求完成下列转化（如果按照索引去做，只能得4分）。(6分)
list3 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},
    {"name": "wusir", "hobby": "喊麦"},
    {"name": "wusir", "hobby": "街舞"},
    {"name": "太白", "hobby": "街舞"},
    {"name": "太白", "hobby": "开车"},
]
# 如何把上面的列表转换成下方的列表？
list4 = [
    {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
    {"name": "wusir", "hobby_list": ["喊麦", "街舞"]},
]
# dic = {'alex':
#            {"name": "alex", "hobby_list": ["抽烟", "喝酒", "烫头", "Massage"]},
#         'wusir':
#             {"name": "alex", "hobby_list": ["喊麦", "街舞"]},
#  }
a = 2
# print(list(dic.values()))
# list5 = []
# dic1 = {'name':'alex','hobby_list':[]}
# dic2 = {'name':'wusir','hobby_list':[]}
# for i in list3:
#     if i['name'] == 'alex':
#         dic1['hobby_list'].append(i['hobby'])
#     else:
#         dic2['hobby_list'].append(i['hobby'])
# list5.append(dic1)
# list5.append(dic2)
# print(list5)
list3 = [
    {"name": "alex", "hobby": "抽烟"},
    {"name": "alex", "hobby": "喝酒"},
    {"name": "alex", "hobby": "烫头"},
    {"name": "alex", "hobby": "Massage"},
    {"name": "wusir", "hobby": "喊麦"},
    {"name": "wusir", "hobby": "街舞"},
    {"name": "太白", "hobby": "街舞"},
    {"name": "太白", "hobby": "开车"},
]
dic = {}
for i in list3:
    if i['name'] not in dic:
        dic[i['name']] = {'name': i['name'], 'hobby_list': [i['hobby'], ]}
        print(dic)
        # dic = {'alex':{"name": "alex", "hobby_list": ["抽烟",],
        #        'wusir':{"name": "wusir", "hobby_list": ["喊麦",]}
    else:
        dic[i['name']]['hobby_list'].append(i['hobby'])
print(list(dic.values()))
