# dic = {"name_list":['张三','lisi','隔壁王叔叔'],
#        'dic2':{'name':'太白','age':12},
#        }
# #1 ,给列表追加一个元素：'旺旺'
# # l1 = dic['name_list']
# # l1.append('旺旺')
# dic['name_list'].append('旺旺')
# print(dic)
# #,2,给列表lisi全部大写
# # print(dic['name_list'][1].upper())
# dic['name_list'][1] = dic['name_list'][1].upper()
# print(dic)
# #3，给dic2 对应的字典添加一个键值对：hobby：girl.
# dic['dic2']['hobby'] = 'girl'
# print(dic)

dic = {
    'name':'汪峰',
    'age':48,
    'wife':[{'name':'国际章','age':38}],
    'children':{'girl_first':'小苹果','girl_second':'小怡','girl_three':'顶顶'}
}

name = dic['name']
print(name)

l1 = dic['wife']  # 先获取到这个列表
print(type(l1))
print(l1)
di = l1[0]  # 列表按照索引取值，这个字典是列表的第一个元素，所以通过索引获取到这个字典
print(type(di))
print(di)

# 当然上面是分布获取的，我们还可以合并去写：
di2 = dic['wife'][0]
print(di2)


print(l1[0]['name'])

print(dic['children']['girl_three'])